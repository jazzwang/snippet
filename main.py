import requests
from requests.adapters import HTTPAdapter, Retry


def get_vscode_extensions(max_page=10000, page_size=100,
                          include_versions=True, include_files=True, include_category_and_tags=True, include_shared_accounts=True, include_version_properties=True,
                          exclude_non_validated=False, include_installation_targets=True, include_asset_uri=True, include_statistics=True,
                          include_latest_version_only=False, unpublished=False, include_name_conflict_info=True, api_version='7.2-preview.1', session=None):
    """
    Fetches VSCode extension metadata from the Visual Studio Marketplace API.

    Args:
        max_page (int): Maximum number of pages to retrieve.
        page_size (int): Number of extensions per page.
        include_versions (bool): Include version details.
        include_files (bool): Include file details for each version.
        include_category_and_tags (bool): Include category and tags.
        include_shared_accounts (bool): Include shared accounts info.
        include_version_properties (bool): Include version properties.
        exclude_non_validated (bool): Exclude non-validated extensions.
        include_installation_targets (bool): Include installation targets.
        include_asset_uri (bool): Include asset URIs.
        include_statistics (bool): Include statistics like install count.
        include_latest_version_only (bool): Only fetch the latest version.
        unpublished (bool): Include unpublished extensions.
        include_name_conflict_info (bool): Include name conflict information.
        api_version (str): API version to use for the request.
        session (requests.Session): An optional requests session object for reuse and retries.

    Yields:
        dict: A dictionary representing a single VSCode extension.
    """
    if not session:
        # Create a new session if one isn't provided
        session = requests.session()

    headers = {'Accept': f'application/json; charset=utf-8; api-version={api_version}'}

    # Flags control the amount and type of data returned for each extension.
    # Each flag corresponds to a specific detail level or data inclusion.
    flags = 0
    if include_versions:
        flags |= 0x1  # Details about each version of the extension

    if include_files:
        flags |= 0x2  # Files associated with each version

    if include_category_and_tags:
        flags |= 0x4 # Categories and tags

    if include_category_and_tags:
        flags |= 0x4

    if include_shared_accounts:
        flags |= 0x8  # Shared accounts information

    # This flag is duplicated, it should be removed or corrected if it's meant to be different.
    if include_shared_accounts:
        flags |= 0x8

    if include_version_properties:
        flags |= 0x10 # Version-specific properties

    if exclude_non_validated:
        flags |= 0x20 # Exclude extensions that haven't been validated

    if include_installation_targets:
        flags |= 0x40 # Targets like VSCode, Visual Studio, Azure DevOps

    if include_asset_uri:
        flags |= 0x80 # URIs for assets (e.g., VSIX package)

    if include_statistics:
        flags |= 0x100 # Installation counts, ratings, etc.

    if include_latest_version_only:
        flags |= 0x200 # Only return data for the latest version

    if unpublished:
        flags |= 0x1000 # Include extensions that are not published

    if include_name_conflict_info:
        flags |= 0x8000 # Information about potential name conflicts

    for page in range(1, max_page + 1):
        # Construct the request body for the extension query API
        body = {
            "filters": [
                {
                    "criteria": [
                        {
                            "filterType": 8, # Filter by InstallationTarget
                            "value": "Microsoft.VisualStudio.Code" # Target VSCode extensions
                        }
                    ],
                    "pageNumber": page,
                    "pageSize": page_size,
                    "sortBy": 0, # Sort by relevance
                    "sortOrder": 0 # Ascending
                }
            ],
            "assetTypes": [], # No specific asset types requested
            "flags": flags # Use the calculated flags
        }

        # Make the POST request to the Marketplace API
        r = session.post('https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery', json=body, headers=headers)
        r.raise_for_status() # Raise an exception for HTTP errors
        response = r.json() # Parse the JSON response

        # Extract extensions from the first result set
        extensions = response['results'][0]['extensions']
        for extension in extensions:
            yield extension # Yield each extension found

        # If the number of extensions returned is less than page_size, it means we've reached the last page
        if len(extensions) != page_size:
            break


def main():
    """
    Main function to retrieve and process VSCode extension information.
    Sets up a requests session with a retry strategy and iterates through extensions.
    """
    # Define a retry strategy for handling transient network issues or API rate limits
    retry_strategy = Retry(
        total=3, # Total number of retries
        backoff_factor=1, # Exponential backoff factor (1s, 2s, 4s delays)
        status_forcelist=[429, 500, 502, 503, 504], # HTTP status codes to retry on
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"] # Include POST for the API call
    )
    # Create an HTTPAdapter with the retry strategy
    adapter = HTTPAdapter(max_retries=retry_strategy)
    # Create a new session and mount the adapter to handle retries for http and https
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Iterate over each extension yielded by get_vscode_extensions
    for extension in get_vscode_extensions(session=session):
        # Extract relevant information from the extension dictionary
        extension_name = extension['extensionName']
        extension_description = extension['extensionName'] # Note: This might be a typo, usually 'displayName' or 'shortDescription' is used for description.
        extensions_versions = extension['versions']
        # Convert list of statistics dictionaries to a single dictionary for easy lookup
        extensions_statistics = dict({(item['statisticName'], item['value']) for item in extension['statistics']})
        extension_publisher_username = extension['publisher']['publisherName']

        # Iterate through each version of the current extension
        for extension_version_info in extensions_versions:
            extension_version = extension_version_info['version']
            # Construct the direct download URL for the VSIX package
            extension_artifact_download_url = f'https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{extension_publisher_username}/vsextensions/{extension_name}/{extension_version}/vspackage'
            # Print the extracted details (extension name, description, version, download URL, install count)
            print(extension_name, extension_description, extension_version, extension_artifact_download_url, extensions_statistics.get('install', 'N/A'))


if __name__ == '__main__':
    main()

import requests
from requests.adapters import HTTPAdapter, Retry


def get_vscode_extensions(max_page=10000, page_size=100,
                          include_versions=True, include_files=True, include_category_and_tags=True, include_shared_accounts=True, include_version_properties=True,
                          exclude_non_validated=False, include_installation_targets=True, include_asset_uri=True, include_statistics=True,
                          include_latest_version_only=False, unpublished=False, include_name_conflict_info=True, api_version='7.2-preview.1', session=None):
    if not session:
        session = requests.session()

    headers = {'Accept': f'application/json; charset=utf-8; api-version={api_version}'}

    flags = 0
    if include_versions:
        flags |= 0x1

    if include_files:
        flags |= 0x2

    if include_category_and_tags:
        flags |= 0x4

    if include_shared_accounts:
        flags |= 0x8

    if include_shared_accounts:
        flags |= 0x8

    if include_version_properties:
        flags |= 0x10

    if exclude_non_validated:
        flags |= 0x20

    if include_installation_targets:
        flags |= 0x40

    if include_asset_uri:
        flags |= 0x80

    if include_statistics:
        flags |= 0x100

    if include_latest_version_only:
        flags |= 0x200

    if unpublished:
        flags |= 0x1000

    if include_name_conflict_info:
        flags |= 0x8000

    for page in range(1, max_page + 1):
        body = {
            "filters": [
                {
                    "criteria": [
                        {
                            "filterType": 8,
                            "value": "Microsoft.VisualStudio.Code"
                        }
                    ],
                    "pageNumber": page,
                    "pageSize": page_size,
                    "sortBy": 0,
                    "sortOrder": 0
                }
            ],
            "assetTypes": [],
            "flags": flags
        }

        r = session.post('https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery', json=body, headers=headers)
        r.raise_for_status()
        response = r.json()

        extensions = response['results'][0]['extensions']
        for extension in extensions:
            yield extension

        if len(extensions) != page_size:
            break


def main():
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    for extension in get_vscode_extensions(session=session, page_size=10):
        extension_name = extension['extensionName']
        extension_description = extension['extensionName']
        extensions_versions = extension['versions']
        extensions_statistics = dict({(item['statisticName'], item['value']) for item in extension['statistics']})
        extension_publisher_username = extension['publisher']['publisherName']

        for extension_version_info in extensions_versions:
            extension_version = extension_version_info['version']
            extension_artifact_download_url = f'https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{extension_publisher_username}/vsextensions/{extension_name}/{extension_version}/vspackage'
            print(extension_name, extension_description, extension_version, extension_artifact_download_url, extensions_statistics['install'])


if __name__ == '__main__':
    main()

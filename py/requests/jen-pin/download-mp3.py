import os
import requests
import argparse
from urllib.parse import unquote, urlparse

def download_file(url, headers):
    """
    Downloads a single file using the given URL and headers,
    saving it with a filename derived from the URL path.
    """
    try:
        # 1. Parse the URL to get the path
        parsed_url = urlparse(url)
        url_path = parsed_url.path

        # 2. Decode the URL path (e.g., %E5%A5%BD%E6%97%A5 -> 好日)
        decoded_path = unquote(url_path)

        # 3. Get the basename (the filename part)
        output_filename = os.path.basename(decoded_path)

        # The Range header in the original curl command is a partial download.
        # It's set globally here, but in a real-world scenario, you might
        # remove it or adjust it based on the file.
        print(f"Attempting to download to: {output_filename}")
        
        # Use stream=True for large files
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # Write the content to the file
        with open(output_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
                    
        print(f"✅ Success! Content saved to {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading {url}: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred for {url}: {e}")
    print("-" * 40)


# --- Main Program ---
# parsing CLI arguments
parser = argparse.ArgumentParser(description="Download MP3 from Google Cloud Storage.")
parser.add_argument("--input", "-i", help="input CSV file, delimiter: ';', first column should be 'readmoo url'.", required=True)
args = parser.parse_args()

INPUT_FILE = args.input

# Define the common headers from the original curl command
COMMON_HEADERS = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://listen.jen-pin.com.tw/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'DNT': '1',
}

# Create a sample input file for testing if it doesn't exist
if not os.path.exists(INPUT_FILE):
    print(f"Creating sample file: {INPUT_FILE}")
    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        # The URL from your original curl command
        f.write('https://storage.googleapis.com/listen-jen-pin-com-tw/mlgy-hhye-abrs/01-01-%E9%96%8B%E5%A0%B4.mp3\n')

# Read URLs from the input file and process each one
try:
    print(f"Reading URLs from {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            url = line.strip()
            if url: # Process only non-empty lines
                download_file(url, COMMON_HEADERS)
except FileNotFoundError:
    print(f"🚨 Error: Input file '{INPUT_FILE}' not found. Please create it with one URL per line.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

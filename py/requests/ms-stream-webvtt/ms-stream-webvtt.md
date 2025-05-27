# Download webvtt transcript from Microsoft Stream

## from Bing Copilot

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how to download a transcript from Microsoft Stream using python or powershell?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Downloading a transcript from Microsoft Stream using Python or PowerShell requires interacting with the Microsoft Graph API, as Microsoft Stream integrates with it for managing video content and metadata. Below are examples for both Python and PowerShell approaches:

### **Python Approach**

1.  **Set Up Microsoft Graph API**:

    -   Register an app in Azure Active Directory.
    -   Obtain the necessary permissions (e.g., `Video.Read.All`).
    -   Generate a client ID, client secret, and tenant ID.
    
2.  **Install Required Libraries**:

    ```bash
    pip install requests msal
    ```

3.  **Python Script**:

    ```python
    import requests
    from msal import ConfidentialClientApplication

    # Azure AD credentials
    CLIENT_ID = "your-client-id"
    CLIENT_SECRET = "your-client-secret"
    TENANT_ID = "your-tenant-id"

    # Microsoft Graph API endpoint
    GRAPH_API_URL = "https://graph.microsoft.com/v1.0"

    # Authenticate and get access token
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET,
    )
    token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    access_token = token_response.get("access_token")

    # Video ID and transcript download
    video_id = "your-video-id"
    headers = {"Authorization": f"Bearer {access_token}"}
    transcript_url = f"{GRAPH_API_URL}/videos/{video_id}/transcript"

    response = requests.get(transcript_url, headers=headers)
    if response.status_code == 200:
        with open("transcript.vtt", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Transcript downloaded successfully!")
    else:
        print(f"Failed to download transcript: {response.status_code}, {response.text}")
    ```

### **PowerShell Approach**

1.  **Set Up Microsoft Graph API**:

    -   Follow the same steps as above to register an app and obtain credentials.

2.  **Install Required Module**:

    ```powershell
    Install-Module -Name Microsoft.Graph -Scope CurrentUser
    ```

3.  **PowerShell Script**:

    ```powershell
    # Azure AD credentials
    $ClientId = "your-client-id"
    $ClientSecret = "your-client-secret"
    $TenantId = "your-tenant-id"

    # Authenticate and get access token
    $Body = @{
        grant_type    = "client_credentials"
        client_id     = $ClientId
        client_secret = $ClientSecret
        scope         = "https://graph.microsoft.com/.default"
    }
    $TokenResponse = Invoke-RestMethod -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" -Method Post -Body $Body
    $AccessToken = $TokenResponse.access_token

    # Video ID and transcript download
    $VideoId = "your-video-id"
    $Headers = @{ Authorization = "Bearer $AccessToken" }
    $TranscriptUrl = "https://graph.microsoft.com/v1.0/videos/$VideoId/transcript"

    $Response = Invoke-RestMethod -Uri $TranscriptUrl -Headers $Headers -Method Get
    if ($Response) {
        $TranscriptPath = "transcript.vtt"
        $Response | Out-File -FilePath $TranscriptPath -Encoding utf8
        Write-Host "Transcript downloaded successfully to $TranscriptPath"
    } else {
        Write-Host "Failed to download transcript"
    }
    ```

### Notes:

-   Replace placeholders like `your-client-id`, `your-client-secret`, `your-tenant-id`, and `your-video-id` with actual values.
-   Ensure your app has the correct permissions in Azure AD.
-   The transcript is typically in `.vtt` (WebVTT) format.

If you encounter issues, verify permissions and API endpoint availability. Let me know if you need further clarification!
</td></tr></table>

## from Perplexity

- https://www.perplexity.ai/search/how-to-download-a-transcript-f-ENk5H5HOT7WrqucyUJ3YZg

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how to download a transcript from Microsoft Stream using python or powershell?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
To download a transcript from Microsoft Stream using Python or PowerShell, here are the practical approaches based on available information:

### Using Python

-   Microsoft Stream provides an API endpoint that returns transcript data in JSON format. You can fetch this transcript data by calling the API URL pattern:

    ```
    https://euno-1.api.microsoftstream.com/api/videos/{videoId}/events?$filter=Type eq 'transcript'&api-version=1.4-private
    ```

    Replace `{videoId}` with the actual video ID from the Stream URL.

-   A sample JavaScript snippet (which can be adapted to Python with requests) extracts and joins the transcript text from the JSON response:

    ```javascript
    const text = r.value
    .filter(entry=> entry.type ==="transcript").map(entry=> entry.eventData.text.replace(/\r\n/g,' ')).join(" ");`
    ```

-   In Python, you would authenticate (using your Microsoft credentials or OAuth token), make a GET request to the above API, parse the JSON, extract the transcript text, and save it to a file.

-   There is also a GitHub project `msstream-dl` that downloads Microsoft Stream videos and may be adaptable to extract transcripts programmatically in Python [[5]](https://gist.github.com/JakeStanger/523b0e6a3d0f3c004482d585fc10754e)[[6]](https://github.com/ranahaani/msstream-dl).

### Using PowerShell

-   PowerShell itself does not have a built-in cmdlet to directly download Microsoft Stream transcripts.

-   However, you could use PowerShell to invoke a web request to the Stream transcript API (similar to the Python approach), authenticate, parse JSON, and save the transcript text.

-   The `Start-Transcript` cmdlet in PowerShell is unrelated to Microsoft Stream transcripts; it records your PowerShell session commands/output to a text file and cannot be used to download Stream transcripts[7](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7.4&viewFallbackFrom=powershell-7.1)[9](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7.5).

### Manual or Browser-based Workaround

-   If you have access to the video owner settings, you can go to the Microsoft Stream portal, open the video details, and under Captions or Transcript settings, there may be an option to "Download Captions" or "Download Transcript" as a .VTT file, which contains the transcript with timestamps. This can be downloaded manually or automated via scripting if accessible [[2]](https://techcommunity.microsoft.com/discussions/streamforum/download-transcripts/1101274)[[3]](https://answers.microsoft.com/en-us/msoffice/forum/all/download-transcript-from-microsoft-stream/18fb51f5-3b11-49c6-b18a-44bf6fd524ea)[[8]](https://www.marquette.edu/digital-learning/documents/download-transcript-stream-videos.docx).

-   If the direct download is not available, one workaround is to capture the transcript JSON from network calls in the browser developer tools and then process it as shown above [[2]](https://techcommunity.microsoft.com/discussions/streamforum/download-transcripts/1101274).

### Summary

| Method | Description | Notes |
| --- |  --- |  --- |
| Python API call | Use Microsoft Stream API to fetch transcript JSON, parse and save text | Requires authentication and API access |
| PowerShell | Invoke web request to Stream API, parse JSON, save transcript | No direct cmdlet, needs scripting |
| Manual Download | Download transcript .VTT file from Stream portal if you have permission | Easiest if available |

For automated scripting, the Python approach using the Stream API is the most straightforward if you handle authentication properly. The PowerShell approach would be similar but requires more manual JSON handling.

References: [[2]](https://techcommunity.microsoft.com/discussions/streamforum/download-transcripts/1101274)[[3]](https://answers.microsoft.com/en-us/msoffice/forum/all/download-transcript-from-microsoft-stream/18fb51f5-3b11-49c6-b18a-44bf6fd524ea)[[5]](https://gist.github.com/JakeStanger/523b0e6a3d0f3c004482d585fc10754e)[[6]](https://github.com/ranahaani/msstream-dl)[[7]](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7.4&viewFallbackFrom=powershell-7.1)[[8]](https://www.marquette.edu/digital-learning/documents/download-transcript-stream-videos.docx)

### Citations:

1.  <https://support.microsoft.com/en-us/office/view-edit-and-manage-video-transcripts-and-captions-3cb9acb6-05b2-4f59-a50d-7df61123aa20>
2.  <https://techcommunity.microsoft.com/discussions/streamforum/download-transcripts/1101274>
3.  <https://answers.microsoft.com/en-us/msoffice/forum/all/download-transcript-from-microsoft-stream/18fb51f5-3b11-49c6-b18a-44bf6fd524ea>
4.  <https://office365itpros.com/2023/07/25/stream-transcripts/>
5.  <https://gist.github.com/JakeStanger/523b0e6a3d0f3c004482d585fc10754e>
6.  <https://github.com/ranahaani/msstream-dl>
7.  <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7.4&viewFallbackFrom=powershell-7.1>
8.  <https://www.marquette.edu/digital-learning/documents/download-transcript-stream-videos.docx>
9.  <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7.5>
10.  <https://superuser.com/questions/1510596/how-to-capture-record-download-multiple-streaming-audio-urls-with-a-cmd-or-p>

* * * *

Answer from Perplexity: https://www.perplexity.ai/search/how-to-download-a-transcript-f-ENk5H5HOT7WrqucyUJ3YZg?utm\_source=copy\_output
</td></tr></table>

## from Gemini

- https://g.co/gemini/share/75e9629d91e8

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how to download a transcript from Microsoft Stream using python or powershell?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Downloading transcripts from Microsoft Stream programmatically (using Python or PowerShell) can be a bit tricky because Microsoft Stream, especially the newer version built on SharePoint, doesn't always expose a direct public API for this purpose. However, there are a few approaches and workarounds you can explore:

**Understanding the Challenge**

-   **No Direct Public API (for all scenarios):** While there are some Graph API endpoints related to Teams meeting transcripts, a universal API to download transcripts from any Stream video (especially those uploaded directly to Stream or integrated with SharePoint/OneDrive) isn't readily available for simple scripting.
-   **Authentication:** You'll need to authenticate with Microsoft 365. This often involves OAuth 2.0 or browser-based login flows, which can be complex to automate.
-   **Dynamic URLs/VTT Files:** Transcripts are usually in WebVTT (.vtt) format. The URL to the .vtt file is often dynamically generated or hidden behind JavaScript, making it hard to predict or directly access.

**Methods and Workarounds**

Here are the common approaches, ranging from manual to more automated, with considerations for Python and PowerShell:

### **1\. Manual Download (and then process with Python/PowerShell)**

This is the simplest and most reliable method if you only need to download a few transcripts. Once downloaded, you can use Python or PowerShell to parse and process the .vtt file.

**Steps:**

1.  **Open the video in Microsoft Stream.**
2.  **Access "Video settings" or "Update video details":** Look for a "..." (More actions) menu or a "Video settings" panel on the right-hand side of the video player.
3.  **Find "Transcripts and captions":** Expand this section.
4.  **Download the .vtt file:** There should be a "Download" option next to the transcript language.

**Processing the .vtt file with Python/PowerShell:**

Once you have the `.vtt` file, it contains time codes and text. You can parse it to extract just the text.

**Python Example for .vtt parsing:**

Python

```python
def extract_text_from_vtt(vtt_filepath):
    text_content = []
    with open(vtt_filepath, 'r', encoding='utf-8') as f:
        # Skip the WEBVTT header
        f.readline()

        for line in f:
            line = line.strip()
            if not line:
                continue
            # Skip timestamp lines (e.g., 00:00:00.000 --> 00:00:05.000)
            if '-->' in line:
                continue
            # Add text lines
            text_content.append(line)
    return "\n".join(text_content)

# Usage:
# transcript_file = "path/to/your/transcript.vtt"
# extracted_text = extract_text_from_vtt(transcript_file)
# print(extracted_text)

```

**PowerShell Example for .vtt parsing:**

PowerShell

```powershell
function Extract-TextFromVTT {
    param (
        [string]$VttFilePath
    )

    $textContent = @()
    $content = Get-Content -Path $VttFilePath -Encoding UTF8

    # Skip the WEBVTT header
    $skipHeader = $true
    foreach ($line in $content) {
        if ($skipHeader) {
            if ($line.Trim() -eq "WEBVTT") {
                $skipHeader = $false
                continue
            }
        }

        $line = $line.Trim()
        if ([string]::IsNullOrEmpty($line)) {
            continue
        }
        # Skip timestamp lines (e.g., 00:00:00.000 --> 00:00:05.000)
        if ($line -like "*-->*") {
            continue
        }
        $textContent += $line
    }
    return ($textContent -join "`n")
}

# Usage:
# $transcriptFile = "C:\path\to\your\transcript.vtt"
# $extractedText = Extract-TextFromVTT -VttFilePath $transcriptFile
# Write-Host $extractedText

```

### **2\. Browser Automation (Python with Selenium/Playwright)**

This method simulates a user interacting with the browser to log in and download the file. It's more complex but can automate the entire process.

**Considerations:**

-   **Browser Driver:** Requires installing a browser driver (e.g., ChromeDriver for Chrome).
-   **Headless Mode:** Can run in headless mode (without a visible browser window) for server environments.
-   **Updates:** Microsoft Stream's UI might change, breaking your automation scripts.

**Python Example (using Selenium - conceptual):**

Python

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.supportimport expected_conditions as EC
import time

# --- Configuration ---
STREAM_VIDEO_URL = "YOUR_MICROSOFT_STREAM_VIDEO_URL"
YOUR_USERNAME = "your_email@yourdomain.com"
YOUR_PASSWORD = "your_password" # Consider using environment variables or a secure vault

# --- Initialize WebDriver ---
# Make sure you have the correct WebDriver for your browser (e.g., chromedriver.exe)
# in your PATH or specify the path to it.
driver = webdriver.Chrome() # Or Firefox, Edge, etc.
driver.get(STREAM_VIDEO_URL)

try:
    # --- Login Process (Highly dependent on your organization's login page) ---
    # This is a generic example. You'll need to inspect your actual login page
    # to find the correct element IDs/names.

    # Wait for email input and enter username
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "i0116")) # Common ID for Microsoft email input
    )
    email_input.send_keys(YOUR_USERNAME)
    driver.find_element(By.ID, "idSIButton9").click() # Common ID for "Next" or "Sign in" button

    # Wait for password input and enter password
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "i0118")) # Common ID for Microsoft password input
    )
    password_input.send_keys(YOUR_PASSWORD)
    driver.find_element(By.ID, "idSIButton9").click() # Common ID for "Sign in" button

    # Handle "Stay signed in?" prompt if it appears
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "idBtn_Back")) # "No" button for "Stay signed in?"
        ).click()
    except:
        pass # No "Stay signed in?" prompt

    # --- Navigate to Transcript Download ---
    # Wait for video page to load
    WebDriverWait(driver, 30).until(
        EC.url_contains("stream.office.com/video/")
    )

    # Click on "Video settings" or similar to reveal options
    # You'll need to find the correct element selector for your Stream interface
    try:
        settings_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Video settings'], button[data-automationid='VideoSettings']"))
        )
        settings_button.click()
    except:
        print("Could not find video settings button, trying other selectors...")
        # Add more robust selectors if the above fails

    # Expand "Transcripts and captions" section if it's not already open
    try:
        transcript_section_header = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h2[contains(text(), 'Transcripts and captions')]"))
        )
        # Check if it's already expanded or needs clicking
        if "expanded" not in transcript_section_header.get_attribute("aria-expanded"):
            transcript_section_header.click()
    except:
        print("Could not find or expand transcript section.")

    # Find the download link for the .vtt file
    # This selector is highly prone to change. Inspect the page!
    download_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Download transcript') or contains(@title, 'Download caption file')]"))
    )
    download_link.click()

    print("Transcript download initiated. Check your browser's download directory.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5) # Give some time for download to start
    driver.quit()

```

**PowerShell (using browser automation via `Selenium.WebDriver` module or similar):**

PowerShell can also interact with browsers, but it's generally less ergonomic for complex UI automation than Python with Selenium/Playwright. You'd need to install the Selenium WebDriver module for PowerShell.

PowerShell

```powershell
# This is a conceptual example and requires installing the Selenium.WebDriver module
# Install-Module -Name Selenium.WebDriver -Force

# Add-Type -Path "C:\path\to\WebDriver.dll" # Adjust path as needed
# Add-Type -Path "C:\path\to\Selenium.WebDriver.dll" # Adjust path as needed

# $Driver = New-Object OpenQA.Selenium.Chrome.ChromeDriver
# $Driver.Navigate().GoToURL("YOUR_MICROSOFT_STREAM_VIDEO_URL")

# ... (Similar logic to Python for login and navigating UI) ...

# $Driver.Quit()

```

For more complex UI interaction in PowerShell, consider using the `IE.Application` COM object (if IE is available and you're targeting older web pages) or a more robust framework that can drive a headless browser. However, for modern web applications like Stream, dedicated browser automation libraries like Selenium or Playwright are usually preferred, and Python is generally a better fit for them.

### **3\. Inspecting Network Traffic / Direct API Calls (Advanced)**

This is the most challenging but potentially most robust method if you can identify the underlying API calls.

**Steps:**

1.  **Open Microsoft Stream** in your browser (Chrome/Firefox recommended).
2.  **Open Developer Tools** (F12).
3.  **Go to the "Network" tab.**
4.  **Filter for requests** related to "transcript" or ".vtt" or "streamContent".
5.  **Play the video or click the download button.** Observe the network requests.
6.  **Identify the API endpoint** that serves the transcript data (often a `.vtt` file or a JSON containing the transcript data).
7.  **Examine the request headers and payload.** You'll need to understand how authentication tokens are passed (e.g., `Authorization` header with a bearer token).

**Example of a potential API endpoint found by others:**

`https://<location>.api.microsoftstream.com/api/texttracks/...` or `https://<URLToYourStreamVideo>/streamContent?format=json`

**Challenges:**

-   **Authentication:** This is the biggest hurdle. You'll likely need to obtain an OAuth token. This might involve using Azure AD authentication libraries (MSAL for Python) if your application is registered in Azure AD, or complex web scraping to extract tokens from a browser session.

-   **Dynamic URLs:** The exact URL for the transcript can vary.

-   **Microsoft Graph API:** For Teams meeting recordings, there *are* Microsoft Graph API endpoints for accessing meeting transcripts. If your Stream video is a Teams meeting recording, this is the most legitimate and stable approach.

    -   **Microsoft Graph Documentation:** Search for "Teams meeting transcript API" on the Microsoft Graph documentation. You'd typically use `GET /users/{id}/onlineMeetings/{id}/transcripts` or similar.
    -   **Requires Azure AD App Registration:** You'll need to register an application in Azure AD with appropriate permissions (e.g., `OnlineMeetings.Read.All`).
    -   **Python with MSAL and requests:**

    Python

    ```python
    import requests
    import msal # pip install msal

    # --- Azure AD App Registration Details ---
    TENANT_ID = "YOUR_TENANT_ID"
    CLIENT_ID = "YOUR_CLIENT_ID"
    CLIENT_SECRET = "YOUR_CLIENT_SECRET" # Or use certificate/user flow

    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    SCOPE = ["https://graph.microsoft.com/.default"] # Or more specific scopes like "OnlineMeetings.Read.All"

    app = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY
    )

    # Acquire token
    result = app.acquire_token_for_client(scopes=SCOPE)

    if"access_token"in result:
        access_token = result["access_token"]
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # --- Example: Get Teams meeting transcripts (requires meeting ID) ---
        # Replace with your actual user ID and online meeting ID
        user_id = "YOUR_USER_ID"
        online_meeting_id = "YOUR_ONLINE_MEETING_ID"
        graph_url = f"https://graph.microsoft.com/v1.0/users/{user_id}/onlineMeetings/{online_meeting_id}/transcripts"

        response = requests.get(graph_url, headers=headers)

        if response.status_code == 200:
            transcript_data = response.json()
            # The transcript data might be a JSON object with links to download the VTT.
            # You'll need to parse this JSON to find the actual download URL.
            print("Transcript data received:", transcript_data)
            # You might need to make another request to download the actual .vtt file
            # from a URL provided in transcript_data.
        else:
            print(f"Error getting transcript: {response.status_code} - {response.text}")
    else:
        print("Could not acquire token:", result.get("error"), result.get("error_description"))

    ```

**Recommendations:**

1.  **If a few transcripts:** Stick to the **manual download** and then use Python/PowerShell for parsing. It's the most reliable and least prone to breaking.
2.  **If automating for a controlled environment (e.g., internal tool, stable UI):** Consider **browser automation (Selenium/Playwright)**. Be prepared to maintain your scripts if Stream's UI changes.
3.  **If dealing with Teams meeting recordings and have Azure AD application development capabilities:** Explore the **Microsoft Graph API**. This is the most "official" and stable programmatic approach for supported scenarios.
4.  **Avoid direct API calls discovered through network inspection unless absolutely necessary** and you understand the authentication and potential for breaking changes. Microsoft might change these internal APIs without notice.

Before attempting any automation, ensure you have the necessary permissions to access the Stream videos and their transcripts.
</td></tr></table>
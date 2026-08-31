"""
使用 Playwright 存取指定網頁並將網路互動存成 HAR 檔案
"""
from playwright.sync_api import sync_playwright
import os

URL = "https://share.google/aimode/c61jOgQXCYJmhkOV9"
HAR_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "network_capture.har")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 建立 context 時指定 record_har_path，Playwright 會自動記錄所有網路請求
        context = browser.new_context(
            record_har_path=HAR_FILE,
            record_har_url_filter="**/*",          # 記錄所有 URL
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
        )

        page = context.new_page()

        print(f"正在存取: {URL}")
        page.goto(URL, wait_until="networkidle", timeout=60000)

        # 額外等待幾秒，確保動態載入的資源也被捕獲
        page.wait_for_timeout(5000)

        print(f"頁面標題: {page.title()}")

        # 關閉 context 時 HAR 檔案會自動寫入磁碟
        context.close()
        browser.close()

    file_size = os.path.getsize(HAR_FILE)
    print(f"HAR 檔案已儲存: {HAR_FILE}")
    print(f"檔案大小: {file_size:,} bytes")


if __name__ == "__main__":
    main()

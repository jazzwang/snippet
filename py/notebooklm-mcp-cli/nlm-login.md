- https://deepwiki.com/search/df7335f2-e677-488e-bf07-c046ed00eb75

# DeepWiki Q&A with Code Context for Repository: jacob-bd/gemini-notebook-mcp-cli
## Q1

如果我想要撰寫一個新的 CLI 想要取用此專案登入 google 帳號的部份，該從哪一個程式碼開始？

### Answer

## 簡答

從 `src/notebooklm_tools/cli/main.py` 的 `login_callback` 開始看——這是 `nlm login` 的入口，串起了整個 Google 登入流程。實際的 cookie 擷取邏輯在 `src/notebooklm_tools/utils/cdp.py` 的 `extract_cookies_via_cdp`（Chromium 系）與 `utils/auth_browser.py` 的 `extract_cookies_via_browser`（Firefox），儲存則由 `services/auth.py` 的 `AuthManager` 與 `core/auth.py` 的 `save_tokens_to_cache` 負責。 gemini-notebook-mcp-cli:427-484 gemini-notebook-mcp-cli:1927-1954 gemini-notebook-mcp-cli:257-262 

## 詳細說明

### 1. CLI 入口：`login_callback`

`nlm login` 由 `login_app` 的 callback `login_callback` 處理，支援 `--manual`、`--check`、`--profile`、`--provider`、`--cdp-url`、`--wsl`、`--storage` 等選項。 gemini-notebook-mcp-cli:427-484 

### 2. 三條登入路徑

`login_callback` 內部依參數分流：

| 路徑 | 觸發條件 | 呼叫的函式 |
|---|---|---|
| 外部 CDP | `--provider openclaw` 或自訂 `--cdp-url` | `extract_cookies_via_existing_cdp` |
| Firefox | `select_auth_backend()` 回傳 `firefox_profile` | `extract_cookies_via_browser`（讀取隔離 profile 的 cookie store） |
| Chromium（預設） | 其他情況 | `extract_cookies_via_cdp`（CDP over WebSocket） | gemini-notebook-mcp-cli:731-799 

### 3. Cookie 擷取核心：`utils/cdp.py`

`extract_cookies_via_cdp` 會啟動受管 Chrome、連上 DevTools Protocol、等待使用者登入（最長 300 秒），再取出 cookies 與 CSRF token。登入目標 URL 由 `get_notebooklm_url()` 依 `get_base_url()` 決定（含 Enterprise host 分支）。 gemini-notebook-mcp-cli:101-125 gemini-notebook-mcp-cli:58-71 

### 4. 儲存：`AuthManager` → `save_tokens_to_cache`

擷取結果（`cookies`、`csrf_token`、`session_id`、`email`、`build_label`、`base_host`）透過 `auth.save_profile(...)` 寫入 `~/.notebooklm-mcp-cli/profiles/<name>/`；底層 `save_tokens_to_cache` 會處理 profile lock、protected/file 兩種儲存模式與 root `auth.json` 鏡像。 gemini-notebook-mcp-cli:891-904 gemini-notebook-mcp-cli:299-348 

### 5. 無頭刷新（可選）

若你的 CLI 需要自動刷新過期 session，可看 `run_headless_auth` / `_run_headless_auth_unlocked`：它用已存的 Chrome profile 無互動地重新取 token，並以 per-profile file lock 序列化。 gemini-notebook-mcp-cli:2155-2207 

### 建議閱讀順序

1. `cli/main.py` `login_callback` — 流程總覽與參數
2. `utils/cdp.py` `extract_cookies_via_cdp` — CDP 擷取實作
3. `utils/auth_browser.py` `select_auth_backend` / `extract_cookies_via_browser` — 瀏覽器選擇與 Firefox 路徑
4. `services/auth.py` `AuthManager` + `core/auth.py` `save_tokens_to_cache` — 憑證儲存
5. `docs/AUTHENTICATION.md` — 設計說明 gemini-notebook-mcp-cli:10-30 

## Notes

- 注意專案的分層規則：`cli/` 不得直接 import `core/`，應經由 `services/`；若你要寫新 CLI，建議直接呼叫 `services/auth.py` 的 `AuthManager` 與 `utils/` 的擷取函式。 gemini-notebook-mcp-cli:45-50 
- `core/auth.py` 中的 `extract_tokens_via_chrome_devtools` 是 `NotImplementedError` 的 placeholder，不是真正的實作，請勿誤用。 gemini-notebook-mcp-cli:351-375 
- 此專案沒有官方 Google API，登入本質是「從受管瀏覽器 session 取 cookie」，所以你的新 CLI 也需要能啟動/連接瀏覽器（或接受手動 cookie 匯入的 `--manual`/`--file` 路徑）。 gemini-notebook-mcp-cli:12-17 

Wiki pages you might want to explore:
- [Getting Started (jacob-bd/gemini-notebook-mcp-cli)](/wiki/jacob-bd/gemini-notebook-mcp-cli#1.1)
- [Utilities and Platform Support (jacob-bd/gemini-notebook-mcp-cli)](/wiki/jacob-bd/gemini-notebook-mcp-cli#7)

### Citations

**File:** src/notebooklm_tools/cli/main.py (L427-484)

```python
@login_app.callback(invoke_without_command=True)
def login_callback(
    ctx: typer.Context,
    manual: bool = typer.Option(
        False,
        "--manual",
        "-m",
        help="Manually provide cookies from a file",
    ),
    check: bool = typer.Option(
        False,
        "--check",
        help="Only check if current auth is valid",
    ),
    profile: str | None = typer.Option(
        None,
        "--profile",
        "-p",
        help="Profile name (uses config default if not specified)",
    ),
    cookie_file: str | None = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to file containing cookies (for manual mode)",
    ),
    provider: str = typer.Option(
        "builtin",
        "--provider",
        help="Auth provider: builtin (default) or openclaw",
    ),
    cdp_url: str = typer.Option(
        "http://127.0.0.1:18800",
        "--cdp-url",
        help="CDP endpoint URL for external provider mode",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force overwrite even if profile has credentials for a different account",
    ),
    clear: bool = typer.Option(
        False,
        "--clear",
        help="Delete the localized browser profile data before logging in, to switch Google accounts",
    ),
    wsl: bool = typer.Option(
        False,
        "--wsl",
        help="Launch Windows Chrome from WSL (fixes terminal corruption on WSL2)",
    ),
    storage: str | None = typer.Option(
        None,
        "--storage",
        help="Where to keep the saved login for a NEW profile: 'protected' (OS keystore, "
        "recommended) or 'file'. Skips the question.",
    ),
) -> None:
```

**File:** src/notebooklm_tools/cli/main.py (L731-799)

```python
        elif provider == "openclaw" or (provider == "builtin" and cdp_url != _BUILTIN_CDP_DEFAULT):
            # External CDP path: connect to an already-running browser.
            # Triggered by --provider openclaw OR when the user explicitly
            # passes a --cdp-url (indicating they have a running Chrome).
            label = "openclaw" if provider == "openclaw" else "builtin (external CDP)"
            console.print("[bold]Using external CDP authentication[/bold]")
            console.print(f"[dim]Provider: {label} | CDP: {cdp_url}[/dim]\n")

            result = extract_cookies_via_existing_cdp(
                cdp_url=cdp_url,
                wait_for_login=True,
                login_timeout=300,
            )
        else:
            backend = select_auth_backend()
            if backend is None:
                extract_cookies_via_browser(profile_name=profile, clear_profile=clear)
                raise AssertionError("Authentication backend unexpectedly returned no result")

            managed_browser_backend = backend["backend"]
            managed_browser_name = backend["browser"]
            if managed_browser_backend == "firefox_profile":
                console.print("[bold]Launching Firefox for authentication...[/bold]")
                console.print("[dim]Using an isolated Firefox profile[/dim]\n")
                result, _ = extract_cookies_via_browser(
                    profile_name=profile,
                    clear_profile=clear,
                    preferred="firefox",
                )
            else:
                from notebooklm_tools.utils.cdp import get_chrome_path
                from notebooklm_tools.utils.config import (
                    check_migration_sources,
                    get_storage_dir,
                    run_migration,
                )

                get_chrome_path()
                console.print(
                    f"[bold]Launching {managed_browser_name} for authentication...[/bold]"
                )
                console.print("[dim]Using Chrome DevTools Protocol[/dim]\n")

                chrome_profile = get_storage_dir() / "chrome-profile"
                profile_exists = chrome_profile.exists() and (
                    (chrome_profile / "Default").exists()
                    or (chrome_profile / "Local State").exists()
                )
                if not profile_exists and not clear:
                    sources = check_migration_sources()
                    if sources["chrome_profiles"]:
                        console.print(
                            "[yellow]Found Chrome profile from legacy installation![/yellow]"
                        )
                        for src in sources["chrome_profiles"]:
                            console.print(f"  [dim]{src}[/dim]")
                        console.print("[dim]Migrating to new location...[/dim]")
                        for action in run_migration(dry_run=False):
                            console.print(f"  [green]✓[/green] {action}")
                        console.print()

                console.print(f"Starting {managed_browser_name}...")
                result = extract_cookies_via_cdp(
                    auto_launch=True,
                    wait_for_login=True,
                    login_timeout=300,
                    profile_name=profile,
                    clear_profile=clear,
                )
```

**File:** src/notebooklm_tools/cli/main.py (L891-904)

```python
                _save_with_storage_choice(
                    profile,
                    choice,
                    lambda: auth.save_profile(
                        cookies=cookies,
                        csrf_token=csrf_token,
                        session_id=session_id,
                        email=email,
                        force=True,  # Allow overwrite on retry
                        build_label=build_label,
                        base_host=base_host,
                        browser_backend=managed_browser_backend or None,
                    ),
                )
```

**File:** src/notebooklm_tools/utils/cdp.py (L101-125)

```python
def get_notebooklm_url() -> str:
    """Return the browser URL used to authenticate the configured account."""
    base_url = get_base_url()
    host = (urlparse(base_url).hostname or "").lower()
    enterprise_hosts = {
        "notebooklm.cloud.google.com",
        "notebook.cloud.google.com",
        "vertexaisearch.cloud.google.com",
    }
    if host not in enterprise_hosts:
        return f"{base_url}/"

    project_id = get_enterprise_project_id()
    if not project_id:
        raise ValueError(
            "NOTEBOOKLM_PROJECT_ID is required when authenticating Gemini Notebook Enterprise."
        )
    location = get_enterprise_location()
    prefix = (
        f"/notebooklm/{location}" if host == "vertexaisearch.cloud.google.com" else f"/{location}"
    )
    return f"{base_url}{prefix}/?project={quote(project_id, safe='')}"


NOTEBOOKLM_URL = get_notebooklm_url()
```
**File:** src/notebooklm_tools/utils/cdp.py (L1927-1954)
```python
def _run_headless_auth_unlocked(
    port: int = 9223,
    timeout: int = 30,
    profile_name: str = "default",
    expected_revision: str | None = None,
    force: bool | None = None,
    raise_on_error: bool = False,
    expected_file_fingerprint: str | None = None,
) -> "Any | None":
    """Run authentication in headless mode (no user interaction).

    This only works if the Chrome profile already has saved Google login.
    The Chrome process is automatically terminated after token extraction.

    Used for automatic token refresh when cached tokens expire.

    Args:
        port: Chrome DevTools port (use different port to avoid conflicts)
        timeout: Maximum time to wait for auth extraction
        profile_name: The profile name to use for Chrome
        expected_revision: Optional expected revision for compare-and-save
        force: If True, overwrite without revision check
        raise_on_error: If True, surface safe browser infrastructure failures
            instead of collapsing them to None.

    Returns:
        AuthTokens if successful, None if failed or no saved login
    """
```

**File:** src/notebooklm_tools/utils/cdp.py (L2155-2207)

```python
def run_headless_auth(
    port: int = 9223,
    timeout: int = 30,
    profile_name: str = "default",
    expected_revision: str | None = None,
    force: bool | None = None,
    raise_on_error: bool = False,
    expected_file_fingerprint: str | None = None,
) -> "Any | None":
    """Serialize headless recovery per profile across CLI and MCP processes.

    A second caller reuses a validated credential revision saved by the winner
    instead of launching a second browser against the same Google session.
    Locks are separate from credential-storage locks to avoid nesting them
    across the browser/network operation.
    """
    from filelock import FileLock
    from filelock import Timeout as FileLockTimeout

    from notebooklm_tools.core.auth import auth_state_fingerprint, load_cached_tokens
    from notebooklm_tools.utils.config import get_storage_dir, validate_profile_name

    validate_profile_name(profile_name, strict=False)
    before = load_cached_tokens(profile_name=profile_name)
    before_revision = expected_revision or getattr(before, "revision", None)
    before_file_fingerprint = auth_state_fingerprint(before)
    before_extracted = getattr(before, "extracted_at", 0) or 0
    lock_dir = get_storage_dir() / "locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    lock = FileLock(lock_dir / f"{profile_name}.recovery.lock", timeout=max(1, timeout))

    try:
        with lock:
            updated = load_cached_tokens(profile_name=profile_name)
            revision_changed = updated is not None and (
                (before_revision is not None and updated.revision != before_revision)
                or (before_revision is None and (updated.extracted_at or 0) > before_extracted)
            )
            if (
                not force
                and revision_changed
                and _validate_headless_candidate(updated, profile_name)
            ):
                return updated
            return _run_headless_auth_unlocked(
                port=port,
                timeout=timeout,
                profile_name=profile_name,
                expected_revision=before_revision,
                force=force,
                raise_on_error=raise_on_error,
                expected_file_fingerprint=before_file_fingerprint,
            )
```

**File:** src/notebooklm_tools/core/auth.py (L257-262)

```python
    """Save tokens to a profile and mirror the configured default to auth.json in file mode.

    Takes the profile lock first to serialize with concurrent migrations or saves.
    Writes root mirror only for file-mode configured default profile.
    Propagates all errors without swallowing.
    """
```

**File:** src/notebooklm_tools/core/auth.py (L299-348)

```python
        if disk_mode == "file" and target_profile == default_profile:
            root_cache = get_cache_path()
            # The root cache is a legacy mirror, never an authority over an
            # existing profile. Reject a stale mirror being written back even
            # when force=True (which only bypasses account replacement checks).
            manager = get_auth_manager(target_profile)
            if root_cache.exists() and manager.profile_exists():
                try:
                    mirrored = _read_json_with_windows_retry(root_cache)
                except (OSError, ValueError):
                    mirrored = None
                if isinstance(mirrored, dict) and mirrored.get("cookies") == tokens.cookies:
                    current = manager.load_profile(force_reload=True)
                    if current.cookies != tokens.cookies:
                        from notebooklm_tools.core.credential_store import StaleRevisionError

                        raise StaleRevisionError(target_profile, "stale-root-mirror", None)
            root_data = {
                "cookies": tokens.cookies,
                "csrf_token": tokens.csrf_token or "",
                "session_id": tokens.session_id or "",
                "build_label": tokens.build_label or "",
                "base_host": tokens.base_host or "",
                "email": "",
            }
            meta_path = get_profile_dir(target_profile, create=False) / "metadata.json"
            if meta_path.exists():
                with contextlib.suppress(Exception):
                    m = json.loads(meta_path.read_text(encoding="utf-8"))
                    if isinstance(m, dict) and m.get("email"):
                        root_data["email"] = m["email"]

        manager = get_auth_manager(target_profile)
        saved_profile = manager.save_profile(
            cookies=tokens.cookies,
            csrf_token=tokens.csrf_token or None,
            session_id=tokens.session_id or None,
            build_label=tokens.build_label or None,
            base_host=tokens.base_host or None,
            force=force,
            expected_revision=expected_revision,
        )
        # Publish the legacy root mirror only after the canonical profile save
        # succeeds. A rejected or failed profile write must not publish tokens.
        if disk_mode == "file" and target_profile == default_profile:
            _atomic_write_json(root_cache, root_data)

    if not silent:
        logger.info(f"Auth tokens cached for profile '{target_profile}'")
    return getattr(saved_profile, "revision", None)
```

**File:** src/notebooklm_tools/core/auth.py (L351-375)

```python
def extract_tokens_via_chrome_devtools() -> AuthTokens | None:
    """
    Extract auth tokens using Chrome DevTools.

    This function assumes Chrome DevTools MCP is available and connected
    to a Chrome browser. It will:
    1. Navigate to notebooklm.google.com
    2. Check if logged in
    3. If not, wait for user to log in
    4. Extract cookies and CSRF token

    Returns:
        AuthTokens if successful, None otherwise
    """
    # This is a placeholder - the actual implementation would use
    # Chrome DevTools MCP tools. Since we're inside an MCP server,
    # we can't directly call another MCP's tools.
    #
    # Instead, we'll provide a CLI command that can be run separately
    # to extract and cache the tokens.

    raise NotImplementedError(
        "Direct Chrome DevTools extraction not implemented. "
        "Use the 'nlm login' CLI command instead."
    )
```

**File:** docs/AUTHENTICATION.md (L10-30)

```markdown
## Overview

Gemini Notebook uses browser cookies for authentication (there is no official API). The CLI/MCP extracts these cookies automatically from a managed browser session:

- Chromium-family browsers use Chrome DevTools Protocol (CDP)
- Firefox uses an isolated profile and reads its cookie store directly (no CDP or WebDriver required)

**Supported browsers**: Google Chrome, Arc (macOS), Dia (macOS) Brave, Microsoft Edge, Microsoft Edge Beta, Chromium, Firefox, Vivaldi, Opera.

On Windows, standalone Chromium is discovered in the standard machine-wide
locations under `C:\Program Files` and `C:\Program Files (x86)`, plus the
per-user `%LOCALAPPDATA%\Chromium\Application\chrome.exe` location. You can
select it explicitly with `nlm config set auth.browser chromium`.

**Two authentication methods are available:**

| Method                   | Best For                        | Requires                        |
| ------------------------ | ------------------------------- | ------------------------------- |
| **Auto Mode** (default)  | Most users                      | Any supported browser installed |
| **File Mode** (`--file`) | Complex setups, troubleshooting | Manual cookie extraction        |

```

**File:** docs/AUTHENTICATION.md (L58-71)

```markdown
Chromium/CDP login waits up to 300 seconds for sign-in. A page at
`notebook.google.com`, an HTTP 200 response, or an anonymous `NID` cookie does
not prove authentication. Login waits for signed-in Google cookies and the
app's CSRF token before saving credentials or reporting success. A timeout
does not save anonymous credentials or replace an existing saved login.

### What Happens Behind the Scenes

1. The first available supported browser is detected (or your preferred browser if configured)
2. A dedicated browser profile is created for authentication
3. The browser launches with the appropriate automation backend
4. You log in to Gemini Notebook via the browser
5. Signed-in cookies and the CSRF token are extracted and cached; session fields are refreshed automatically when needed
6. Builtin login closes the browser it launched after successful extraction. Externally managed CDP browsers remain open.
```
**File:** CONTRIBUTING.md (L45-50)
```markdown
**This layering is non-negotiable:**

- `cli/` and `mcp/` are thin wrappers. They handle UX concerns (prompts, spinners, JSON responses) and delegate everything to `services/`
- `services/` contains all business logic, validation, and error handling. Returns typed dicts.
- `cli/` and `mcp/` must **never** import from `core/` directly. Always go through `services/`
- `services/` raises `ServiceError` / `ValidationError`. Never raw exceptions.
```

## Q2

如果我想要撰寫一個新的 CLI 想要取用此專案登入 google 帳號的部份，該從哪一個程式碼開始？

## Google 帳號登入流程（nlm login）

涵蓋新 CLI 複用 Google 登入所需的完整路徑：CLI 入口分流、Chromium CDP 擷取、Firefox/外部 CDP 替代路徑、憑證儲存與無頭刷新。重點位置：[1a] CLI 入口、[2b] CDP 擷取主函式、[4b] AuthManager.save_profile、[5b] 無頭刷新鎖。

### 1. CLI 入口與登入路徑分流

nlm login 指令的入口，依 --provider/--cdp-url/瀏覽器偵測分流到三條擷取路徑。是其他所有 trace 的上游。

### 1a. login_callback 入口 (`main.py:428`)

nlm login 的 Typer callback，解析 --manual/--check/--provider/--cdp-url/--profile/--storage 等選項

```text
def login_callback(ctx: typer.Context, manual: bool, ..., provider: str = "builtin", cdp_url: str = "http://127.0.0.1:18800", ...)
```
### 1b. 外部 CDP 路徑 (`main.py:739`)

--provider openclaw 或自訂 --cdp-url 時，連接已在執行的瀏覽器

```text
result = extract_cookies_via_existing_cdp(cdp_url=cdp_url, wait_for_login=True, login_timeout=300)
```
### 1c. 選擇 auth backend (`main.py:745`)

偵測可用瀏覽器，決定走 firefox_profile 或 chromium_cdp

```text
backend = select_auth_backend()
```
### 1d. Firefox 路徑 (`main.py:753`)

backend 為 firefox_profile 時，用隔離 Firefox profile 登入

```text
result, _ = extract_cookies_via_browser(profile_name=profile, clear_profile=clear, preferred="firefox")
```

### 1e. Chromium CDP 路徑（預設） (`main.py:789`)

啟動受管 Chrome，透過 CDP 等待登入並擷取 cookies

```text
result = extract_cookies_via_cdp(auto_launch=True, wait_for_login=True, login_timeout=300, profile_name=profile, clear_profile=clear)
```

### 2. Chromium CDP cookie 擷取

預設登入路徑的核心：瀏覽器選擇 → 啟動受管 Chrome → CDP 連線 → 等待登入 → 取 cookies/CSRF token。

### 2a. select_auth_backend 選擇 Chromium (`auth_browser.py:61`)

依 config auth.browser 偏好找 Chrome/Arc/Edge/Brave 等 Chromium 系瀏覽器

```text
chromium_path = _get_chromium_path(preferred if preferred in CHROMIUM_BROWSER_KEYS else "auto")
```

### 2b. extract_cookies_via_browser 委派 CDP (`auth_browser.py:114`)

統一入口，依 backend 分派到 CDP 或 Firefox 實作

```text
result = extract_cookies_via_cdp(auto_launch=True, wait_for_login=wait_for_login, login_timeout=login_timeout, profile_name=profile_name, clear_profile=clear_profile)
```
### 2c. 複用已存在的 NLM Chrome (`cdp.py:1577`)

先找是否已有帶 remote-debugging 的受管 Chrome 實例

```text
existing_port, debugger_url = find_existing_nlm_chrome(profile_name=profile_name)
```
### 2d. 啟動受管 Chrome (`cdp.py:1615`)

以每個 profile 專屬的 user-data-dir 啟動 Chrome 並開啟 CDP port

```text
if not launch_chrome(port, profile_name=profile_name):
```
### 2e. 輪詢 CDP endpoint (`cdp.py:1632`)

最多等 30 秒等 Chrome 暴露 DevTools endpoint，含 Windows handoff 處理

```text
debugger_url = get_debugger_url(port, tries=1, timeout=1)
```
### 2f. 從頁面擷取 cookies (`cdp.py:1687`)

導向 NotebookLM URL，等待已登入 Google cookies 與 CSRF token（最長 300s）

```text
result = extract_cookies_from_page(_cdp_http_base(port), wait_for_login, login_timeout)
```
### 2g. get_notebooklm_url 決定登入目標 (`cdp.py:122`)

依 base_url 判斷一般版或 Enterprise host，組出登入頁 URL

```text
return f"{base_url}{prefix}/?project={quote(project_id, safe='')}"
```
### 3. Firefox 與外部 CDP 替代路徑

非 Chromium 的兩條路徑：Firefox 直接讀隔離 profile 的 cookie store；外部 CDP 連接已由外部管理的瀏覽器。

### 3a. 選擇 Firefox backend (`auth_browser.py:56`)

auth.browser=firefox 或 auto 且無 Chromium 時選 Firefox

```text
if preferred == FIREFOX_BROWSER_KEY: if get_firefox_path(): return {"backend": "firefox_profile", "browser": "Firefox"}
```

### 3b. Firefox cookie 擷取 (`auth_browser.py:104`)

啟動隔離 Firefox profile，登入後直接讀取 cookie store（不需 CDP/WebDriver）

```text
result = extract_cookies_via_firefox(wait_for_login=wait_for_login, login_timeout=login_timeout, profile_name=profile_name, clear_profile=clear_profile)
```
### 3c. 外部 CDP 擷取 (`cdp.py:1692`)

連到已執行的 Chrome CDP endpoint（如 OpenClaw 管理的瀏覽器），瀏覽器生命週期由外部負責

```text
def extract_cookies_via_existing_cdp(cdp_url: str, wait_for_login: bool = True, login_timeout: int = 300)
```
### 4. 憑證儲存（services → core）

擷取到的 cookies/CSRF token 經 services 層存入 profile 目錄；新 CLI 應使用此層而非直接 import core。

### 4a. CLI 呼叫 save_profile (`main.py:893`)

擷取成功後，依使用者選擇的 storage 模式（protected/file）儲存

```text
lambda: auth.save_profile(cookies=cookies, csrf_token=csrf_token, session_id=session_id, email=email, force=True, build_label=build_label, base_host=base_host, browser_backend=managed_browser_backend or None)
```
### 4b. services 層 re-export (`auth.py:90`)

cli/mcp 不可直接 import core，須經此 shim（lazy resolve 以支援 monkeypatch）

```text
def save_tokens_to_cache(tokens, silent=False, profile_name=None, expected_revision=None, force=True): return _core_auth.save_tokens_to_cache(tokens, silent=silent, **kwargs)
```
### 4c. AuthManager.save_profile 寫入 profile (`auth.py:334`)

在 profile lock 下寫入 ~/.notebooklm-mcp-cli/profiles/<name>/，含 revision 比較以防 stale 覆寫

```text
saved_profile = manager.save_profile(cookies=tokens.cookies, csrf_token=tokens.csrf_token or None, ..., force=force, expected_revision=expected_revision)
```
### 4d. 寫入 legacy root mirror (`auth.py:345`)

file 模式的預設 profile 會額外原子寫入 auth.json 鏡像（僅在 profile 儲存成功後）

```text
if disk_mode == "file" and target_profile == default_profile: _atomic_write_json(root_cache, root_data)
```
### 5. 無頭 session 刷新

已登入的 profile 過期時，無互動地用已存 Chrome profile 重新取 token，以 per-profile file lock 序列化。

### 5a. auth_browser 的 headless 入口 (`auth_browser.py:136`)

依 profile 儲存的 browser_backend 選擇 headless 刷新路徑

```text
def run_headless_auth(profile_name="default", timeout=30, expected_revision=None, force=None, ...)
```
### 5b. per-profile recovery lock (`cdp.py:2183`)

序列化 CLI/MCP 多進程的並發刷新；第二個 caller 複用 winner 已存的 revision

```text
lock = FileLock(lock_dir / f"{profile_name}.recovery.lock", timeout=max(1, timeout))
```
### 5c. 執行無頭擷取 (`cdp.py:2200`)

啟動 headless Chrome 用已存 Google session 重取 token，完成後自動關閉瀏覽器

```text
return _run_headless_auth_unlocked(port=port, timeout=timeout, profile_name=profile_name, expected_revision=before_revision, force=force, ...)
```

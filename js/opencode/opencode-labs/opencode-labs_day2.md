<div style="background-color:lightyellow;">

## Day 2: Navigating the TUI & The "Plan-First" Workflow

### 1. Launching into "Project Mode"

Always launch OpenCode from the root of a project. This gives the agent the correct "context" of your file structure.

1. Open your Ubuntu terminal.
2. Navigate to your lab folder: `cd ~/opencode-lab`
3. Launch the interface: `opencode`

---

### 2. The Power of "Plan Mode" vs. "Build Mode"

In the TUI, you will see a toggle (usually at the top or switched via `Tab`).

* **Plan Mode (The Architect):** The agent can read files, search the web, and suggest logic, but it **cannot** write to your disk. It’s "Read-Only." Use this to brainstorm or explore.
* **Build Mode (The Engineer):** The agent has "Write" permissions. It can create files, delete code, and run terminal commands.

**The Golden Rule:** Never start in Build Mode. Always ask for a plan first to save your API tokens and prevent unwanted code changes.

---

### 3. Mastering the "@" Mentions

Just like on Discord or Slack, OpenCode uses the `@` symbol to focus the AI's "eyes" on specific things. Try these in the chat box:

* **`@file`**: Type `@` followed by a filename (e.g., `@sys_info.py`) to attach that specific file to your prompt.
* **`@folder`**: Attach an entire directory for context.
* **`@terminal`**: Sends the recent output of your terminal to the AI (great for debugging errors).
* **`@web`**: (If enabled) tells the agent to search the internet for documentation.

---

### 4. Hands-on Lab: The "Discovery" Exercise

Let’s practice navigating a small codebase without writing a single line of code yet.

1. **Step A (Setup):** In your terminal, quickly grab a tiny sample project:

```bash
git clone https://github.com/huggingface/chat-ui-template.git test-repo
cd test-repo
opencode .
```


2. **Step B (Plan Mode):** Switch to **Plan Mode**. Ask the agent:

> "I'm new here. Using `@test-repo`, can you explain the project structure and tell me where the main entry point for the API is?"


3. **Step C (Deep Dive):** Once it answers, use the `@` mention for the specific file it suggested:

> "Looking at `@src/lib/server/api.ts` (or whatever file it found), what environment variables do I need to set up to make this work?"

---

### 5. Essential Keyboard Shortcuts

To move fast in the OpenCode TUI, memorize these three:

| Shortcut | Action |
| --- | --- |
| `Tab` | Switch between Plan and Build modes |
| `Ctrl + C` | Cancel a running agent process (if it starts looping) |
| `Ctrl + L` | Clear the chat history to refresh the context window |
| `/` | Open the command menu (Connect, Settings, Clear) |

---

## Day 2 Success Checklist

* [ ] You successfully navigated between **Plan** and **Build** modes.
* [ ] You used the **`@`** symbol to reference a specific file.
* [ ] You understood why the agent recommended a specific file without it editing your code.

</div>

-----

<div style="background-color:lightgreen;">

## 實測 #1

</div>

- 步驟中的 HuggingFace 測試 git repo 已經不存在
```bash
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ git clone https://github.com/huggingface/chat-ui-template.git test-repo
Cloning into 'test-repo'...
remote: Repository not found.
fatal: repository 'https://github.com/huggingface/chat-ui-template.git/' not found
```
- 查了一下，可能已經更名為 https://github.com/huggingface/chat-ui
- 所以把步驟改成
```bash
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ git clone https://github.com/huggingface/chat-ui test-repo
Cloning into 'test-repo'...
remote: Enumerating objects: 28881, done.
remote: Counting objects: 100% (1379/1379), done.
remote: Compressing objects: 100% (492/492), done.
remote: Total 28881 (delta 1143), reused 904 (delta 885), pack-reused 27502 (from 2)
Receiving objects: 100% (28881/28881), 10.40 MiB | 19.02 MiB/s, done.
Resolving deltas: 100% (19739/19739), done.
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ cd test-repo/
@jazzwang ➜ .../js/opencode/opencode-labs/test-repo (main) $ opencode .
```
- 原本這一段 prompt 也不太合理，如果已經進到 `test-erpo` 子目錄底下才啟動 opencode，那就沒辦法用 `@test-repo` 來指定 `test-erpo` 子目錄
```
> "I'm new here. Using `@test-repo`, can you explain the project structure and tell me where the main entry point for the API is?"
```
- 因為 test-repo 內容可能不一樣，所以把 prompt 改成
```
Looking at @src/lib/server/apiToken.ts , what environment variables do I need to set up to make this work?
```
- 結果：
<div  style="background-color:lightgray;">

Based on `apiToken.ts`, you need these environment variables:

**If using user authentication:**
- `USE_USER_TOKEN=true` - Uses the authenticated user's token

**Otherwise (for API access):**
- `OPENAI_API_KEY` - Primary API key (used if `USE_USER_TOKEN` is not "true")
- `HF_TOKEN` - Fallback token (used if `OPENAI_API_KEY` is not set)

The priority order is:
1. User token (if `USE_USER_TOKEN=true` and user is authenticated)
2. `OPENAI_API_KEY`
3. `HF_TOKEN`

</div>

-----

<div style="background-color:lightyellow;">
For **Day 2**, we are moving from "Can I run this?" to "How do I control this?" This lab, titled **"Operation: Code Scout,"** focuses on using OpenCode as a high-level architect before you ever let it touch your source code.

---

## Day 2 Lab: Operation "Code Scout"

In this lab, you will explore a "mystery" codebase, map its dependencies, and simulate a debugging session using context mentions.

### Phase 1: The Setup

We need a project with enough files to be interesting but small enough to keep your head from spinning.

1. **Open Ubuntu WSL.**
2. **Clone this small FastAPI project** (a common web framework):

```bash
git clone https://github.com/tiangolo/full-stack-fastapi-template.git day2-lab
cd day2-lab/backend
```

3. **Launch OpenCode:**

```bash
opencode .
```
---

### Phase 2: The Architect's Walkthrough (Plan Mode)

Your goal is to understand the project without writing a single line of code.

1. **Switch to Plan Mode:** Press `Tab` until the UI indicates you are in **Plan** or **Architect** mode.
2. **The Scout Prompt:** Type the following:

> "Summarize the directory structure of this backend. What is the main entry point where the app starts, and which database is being used?"


3. **Verify the Context:** Note how OpenCode reads the `pyproject.toml` or `requirements.txt` to answer the database question.

---

### Phase 3: Surgical Context with `@`

Now, let’s test how well OpenCode can "see" specific files you point at.

1. **The Target:** Find a file related to "users" or "models" (likely in `app/models/`).
2. **The Context Prompt:** Use the `@` symbol to reference it:

> "Look at `@app/models/user.py`. Explain the relationship between the `User` model and any other models in this project. Does it have a one-to-many relationship with anything?"

3. **The Multi-File Prompt:** Ask it to compare two files:

> "Compare `@app/schemas/user.py` and `@app/models/user.py`. Why do we have two different files for the same 'User' entity?"

---

### Phase 4: The Detective (Terminal Integration)

The agent can see what's happening in your terminal. Let's simulate a "failed" environment check.

1. **Try to run the app (it will likely fail due to missing dependencies):**

```bash
python3 -m app.main
```

2. **Use `@terminal`:** In the OpenCode chat, type:

> "I just tried to run the app and got an error. Look at `@terminal` and tell me which library I am missing and how to install it in this WSL environment."

---

### Phase 5: The "Dry Run" Challenge

Before finishing, ask the agent to **plan** a change without **executing** it.

1. **The Challenge Prompt:**

> "I want to add a 'phone_number' field to the User model. In **Plan Mode**, give me a step-by-step list of every file I would need to modify to make this work, from the database model to the API schema."

2. **The Review:** Read the plan. Does it make sense? Did it miss the migration file? This is where you develop your "AI Oversight" skills.

---

### Day 2 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully toggled into **Plan Mode** | ☐ |
| Used **`@file`** to analyze a specific script | ☐ |
| Used **`@terminal`** to diagnose a shell error | ☐ |
| Received a multi-step plan without any files being edited | ☐ |

---

**How did OpenCode handle the "Phone Number" plan? Did it feel like it "understood" the full stack, or did it miss a spot?** When you're ready, we can move to **Day 3: The Project Brain**, where we learn how to configure `AGENTS.md` to make the AI follow your specific rules!

</div>

-----

<div style="background-color:lightgreen;">

## 實測 #2

</div>

- 在 Github Codespace 上測試：

```bash
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ cd /tmp
@jazzwang ➜ /tmp $ git clone https://github.com/tiangolo/full-stack-fastapi-template.git day2-lab
@jazzwang ➜ /tmp $ cd day2-lab/backend/
@jazzwang ➜ /tmp/day2-lab/backend (master) $ opencode .
```

### Phase 2: The Architect's Walkthrough (Plan Mode)

- 按 `TAB` 切換到 `Plan Mode`

- Prompt

```
Summarize the directory structure of this backend. What is the main entry point where the app starts, and which database is being used?
```

- 錯誤訊息：

```
Error: certificate is not yet valid
```

- 用 `/export` 匯出紀錄也看不到是什麼錯誤。切換了 `kimi-k2.5-free` 跟 `minimax-m2.5-free` 都是類似的錯誤。改用本地端 Windows 11 的環境試試看

```bash
/tmp$ git clone https://github.com/tiangolo/full-stack-fastapi-template.git day2-lab
/tmp$ cd day2-lab/backend
/tmp/day2-lab/backend$ opencode .
```

- 這台有設定 Gemini 2.5 ，就正常有結果了。
- 結果：

This backend application has the following directory structure:

*   `alembic.ini`: Alembic configuration.
*   `app/`: Contains the main application logic, including:
    *   `alembic/`: Alembic migration scripts.
    *   `api/`: API endpoints.
    *   `core/`: Core configurations (e.g., `config.py`).
    *   `crud.py`: Database CRUD operations.
    *   `email-templates/`: Email templates.
    *   `main.py`: The main entry point.
    *   `models.py`: SQLAlchemy database models.
*   `Dockerfile`: Dockerization setup.
*   `pyproject.toml`: Project dependencies and metadata.
*   `README.md`: Project documentation.
*   `scripts/`: Utility scripts.
*   `tests/`: Application tests.

The main entry point of the application is `app/main.py`, which sets up a FastAPI application.

The database being used is **PostgreSQL**, as indicated by the `PostgresDsn` type in `app/core/config.py` and the `SQLALCHEMY_DATABASE_URI` configuration, along with the presence of Alembic for database migrations.

### Phase 3: Surgical Context with @

- Prompt

```
Look at @app\api\routes\users.py . Explain the relationship between the User model and any other models in this project. Does it have a one-to-many relationship with anything?
```

- 結果：

#### Assistant (`Plan` · `gemini-2.5-flash` · 6.1s)

**Analyzing User Model Relationships**

I've examined the `app/models.py` file. I'm focusing on the `User` model and its connections to other models. Specifically, I'm analyzing the relationships between the `User` and other entities based on the code provided in lines 49-56, with a focus on how the relationships are structured.


**Examining User-Item Relationships**

I've confirmed the one-to-many relationship between `User` and `Item` based on the `app/models.py` file, as highlighted in lines 49-56, and lines 87-96. The `User` model, through its `items` relationship, links to multiple `Item` instances. The `Item` model, in turn, establishes a foreign key (`owner_id`) back to a single `User`. I'm now exploring the implications of `cascade_delete=True` on the `items` relationship.



**Clarifying Item-User Ownership**

I've just confirmed the one-to-many relationship between `User` and `Item` after examining `app/models.py`. A user can have many items, as shown by the `items` relationship in the `User` model, which links to multiple `Item` instances. This is supported by the `owner_id` foreign key in the `Item` model, which references a single `User`. I'm now certain about this relationship.

The `User` model has a one-to-many relationship with the `Item` model. Each user can own multiple items, and each item belongs to a single user.

Other models like `UserCreate`, `UserPublic`, `UpdatePassword`, `Message`, `Token`, `TokenPayload`, and `NewPassword` are Pydantic models for data handling and do not represent direct database relationships with the `User` model.

- 備註：原本 Gemini 規劃的 Lab2 實驗要比較兩個檔案，不過路徑不正確，就先忽略了。
```
Compare @app/schemas/user.py and @app/models/user.py. Why do we have two different files for the same 'User' entity?
```

### Phase 4: The Detective (Terminal Integration)

- 懷疑這部份有幻覺，因為找不到 `@terminal` 可以用

### Phase 5: The "Dry Run" Challenge

- Prompt: 略修正原始的 Prompt，移除 "In Plan Mode, "

```
I want to add a 'phone_number' field to the User model. give me a step-by-step list of every file I would need to modify to make this work, from the database model to the API schema.
```

- 結果：

#### Assistant (`Plan` · `gemini-2.5-flash` · 6.7s)

**Analyzing CRUD Implementation**

I've located `app/crud.py` and am focusing on how user creation and updates are implemented, specifically how the `phone_number` field is handled in these functions. I need to understand this to ensure the correct modifications are made.


**Confirming Modifications Needed**

I've determined the exact modifications needed across several files. It looks like `app/models.py` needs updating to include `phone_number` in `UserBase`, `UserRegister`, `UserUpdateMe`, and `UserPublic` models. Then, I need to modify `app/crud.py` to handle persisting and updating this field during user creation and updates. Finally, I'll need to generate and apply a database migration. I'll double check `app/api/routes/users.py` to ensure no changes are needed there as the models are imported.


**Outlining Next Steps**

Now, I've outlined the precise modifications across `app/models.py` and `app/crud.py`, providing specific details for the `phone_number` field. This list includes adding the field to various models and functions. I've also outlined the migration steps using Alembic and a verification step for `app/api/routes/users.py`, ensuring all components work in harmony.

Here's a step-by-step list of every file you would need to modify to add a 'phone_number' field to the User model, from the database model to the API schema:

1.  **`app/models.py`**:
    *   Add `phone_number: str | None = Field(default=None, max_length=20)` to the `UserBase` class. This will ensure the field is available in the base schema and inherited by other related models.
    *   Add `phone_number: str | None = Field(default=None, max_length=20)` to the `UserRegister` class.
    *   Add `phone_number: str | None = Field(default=None, max_length=20)` to the `UserUpdateMe` class.
    *   Verify that `UserPublic` correctly inherits or explicitly includes the `phone_number` field from `UserBase` to be exposed in API responses.

2.  **`app/crud.py`**:
    *   Update the `create_user` function to ensure it accepts and persists the `phone_number` field when a new user is created.
    *   Update the `update_user` function to ensure it accepts and updates the `phone_number` field when a user's information is modified.

3.  **Database Migration (via Alembic)**:
    *   Run `alembic revision --autogenerate -m "Add phone_number to User model"` in your terminal. This will generate a new migration script in the `app/alembic/versions/` directory.
    *   **Review the generated migration script**: Open the newly created Python file in `app/alembic/versions/` and verify that it correctly includes operations to add a `phone_number` column (e.g., `op.add_column('user', sa.Column('phone_number', sa.String(length=20), nullable=True))`) to the `user` table.
    *   Apply the migration to your database by running `alembic upgrade head` in your terminal.

4.  **`app/api/routes/users.py` (Verification/Implicit Changes)**:
    *   No direct code modifications are typically needed in this file for adding a field, as the API endpoints (`create_user`, `update_user_me`, etc.) use the Pydantic models (like `UserCreate`, `UserUpdateMe`, `UserPublic`) defined in `app/models.py`.
    *   However, after making the changes in `app/models.py` and `app/crud.py`, you should test these API endpoints to ensure they correctly accept `phone_number` in request bodies and return it in response bodies.

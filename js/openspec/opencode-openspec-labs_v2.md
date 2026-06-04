# OpenCode + OpenSpec Labs (15-Day Plan)

> Targets: OpenSpec v1.4+ · OpenCode (latest) · Python 3.11+ · FastAPI · ~1 h/day
> Stack: backend-first · OpenCode-native slash commands (`/opsx:*`) · no MCP, no API keys
> Generated 2026-06-04

This file is a self-contained 15-day hands-on plan to learn OpenSpec end-to-end on top
of the OpenCode TUI, building Python/FastAPI backends. It does **not** reference the
adjacent `opencode-openspec-labs_day1.md` / `_day2.md` files. The previous 5-day
Gemini curriculum is preserved verbatim in **Appendix A** for historical reference.

## 0. Prerequisites (verify once)

```bash
node --version      # >= 20.19.0
python --version    # >= 3.11
pip install "fastapi[standard]" sqlmodel pytest httpx argon2-cffi "pyjwt[crypto]"
openspec --version  # any 1.4.x is fine
opencode --version  # any recent build
```

Scratch root for all labs:

```text
C:\Users\jazzw\git\snippet\js\openspec\lab-day{1..15}\
```

## 0.1 Daily template (~60 min)

- **0-5 min**   read today's section
- **5-15 min**  set up the scratch repo (`mkdir lab-dayN && cd lab-dayN`)
- **15-45 min** run the OpenSpec command(s) of the day
- **45-55 min** append 實測 notes (and resolve any pitfalls)
- **55-60 min** `openspec list` to confirm the change is in the expected state

Hard cap per day: 75 min. If you blow past that, stop and split the work across two days.

---

## Phase 1 — Foundations (Days 1-5)

### Day 1 — Env + Agentic Infrastructure

**Goal:** Stand up a FastAPI-anchored scratch repo, initialize OpenSpec inside it, install
the `opencode-plugin-openspec` so the TUI shows the `openspec-plan` mode, and commit the
initial scaffolding.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** none (Day 1 of 15).

#### Setup

```bash
mkdir "C:\Users\jazzw\git\snippet\js\openspec\lab-day1"
cd       "C:\Users\jazzw\git\snippet\js\openspec\lab-day1"
git init
npm install -g opencode-ai @fission-ai/openspec@latest
openspec --version
```

Expected:

```text
1.4.x
```

#### Walkthrough

**Step 1 — Initialize OpenSpec**

```bash
openspec init
```

Choose `OpenCode` from the interactive picker. After completion you should see:

```text
.
├── AGENTS.md
├── openspec/
│   ├── project.md        # empty template
│   ├── specs/            # source of truth (initially empty)
│   ├── changes/          # active change folders
│   └── archive/
└── opencode.json         # OpenCode project config
```

**Step 2 — Fill `openspec/project.md` with FastAPI context**

Edit `openspec/project.md` so the agent knows the stack on Day 2 onward:

```markdown
# Project Context

## Purpose
A small FastAPI service used as the test bed for the 15-day OpenSpec lab series.

## Tech Stack
- Python 3.11+
- FastAPI (standard extras — uvicorn, httpx)
- SQLModel (Pydantic + SQLAlchemy 2.0) for persistence
- pytest + httpx.AsyncClient for tests
- argon2-cffi for password hashing
- PyJWT for access tokens

## Coding Conventions
- Type hints on every public function.
- Pydantic v2 models in `app/schemas.py`.
- Routers grouped by domain in `app/routers/<domain>.py`.
- Tests in `tests/test_<file>.py`, one test file per module.
- No global mutable state; use FastAPI `Depends`.

## Directory Structure
- `app/main.py`          FastAPI entrypoint
- `app/routers/`         route modules
- `app/schemas.py`       Pydantic models
- `app/db.py`            SQLModel engine + session
- `tests/`               pytest suite
```

**Step 3 — Install the OpenSpec plugin for OpenCode**

Edit `opencode.json` (created by `openspec init`):

```json
{
  "plugin": ["opencode-plugin-openspec"]
}
```

**Step 4 — Launch the TUI and confirm the plan mode**

```bash
opencode
```

You should see the TUI prompt. Toggle to `Plan` mode with **Tab** and confirm the
status bar shows `openspec-plan` (rendered in `#FF6B6B`). The "OpenSpec Architect"
agent should be visible in the agent picker (`Ctrl+Alt+A`).

**Step 5 — First commit**

```bash
git add .
git commit -m "chore: openspec init + fastapi project context"
```

#### 實測 (verification)

```bash
openspec list
```

Expected:

```text
No active changes.
```

```bash
openspec show openspec-plan 2>nul || echo "openspec-plan is a TUI mode, not a CLI change"
```

#### Common pitfalls

- **`openspec: command not found` on Windows** — close and reopen the terminal so the
  updated PATH is loaded.
- **`opencode-plugin-openspec` not appearing in the TUI** — confirm `opencode.json` is
  valid JSON (no trailing commas) and that you launched `opencode` from the project root.
- **`openspec init` hangs** — answer the AI-tool picker quickly; the prompt does not
  have a default.

#### Exit criteria

You are done when `openspec list` prints `No active changes.`, the OpenCode TUI shows
the `openspec-plan` mode in pink, and the initial commit is on disk.

#### References

- Fission-AI/OpenSpec getting-started: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md>
- openspec.dev: <https://openspec.dev/>

---

### Day 2 — Proposal + Delta Specs

**Goal:** Run `/opsx:propose` against a fresh change-id, inspect the generated
`proposal.md` + delta spec, hand-edit a `## MODIFIED Requirements` block, and validate.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 1 complete (a lab-day1 repo with the OpenSpec scaffold).

#### Setup

```bash
cd "C:\Users\jazzw\git\snippet\js\openspec\lab-day1"
```

#### Walkthrough

**Step 1 — Open the TUI and propose a placeholder change**

```bash
opencode
```

In the TUI:

```text
/opsx:propose add-hello-endpoint
```

The agent scaffolds `openspec/changes/add-hello-endpoint/` containing:

```text
openspec/changes/add-hello-endpoint/
├── proposal.md       # why + scope
├── specs/
│   └── api/
│       └── spec.md   # delta spec (ADDED Requirements)
├── design.md         # technical approach
└── tasks.md          # implementation checklist
```

**Step 2 — Inspect the generated proposal**

```bash
openspec show add-hello-endpoint --type proposal
openspec show add-hello-endpoint --type spec
openspec show add-hello-endpoint --type design
openspec show add-hello-endpoint --type tasks
```

The `--type` flag is illustrative; the canonical subcommands are
`openspec list`, `openspec show <change-id>`, and `openspec view <change-id>`.

**Step 3 — Hand-edit a `## MODIFIED Requirements` block**

Open `openspec/changes/add-hello-endpoint/specs/api/spec.md` and add a section that
*modifies* an existing requirement rather than adding a new one. This exercises the
delta-spec discipline before any code is written:

```markdown
## MODIFIED Requirements

### Requirement: Health check
The system SHALL expose a `GET /health` endpoint that returns a JSON object.

#### Scenario: Liveness probe
- GIVEN the service is running
- WHEN a client calls `GET /health`
- THEN the response status is 200
- AND the body is `{"status": "ok", "version": "0.2.0"}`
```

(Previously the body had no `version` field; the MODIFIED block documents the diff.)

**Step 4 — Validate strictly**

```bash
openspec validate add-hello-endpoint --strict
```

Expected:

```text
Change 'add-hello-endpoint' is valid
```

#### 實測

```bash
openspec list
```

Expected:

```text
Changes:
  add-hello-endpoint
```

#### Common pitfalls

- **Change-id conflicts** — if `/opsx:propose` picks a name that already exists in
  `openspec/changes/`, pass an explicit id: `/opsx:propose add-hello-endpoint-2`.
- **`openspec validate` complains about cross-references** — every requirement
  referenced by another requirement must exist in the same change folder.

#### Exit criteria

You are done when `openspec validate add-hello-endpoint --strict` returns
`Change 'add-hello-endpoint' is valid` and the file `specs/api/spec.md` contains
both an `## ADDED Requirements` and a `## MODIFIED Requirements` section.

#### References

- thedocs Quick Start: <https://thedocs.io/openspec/quick_start/>
- OpenSpec spec format conventions: <https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/openspec-conventions/spec.md>

---

### Day 3 — Design + Tasks (Expanded Profile)

**Goal:** Use the Expanded workflow profile to author `design.md` and `tasks.md` by
hand for the change from Day 2, and confirm the dependency-graph ordering
(proposal → specs → design → tasks).

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 2 complete (valid `add-hello-endpoint` change).

#### Walkthrough

**Step 1 — Switch to the Expanded profile**

```bash
openspec config profile
```

Choose `expanded`. From now on `/opsx:new` creates the change skeleton and
`/opsx:continue` produces the next required artifact (design.md, then tasks.md)
one at a time.

**Step 2 — Author `design.md` by hand**

Open `openspec/changes/add-hello-endpoint/design.md` and replace the template with:

```markdown
# Design: add-hello-endpoint

## Approach
Single-file FastAPI router mounted in `app/main.py`. No new dependencies.

## Data model
None. The endpoint is stateless.

## API contract
- `GET /health` → 200 `{"status": "ok", "version": "0.2.0"}`
- `GET /hello?name=<str>` → 200 `{"message": "hello, <name>"}` (default name = `world`)

## Error handling
- 422 if `name` is longer than 64 chars (Pydantic `Query(max_length=64)`).
- No other 4xx/5xx paths.

## Testing
- `tests/test_health.py`: two cases — default + custom name.
- Use `httpx.AsyncClient` against the FastAPI app via `ASGITransport`.
```

**Step 3 — Author `tasks.md` by hand**

```markdown
# Tasks: add-hello-endpoint

## 1. Router module
- [ ] 1.1 Create `app/routers/health.py` with `GET /health` and `GET /hello`
- [ ] 1.2 Add `app/routers/health.py` to `app/main.py` via `app.include_router`

## 2. Tests
- [ ] 2.1 Create `tests/test_health.py` with two `@pytest.mark.asyncio` cases
- [ ] 2.2 Run `pytest -q` and confirm green

## 3. Verification
- [ ] 3.1 `openspec validate add-hello-endpoint --strict`
- [ ] 3.2 `openspec show add-hello-endpoint --type tasks` shows all boxes checked
```

**Step 4 — Confirm the dependency order**

```bash
openspec validate add-hello-endpoint --strict
```

Expected:

```text
Change 'add-hello-endpoint' is valid
```

#### 實測

```bash
openspec show add-hello-endpoint
```

Confirm the output lists all four artifacts and that `design.md` references
the requirement/scenario IDs from `specs/api/spec.md`.

#### Common pitfalls

- **`design.md` written before `specs/` is final** — the Expanded profile blocks
  this by default; if you bypass it, you may need to re-run `/opsx:continue` to
  regenerate the dependent artifact.
- **Tasks too coarse** — anything larger than ~30 min of work should be split.

#### Exit criteria

You are done when `design.md` and `tasks.md` exist with the content above,
`openspec validate --strict` is green, and no task box is checked yet (apply is
Day 4's job).

#### References

- OpenSpec Expanded workflow: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md>

---

### Day 4 — Apply (Build Mode + Subagents)

**Goal:** Run `/opsx:apply` to implement the change from Day 3, practice toggling
between Plan and Build with **Tab**, and invoke `@explore` + `@code-reviewer` in
parallel.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 3 complete (design.md + tasks.md ready, all boxes unchecked).

#### Walkthrough

**Step 1 — Apply the change**

In the OpenCode TUI:

```text
/opsx:apply add-hello-endpoint
```

The agent walks `tasks.md` top-down, ticking each box after it lands a file edit.
Expected log lines:

```text
Working on 1.1: Create app/routers/health.py ... done
Working on 1.2: Wire router into app/main.py ... done
Working on 2.1: Create tests/test_health.py ... done
Working on 2.2: Run pytest -q ... 2 passed
Working on 3.1: openspec validate add-hello-endpoint --strict ... valid
```

**Step 2 — Toggle to Plan mode for a moment**

Press **Tab** to switch to `Plan` mode. Confirm the status bar flips to
`openspec-plan` (pink) and the agent refuses to edit non-spec files. Press **Tab**
again to return to Build.

**Step 3 — Invoke subagents in parallel**

In a single message:

```text
@explore list every file in this repo that imports from `fastapi`
@code-reviewer review app/routers/health.py for unnecessary complexity
```

Both subagents run in parallel because they are read-only. Expected:

```text
@explore: 4 files import from fastapi: app/main.py, app/routers/health.py, tests/test_health.py, ...
@code-reviewer: health.py is 18 lines, no obvious simplifications
```

**Step 4 — Confirm all tasks checked**

```bash
openspec show add-hello-endpoint --type tasks
```

All boxes in `tasks.md` should now be `- [x]`.

#### 實測

```bash
pytest -q
```

Expected:

```text
2 passed in 0.3s
```

#### Common pitfalls

- **Agent stuck in Plan mode after Tab** — toggle twice (sometimes the first press
  is consumed by the input box). Check the status bar color, not the prompt text.
- **Subagent can’t read the project** — `@explore` and `@code-reviewer` are
  read-only by default; if a subagent complains about permissions, you’re
  probably trying to invoke a Build-mode subagent like `@general` in a
  Plan-mode session.

#### Exit criteria

You are done when `pytest -q` is green, every box in `tasks.md` is checked, and
you have at least one log line from `@explore` and one from `@code-reviewer`.

#### References

- OpenCode subagents: <https://opencode.ai/docs/agents/>
- OpenCode tools: <https://opencode.ai/docs/tools/>

---

### Day 5 — Verify + Archive + Customization Primer

**Goal:** Run `/opsx:verify` and `/opsx:archive` on the change from Day 4, then
skim the customization surface (`openspec/schemas/`, `SKILL.md`) without
implementing anything.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 4 complete (apply finished, all task boxes checked).

#### Walkthrough

**Step 1 — Verify**

In the TUI:

```text
/opsx:verify add-hello-endpoint
```

Expected output covers three dimensions:

```text
Completeness: 5/5 tasks checked, 2/2 requirements have implementation
Correctness:  2/2 scenarios pass (pytest)
Coherence:    design.md references match the implemented router layout
```

If any dimension fails, the agent either updates the implementation or the spec.
Do not skip the coherence check — that is what catches "vibe coding" drift.

**Step 2 — Archive**

In the TUI:

```text
/opsx:archive add-hello-endpoint
```

Two things happen:

1. `## ADDED Requirements` blocks are appended to `openspec/specs/api/spec.md`.
2. The change folder is moved to `openspec/changes/archive/2026-06-04-add-hello-endpoint/`.

```bash
openspec list
```

Expected:

```text
No active changes.
```

**Step 3 — Skim the customization surface (no implementation today)**

```bash
ls openspec/schemas/
cat openspec/AGENTS.md
```

Read the schema names. The default is `spec-driven`; the `spec-driven-with-adr`
variant adds an `adr/` directory next to `specs/`. Days 11 and 12 revisit these.

#### 實測

```bash
openspec show add-hello-endpoint --json 2>/dev/null | head -50 || true
```

(Use `--json` if your version supports it; otherwise just confirm the folder is
now under `archive/`.)

#### Common pitfalls

- **Archive silently fails because of a stray untracked file** — run `git status`
  first; OpenSpec refuses to archive if the working tree has uncommitted changes
  that would be lost.
- **The `add-hello-endpoint` change already shows in `openspec list` after archive** —
  you are looking at the wrong list. `openspec list` shows active; archived
  changes are visible via `ls openspec/changes/archive/`.

#### Exit criteria

You are done when `openspec list` reports no active changes, the change folder is
under `openspec/changes/archive/`, and you have a mental model of where custom
schemas and skills will live (Days 11 & 12).

#### References

- OpenSpec CLI reference (`archive`): <https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md>

---

## Phase 2 — Compact Python Labs (Days 6-10)

### Day 6 — Todo API (Greenfield propose → archive)

**Goal:** Use the GIGAZINE kitchen-timer walkthrough as inspiration to build a tiny
`POST/GET/PATCH/DELETE /todos` FastAPI service in a fresh repo, walking the full
`propose → apply → archive` loop in one session.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 5 (you know the full loop end-to-end).

#### Setup

```bash
mkdir "C:\Users\jazzw\git\snippet\js\openspec\lab-day6"
cd       "C:\Users\jazzw\git\snippet\js\openspec\lab-day6"
git init
openspec init           # choose OpenCode
```

Copy the FastAPI project context from Day 1 into `openspec/project.md`.

#### Walkthrough

**Step 1 — Propose**

```text
/opsx:propose add-todo-api
```

The change folder should contain:

```text
openspec/changes/add-todo-api/
├── proposal.md
├── specs/
│   └── todos/
│       └── spec.md     # ADDED Requirements: Create, List, Get, Patch, Delete
├── design.md
└── tasks.md
```

**Step 2 — Apply**

```text
/opsx:apply add-todo-api
```

Anchor code (this is what the agent should produce in `app/routers/todos.py`):

```python
from fastapi import APIRouter, HTTPException
from app.schemas import TodoIn, TodoOut
from app.db import session_dep

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("", response_model=TodoOut, status_code=201)
async def create_todo(payload: TodoIn, session: session_dep) -> TodoOut:
    todo = Todo.from_pydantic(payload)
    session.add(todo); session.commit(); session.refresh(todo)
    return todo.to_pydantic()

@router.get("", response_model=list[TodoOut])
async def list_todos(session: session_dep) -> list[TodoOut]:
    return [t.to_pydantic() for t in session.query(Todo).all()]

@router.get("/{todo_id}", response_model=TodoOut)
async def get_todo(todo_id: int, session: session_dep) -> TodoOut:
    todo = session.get(Todo, todo_id)
    if not todo: raise HTTPException(404, "not found")
    return todo.to_pydantic()

@router.patch("/{todo_id}", response_model=TodoOut)
async def patch_todo(todo_id: int, patch: TodoIn, session: session_dep) -> TodoOut:
    todo = session.get(Todo, todo_id)
    if not todo: raise HTTPException(404, "not found")
    todo.update_from(patch); session.commit()
    return todo.to_pydantic()

@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: int, session: session_dep) -> None:
    todo = session.get(Todo, todo_id)
    if not todo: raise HTTPException(404, "not found")
    session.delete(todo); session.commit()
```

**Step 3 — Verify and archive**

```text
/opsx:verify add-todo-api
/opsx:archive add-todo-api
```

#### 實測

```bash
pytest -q
openspec list
```

Expected: `5 passed` and `No active changes.`

#### Common pitfalls

- **In-memory SQLite vs file SQLite** — keep it in-memory for the lab
  (`sqlite:///:memory:`) so Day 7 doesn’t fight a leftover DB file.
- **Pydantic v2 vs v1** — this lab assumes v2. If your `pip install` brought in
  v1, pin with `pydantic>=2,<3`.

#### Exit criteria

You are done when `add-todo-api` is archived, `openspec/specs/todos/spec.md`
contains the five CRUD requirements, and the test suite is green.

#### References

- GIGAZINE walkthrough (kitchen-timer pattern): <https://gigazine.net/gsc_news/en/20251026-openspec/>
- QubitTool SDD tutorial: <https://qubittool.com/blog/openspec-sdd-tutorial>

---

### Day 7 — Delta Spec: Pagination + `?status=` Filter (MODIFIED)

**Goal:** Practice `## MODIFIED Requirements` by adding pagination and a status
filter to the todos list endpoint, with a new scenario describing the modified
behavior.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 6 (archived `add-todo-api`).

#### Setup

```bash
cd "C:\Users\jazzw\git\snippet\js\openspec\lab-day6"
```

#### Walkthrough

**Step 1 — Propose a MODIFIED change**

```text
/opsx:propose paginate-todo-list
```

After the agent scaffolds the change, open `specs/todos/spec.md` and replace any
ADDED-only block with a MODIFIED block. The `Requirement: List todos` block should
become:

```markdown
### Requirement: List todos
The system SHALL return a paginated, filterable list of todos.

#### Scenario: Default page
- GIVEN 30 todos exist
- WHEN a client calls `GET /todos`
- THEN the response contains the first 20 todos in insertion order
- AND the response includes `X-Total-Count: 30`

#### Scenario: Filter by status
- GIVEN 30 todos exist, 8 are `done`
- WHEN a client calls `GET /todos?status=done&limit=5`
- THEN the response contains the 5 oldest `done` todos

#### Scenario: Page out of range
- GIVEN 5 todos exist
- WHEN a client calls `GET /todos?offset=10`
- THEN the response is an empty array
- AND the status is 200
```

**Step 2 — Implement**

```text
/opsx:apply paginate-todo-list
```

Anchor code in `app/routers/todos.py`:

```python
from fastapi import Query
from typing import Literal

@router.get("", response_model=list[TodoOut])
async def list_todos(
    session: session_dep,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    status: Literal["open", "done"] | None = None,
) -> list[TodoOut]:
    q = session.query(Todo)
    if status is not None:
        q = q.where(Todo.status == status)
    q = q.order_by(Todo.id).offset(offset).limit(limit)
    return [t.to_pydantic() for t in q.all()]
```

**Step 3 — Add pagination response header**

In `app/main.py`, wrap the router with middleware to set `X-Total-Count` (or
return a custom JSON envelope). Either is acceptable; the spec just requires
the header.

#### 實測

```bash
pytest -q
openspec validate paginate-todo-list --strict
```

#### Common pitfalls

- **Forgetting to update `### Requirement: List todos` instead of adding a new
  requirement** — the spec should show the *diff*, not a parallel "List todos
  v2" requirement. Use `## MODIFIED Requirements`.
- **Total-count performance** — for the lab, a second `count()` query is fine.
  Don’t over-engineer.

#### Exit criteria

You are done when `## MODIFIED Requirements` in `specs/todos/spec.md` has three
scenarios (default page, filter, out-of-range) and `openspec validate --strict`
is green.

#### References

- thedocs Quick Start: <https://thedocs.io/openspec/quick_start/>
- Recca dark-mode delta walkthrough: <https://recca0120.github.io/en/2026/03/08/openspec-sdd>

---

### Day 8 — OAuth2 Password Flow + JWT

**Goal:** Add a stateless authentication module to the todo service using FastAPI’s
`OAuth2PasswordRequestForm` and PyJWT. The spec covers token issuance, refresh,
and a `current_user` dependency.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 7 (pagination + filter in place).

#### Setup

```bash
cd "C:\Users\jazzw\git\snippet\js\openspec\lab-day6"
```

#### Walkthrough

**Step 1 — Propose**

```text
/opsx:propose add-auth
```

The agent scaffolds `openspec/changes/add-auth/` with a `specs/auth/spec.md`
containing three requirements: `Register user`, `Issue access token`, and
`Require auth on todos`. Accept the proposal.

**Step 2 — Anchor the spec manually**

The `design.md` should cover:

```markdown
# Design: add-auth

## Password hashing
argon2-cffi (memory-hard, OWASP-recommended).

## Token model
- Access token: HS256 JWT, 15 min TTL, claims = `{sub, exp, iat}`.
- Refresh token: opaque random 32 bytes, 7 day TTL, stored in DB.

## Endpoints
- `POST /auth/register` → 201
- `POST /auth/token` (OAuth2PasswordRequestForm) → 200 `{access_token, refresh_token, token_type}`
- `POST /auth/refresh` → 200 new access token
- `GET /auth/me` → 200 current user

## current_user dependency
Reads `Authorization: Bearer <jwt>`, decodes, returns the User row. 401 on
any failure (missing, expired, malformed).
```

**Step 3 — Apply**

```text
/opsx:apply add-auth
```

Anchor code in `app/routers/auth.py`:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from argon2 import PasswordHasher
import jwt, time, secrets

router = APIRouter(prefix="/auth", tags=["auth"])
ph = PasswordHasher()
SECRET = "dev-secret-change-me"   # move to env on Day 9

@router.post("/register", status_code=201)
async def register(payload: RegisterIn, session: session_dep) -> UserOut:
    user = User(email=payload.email, password_hash=ph.hash(payload.password))
    session.add(user); session.commit()
    return user.to_out()

@router.post("/token")
async def token(form: OAuth2PasswordRequestForm = Depends(), session: session_dep) -> TokenOut:
    user = session.query(User).filter_by(email=form.username).first()
    if not user or not ph.verify(user.password_hash, form.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "bad credentials")
    return TokenOut(
        access_token=jwt.encode({"sub": user.email, "exp": time.time() + 900}, SECRET, "HS256"),
        refresh_token=secrets.token_urlsafe(32),
        token_type="bearer",
    )
```

**Step 4 — Wire `current_user` into the todos router**

Add `Depends(current_user)` to every todo endpoint; reject with 401 if no token.
The spec scenario for `Require auth on todos` should describe this exactly.

#### 實測

```bash
pytest -q
```

Expected at least: `register, login, refresh, list-with-auth, list-without-auth-401`.

#### Common pitfalls

- **Storing the JWT secret in source** — use `os.environ["APP_SECRET"]` from Day 9
  onward. For the lab, the inline value is acceptable, but the spec must call it
  out as a `SHOULD` (not `SHALL`) for now.
- **Refresh token rotation** — out of scope for this lab; spec it as
  `### Requirement: Refresh token rotation` and add it to a future change folder.

#### Exit criteria

You are done when `POST /auth/token` issues a JWT, `GET /todos` returns 401
without a token, and the auth scenarios in `specs/auth/spec.md` are all green.

#### References

- FastAPI security tutorial: <https://fastapi.tiangolo.com/tutorial/security/>
- jmysu SaaS hands-on: <https://jmysu.com/en/docs/prompt-to-product/16-openspec-practice>

---

### Day 9 — Budget Tracker API (SQLModel + `/summary` Aggregation)

**Goal:** Add a second domain — `Category` and `Expense` — to the lab-day6 service.
Implement a `GET /summary?month=YYYY-MM` aggregation endpoint. Adapted from the
Khaled Ahmed Substack budget-tracker walkthrough, stripped to backend only.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 8 (auth in place, user table populated).

#### Setup

```bash
cd "C:\Users\jazzw\git\snippet\js\openspec\lab-day6"
```

#### Walkthrough

**Step 1 — Propose**

```text
/opsx:propose add-budget-tracker
```

The change folder will gain a `specs/budget/spec.md` with three requirements:
`Category CRUD`, `Expense CRUD`, and `Monthly summary aggregation`.

**Step 2 — Author the design**

```markdown
# Design: add-budget-tracker

## Data model
- `Category(id, user_id, name, monthly_limit_cents: int)`
- `Expense(id, user_id, category_id, amount_cents: int, occurred_on: date, note: str | None)`

Both rows are scoped by `user_id` (FK to `users.id`).

## Endpoints
- `POST/GET/PATCH/DELETE /categories` — standard CRUD, scoped to current user.
- `POST/GET/PATCH/DELETE /expenses` — standard CRUD, scoped to current user.
- `GET /summary?month=YYYY-MM` — returns
  `{ "by_category": [{"category_id": int, "name": str, "spent_cents": int, "limit_cents": int}], "net_savings_cents": int }`.

## Money handling
All amounts in integer cents. Never use `float` for money.

## Indexes
`expenses(user_id, occurred_on)` for the summary query.
```

**Step 3 — Apply**

```text
/opsx:apply add-budget-tracker
```

Anchor code for the summary query (`app/routers/budget.py`):

```python
from datetime import date
from sqlmodel import select, func

@router.get("/summary")
async def summary(month: str, session: session_dep, user: User = Depends(current_user)) -> SummaryOut:
    year, mon = map(int, month.split("-"))
    start = date(year, mon, 1)
    end   = date(year + (mon // 12), (mon % 12) + 1, 1)

    rows = session.exec(
        select(Category.name, func.coalesce(func.sum(Expense.amount_cents), 0))
        .select_from(Category)
        .outerjoin(Expense, (Expense.category_id == Category.id)
                            & (Expense.occurred_on >= start)
                            & (Expense.occurred_on <  end))
        .where(Category.user_id == user.id)
        .group_by(Category.id)
    ).all()

    spent = {name: int(total) for name, total in rows}
    limit = {c.name: c.monthly_limit_cents for c in user.categories}
    total_limit = sum(limit.values())
    total_spent = sum(spent.values())
    return SummaryOut(
        by_category=[CategorySpend(name=n, spent_cents=spent.get(n, 0), limit_cents=limit.get(n, 0))
                     for n in set(spent) | set(limit)],
        net_savings_cents=total_limit - total_spent,
    )
```

#### 實測

```bash
pytest -q
openspec validate add-budget-tracker --strict
```

Expected: at least 6 tests (one CRUD pair per resource, plus the summary case).

#### Common pitfalls

- **Time-zone bleed-through** — `occurred_on` is a `date`, not a `datetime`, so
  DST is irrelevant. Keep it that way.
- **Outer join + group_by cardinality** — SQLModel’s outer join can multiply
  rows if you join on the wrong column. The `(category_id, occurred_on range)`
  triple is what keeps the cardinality sane.

#### Exit criteria

You are done when `GET /summary?month=2026-06` returns the right shape against a
seeded in-memory DB, the spec has the three requirements, and the test suite
is green.

#### References

- Khaled Ahmed budget-tracker walkthrough: <https://khaledea.substack.com/p/ai-driven-development-with-openspec>

---

### Day 10 — Brownfield on Your Snippet (Explore Mode First)

**Goal:** Take one of your existing repos under `C:\Users\jazzw\git\snippet` and
add a small new endpoint, using `/opsx:explore` as the very first step (per Dan
Clarke’s "explore is my go-to starting point" recommendation).

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** any of Days 6-9 complete. Pick a real repo to modify.

#### Walkthrough

**Step 1 — Pick the target repo**

Candidates: any of your snippet projects that already has a `pyproject.toml` or
`requirements.txt`. Avoid anything still in pre-alpha.

**Step 2 — Run explore first**

```bash
cd <path-to-your-snippet-repo>
opencode
```

In the TUI:

```text
/opsx:explore add a new endpoint that returns a build-info object
```

The agent will:

1. Scan the repo and report the detected framework.
2. Ask you clarifying questions (3-5 of them).
3. Suggest a change-id and a tentative `proposal.md` outline.
4. **Stop and wait** for you to say "ok, proceed with propose" before scaffolding
   the change folder.

This is the killer feature: explore does the codebase discovery, the
questioning, and the proposal sketch — all without writing any files yet.

**Step 3 — Promote explore output into a change**

If you are happy with the explore summary, in the same TUI session:

```text
/opsx:propose
```

OpenSpec reuses the explore summary to generate `proposal.md`, `specs/`,
`design.md`, and `tasks.md` immediately.

**Step 4 — Apply and archive as usual**

```text
/opsx:apply
/opsx:verify
/opsx:archive
```

#### 實測

```bash
openspec list
```

Expected: no active changes (you archived it). The new spec is now in your
brownfield repo’s `openspec/specs/`.

#### Common pitfalls

- **Explore silently scaffolding a change** — the canonical behavior of
  `/opsx:explore` is read-only. If your plugin version differs, double-check
  that no folder appeared under `openspec/changes/` after the explore step.
- **Brownfield conflict with existing docs** — if the target repo already has
  an `openspec/` directory, do not re-run `openspec init`; just open the TUI
  from the project root.

#### Exit criteria

You are done when you have a real new endpoint in your snippet repo, the
OpenSpec spec for it is in `openspec/specs/`, and the change is archived.

#### References

- Dan Clarke "explore mode is brilliant": <https://www.danclarke.com/openspec>

---

## Phase 3 — Advanced (Days 11-15)

### Day 11 — Custom TDD-Driven Schema

**Goal:** Author a custom `tdd-driven` schema that requires a `tests/strategy.md`
artifact before `proposal.md` can be applied. Run one tiny change through it.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 10 (you have a brownfield project with OpenSpec in it).

#### Walkthrough

**Step 1 — Create the schema folder**

```bash
mkdir -p openspec/schemas/tdd-driven
```

Create `openspec/schemas/tdd-driven/schema.yaml`:

```yaml
id: tdd-driven
name: TDD-Driven Change
description: >
  Requires a tests-first strategy before proposal can be drafted.
artifacts:
  - id: tests-strategy
    template: tests/strategy.md
    generates: []
    requires: []
  - id: proposal
    template: proposal.md
    requires: [tests-strategy]
  - id: specs
    template: specs
    requires: [proposal]
  - id: design
    template: design.md
    requires: [specs]
  - id: tasks
    template: tasks.md
    requires: [design]
  - id: tests
    template: tests
    requires: [tasks]
    applies: true
```

**Step 2 — Wire the schema into a project**

In `openspec/config.yaml`:

```yaml
schema: tdd-driven
rules:
  tests-strategy: |
    Document the failing tests you intend to write BEFORE any production code.
    Each test must map to a scenario in the eventual `specs/*.md`.
```

**Step 3 — Try to skip the strategy**

```text
/opsx:new add-redis-cache
/opsx:continue
```

Expected: OpenSpec refuses to advance past `tests-strategy` until the file
exists with at least one bullet. This is the win — you cannot skip the
test plan.

**Step 4 — Fill the strategy, then proceed**

```markdown
# Tests Strategy: add-redis-cache

## Failing tests we will write
- `tests/test_cache.py::test_cache_miss_returns_db_result`
- `tests/test_cache.py::test_cache_hit_skips_db`
- `tests/test_cache.py::test_cache_ttl_expires`

## Map to scenarios
- test_cache_miss → spec.md "Scenario: cache miss"
- test_cache_hit  → spec.md "Scenario: cache hit"
- test_cache_ttl  → spec.md "Scenario: TTL expiry"
```

Now `/opsx:continue` should accept it and move to `proposal`.

#### 實測

```bash
openspec schema validate tdd-driven
```

Expected:

```text
Schema 'tdd-driven' is valid
```

#### Common pitfalls

- **`openspec schema validate` flags a circular dependency** — every `requires`
  edge must form a DAG. Drawing the graph on paper before encoding it catches
  this in 30 seconds.

#### Exit criteria

You are done when `openspec schema validate tdd-driven` is green and the
`add-redis-cache` change cannot advance past `tests-strategy` without a
populated file.

#### References

- OpenSpec customization docs: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md>
- intent-driven.dev schemas overview: <https://intent-driven.dev/knowledge/openspec>

---

### Day 12 — ADR Schema (`spec-driven-with-adr`)

**Goal:** Adopt the `spec-driven-with-adr` schema and write a real Architectural
Decision Record for a choice in your lab-day6 repo (e.g., "Why SQLModel over
raw SQLAlchemy 2.0 for the budget tracker").

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 11 (you understand how custom schemas work).

#### Walkthrough

**Step 1 — Switch the schema**

In `openspec/config.yaml`:

```yaml
schema: spec-driven-with-adr
```

Run `openspec update` to refresh the agent instructions.

**Step 2 — Create an ADR folder**

```bash
mkdir -p openspec/adr
```

Create `openspec/adr/0001-sqlmodel-over-sqlalchemy.md`:

```markdown
# ADR 0001: Use SQLModel (not raw SQLAlchemy 2.0) for ORM access

## Status
Accepted · 2026-06-04

## Context
The budget tracker has ~10 entities. Pydantic v2 is already required for
request/response validation. Two candidates:
1. Raw SQLAlchemy 2.0 with separate Pydantic schemas.
2. SQLModel, which fuses Pydantic and SQLAlchemy into one declarative class.

## Decision
Adopt SQLModel.

## Consequences
- (+) One class per entity; less boilerplate.
- (+) Type-checked Pydantic schemas for free.
- (-) Less mature async story than SQLAlchemy 2.0 (acceptable for our scale).
- (-) Migration tooling is thinner than Alembic-standalone; we mitigate with
      `alembic` directly when needed.

## Alternatives considered
- Raw SQLAlchemy 2.0 + Pydantic: rejected (2x classes per entity).
- Tortoise ORM: rejected (smaller community, no FastAPI-native patterns).
```

**Step 3 — Reference the ADR in `design.md`**

In any future `design.md`, add a "Related ADRs" line:

```markdown
## Related ADRs
- ADR 0001 — Use SQLModel (not raw SQLAlchemy 2.0) for ORM access
```

**Step 4 — Verify the schema is in effect**

```text
/opsx:new add-redis-cache
/opsx:continue
```

The agent should now prompt you to update or create an ADR if the change
touches a sensitive area (e.g., introduces a new external dependency).

#### 實測

```bash
ls openspec/adr/
openspec schema list
```

Expected: `0001-sqlmodel-over-sqlalchemy.md` is present, and `spec-driven-with-adr`
is in the schema list.

#### Common pitfalls

- **Mixing schemas mid-project** — once a change is in flight under one schema,
  do not switch. Finish the change, archive it, then update `config.yaml`.

#### Exit criteria

You are done when ADR 0001 exists, is referenced from a `design.md`, and the
project is running under `spec-driven-with-adr`.

#### References

- intent-driven.dev ADR section: <https://intent-driven.dev/knowledge/openspec>

---

### Day 13 — Git Worktrees + SubAgents in Parallel

**Goal:** Split the budget-tracker repo into two parallel worktrees, each with
its own SubAgent applying a different change. Each subagent runs `/opsx:verify`
before merge. Merge and archive sequentially.

**Time:** ~60 min · hard cap 90 min (this day is tight)

**Prerequisites:** Day 12 (ADRs in place, project schema is `spec-driven-with-adr`).

#### Walkthrough

**Step 1 — Create two worktrees**

```bash
cd <lab-day6-repo>
git worktree add ../lab-day6-csv     -b feature/csv-export
git worktree add ../lab-day6-tags    -b feature/tag-filter
```

**Step 2 — OpenCode sessions, one per worktree**

Terminal A:

```bash
cd ../lab-day6-csv
opencode
```

In the TUI:

```text
/opsx:propose add-csv-export
/opsx:apply add-csv-export
/opsx:verify add-csv-export
```

Do **not** archive yet. The change stays active in this worktree.

Terminal B:

```bash
cd ../lab-day6-tags
opencode
```

```text
/opsx:propose add-tag-filter
/opsx:apply add-tag-filter
/opsx:verify add-tag-filter
```

Same — do not archive.

**Step 3 — Merge in order**

```bash
cd <lab-day6-repo>           # back to main checkout
git merge feature/csv-export
git merge feature/tag-filter
```

Resolve any conflicts (likely none if the two changes touched different files).
Then in either TUI session, or from the CLI:

```bash
openspec archive add-csv-export
openspec archive add-tag-filter
```

**Step 4 — Confirm the source of truth is consistent**

```bash
openspec list
openspec show specs --type spec
```

The `specs/budget/spec.md` should now show both new requirements (CSV export
and tag filter) merged in.

#### 實測

```bash
git worktree list
pytest -q
```

Expected: two worktrees (you can `git worktree remove` them after merge), and
the test suite covers both new features.

#### Common pitfalls

- **Worktrees with the same OpenSpec state** — both worktrees share the same
  `.git` so they share the same git history, but each has its own working copy.
  The change folders under `openspec/changes/` are per-worktree until archive.
- **Subagent permissions in a worktree** — subagents may not have write access
  outside the main checkout; confirm the `permission` block in `opencode.json`
  allows edits under `../lab-day6-csv/...` (or move the worktrees under the
  main repo, e.g. `git worktree add .worktrees/csv -b feature/csv-export`).

#### Exit criteria

You are done when both changes are merged into the main branch, both spec
deltas are visible in `openspec/specs/budget/spec.md`, and the worktrees are
removed.

#### References

- intent-driven.dev "Git Worktrees" section: <https://intent-driven.dev/knowledge/openspec>
- OpenCode agents doc: <https://opencode.ai/docs/agents/>

---

### Day 14 — OpenCode TUI Mastery

**Goal:** Go deep on OpenCode itself: define a custom subagent in `opencode.json`,
launch the headless server with `OPENCODE_SERVER_PASSWORD`, and resume a session
with `---continue`.

**Time:** ~60 min · hard cap 75 min

**Prerequisites:** Day 13 (you are comfortable with the agentic loop).

#### Walkthrough

**Step 1 — Define a custom subagent**

Edit `opencode.json`:

```json
{
  "plugin": ["opencode-plugin-openspec"],
  "agent": {
    "test-architect": {
      "description": "Generates pytest cases for a given module.",
      "mode": "build",
      "tools": { "edit": "allow", "bash": "allow" },
      "prompt": "You write tests. For every public function, add at least one happy-path and one edge-case test. Use the existing pytest fixtures. Do not touch production code."
    }
  }
}
```

**Step 2 — Invoke the custom subagent**

```text
@test-architect add tests for app/routers/budget.py
```

Expected: a new `tests/test_budget.py` with at least three test functions.

**Step 3 — Launch the headless server**

```bash
export OPENCODE_SERVER_PASSWORD=dev-password
opencode serve --port 4096 &
```

From another terminal, hit the server:

```bash
curl -u :dev-password http://localhost:4096/health
```

Expected:

```json
{"status":"ok"}
```

**Step 4 — Resume a session**

In the TUI, press **Ctrl+P** and pick a previous session, or use the CLI:

```bash
opencode --continue "continue the test-architect work on app/routers/auth.py"
```

The agent picks up the prior session’s context.

#### 實測

```bash
curl -s -u :dev-password http://localhost:4096/sessions | head -20
```

Expected: a JSON list of sessions.

#### Common pitfalls

- **`OPENCODE_SERVER_PASSWORD` is empty** — the server still binds but refuses
  every request with 401. Always set a non-empty value, even in dev.
- **Custom subagent name conflicts with built-in** — `general`, `explore`,
  `code-reviewer`, `debugger` are reserved. Pick something else.

#### Exit criteria

You are done when `@test-architect` has produced at least one new test file,
the OpenCode server is reachable on `localhost:4096`, and a `--continue`
session re-loads a prior context.

#### References

- OpenCode server: <https://opencode.ai/docs/server/>
- OpenCode CLI: <https://opencode.ai/docs/cli/>

---

### Day 15 — Capstone: Dogfood on Fission-AI/OpenSpec (Local Fork)

**Goal:** Clone `Fission-AI/OpenSpec` into a local fork, pick one scenario in
`openspec/specs/openspec-conventions/spec.md`, propose a tightening as a new
scenario, walk it through `/opsx:propose → /opsx:archive`. **No PR is opened.**

**Time:** ~60 min · hard cap 90 min

**Prerequisites:** all 14 prior days. You now know the workflow end-to-end.

#### Setup

```bash
cd "C:\Users\jazzw\git\snippet\js\openspec"
git clone https://github.com/Fission-AI/OpenSpec.git openspec-fork
cd openspec-fork
git remote remove origin     # local-only; no push
```

#### Walkthrough

**Step 1 — Read the conventions spec**

```bash
cat openspec/specs/openspec-conventions/spec.md
```

Identify a scenario that is missing. A good candidate: there is currently no
scenario that says "When archiving a change, the `## REMOVED Requirements`
block must reference the spec being removed". Add it.

**Step 2 — Propose the tightening**

In the TUI:

```text
/opsx:propose clarify-removed-requirements-archival
```

The agent scaffolds a change folder. Open `specs/openspec-conventions/spec.md`
inside the change folder and add a new scenario under the most relevant
requirement:

```markdown
#### Scenario: REMOVED block references the source spec
- WHEN a change contains a `## REMOVED Requirements` block
- THEN each removed requirement SHALL cite the file path of the spec it
      originated from (e.g. `source: openspec/specs/auth-legacy/spec.md`)
- AND the citation SHALL be preserved through archive
```

**Step 3 — Apply (no production code; only spec edits)**

```text
/opsx:apply clarify-removed-requirements-archival
```

For this change, "apply" is mostly a no-op — there is no production code to
touch. The agent will:
1. Update `tasks.md` to reflect that the only task is "no code change; spec
   only".
2. Check the box.

**Step 4 — Verify and archive**

```text
/opsx:verify clarify-removed-requirements-archival
/opsx:archive clarify-removed-requirements-archival
```

**Step 5 — Inspect the result**

```bash
openspec show openspec-conventions --type spec
```

The new scenario should now be part of the source-of-truth spec.

#### 實測

```bash
openspec list
ls openspec/changes/archive/
```

Expected: no active changes; one new archived folder for today.

#### Common pitfalls

- **Editing the source-of-truth spec directly** — never edit
  `openspec/specs/openspec-conventions/spec.md` from the main checkout. All
  edits must go through a change folder under `openspec/changes/`.
- **Drift between upstream and your fork** — you forked but removed the
  remote. If you want to pull in upstream changes later, re-add it:
  `git remote add upstream https://github.com/Fission-AI/OpenSpec.git`.

#### Exit criteria

You are done when the new scenario for `## REMOVED Requirements` is in
`openspec/specs/openspec-conventions/spec.md` and the change is archived
under `openspec/changes/archive/2026-06-04-clarify-removed-requirements-archival/`.

#### References

- Fission-AI/OpenSpec CONTRIBUTING: <https://github.com/Fission-AI/OpenSpec/blob/main/CONTRIBUTING.md>
- openspec-conventions spec: <https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/openspec-conventions/spec.md>

---

## Appendix A — Historical Reference

> The following 5-day curriculum (Gemini 3 Thinker, 2026-02-27) and 37 reference
> links are preserved verbatim from the previous version of this file. The
> independent 15-day plan above supersedes it; this appendix is kept for
> historical context only.

### A.1 Protocol for Spec-Driven Development (original 5-day plan)

- 2026-02-27
- Generated by Gemini 3 Thinker - Deep Research

#### A 5-Day Technical Curriculum for OpenSpec and OpenCode Integration

The contemporary landscape of software engineering is currently defined by a fundamental shift from manual code authorship toward the orchestration of high-reasoning autonomous agents. This transition, frequently categorized under the broader umbrella of Software 2.0, necessitates a rigorous structural framework to mitigate the stochastic nature of large language model (LLM) outputs and ensure alignment with complex architectural requirements. Spec-Driven Development (SDD) represents the primary methodology for achieving this stability, serving as an "Engineering Manual" that bridges the gap between human intent and machine execution. By establishing a clear separation between the planning phase, focused on architectural integrity and behavioral specifications, and the implementation phase, focused on task execution and verification, tools like OpenSpec and OpenCode enable a deterministic, reviewable, and auditable development lifecycle.

The following laboratory curriculum provides an exhaustive five-day technical progression designed to transition professional development teams from traditional imperative coding practices to a mature, agent-led engineering ecosystem. The curriculum emphasizes the use of OpenCode as the execution engine and OpenSpec as the architectural supervisor, leveraging specialized plugins and subagent hierarchies to maximize project velocity without sacrificing code quality.

#### Day 1: Environment Architecture and Agentic Infrastructure

The initial phase of deploying a spec-driven workflow involves the establishment of a robust local environment and the formalization of the project's "Agentic Constitution". Unlike conventional development tools that function as static editors, OpenCode and OpenSpec operate as a localized layer atop the existing file system, utilizing a server-client architecture to manage pseudo-terminal (PTY) sessions and long-lived agent interactions.

##### 1.1 Establishing the Local Runtime and Server Architecture

The foundational requirement for the OpenSpec ecosystem is a modern Node.js environment, specifically requiring version v≥20.19.0 to handle the asynchronous input/output operations and the complex permissioning systems utilized by the agentic tools. OpenCode is designed as an open-source AI coding agent that can be accessed via a terminal user interface (TUI), a desktop application, or a headless server.

| Platform | Recommended Installation Method | Technical Command |
| --- |  --- | --- |
| macOS/Linux | Homebrew (Most up-to-date) | `brew install anomalyco/tap/opencode` |
| Linux/Unix | Binary Installation Script | `curl -fsSL https://opencode.ai/install \| bash` |
| Windows | WSL (Recommended) or Chocolatey | `choco install opencode` |
| Universal | NPM/Bun/PNPM Package | `npm install -g opencode-ai @fission-ai/openspec@latest` |

Upon installation, OpenCode initiates a TUI that communicates with a background server via an OpenAPI 3.1 specification. This architecture allows for programmatic interaction with the agent, enabling tools like `openspecui` to provide reactive search and visual progress tracking for complex changes. The server can be protected with basic authentication by setting the `OPENCODE_SERVER_PASSWORD` environment variable, ensuring that remote or shared environments remain secure.

##### 1.2 Initializing Project Identity and Agent Rules

Once the binaries are accessible, the project must be initialized to generate the metadata required for agent awareness. Running the command `/init` within the OpenCode TUI triggers a deep analysis of the local codebase, scanning file structures, dependency graphs, and existing coding patterns. This process culminates in the creation of an `AGENTS.md` file (or `CLAUDE.md` for compatibility with legacy systems), which serves as the primary repository for project-specific instructions and behavioral constraints.

The `AGENTS.md` file is a critical artifact that must be committed to version control. It ensures that any agent, whether built-in or custom, adheres to the architectural standards of the repository. The hierarchy of rules in OpenCode follows a precise precedence logic, ensuring that local expertise always overrides global defaults.

| Rule Category | File Location | Precedence Level |
| --- | --- | --- |
| Project-Specific | `<root>/AGENTS.md` | Primary (Highest) |
| Project-Specific (Fallback) | `<root>/CLAUDE.md` | Secondary (Used if AGENTS.md is absent) |
| Global User Rules | `~/.config/opencode/AGENTS.md` | Tertiary |
| Global Fallback | `~/.claude/CLAUDE.md` | Quaternary |

##### 1.3 Configuring Specialized Agent Profiles and Plugins

The final task for Day One is the integration of the `opencode-plugin-openspec`, which bridges the two tools by introducing the "OpenSpec Architect" agent. This agent is specifically configured with "Smart Permissions" that allow it to edit specification files while maintaining the application codebase in a read-only state. This separation is the cornerstone of SDD, preventing agents from "vibe coding" or making premature implementation changes before the plan is approved.

To install the plugin, the developer updates the `opencode.json` configuration file, adding `"opencode-plugin-openspec"` to the `plugin` array. This plugin automatically detects if a workspace is an OpenSpec project and enables the `openspec-plan` mode, identified in the TUI by a distinct color code (#FF6B6B).

#### Day 2: The Specification Phase and Semantic Alignment

Day Two focuses on the transition from high-level intent to structured, verifiable requirements. In the SDD workflow, the goal is to achieve human-agent alignment on "What" needs to be built before addressing "How" it will be implemented. This is managed through the creation of a "Change" folder, which acts as an isolated sandbox for all planning artifacts.

##### 2.1 The Change Proposal Mechanism

Initiating a feature or architectural refactor begins with the `/opsx:propose` command (or `openspec new` in standalone CLI mode). This command scaffolds a directory within `openspec/changes/<change-name>/` and generates the initial `proposal.md`. The proposal serves to clarify the "Intent" and "Scope" of the work, defining the business problem and the high-level capabilities required to solve it.

The effective use of the `/opsx:propose` command requires high-reasoning models such as Opus4.5 or GPT5.2. These models are better equipped to handle the "Consensual Planning" process, where the agent investigates the existing codebase (using the `explore` subagent) and suggests an approach that minimizes technical debt and maintains backwards compatibility.

##### 2.2 Drafting Verifiable Scenarios (Gherkin Implementation)

OpenSpec formalizes requirements through the use of "Delta Specs". Instead of maintaining a monolithic documentation file, OpenSpec creates modular specifications that describe only the behavior being added, modified, or removed in a specific change. These specs utilize Gherkin-style scenarios (Given/When/Then) to ensure that requirements are not just descriptive, but testable.

| Spec Section | Purpose | Example Requirement |
| --- | --- | --- |
| `## ADDED` | New features or behaviors | "The system SHALL support OAuth2 login." |
| `## MODIFIED` | Changes to existing logic | "Session timeouts are reduced from 60 to 30 minutes." |
| `## REMOVED` | Deprecated or deleted functionality | "Legacy basic auth is no longer supported." |
| `#### Scenario` | Concrete examples of the behavior | "GIVEN a user... WHEN they login... THEN..." |

The significance of the scenario-based approach lies in its ability to support automated verification. When the agent later implements the code, it can refer to these scenarios to ensure that edge cases, such as session expiration or invalid credentials, are handled as specified.

##### 2.3 Context Hygiene and Verification Logic

As the number of specification artifacts grows, the "Context Window" of the agent can become saturated with irrelevant data. This degradation of context is a primary cause of agentic hallucination. To counteract this, OpenSpec benefits from a "Clean Room" approach where the agent is encouraged to "refresh" its context before starting implementation.

The developer should run `openspec validate <change-id> --strict` at the end of Day Two. This command identifies any logical inconsistencies between the `proposal.md` and the `spec.md`. For example, if the proposal mentions a "mobile-first" approach but the specs do not include scenarios for responsive layouts, the validation tool will flag the omission, forcing the agent to align the artifacts before proceeding to the design phase.

#### Day 3: Technical Design and Task Decomposition

On Day Three, the curriculum moves from "What" to "How." The artifacts generated during this phase, the `design.md` and `tasks.md`, serve as the technical blueprint and implementation checklist, respectively. This stage represents the "Engineering" in Spec-Driven Development, where architectural decisions are finalized and the work is broken down into atomic, executable units.

##### 3.1 The Expanded Workflow Profile

For complex architectural changes, the "Core Profile" (which generates all artifacts in one step) may be too broad. Professional teams often utilize the "Expanded Workflow," enabled via `openspec config profile`. This allows for a granular, step-by-step artifact creation process.

1.  **`/opsx:new`**: Initializes the change metadata and folder structure.
2.  **`/opsx:continue`**: Analyzes the dependency graph of the current change and generates the next required artifact template.
3.  **`/opsx:ff` (Fast-Forward)**: Rapidly generates all remaining planning artifacts once the human is satisfied with the initial direction.

This dependency-aware workflow ensures that a `design.md` is never created before the `specs` are finalized, and `tasks.md` are never generated before the technical approach is established.

##### 3.2 Architectural Design and ADR Integration

The `design.md` artifact is where the agent documents technical decisions, such as data schemas, API contracts, and integration patterns. In larger projects, this file functions as a localized Architecture Decision Record (ADR).

To ensure the design aligns with organizational standards, OpenSpec allows for the injection of "Project Context" via `openspec/config.yaml`. This context provides the agent with the project's tech stack (e.g., "React with Tailwind"), testing preferences ("Vitest and Testing Library"), and naming conventions.

| Configuration Field | Purpose | Impact on Design |
| --- | --- | --- |
| `context:` | Global project information | Ensures tech stack consistency |
| `rules: design:` | Per-artifact constraints | Enforces patterns like "Use CSS variables" |
| `schema:` | Workflow definition | Controls the sequence of artifact generation |

##### 3.3 Task Decomposition and Implementation Mapping

The final output of the planning phase is the `tasks.md` file. This file contains a hierarchical checklist that the agent will follow during the implementation phase. A well-structured task list avoids vague instructions like "implement feature" and instead focuses on atomic actions.

Example `tasks.md` structure:

```markdown
1. **Database Layer**
  - [ ] 1.1 Create migration for `user_preferences` table
  - [ ] 1.2 Update Prisma schema and regenerate client

2. **API Layer**
  - [ ] 2.1 Implement GET `/api/preferences` route
  - [ ] 2.2 Add zod validation middleware

3. **UI Layer**
  - [ ] 3.1 Create `ThemeToggle` component
```

This persistent task list allows the agent to maintain state across restarts or even across different coding tools, as the `tasks.md` file acts as the single source of truth for implementation progress.

#### Day 4: Agentic Execution and Orchestrated Implementation

Day Four marks the transition from planning to execution. The focus shifts to "Build Mode," where the OpenCode agent is granted write permissions to the application codebase to implement the agreed-upon tasks. This phase is characterized by the use of specialized subagents and parallel execution strategies to maximize efficiency.

##### 4.1 Implementing via /opsx:apply

The primary mechanism for implementation is the `/opsx:apply` command. When invoked, the agent reads the `tasks.md` file, identifies the first incomplete item, and begins writing the necessary code, creating files, and running tests. During this process, the agent utilizes its full toolset, including `edit` for precise string replacements, `write` for new file creation, and `bash` for system commands.

One of the key benefits of the OpenCode TUI is the ability to toggle between "Build" and "Plan" modes using the **Tab** key. If the agent encounters an unforeseen architectural challenge during implementation, the developer can switch back to "Plan" mode to update the `design.md` and `tasks.md` before resuming the work. This iterative loop ensures that the implementation never drifts significantly from the intended design.

##### 4.2 Orchestration and Subagent Delegation

OpenCode employs an "Orchestrator Pattern," where a primary agent delegates specific units of work to specialized subagents. This is particularly useful for parallelizing tasks or performing multi-perspective reviews.

| Subagent | Role | Operational Mode |
| --- | --- | --- |
| `@general` | Multi-step task execution | Build (Full tool access) |
| `@explore` | Read-only codebase discovery | Plan (Fast, no-edit) |
| `@code-reviewer` | Quality and pattern analysis | Review (Read-only) |
| `@debugger` | Root cause investigation | Debug (Bash access enabled) |
| `@test-architect` | Test generation and strategy | Build (Write access to tests/) |

Insightful orchestration involves invoking multiple subagents in a single message to trigger parallel execution. For example, a developer can ask the orchestrator to: "@code-reviewer check these changes for performance bottlenecks while @test-architect generates a unit test suite for the new utility function". This reduces total wait time, as independent tasks are processed simultaneously.

##### 4.3 Automated Verification and Guardrails

To prevent the introduction of security vulnerabilities or breaking changes, OpenCode supports a variety of "Guardrails" and "Plugins". These run automatically in the background to verify the work before it is committed.

-   **Security-Scan Plugin**: Blocks edits to sensitive files like `.env` or credential stores.
-   **Auto-Format Plugin**: Automatically runs formatters like Prettier or Black after every file edit.
-   **Verification Agent**: Monitors for changes to 3+ files and automatically prompts the developer to run the test suite.

Additionally, the `/undo` command provides a vital safety net, allowing the developer to revert the most recent set of changes and restore the original prompt for refinement. This "undo/redo" capability is essential for managing the trial-and-error nature of agentic coding.

#### Day 5: Verification, Archiving, and System Evolution

The final day of the curriculum is dedicated to quality assurance and the formalization of new system knowledge. This ensures that the documentation (the "Source of Truth") remains in sync with the implementation and that the project remains maintainable as it scales.

##### 5.1 Formal Verification and the /opsx:verify Command

Before a change is finalized, the `/opsx:verify` command is executed to validate the implementation against the planning artifacts. This check is conducted across three primary dimensions:

-   **Completeness**: Ensures all requirements in the `spec.md` have corresponding implementation and that all items in `tasks.md` are marked complete.
-   **Correctness**: Validates that the code adheres to the scenarios defined in the specifications and handles specified edge cases.
-   **Coherence**: Checks that design decisions are reflected consistently across the new code, such as the choice of a specific design pattern or library.

If the verification tool identifies a "drift" between the artifacts and the code, the agent will suggest either updating the implementation or modifying the specs to reflect what was actually built, maintaining an accurate audit trail.

##### 5.2 Syncing Delta Specs and Archiving the Change

Once verification is successful, the "Delta Specs" contained within the change folder must be merged into the project's main specification directory (`openspec/specs/`). The `/opsx:sync` command performs this merge agentically, resolving any conflicts between the new changes and existing documentation.

Finally, the `/opsx:archive` command is run. This command:

1.  Moves the completed change folder to an archive directory: `openspec/changes/archive/YYYY-MM-DD-<name>/`.
2.  Preserves all artifacts (proposal, design, tasks) for future audits.
3.  Clears the active change list, preparing the environment for the next work cycle.

This archival process is a critical distinction between SDD and traditional development. In SDD, the "Source of Truth" (`openspec/specs/`) is a living document that evolves with every change, ensuring that the system's current capabilities are always accurately documented.

##### 5.3 Customizing the Workflow: Schemas and Skills

For advanced teams, the default `spec-driven` schema can be customized or replaced entirely. Custom schemas, located in `openspec/schemas/`, allow teams to define their own artifact sequences and dependency rules. For example, a "TDD-Driven" schema might require a `test-strategy.md` before the `proposal.md` can be implemented.

| Schema Feature | Configuration Option | Use Case |
| --- | --- | --- |
| **Artifact Sequence** | `requires: [artifact_id]` | Enforcing strict phase gates (e.g., Security Review before Code) |
| **Custom Templates** | `template: filename.md` | Enforcing corporate branding or documentation standards |
| **Per-Artifact Rules** | `rules: artifact_id:` | Injecting specific prompts for complex artifacts like Threat Models |

Furthermore, the agent's knowledge can be extended through "Agent Skills", reusable instruction sets defined in `SKILL.md` files. Skills are discovered by walking up from the current directory and can be granted specific permissions (allow, ask, or deny) in the `opencode.json` file.

##### 5.4 Maintenance and Troubleshooting

Maintaining a high-performance agentic environment requires periodic cleanup of caches and configuration files. Common issues often stem from corrupted session caches or protocol mismatches between the client and the background server.

| Symptom | Probable Cause | Resolution |
| --- | --- | --- |
| Agent fails to edit files | Permission denied in `opencode.json` | Update `"permission": { "edit": "allow" }` |
| Plugins causing TUI to hang | Misconfigured or conflicting plugin | Disable by setting `"plugin":` in config |
| Session context is degraded | Too many messages in history | Use `/undo` or start a new session with `--continue` |
| Spec validation errors | Circular dependencies in custom schema | Run `openspec schema validate <name>` |

Through the diligent application of the five-day curriculum, professional development teams can achieve a state of "Deterministic Development." By leveraging the OpenSpec and OpenCode toolchain, they move beyond the unpredictability of raw LLM interaction and toward a mature engineering process where human creativity is amplified by agentic execution, all while maintaining the highest standards of architectural integrity and system documentation.

### A.2 Reference (original 37 links)

- Software 2.0: Code is Cheap, Good Taste is Not - Aaronontheweb: <https://aaronstannard.com/beginning-of-software-2-0/>
- Fission-AI/OpenSpec: Spec-driven development (SDD) for AI coding assistants. - GitHub: <https://github.com/Fission-AI/OpenSpec>
- Programming - LLBBL Blog: <https://llbbl.blog/categories/programming/>
- A Practical Development Guide Based on OpenSpec + Claude CLI | by HBLOG - Medium: <https://jxausea.medium.com/a-practical-development-guide-based-on-openspec-claude-cli-26da7df71356>
- Octane0411/opencode-plugin-openspec: An OpenCode ... - GitHub: <https://github.com/Octane0411/opencode-plugin-openspec>
- OpenSpec: Spec-Driven Development for AI Coding Assistants - MCP Market: <https://mcpmarket.com/server/openspec>
- Anyone using OpenSpec custom schemas with OpenCode? : r/opencodeCLI - Reddit: <https://www.reddit.com/r/opencodeCLI/comments/1rdi8hp/anyone_using_openspec_custom_schemas_with_opencode/>
- opencode-workflow/README.md at main - GitHub: <https://github.com/CloudAI-X/opencode-workflow/blob/main/README.md>
- OpenSpec vs Spec Kit: Choosing the Right AI-Driven Development Workflow for Your Team: <https://hashrocket.com/blog/posts/openspec-vs-spec-kit-choosing-the-right-ai-driven-development-workflow-for-your-team>
- Server | OpenCode: <https://opencode.ai/docs/server/>
- jixoai/openspecui - GitHub: <https://github.com/jixoai/openspecui>
- Intro | AI coding agent built for the terminal - OpenCode: <https://opencode.ai/docs/>
- CLI | OpenCode: <https://opencode.ai/docs/cli/>
- Rules | OpenCode: <https://opencode.ai/docs/rules/>
- OpenSpec/docs/getting-started.md at main - Fission-AI/OpenSpec ...: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md>
- OpenSpec/docs/commands.md at main - Fission-AI/OpenSpec ...: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md>
- openspec | Skills Marketplace - LobeHub: <https://lobehub.com/skills/openclaw-skills-openspec>
- openspec-continue-change | Skills Ma... - LobeHub: <https://lobehub.com/ko/skills/sap-e-mobility-charging-stations-simulator-openspec-continue-change>
- Agents - OpenCode: <https://opencode.ai/docs/agents/>
- How to make AI follow your instructions more for free (OpenSpec) - DEV Community: <https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85>
- \[Question\] How to integrate automated testing and bug fixing into Custom Workflows? - Issue #693 - Fission-AI/OpenSpec - GitHub: <https://github.com/Fission-AI/OpenSpec/issues/693>
- OpenSpec/docs/opsx.md at main - GitHub: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md>
- OpenSpec/docs/customization.md at main - GitHub: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md>
- Tools | OpenCode: <https://opencode.ai/docs/tools/>
- OpenSpec now supports OpenCode natively! : r/opencodeCLI - Reddit: <https://www.reddit.com/r/opencodeCLI/comments/1nqu1wk/openspec_now_supports_opencode_natively/>
- Troubleshooting | OpenCode: <https://opencode.ai/docs/troubleshooting/>
- Common OpenCode Errors and How to Fix Them: Complete Troubleshooting Guide: <https://www.steffenstein.com/blog/common-opencode-errors-troubleshooting-guide/>
- Spec Coding — QubitTool: <https://qubittool.com/blog/spec-coding-practical-guide>
- Trying Out OpenSpec in OpenCode: My Experience with Spec ...: <https://kd05.com/p/openspec-opencode-experience>
- OpenSpec Tutorial: Master Spec-Driven Development (SDD) [2026] | QubitTool: <https://qubittool.com/blog/openspec-sdd-tutorial>
- Spec-Driven Development (SDD): The Definitive 2026 Guide · BCMS: <https://thebcms.com/blog/spec-driven-development>
- How to generate consistent code using OpenSpec, which makes specification-driven development easy to adopt - GIGAZINE: <https://gigazine.net/gsc_news/en/20251026-openspec/>
- OpenSpec Changes Everything — No More Vibe Coding! (Full Step ...) - YouTube: <https://www.youtube.com/watch?v=xwpmPP4mNBQ>
- OpenSpec | Spec-Driven Development | intent-driven.dev: <https://intent-driven.dev/knowledge/openspec>
- OpenSpec - Spec-driven development for AI coding assistants - Aitoolnet: <https://www.aitoolnet.com/openspec>
- OpenSpec - Lightweight & portable spec driven framework for AI coding assistants! - Cursor Community Forum: <https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052>
- OpenSpec - thedocs.io: <https://thedocs.io/openspec>
- AI-Driven Development with OpenSpec: A Step-by-Step Walkthrough - Substack: <https://khaledea.substack.com/p/ai-driven-development-with-openspec>
- OpenSpec Hands-on Guide - jmysu: <https://jmysu.com/en/docs/prompt-to-product/16-openspec-practice>
- OpenSpec: Make AI Coding Assistants Follow a Spec, Not Just Guess - Recca: <https://recca0120.github.io/en/2026/03/08/openspec-sdd>
- OpenSpec - a lightweight AI-driven spec framework - Dan Clarke: <https://www.danclarke.com/openspec>

---

## Appendix B — Slash-Command Cheat Sheet

| Command | Where it runs | What it does |
| --- | --- | --- |
| `/opsx:propose <id>` | TUI | Scaffolds a full change folder (proposal, specs, design, tasks) in one shot. |
| `/opsx:new <id>` | TUI | Initializes the change metadata only; pairs with Expanded profile. |
| `/opsx:continue` | TUI | Generates the next required artifact in the dependency graph. |
| `/opsx:ff` | TUI | Fast-forward: generates all remaining artifacts at once. |
| `/opsx:apply <id>` | TUI | Walks `tasks.md` top-down, ticking each box as it lands. |
| `/opsx:verify <id>` | TUI | Runs the three-dimension check (completeness, correctness, coherence). |
| `/opsx:sync` | TUI | Merges delta specs into `openspec/specs/` before archive. |
| `/opsx:archive <id>` | TUI | Moves the change folder to `openspec/changes/archive/<date>-<id>/`. |
| `/opsx:explore` | TUI | Read-only codebase + requirements discovery; no files written. |
| `openspec list` | CLI | Lists active changes. |
| `openspec show <id>` | CLI | Renders the change summary in the terminal. |
| `openspec validate <id> --strict` | CLI | Strict schema + cross-reference validation. |
| `openspec schema list` | CLI | Lists installed schemas. |
| `openspec schema validate <name>` | CLI | Validates a custom schema. |
| `openspec config profile` | CLI | Switch between Core and Expanded profiles. |
| `openspec update` | CLI | Refreshes AI guidance after a CLI upgrade. |
| `openspec archive <id> --yes` | CLI | Non-interactive archive. |

---

## Appendix C — Troubleshooting Quick-Reference

### C.1 `openspec: command not found` on Windows
- Cause: terminal opened before `npm install -g` updated PATH.
- Fix: open a new PowerShell / Git Bash / Windows Terminal tab.

### C.2 Plugin not appearing in the TUI
- Symptom: `openspec-plan` mode is missing or the Architect agent is not in the picker.
- Fix:
  1. Confirm `opencode.json` is valid JSON (no trailing commas).
  2. Re-launch `opencode` from the project root, not a subdirectory.
  3. Run `openspec update` to refresh the AI guidance.

### C.3 Agent stuck in Plan mode after Tab
- Symptom: edit commands silently fail after pressing Tab.
- Cause: Tab toggles Plan ↔ Build. The first press can be consumed by the input
  box.
- Fix: check the status bar color (`#FF6B6B` = Plan, neutral = Build). Toggle
  once more if the status bar did not change.

### C.4 Schema not picked up after `openspec update`
- Symptom: `/opsx:new` still uses the old schema.
- Fix:
  1. Confirm `openspec/schemas/<name>/schema.yaml` is present.
  2. Confirm `openspec/config.yaml` has `schema: <name>`.
  3. Re-launch the TUI (it caches the schema on startup).

### C.5 Worktree conflicts when archiving sequentially
- Symptom: `openspec archive` complains that the spec was modified by another
  branch.
- Fix:
  1. `git fetch` the main branch in the worktree.
  2. `git merge origin/main` (or `git rebase`).
  3. Re-run `openspec validate <id> --strict` before archive.

### C.6 `openspec validate --strict` complains about cross-references
- Symptom: a `Requirement:` block is flagged because a referenced requirement
  does not exist.
- Fix: every requirement ID referenced by another requirement must exist in
  the same change folder, or already be in `openspec/specs/`.

---

## Appendix D — Source URL Index (grouped by day)

### Days 1-5 (Foundations)

- Fission-AI/OpenSpec getting-started — <https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md>
- openspec.dev — <https://openspec.dev/>
- thedocs Quick Start — <https://thedocs.io/openspec/quick_start/>
- OpenSpec spec format conventions — <https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/openspec-conventions/spec.md>
- OpenSpec Expanded workflow — <https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md>
- OpenCode subagents — <https://opencode.ai/docs/agents/>
- OpenCode tools — <https://opencode.ai/docs/tools/>
- OpenSpec CLI reference (`archive`) — <https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md>

### Days 6-10 (Compact Python Labs)

- GIGAZINE kitchen-timer walkthrough — <https://gigazine.net/gsc_news/en/20251026-openspec/>
- QubitTool SDD tutorial — <https://qubittool.com/blog/openspec-sdd-tutorial>
- Recca dark-mode delta walkthrough — <https://recca0120.github.io/en/2026/03/08/openspec-sdd>
- FastAPI security tutorial — <https://fastapi.tiangolo.com/tutorial/security/>
- jmysu SaaS hands-on — <https://jmysu.com/en/docs/prompt-to-product/16-openspec-practice>
- Khaled Ahmed budget-tracker walkthrough — <https://khaledea.substack.com/p/ai-driven-development-with-openspec>
- Dan Clarke "explore mode is brilliant" — <https://www.danclarke.com/openspec>

### Days 11-15 (Advanced)

- OpenSpec customization docs — <https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md>
- intent-driven.dev (schemas + ADRs + worktrees) — <https://intent-driven.dev/knowledge/openspec>
- OpenCode server — <https://opencode.ai/docs/server/>
- OpenCode CLI — <https://opencode.ai/docs/cli/>
- Fission-AI/OpenSpec CONTRIBUTING — <https://github.com/Fission-AI/OpenSpec/blob/main/CONTRIBUTING.md>
- openspec-conventions spec — <https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/openspec-conventions/spec.md>

---

## Appendix E — Glossary

- **SDD (Spec-Driven Development)** — A methodology where the specification is
  the primary artifact and code is derived from it. Inverts the traditional
  flow where code is the source of truth and specs rot in a doc.
- **Brownfield** — An existing project with established code. OpenSpec is
  designed brownfield-first; specs live alongside existing code without
  requiring a rewrite.
- **Greenfield** — A new project with no prior code. OpenSpec handles greenfield
  cases as a subset of brownfield (the existing code is empty).
- **Delta spec** — A specification that describes the *diff* (ADDED, MODIFIED,
  REMOVED) rather than the full system state. Merged into the source of truth
  on archive.
- **Scenario** — A Given/When/Then example under a Requirement. Each scenario
  is testable; agents use them as acceptance criteria.
- **Subagent** — A specialized agent invoked by name (e.g., `@explore`,
  `@code-reviewer`) for a specific role. Subagents run in parallel when
  invoked in the same message.
- **Worktree** — A separate working copy of a git repo, sharing the same `.git`
  directory. Used to apply changes in parallel without branch-switching.
- **ADR (Architectural Decision Record)** — A short document capturing the
  context, options, and consequences of a significant technical decision. Lives
  outside any single change in the `spec-driven-with-adr` schema.
- **Schema** — A YAML file under `openspec/schemas/<name>/schema.yaml` that
  defines the artifact dependency graph for a project. Default is
  `spec-driven`; alternatives include `tdd-driven` and `spec-driven-with-adr`.
- **MUST / SHALL / SHOULD / MAY** — RFC 2119 keywords expressing requirement
  strength. OpenSpec specs use them consistently.
- **ADDED / MODIFIED / REMOVED** — Section headers in a delta spec describing
  the kind of change relative to the current source of truth.
- **Source of Truth (SoT)** — The specs in `openspec/specs/`. After archive,
  delta specs are merged into SoT and become the new authoritative description.
- **TUI / CLI** — OpenCode runs in a Terminal User Interface (TUI); OpenSpec
  itself is a Command-Line Interface (CLI) plus a set of slash commands
  injected into the TUI.

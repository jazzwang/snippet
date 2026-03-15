from typing import Callable

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Header, Footer, Input, Label
from textual.widget import Widget
from textual.screen import Screen
from textual.events import Key
from textual import work
from datetime import datetime
import json
import platform
import sys
import time
import zoneinfo


def play_beep() -> None:
    """Play a system beep for timer alerts."""
    system = platform.system()
    if system == "Windows":
        try:
            import winsound
            winsound.Beep(800, 500)
            time.sleep(0.1)
            winsound.Beep(800, 500)
        except Exception:
            pass
    else:
        sys.stdout.write("\a")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\a")
        sys.stdout.flush()


class AddTaskScreen(Screen):
    """Modal screen for adding a new task."""

    def __init__(self, on_add: Callable[[str], None]) -> None:
        super().__init__()
        self.on_add = on_add

    def compose(self) -> ComposeResult:
        yield Container(
            Label("Enter task:"),
            Input(placeholder="Task description...", id="task-input"),
            Horizontal(
                Button("Cancel", id="btn-cancel", variant="default"),
                Button("Add", id="btn-add", variant="success"),
            ),
            id="add-task-dialog"
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.add_task()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-add":
            self.add_task()
        elif event.button.id == "btn-cancel":
            self.app.pop_screen()

    def add_task(self) -> None:
        input_widget = self.query_one("#task-input", Input)
        text = input_widget.value
        if text.strip():
            self.on_add(text)
        self.app.pop_screen()


class DeleteTaskScreen(Screen):
    """Modal screen for deleting a task."""

    def __init__(self, task_count: int, on_delete: Callable[[int], None]) -> None:
        super().__init__()
        self.task_count = task_count
        self.on_delete = on_delete

    def compose(self) -> ComposeResult:
        if self.task_count == 0:
            yield Container(
                Label("No tasks to delete."),
                Button("OK", id="btn-ok", variant="primary"),
                id="delete-task-dialog"
            )
        else:
            yield Container(
                Label(f"Enter task number to delete (1-{self.task_count}):"),
                Input(placeholder="Task number...", id="delete-input"),
                Horizontal(
                    Button("Cancel", id="btn-cancel", variant="default"),
                    Button("Delete", id="btn-delete", variant="error"),
                ),
                id="delete-task-dialog"
            )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.delete_task()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-delete":
            self.delete_task()
        elif event.button.id == "btn-cancel" or event.button.id == "btn-ok":
            self.app.pop_screen()

    def delete_task(self) -> None:
        input_widget = self.query_one("#delete-input", Input)
        try:
            index = int(input_widget.value) - 1
            if 0 <= index < self.task_count:
                self.on_delete(index)
        except ValueError:
            pass
        self.app.pop_screen()


class ToggleTaskScreen(Screen):
    """Modal screen for toggling task completion."""

    def __init__(self, task_count: int, on_toggle: Callable[[int], None]) -> None:
        super().__init__()
        self.task_count = task_count
        self.on_toggle = on_toggle

    def compose(self) -> ComposeResult:
        if self.task_count == 0:
            yield Container(
                Label("No tasks to toggle."),
                Button("OK", id="btn-ok", variant="primary"),
                id="toggle-task-dialog"
            )
        else:
            yield Container(
                Label(f"Enter task number to toggle (1-{self.task_count}):"),
                Input(placeholder="Task number...", id="toggle-input"),
                Horizontal(
                    Button("Cancel", id="btn-cancel", variant="default"),
                    Button("Toggle", id="btn-toggle", variant="primary"),
                ),
                id="toggle-task-dialog"
            )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.toggle_task()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-toggle":
            self.toggle_task()
        elif event.button.id == "btn-cancel" or event.button.id == "btn-ok":
            self.app.pop_screen()

    def toggle_task(self) -> None:
        input_widget = self.query_one("#toggle-input", Input)
        try:
            index = int(input_widget.value) - 1
            if 0 <= index < self.task_count:
                self.on_toggle(index)
        except ValueError:
            pass
        self.app.pop_screen()


class WorldClock(Widget):
    """Widget displaying world clocks for London, Tokyo, and New York."""

    def __init__(self) -> None:
        super().__init__()
        self.timezones = {
            "London": zoneinfo.ZoneInfo("Europe/London"),
            "Tokyo": zoneinfo.ZoneInfo("Asia/Tokyo"),
            "New York": zoneinfo.ZoneInfo("America/New_York"),
        }

    def compose(self) -> ComposeResult:
        yield Static("WORLD CLOCK", classes="section-title")
        yield Static("", id="clock-display")

    def on_mount(self) -> None:
        self.update_clocks()
        self.set_interval(1, self.update_clocks)

    def update_clocks(self) -> None:
        now = datetime.now()
        clock_lines = []
        for city, tz in self.timezones.items():
            local_time = now.astimezone(tz)
            clock_lines.append(f"  {city:12} {local_time.strftime('%H:%M:%S')}")
        
        clock_display = self.query_one("#clock-display", Static)
        clock_display.update("\n".join(clock_lines))


class PomodoroTimer(Widget):
    """Widget for Pomodoro timer functionality."""

    def __init__(self) -> None:
        super().__init__()
        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self._remaining = self.work_duration
        self._is_running = False
        self._is_break = False
        self._sessions = 0

    def compose(self) -> ComposeResult:
        yield Static("POMODORO", classes="section-title")
        yield Static("25:00", id="timer-display")
        with Horizontal(id="timer-controls"):
            yield Button("Start", id="btn-start", variant="primary")
            yield Button("Reset", id="btn-reset", variant="default")
        yield Static("Sessions: 0", id="session-count")

    def on_mount(self) -> None:
        self.timer = self.set_interval(1, self.tick)

    def tick(self) -> None:
        if not self._is_running:
            return
        
        if self._remaining > 0:
            self._remaining -= 1
            self.update_display()
        else:
            self.switch_phase()

    def switch_phase(self) -> None:
        if self._is_break:
            self._is_break = False
            self._remaining = self.work_duration
            self._sessions += 1
            self.query_one("#session-count", Static).update(f"Sessions: {self._sessions}")
            self.notify("Break over! Time to work.")
        else:
            self._is_break = True
            self._remaining = self.break_duration
            self.notify("Work session complete! Take a break.")
        
        play_beep()
        self.update_display()

    def update_display(self) -> None:
        minutes = self._remaining // 60
        seconds = self._remaining % 60
        phase = "BREAK" if self._is_break else "WORK"
        display = self.query_one("#timer-display", Static)
        display.update(f"{minutes:02}:{seconds:02}\n{phase}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-start":
            self._is_running = not self._is_running
            btn = self.query_one("#btn-start", Button)
            btn.label = "Pause" if self._is_running else "Start"
        elif event.button.id == "btn-reset":
            self._is_running = False
            self._is_break = False
            self._remaining = self.work_duration
            self.update_display()
            btn = self.query_one("#btn-start", Button)
            btn.label = "Start"


class TodoList(Widget):
    """Widget for persistent to-do list."""

    def __init__(self, data_file: str = "vibedash.json") -> None:
        super().__init__()
        self.data_file = data_file
        self.tasks: list[dict] = []
        self.load_tasks()

    def compose(self) -> ComposeResult:
        yield Static("TO-DO LIST", classes="section-title")
        yield Static("", id="todo-list", markup=False)
        yield Horizontal(
            Button("+ Add", id="btn-add", variant="success"),
            Button("Del", id="btn-delete", variant="error"),
            Button("Toggle", id="btn-toggle", variant="primary"),
            id="todo-controls"
        )

    def on_mount(self) -> None:
        self.render_tasks()

    def load_tasks(self) -> None:
        import os
        try:
            if not os.path.exists(self.data_file):
                self.tasks = []
                return
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = data.get("tasks", [])
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            self.tasks = []

    def save_tasks(self) -> None:
        import os
        import tempfile
        
        temp_path = self.data_file + ".tmp"
        try:
            with open(temp_path, "w") as f:
                json.dump({"tasks": self.tasks}, f, indent=2)
            os.replace(temp_path, self.data_file)
        except OSError as e:
            self.notify(f"Failed to save tasks: {e}", severity="error")
        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass

    def render_tasks(self) -> None:
        lines = []
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["done"] else "[ ]"
            lines.append(f"  {i + 1}. {status} {task['text']}")
        
        if not lines:
            lines = ["  No tasks yet"]
        
        self.query_one("#todo-list", Static).update("\n".join(lines))

    def add_task(self, text: str) -> None:
        if text.strip():
            self.tasks.append({"text": text.strip(), "done": False})
            self.save_tasks()
            self.render_tasks()

    def delete_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            self.render_tasks()

    def toggle_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.save_tasks()
            self.render_tasks()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-add":
            self.app.push_screen(AddTaskScreen(self.add_task))
        elif event.button.id == "btn-delete":
            self.app.push_screen(DeleteTaskScreen(len(self.tasks), self.delete_task))
        elif event.button.id == "btn-toggle":
            self.app.push_screen(ToggleTaskScreen(len(self.tasks), self.toggle_task))


class VibeDash(App):
    """VibeDash - Productivity dashboard with Pomodoro, To-Do, and World Clock."""

    CSS = """
    Screen {
        background: $surface;
    }
    
    #main-container {
        height: 100%;
        padding: 1 2;
    }
    
    .section-title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }
    
    #timer-display {
        text-align: center;
        text-style: bold;
        color: #00ffff;
        margin: 2 0;
    }
    
    #timer-controls {
        align: center middle;
        height: auto;
    }
    
    #timer-controls Button {
        margin: 0 1;
    }
    
    #session-count {
        text-align: center;
        color: #00ffff;
        margin-top: 1;
    }
    
    #clock-display {
        text-align: left;
        color: $text;
        padding: 1 2;
    }
    
    #todo-list {
        padding: 1 2;
        color: $text;
    }
    
    #todo-list .done {
        color: $text-muted;
    }
    
    .column {
        height: 100%;
        border: solid $border;
        padding: 1;
        margin: 0 1;
    }
    
    #sidebar {
        width: 30;
        height: 100%;
        border-left: solid $accent;
        padding: 1;
    }
    
    #todo-controls {
        align: center middle;
        height: auto;
        padding: 1 2;
    }
    
    #todo-controls Button {
        margin: 0 1;
    }
    
    #add-task-dialog, #delete-task-dialog, #toggle-task-dialog {
        align: center middle;
        width: 50;
        height: auto;
        border: solid $accent;
        background: $surface;
        padding: 1 2;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="main-container"):
            with Vertical(classes="column"):
                yield PomodoroTimer()
            with Vertical(classes="column"):
                yield TodoList()
            with Vertical(id="sidebar"):
                yield WorldClock()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "VibeDash"


if __name__ == "__main__":
    app = VibeDash()
    app.run()

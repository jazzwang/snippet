# Click

> Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”.

- 大致上來說，Click 就是方便用 Python Code 寫 CLI 工具的套件。

- ( 2024-07-18 23:36:00 )
```bash
jazzwang:~/git/snippet/python/click$ pip3 install click
Defaulting to user installation because normal site-packages is not writeable
Collecting click
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 811.7 kB/s eta 0:00:00
Installing collected packages: click
Successfully installed click-8.1.7
jazzwang:~/git/snippet/python/click$ python3 hello.py 
Your name: jazz
Hello jazz!
jazzwang:~/git/snippet/python/click$ python3 hello.py --help
Usage: hello.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  --name TEXT      The person to greet.
  --help           Show this message and exit.
```
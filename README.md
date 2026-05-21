# Week 1 — Cloud Engineering Foundations

Hands-on practice from the first week of a structured 30-day cloud engineering program.
Covers Python basics, Git workflow, and Linux  and Rest APIs.

## Contents

| File | Description |
|------|-------------|
| `hello_cloud.py` | First Python script — variables, f-strings, lists, functions |
| `linux-notes.txt` | Linux command reference built during WSL2 practice |
| `python-basics.py` | Data types, if/elif/else, loops, functions — with cloud examples |
| `cloud-cost-calculator.py` | CLI tool to estimate EC2 and S3 monthly cost |
| `python-apis.py` | Lists, dictionaries, file handling practice |
| `weather-script.py` | Fetches live weather for multiple cities via REST API, saves report |

## Environment

- OS: Windows 11 + WSL2 (Ubuntu 24.04)
- Tools: Python 3, VS Code, Git, Windows Terminal
- Libraries: `requests`

## How to Run

```bash
# Day 1 — first Python script
python hello_cloud.py

# Day 2 — view Linux command notes (text file, not a script)
cat linux-notes.txt

# Day 3 — run the cost calculator
python cloud-cost-calculator.py
python python-basics.py

# Day 4
python weather-script.py
```

## Key Concepts Covered

- Python: variables, f-strings, lists, for loops, functions, data types, if/elif/else, while , file I/O
- APIs: GET requests, JSON parsing, error handling with try/except
- Linux: navigation, file operations, nano, grep, file redirection
- Git: init, add, commit, push, branching
- WSL2: running Ubuntu on Windows, accessing Windows files at /mnt/c/

---

*Week 1 — 30-day cloud engineering program · May 2026*

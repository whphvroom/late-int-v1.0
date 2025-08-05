# late-int-v1.0

**late-int-v1.0** is the internal MVP for *Late*, a learning platform focused on speed, simplicity, and utility. 
When someone uses this, their impression should be, it's easy to use, it's fast, and it does exactly what I need, no more or less. 

This version includes:
- **AI Tutor Chat UI** — Ask questions and get help.
- **Save & Review Mode** — Bookmark key answers for future review.
- **Speed Mode** — A bare bones rapid-response mode designed for cramming.

> `int` stands for internal — this version is focused on rapid iteration and validation. A future public version may differ.

## Tech Stack

- **Backend**: FastAPI, OpenAI API
- **Frontend**: TBD
- **Env**: Python 3.11, Conda

## Getting Started

1. Clone the repo
2. Set up environment:
   ```bash
   conda create -n late-int python=3.11
   conda activate late-int
   pip install -r requirements.txt

### `README_DEV.md` — Developer Commands for `late-int-v1.0`

For developers contributing to **Late Internal v1.0**.

---

### Basics 

--- 

#### Setup & Installation

```bash
# Create and activate Conda environment
conda create -n late-int python=3.11
conda activate late-int

# Install backend dependencies
pip install -r backend/requirements.txt
```

---

#### Environment Variables

Create a `.env` file in `backend/`:

```dotenv
OPENAI_API_KEY="your-api-key-here"
```

---

#### Common Git Commands

```bash
# Add remote if not set
git remote add origin https://github.com/whphvroom/late-int-v1.0.git

# Check current remote
git remote -v

# Push code
git status                # Checks for all the changes that have been made 
git add .                 # Stage all changes (or use 'git add <file>' for specific files)
git commit -m "message"   # Commit with a message describing changes
git pull origin main      # Pull latest changes from remote to avoid conflicts (optional but recommended)
git push origin main      # Push your committed changes to GitHub
```
---

### Reminders

--- 
#### Always pull before pushing
Keep your local branch in sync with the remote:
```bash
git pull origin main

### Use feature branches (don't commit directly to main)
git checkout -b feature/your-feature-name

### After making changes 
git add . 
git commit -m "feat: describe your change" 
git push origin feature/your-feature-name

### After installing new packages 
pip freeze > backend/requirements.txt

---

#### Dependency Management

```bash
# Save installed packages to requirements.txt
pip freeze > backend/requirements.txt
```

---

### Testing 

---

#### Manual Sanity Checks 

You can quickly check all backend functionality using the built-in Swagger UI provided by FastAPI:

```bash
cd backend
uvicorn app.main:app --reload
``` 
Then open up the browser and go to: 
http://127.0.0.1:8000/docs

This opens Swagger UI where you can interact with the endpoints

---

### Repo Structure 

--- 

#### Backend 

``` 
backend/
├── app/
│   ├── main.py                  # App entry point
│   ├── routes/
│   │   └── chat.py              # All /chat, /save, /review endpoints
│   ├── services/
│   │   ├── base_model.py        # Abstract interface: BaseModelClient
│   │   ├── openai_client.py     # OpenAI model client
│   │   └── model_router.py      # Chooses which model client to use
│   ├── schemas/
│   │   └── schemas.py           # Pydantic models for request/response
│   └── utils/
│       └── persistence.py       # Save/load JSON Q&A to disk
├── .env                         # API keys
├── requirements.txt             # Python dependencies
└── saved.json                   # Local store of saved Q&As (could move later)
``` 

--- 
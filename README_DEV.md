### `README_DEV.md` — Developer Commands for `late-int-v1.0`

This doc lists common commands used during development of **Late Internal v1.0**.

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

#### Run the API Server (FastAPI + Uvicorn)

```bash
# From project root
cd backend
uvicorn app.main:app --reload
```

- Runs locally at: http://127.0.0.1:8000  
- Swagger docs: http://127.0.0.1:8000/docs

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

## Reminders & Good Practices

### Always pull before pushing
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

#### Testing (TBD)
> Placeholder — add testing commands as testing infra is added.
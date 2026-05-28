# 🚀 Brand Hunt

Automated morning email digest of newly funded Indian brands, scraped from:
- [Inc42](https://inc42.com)
- [YourStory](https://yourstory.com)
- [Entrackr](https://entrackr.com)
- [StartupTalky](https://startuptalky.com)
- [SutraHR](https://sutrahr.com)

Runs every morning at **8:00 AM IST** via GitHub Actions and sends a formatted email to your inbox.

---

## Setup

### 1. Add GitHub Secrets

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name      | Value                                      |
|------------------|--------------------------------------------|
| `EMAIL_SENDER`   | Your Gmail address (e.g. you@gmail.com)    |
| `EMAIL_PASSWORD` | Your Gmail **App Password** (not your login password) |
| `EMAIL_RECEIVER` | Email where you want to receive the digest |

### 2. Create a Gmail App Password

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Search for **App Passwords** → create one for "Mail"
4. Copy the 16-character password → paste as `EMAIL_PASSWORD` secret

### 3. Push to GitHub

```bash
git init
git add .
git commit -m "Initial Brand Hunt setup"
git branch -M main
git remote add origin https://github.com/Shwetadutta97/Brand-Hunt.git
git push -u origin main
```

The workflow will automatically trigger every morning at 8 AM IST. You can also trigger it manually from the **Actions** tab on GitHub.

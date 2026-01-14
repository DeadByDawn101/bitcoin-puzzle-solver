# 🚀 Easy GitHub Upload Guide

## Quick Upload (Copy & Paste Commands)

### Option 1: If This is a NEW Repository

```bash
# 1. Navigate to your project directory
cd /path/to/your/bitcoin-puzzle-solver

# 2. Initialize git (if not already)
git init

# 3. Create the workflows directory
mkdir -p .github/workflows

# 4. Download and place the workflow file
# (Download build-dmg.yml from the files I provided and place it in .github/workflows/)

# 5. Add all files
git add .

# 6. Make your first commit
git commit -m "Initial commit with DMG build workflow"

# 7. Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 8. Push to GitHub
git branch -M main
git push -u origin main

# 9. Create first release tag (optional)
git tag v1.0.0
git push origin v1.0.0
```

### Option 2: If Repository ALREADY EXISTS

```bash
# 1. Navigate to your repository
cd /path/to/your/bitcoin-puzzle-solver

# 2. Pull latest changes
git pull

# 3. Create workflows directory (if it doesn't exist)
mkdir -p .github/workflows

# 4. Download and place the workflow file
# (Download build-dmg.yml from the files I provided and place it in .github/workflows/)

# 5. Add the workflow file
git add .github/workflows/build-dmg.yml

# 6. Commit
git commit -m "Add DMG build workflow"

# 7. Push to GitHub
git push

# 8. Create release tag (optional)
git tag v1.0.0
git push origin v1.0.0
```

---

## 📦 What You'll Upload

I've created a ready-to-upload folder structure:

```
.github/
└── workflows/
    └── build-dmg.yml  ← The fixed workflow file
```

---

## ⚡ Super Quick Method (3 Steps)

### Step 1: Download the workflow file
Download `build-dmg.yml` from the files I provided above.

### Step 2: Place it in your repository
```
your-repo/
├── .github/
│   └── workflows/
│       └── build-dmg.yml  ← Put it here
├── src/
│   └── gui.py  ← Make sure this exists!
└── ...
```

### Step 3: Push to GitHub
```bash
git add .github/workflows/build-dmg.yml
git commit -m "Add automated DMG build workflow"
git push
```

**Done!** 🎉

---

## 🔄 Using GitHub Web Interface (No Command Line)

### Step 1: Go to Your Repository on GitHub

### Step 2: Create the Workflow File
1. Click on **"Add file"** → **"Create new file"**
2. Name it: `.github/workflows/build-dmg.yml`
3. Copy and paste the contents from `build-dmg-fixed.yml`
4. Click **"Commit new file"**

### Step 3: Test It
1. Go to **"Actions"** tab
2. Click **"Build Bitcoin Puzzle Solver DMG with BitCrack"**
3. Click **"Run workflow"**
4. Select your branch
5. Click **"Run workflow"** button

**That's it!** No git commands needed!

---

## ✅ Pre-Upload Checklist

Before you upload, make sure:

- [ ] You have a `src/` directory in your repository
- [ ] `src/gui.py` file exists (your main application)
- [ ] You've downloaded `build-dmg.yml` from the files above
- [ ] You know your GitHub username and repository name

---

## 🎯 After Upload - What Happens Next?

### Automatic Triggers:
- ✅ Workflow runs when you push a tag (like `v1.0.0`)
- ✅ You can manually trigger it from Actions tab
- ✅ Creates a complete DMG installer
- ✅ Automatically creates a GitHub Release

### First Test Run:
```bash
# Create and push a test tag
git tag v1.0.0
git push origin v1.0.0
```

Within a few minutes:
1. Workflow starts automatically
2. Builds BitCrack from source
3. Creates macOS application bundle
4. Packages everything into DMG
5. Creates GitHub Release with DMG attached
6. Ready to download and distribute!

---

## 🆘 Troubleshooting

### "src/ directory not found"
**Solution:** Create a `src/` folder with your `gui.py` file:
```bash
mkdir -p src
# Move your gui.py into src/
```

### "Workflow not appearing in Actions"
**Solution:** 
1. Make sure file is in `.github/workflows/build-dmg.yml`
2. Check file has `.yml` extension (not `.yml.txt`)
3. Refresh the Actions page

### "Build failed"
**Solution:**
1. Click on the failed workflow run
2. Expand the failed step
3. Read the error message
4. Fix and push again

---

## 📞 Need Help?

If you get stuck:
1. Check the Actions tab for detailed error logs
2. Make sure all prerequisites are in your repository
3. Try the manual trigger first (workflow_dispatch)
4. Review the workflow-review.md for details

---

## 🎁 Bonus: Complete Example

Here's a complete example from scratch:

```bash
# Start fresh
cd ~/Projects
mkdir bitcoin-puzzle-solver
cd bitcoin-puzzle-solver

# Create source directory
mkdir -p src
echo 'print("Hello from GUI")' > src/gui.py

# Initialize git
git init

# Create workflows directory
mkdir -p .github/workflows

# Copy your workflow file here
# (Download build-dmg.yml and place it in .github/workflows/)

# Add and commit
git add .
git commit -m "Initial commit with workflow"

# Create repo on GitHub, then:
git remote add origin https://github.com/yourusername/bitcoin-puzzle-solver.git
git branch -M main
git push -u origin main

# Create first release
git tag v1.0.0
git push origin v1.0.0

# Check Actions tab on GitHub - build is running!
```

---

## 🚀 You're All Set!

The workflow is ready to upload. Choose your method:
- ✅ Command line (3 commands)
- ✅ GitHub web interface (click & paste)
- ✅ Desktop GitHub app (drag & drop)

**Pick whichever is easiest for you!**

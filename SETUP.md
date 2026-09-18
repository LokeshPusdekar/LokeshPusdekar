# LokeshPusdekar GitHub Profile — Setup Guide

This package is designed for the **special GitHub profile repository**:

`LokeshPusdekar/LokeshPusdekar`

The README follows the terminal/dashboard philosophy of the reference profile, while using Lokesh's own identity, stack, links and artwork.

## 1. Create the profile repository

Create a public repository named exactly:

`LokeshPusdekar`

GitHub will treat this as your profile README repository.

## 2. Copy the files

Copy everything in this package into the repository root:

```text
LokeshPusdekar/
├── README.md
├── lokesh-ascii.svg
├── lokesh-wordmark.svg
├── contribution-heatmap.svg
├── source-prepped.png
├── scripts/
│   └── make_contribution_svg.py
└── .github/
    └── workflows/
        ├── update-profile-art.yml
        └── snake.yml
```

`source-prepped.png` is kept as the processed source image so the portrait can be regenerated later.

## 3. Push to `main`

```bash
git init
git add .
git commit -m "create terminal-style GitHub profile"
git branch -M main
git remote add origin https://github.com/LokeshPusdekar/LokeshPusdekar.git
git push -u origin main
```

## 4. Enable Actions write permissions

In the **repository**:

`Settings → Actions → General → Workflow permissions`

Select:

**Read and write permissions**

Save the setting.

This is repository-level permission, not your general GitHub account setting.

## 5. Create `PROFILE_TOKEN`

The contribution heatmap uses GitHub's GraphQL contribution calendar.

Create a GitHub token that can read your contribution data, then add it to:

`Repository → Settings → Secrets and variables → Actions → New repository secret`

Name:

`PROFILE_TOKEN`

Do not put the token in `README.md`, Python files, or commits.

## 6. Run the profile-art workflow

Open:

`Actions → Update profile art → Run workflow`

After it succeeds, `contribution-heatmap.svg` will contain the live contribution calendar.

The workflow also runs daily.

## 7. Run the snake workflow

Open:

`Actions → Generate contribution snake → Run workflow`

It publishes the generated snake SVGs to the `output` branch.

The README already points to that branch, so the snake appears after the first successful run.

## 8. About the widgets

The README uses:
- Skill Icons for the stack row
- GitHub Readme Stats for stats
- Streak Stats for streaks
- GitHub Readme Activity Graph for activity

These are external image services. They are intentionally kept simple so the profile repository stays lightweight.

If a third-party widget is rate-limited, the self-hosting option is to deploy your own instance later.

## 9. Customize the visual identity

Main palette:

```text
Background: #0a1017
Chrome:     #22d3ee
Portrait:   #a78bfa
Accent:     #10b981
Text:       #cbd5e1
Muted:      #718096
```

The important files are:

- `lokesh-ascii.svg` — portrait panel
- `lokesh-wordmark.svg` — terminal identity panel
- `README.md` — complete profile layout
- `scripts/make_contribution_svg.py` — live contribution art
- `.github/workflows/update-profile-art.yml` — daily contribution refresh
- `.github/workflows/snake.yml` — contribution snake

## 10. Important GitHub limitation

The profile README cannot execute arbitrary JavaScript.

The design therefore uses:
- ordinary Markdown/HTML
- SVG artwork
- GitHub Actions for generated assets
- external image widgets

That gives the terminal/dashboard feel without relying on unsupported browser scripting inside the README.

## 11. If you want to regenerate the portrait

Install Pillow:

```bash
python -m pip install pillow
```

The supplied `source-prepped.png` is already processed. The current `lokesh-ascii.svg` is the ready-to-use output.

For a later higher-detail portrait generator, keep the original photo outside Git history if you do not want the source image publicly available.

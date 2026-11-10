"""All CineScope presentation content, shared by the Streamlit and Gradio sites."""
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

TITLE = "CineScope"
SUBTITLE = "Movie & TV Show Explorer"
COURSE = "Python GUI Programming · Final Project Presentation"
TEAM = [
    ("Dorji Choden", "Intro, problem & solution,repository"),
    ("Sonam Choki", "Features, architecture"),
    ("Ugyen Lhaden", "Design diagrams, GUI navigation"),
    ("Chimi Wangmo", "Live demo"),
    ("Tenzin Choden", "Technologies, code organisation"),
    ("Kezang Dema", "Challenges, testing"),
]
PROGRAMME = "B.Ed IT"
TUTOR = "Anup Gurung"

PROBLEM = [
    "Movie and TV details are scattered across many websites and streaming platforms.",
    "Users must visit several pages to find posters, genres, ratings, dates and descriptions.",
    "Existing platforms are often cluttered and slow to browse.",
]
SOLUTION = [
    "A simple Python desktop app that brings movie and TV information together in one place.",
    "Live data from the TMDB API, shown in a clean dark interface.",
    "Personal accounts and a watchlist to keep track of titles.",
]
TARGET_USERS = ["Movie and TV enthusiasts", "General users who want quick details"]

FEATURES = [
    ("Login / Account", "Sign up and log in; passwords are hashed"),
    ("Home / Dashboard", "Trending, top-rated and hidden gems"),
    ("Movie Search", "Find movies by title"),
    ("TV Show Search", "Find TV shows by title"),
    ("Genre Filter", "Action, comedy, drama, horror, romance"),
    ("Details", "Poster, rating, date, overview, cast"),
    ("Watchlist", "Add, remove and mark as watched"),
    ("Watch Options", "Netflix and Where-to-Watch links"),
    ("Validation & Errors", "Invalid input, no results, API errors"),
]
FEATURE_NOTE = "Watch Options only links out: CineScope does not stream any content."

ARCH_FLOW = [
    ("User", "Types, clicks, browses"),
    ("GUI modules", "main.py + ui_layout, home, catalog, details, watchlist, account"),
    ("tmdb.py", "API helper"),
    ("TMDB API", "External service"),
]
ARCH_DB = [("database.py", "Accounts and watchlist"), ("SQLite", "cinescope.db")]
ARCH_NOTE = "config.py holds colours and genres; about.py explains the app."
USER_FLOW = ["Login", "Dashboard", "Search", "Results", "Details", "Watchlist / Watch Options"]
ARCH_EXTRA = "Movie data is not stored locally: it is fetched live from TMDB. Only accounts and watchlists live in SQLite."

USE_CASE_IMG = ASSETS / "use_case_diagram.jpg"
USE_CASE_CAPTION = "Use case diagram: the user, CineScope and the external TMDB API"
ERD_IMG = ASSETS / "erd_diagram.png"
ERD_CAPTION = "ERD: one user has many watchlist items (SQLite)"
ERD_NOTE = "Email is unique and passwords are hashed. Users 1-to-many Watchlist, linked by user_id."

GUI_SCREENS = [
    ("Login", "Enter credentials"),
    ("Home", "Main landing page"),
    ("Search", "Movies or TV"),
    ("Results", "Matching titles"),
    ("Details", "Poster, rating, cast"),
    ("Watchlist", "Saved titles"),
    ("Watch Options", "External links"),
]
GUI_PRINCIPLES = [
    ("Dark, modern theme", "Inspired by entertainment platforms; high-contrast text and buttons"),
    ("Consistent layout", "Same navigation and structure on every screen"),
    ("Designed before coded", "Figma wireframes and prototype guided the Python build"),
]

DEMO_STEPS = [
    "Create an account and log in",
    "Explore the dashboard: trending and top-rated",
    "Search a movie, then a TV show",
    "Filter by genre",
    "Open details: poster, rating, overview, cast",
    "Add to watchlist, mark watched, open Where to Watch",
    "Show error handling: empty input, no results, offline",
]

TECHNOLOGIES = [
    ("Python", "Main programming language"),
    ("Tkinter / CustomTkinter", "Windows, frames, labels, entries, buttons, scrollable areas"),
    ("TMDB API + Requests", "Fetch movie and TV data as JSON"),
    ("Pillow + BytesIO", "Convert and display poster images"),
    ("Threading", "Load images and API data without freezing the GUI"),
    ("SQLite", "Store user accounts and watchlists locally"),
    ("JSON, webbrowser, urllib.parse", "Process API data, open external links, format search text"),
    ("Figma + VS Code", "Wireframes and prototype; coding and project management"),
]

MODULES = [
    ("main.py", "Entry point; builds the window, starts the DB, runs the main loop"),
    ("ui_layout.py", "Sidebar, search bar, genre dropdown, scrolling"),
    ("home.py", "Welcome, trending and top-rated rows"),
    ("catalog.py", "Search, filter, posters; threading + image caching"),
    ("details.py", "Description, rating, genres, cast, reviews, links"),
    ("watchlist.py", "Add, remove, view, mark as watched"),
    ("account.py", "Register and log in; checks name, email, password"),
    ("database.py", "SQLite tables, hashing, watchlist queries"),
    ("tmdb.py", "TMDB requests: search, details, genres, hidden gems"),
    ("config.py", "Colours and genre list"),
    ("about.py", "Features and TMDB credit"),
    ("assets/", "Filmstrip texture image"),
]
MODULE_NOTE = "UI, API and database code are kept separate, so each part is easier to test and change."
STRUCTURE_IMG = ASSETS / "project_structure.png"

CHALLENGES = [
    ("Learning Python GUI programming", "Docs, tutorials and tutor guidance"),
    ("Integrating the TMDB API", "Tested requests on their own before joining the GUI"),
    ("Showing posters without freezing the window", "Pillow for images and threading for background loading"),
    ("Internet or API failures", "Clear error messages for no results and network errors"),
]

TESTS = [
    "App launches without errors",
    "Registration with input checks",
    "Login accepts / rejects credentials",
    "TMDB trending and search results",
    "Poster and details display",
    "Watchlist add, remove, watched",
    "Data saved after restart",
    "External watch links open correctly",
    "No-results and API/network errors",
    "Buttons, labels and layout",
]
TEST_SUMMARY = ("Launch, sign-up, login, TMDB, details, watchlist, saved data, external links, "
                "error handling and navigation all pass.")

REPO_URL = "https://github.com/Kezang20/GUI.git"
REPO_WEB = "https://github.com/Kezang20/GUI"
SOURCES = [
    ("TMDB API", "developer.themoviedb.org", "https://developer.themoviedb.org"),
    ("Python and Tkinter", "docs.python.org", "https://docs.python.org"),
    ("CustomTkinter", "customtkinter.tomschimansky.com", "https://customtkinter.tomschimansky.com"),
    ("Pillow and Requests", "documentation", "https://pillow.readthedocs.io"),
    ("SQLite", "sqlite.org/docs.html", "https://sqlite.org/docs.html"),
]
REPO_POINTS = [
    "Project documentation: features, design, workflow, testing, roadmap",
    "README.md with overview, run steps, structure and module descriptions",
    ".gitignore for caches and environments",
    "11 organised modules plus assets",
    "Commits from every member",
    "Project structure in VS Code",
]
TMDB_NOTICE = "This product uses the TMDB API but is not endorsed or certified by TMDB."

# ---------- shared HTML helpers (work in st.markdown and gr.HTML) ----------
CSS = """
.cs-hero{padding:48px 32px;border-radius:18px;background:linear-gradient(135deg,#1a0b0b,#2b0f14 55%,#0d0d12);
 border:1px solid #3a1a1f;text-align:center;color:#f5f5f5;font-family:system-ui,sans-serif}
.cs-eyebrow{letter-spacing:.18em;font-size:.78rem;color:#e5a00d;text-transform:uppercase}
.cs-hero h1{font-size:3.4rem;margin:.2em 0 0;color:#fff}
.cs-hero h3{font-weight:400;color:#cfcfd6;margin:.2em 0 1em}
.cs-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:12px 0;font-family:system-ui,sans-serif}
.cs-card{background:#16161d;border:1px solid #2a2a35;border-radius:14px;padding:16px 18px;color:#eee}
.cs-card b{color:#fff;display:block;margin-bottom:4px}
.cs-card span{color:#a9a9b6;font-size:.92rem}
.cs-num{display:inline-flex;width:28px;height:28px;border-radius:50%;background:#e50914;color:#fff;
 align-items:center;justify-content:center;font-weight:700;font-size:.85rem;margin-bottom:8px}
.cs-flow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-family:system-ui,sans-serif;margin:10px 0}
.cs-pill{background:#e50914;color:#fff;border-radius:999px;padding:6px 14px;font-size:.9rem}
.cs-arrow{color:#e5a00d;font-weight:700}
.cs-pass{color:#46d369;font-weight:700;margin-right:6px}
.cs-big{font-size:3rem;font-weight:800;color:#46d369}
.cs-note{background:#1d1a10;border-left:4px solid #e5a00d;padding:10px 14px;border-radius:6px;color:#eee;font-family:system-ui,sans-serif;margin:10px 0}
"""

def card(title, body, num=None):
    n = f'<div class="cs-num">{num}</div>' if num is not None else ""
    return f'<div class="cs-card">{n}<b>{title}</b><span>{body}</span></div>'

def grid(cards):
    return '<div class="cs-grid">' + "".join(cards) + "</div>"

def pills(items):
    return '<div class="cs-flow">' + '<span class="cs-arrow">→</span>'.join(
        f'<span class="cs-pill">{i}</span>' for i in items) + "</div>"

def note(text):
    return f'<div class="cs-note">{text}</div>'

def hero():
    team = " · ".join(n for n, _ in TEAM)
    return (f'<div class="cs-hero"><div class="cs-eyebrow">{COURSE}</div><h1>🎬 {TITLE}</h1>'
            f'<h3>{SUBTITLE}</h3><div>{team}</div>'
            f'<div style="margin-top:10px;color:#a9a9b6">{PROGRAMME} · Module Tutor: {TUTOR}</div></div>')

def features_html():
    return grid([card(t, d, i + 1) for i, (t, d) in enumerate(FEATURES)])

def team_html():
    return grid([card(n, r) for n, r in TEAM])

def architecture_html():
    flow = pills([f"{t}" for t, _ in ARCH_FLOW])
    details = grid([card(t, d) for t, d in ARCH_FLOW + ARCH_DB])
    return (flow + details + note(ARCH_NOTE) + "<b style='color:#eee'>User flow</b>"
            + pills(USER_FLOW) + note(ARCH_EXTRA))

def gui_html():
    return (pills([f"{i+1}. {n}" for i, (n, _) in enumerate(GUI_SCREENS)])
            + grid([card(n, d, i + 1) for i, (n, d) in enumerate(GUI_SCREENS)])
            + "<h4 style='color:#eee'>Design principles</h4>"
            + grid([card(t, d) for t, d in GUI_PRINCIPLES]))

def demo_html():
    return grid([card(f"Step {i+1}", s, i + 1) for i, s in enumerate(DEMO_STEPS)])

def modules_html():
    return grid([card(n, d) for n, d in MODULES])

def challenges_html():
    return grid([card(c, f"✅ {h}") for c, h in CHALLENGES])

def testing_html():
    cards = [card("", f'<span class="cs-pass">✓</span>{t}') for t in TESTS]
    return ('<div class="cs-big">10/10</div><div style="color:#a9a9b6;font-family:system-ui">test areas complete</div>'
            + grid(cards) + note(TEST_SUMMARY))

def resources_html():
    src = grid([card(n, f'<a href="{u}" target="_blank" style="color:#e5a00d">{d}</a>') for n, d, u in SOURCES])
    return src

"""CineScope – Streamlit version of the final presentation website.
Run:  streamlit run streamlit_app.py
"""
import pandas as pd
import streamlit as st
import content as c

st.set_page_config(page_title="CineScope · Movie & TV Explorer", page_icon="🎬", layout="wide")
st.markdown(f"<style>{c.CSS}</style>", unsafe_allow_html=True)

PAGES = [
    "Home", "Problem & Solution", "What CineScope Does", "System Architecture",
    "Design Diagrams", "GUI & Navigation", "Live Demo", "Technologies",
    "Code Organisation", "Challenges", "Testing & Results", "GitHub & Resources",
]

st.sidebar.title("🎬 CineScope")
st.sidebar.caption(c.SUBTITLE)
page = st.sidebar.radio("Navigate", PAGES, label_visibility="collapsed")
st.sidebar.divider()
st.sidebar.caption(c.TMDB_NOTICE)

def html(s):
    st.markdown(s, unsafe_allow_html=True)

if page == PAGES[0]:
    html(c.hero())
    st.subheader("Team")
    html(c.team_html())

elif page == PAGES[1]:
    st.header("Problem and proposed solution")
    left, right = st.columns(2)
    with left:
        st.subheader("The problem")
        for p in c.PROBLEM:
            st.markdown(f"- {p}")
    with right:
        st.subheader("Our solution")
        for s in c.SOLUTION:
            st.markdown(f"- {s}")
    st.subheader("Target users")
    html(c.grid([c.card(u, "") for u in c.TARGET_USERS]))

elif page == PAGES[2]:
    st.header("What CineScope does")
    html(c.features_html())
    html(c.note(c.FEATURE_NOTE))

elif page == PAGES[3]:
    st.header("System architecture")
    html(c.architecture_html())

elif page == PAGES[4]:
    st.header("System design diagrams")
    a, b = st.columns(2)
    with a:
        st.image(str(c.USE_CASE_IMG), caption=c.USE_CASE_CAPTION, use_container_width=True)
    with b:
        st.image(str(c.ERD_IMG), caption=c.ERD_CAPTION, use_container_width=True)
    html(c.note(c.ERD_NOTE))

elif page == PAGES[5]:
    st.header("GUI design and navigation")
    html(c.gui_html())

elif page == PAGES[6]:
    st.header("Live demonstration")
    html(c.demo_html())

elif page == PAGES[7]:
    st.header("Technologies and GUI components")
    df = pd.DataFrame(c.TECHNOLOGIES, columns=["Technology", "Used for"])
    st.dataframe(df, hide_index=True, use_container_width=True)

elif page == PAGES[8]:
    st.header("How the code is organised")
    html(c.modules_html())
    html(c.note(c.MODULE_NOTE))
    with st.expander("Project structure in VS Code"):
        st.image(str(c.STRUCTURE_IMG), width=260)

elif page == PAGES[9]:
    st.header("Challenges and how we handled them")
    html(c.challenges_html())

elif page == PAGES[10]:
    st.header("Testing and results")
    html(c.testing_html())

elif page == PAGES[11]:
    st.header("GitHub repository and resources")
    left, right = st.columns([1, 2])
    with left:
        st.subheader("Repository")
        st.image(str(c.STRUCTURE_IMG), width=240)
        st.link_button("Open on GitHub", c.REPO_WEB)
        st.code(c.REPO_URL, language=None)
    with right:
        st.subheader("Documentation and sources")
        html(c.resources_html())
        st.subheader("What's in the repo")
        for p in c.REPO_POINTS:
            st.markdown(f"- {p}")

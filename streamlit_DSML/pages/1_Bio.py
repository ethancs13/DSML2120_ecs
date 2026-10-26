import streamlit as st
from pathlib import Path

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Ethan Sroka"
PROGRAM = "Data Science / Machine Learning"
INTRO = (
    "I'm a Data Science & Machine Learning student at MSU Denver, and I also work as a full-stack "
    "developer on Roadrunner Connect, MSU Denver's campus engagement app. On the side I've been "
    "building an interactive map of Denver's power grid that shows where the grid is out of "
    "capacity and which neighborhoods are most cost-burdened. What excites me about data "
    "visualization is how much a design choice changes what people believe, whether it's a "
    "truncated axis on a misleading chart or a map that finally makes public data easy to understand."
)
FUN_FACTS = [
    "I love turning messy public data into visuals people can actually understand, like the interactive map of Denver's power grid I've been building that shows where the grid is full and which neighborhoods are most cost-burdened.",
    "I'm learning data science and machine learning at MSU Denver while working as a full-stack developer on Roadrunner Connect, the university's campus engagement app.",
    "I want to build tools that help cities and residents make better decisions, starting with a map that shows where Denver has room to grow without raising everyone's energy bills.",
]


PHOTO_PATH = "my_photo.jpg"  # Put a file in repo root or set a URL


def find_photo(filename=PHOTO_PATH):
    # Try common locations for multipage apps
    try:
        script_dir = Path(__file__).resolve().parent
    except NameError:
        script_dir = Path.cwd()

    candidates = [
        script_dir / "assets" / filename,          # pages/assets/...
        script_dir.parent / "assets" / filename,   # root/assets/... (common)
        Path("assets") / filename,                 # cwd/assets/...
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return None

photo_src = find_photo(PHOTO_PATH)

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    if photo_src:
        st.image(photo_src, caption=NAME, use_container_width=True)
    else:
        st.info(
            "📷 Place `Your_Photo.jpg` inside an `assets/` folder at the app root "
            "or update the path in `find_photo()`."
        )
        
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")

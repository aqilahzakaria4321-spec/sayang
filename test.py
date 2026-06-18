"""
For Syafiq Hazeq — a little love letter under the stars. 💛

HOW TO RUN THIS:
  1. Install Streamlit (only once):   pip install streamlit
  2. In your terminal, run:           streamlit run for_syafiq.py
  3. It'll open in your browser. That's it!

HOW TO MAKE IT YOURS (look for the ✏️ marks below):
  - Change the date you got together (START_DATE)
  - Rewrite the letter in your own words (THE_LETTER)
  - Swap in your real reasons (REASONS)
  - Add your own photos (drop image files next to this script and
    list their filenames in PHOTOS)
"""

import streamlit as st
from datetime import date
import random

# ─────────────────────────────────────────────────────────────────────────────
# ✏️  PERSONALIZE THESE
# ─────────────────────────────────────────────────────────────────────────────

HIS_NAME = "Syafiq Hazeq"
PET_NAME = "sayang"          # ✏️ your nickname for him (or set to "")

START_DATE = date(2023, 1, 1)  # ✏️ the day you two became "us"

THE_LETTER = """\
Of all the ordinary days in the world, the best ones are the ones with you in them.

I don't always say it out loud, so I'm saying it here, in a little corner
of the internet I built just for you: thank you for being exactly who you are.
For the way you laugh at your own jokes. For making the boring parts of life
feel like somewhere I want to be.

I love you more than I know how to fit into words — so I made you a whole app
instead. 💛
"""

# ✏️ Make these true to him — small, specific, real.
REASONS = [
    "the way you say my name when you're half-asleep",
    "how you always make sure I've eaten",
    "your terrible, wonderful sense of humour",
    "the way your eyes go small when you smile for real",
    "how safe everything feels when you're near",
    "that you remember the tiny things I mention once",
    "the way you hold my hand without thinking about it",
    "how you make even a quiet night feel like the best plan",
]

# ✏️ Put real image files next to this script and list their names here.
# Leave the list empty ( PHOTOS = [] ) if you don't want photos yet.
PHOTOS = []  # e.g. ["us1.jpg", "us2.jpg", "us3.jpg"]
PHOTO_CAPTIONS = []  # optional, same length as PHOTOS

# ✏️ Inside jokes / tiny memories — they show as little notes.
LITTLE_NOTES = [
    "remember our first kiss?",
    "the song that's *ours*",
    "that time we laughed until it hurt",
]

# ─────────────────────────────────────────────────────────────────────────────
#  Page setup + styling
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title=f"For {HIS_NAME} 💛", page_icon="💛", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Caveat:wght@500;700&family=Nunito+Sans:wght@300;400;600&display=swap');

    /* dusk sky background with a soft scatter of stars */
    .stApp {
        background:
            radial-gradient(1px 1px at 20% 30%, rgba(255,235,200,.9), transparent),
            radial-gradient(1px 1px at 70% 20%, rgba(255,235,200,.7), transparent),
            radial-gradient(1px 1px at 40% 70%, rgba(255,235,200,.8), transparent),
            radial-gradient(1px 1px at 85% 60%, rgba(255,235,200,.6), transparent),
            radial-gradient(1px 1px at 55% 45%, rgba(255,235,200,.7), transparent),
            radial-gradient(1200px 700px at 50% -10%, #4a3550 0%, transparent 60%),
            linear-gradient(180deg, #2a1d33 0%, #3b2535 55%, #4a2c33 100%);
        background-attachment: fixed;
    }

    /* hide Streamlit chrome for a cleaner, intimate feel */
    #MainMenu, header, footer {visibility: hidden;}

    .block-container {padding-top: 3rem; max-width: 720px;}

    h1, h2, h3, p, label, span, div {color: #f6ead7;}

    .eyebrow {
        font-family: 'Caveat', cursive;
        font-size: 1.9rem;
        color: #e8b96a;
        text-align: center;
        margin-bottom: -0.4rem;
    }
    .bigname {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 600;
        font-size: 4.2rem;
        line-height: 1.05;
        text-align: center;
        letter-spacing: .5px;
        background: linear-gradient(180deg, #fbf0db, #e8b96a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 .2rem 0;
    }
    .subtle {
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 300;
        text-align: center;
        color: #d9b8c0;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-size: .75rem;
    }

    .paper {
        background: rgba(251, 240, 219, 0.06);
        border: 1px solid rgba(232, 185, 106, 0.25);
        border-radius: 18px;
        padding: 1.8rem 2rem;
        margin: 1.2rem 0;
        box-shadow: 0 18px 50px rgba(0,0,0,.35);
        backdrop-filter: blur(2px);
    }
    .letter {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.35rem;
        line-height: 1.7;
        color: #f6ead7;
        font-style: italic;
        white-space: pre-line;
    }
    .signature {
        font-family: 'Caveat', cursive;
        font-size: 2.1rem;
        color: #e8b96a;
        text-align: right;
        margin-top: .6rem;
    }
    .reason-card {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.7rem;
        line-height: 1.5;
        text-align: center;
        color: #fbf0db;
        font-style: italic;
        min-height: 3.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .section-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.1rem;
        text-align: center;
        color: #f6ead7;
        margin: 2.4rem 0 .2rem 0;
    }
    .note-chip {
        display: inline-block;
        font-family: 'Caveat', cursive;
        font-size: 1.3rem;
        color: #3b2535;
        background: linear-gradient(180deg, #f6e3b0, #e8b96a);
        padding: .35rem 1rem;
        border-radius: 999px;
        margin: .3rem;
        transform: rotate(-2deg);
        box-shadow: 0 6px 16px rgba(0,0,0,.25);
    }

    /* buttons */
    .stButton > button {
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 600;
        color: #3b2535;
        background: linear-gradient(180deg, #f6e3b0, #e8b96a);
        border: none;
        border-radius: 999px;
        padding: .55rem 1.6rem;
        box-shadow: 0 10px 24px rgba(232,185,106,.25);
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(232,185,106,.4);
        color: #3b2535;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
#  Header
# ─────────────────────────────────────────────────────────────────────────────

greeting = f"to my {PET_NAME}," if PET_NAME else "to you,"
st.markdown(f'<div class="eyebrow">{greeting}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="bigname">{HIS_NAME}</div>', unsafe_allow_html=True)

days = (date.today() - START_DATE).days
st.markdown(
    f'<div class="subtle">{days:,} days of us &nbsp;·&nbsp; and counting</div>',
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
#  The letter (unfolds)
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">A letter, just for you</div>', unsafe_allow_html=True)

if "opened" not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<p style='text-align:center;font-size:3rem;margin:.5rem 0;'>💌</p>", unsafe_allow_html=True)
        if st.button("Open the letter", use_container_width=True):
            st.session_state.opened = True
            st.rerun()
else:
    sign = f"— always yours 💛" if not PET_NAME else f"— always yours, {PET_NAME} 💛"
    st.markdown(
        f'<div class="paper"><div class="letter">{THE_LETTER}</div>'
        f'<div class="signature">{sign}</div></div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────────────────────────
#  Reasons deck
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">Reasons I adore you</div>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#d9b8c0;font-family:Nunito Sans;font-weight:300;'>"
    "(there are far too many — here's one at a time)</p>",
    unsafe_allow_html=True,
)

if "reason" not in st.session_state:
    st.session_state.reason = random.choice(REASONS)

st.markdown(
    f'<div class="paper"><div class="reason-card">“{st.session_state.reason}”</div></div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if st.button("Tell me another 💞", use_container_width=True):
        choices = [r for r in REASONS if r != st.session_state.reason] or REASONS
        st.session_state.reason = random.choice(choices)
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
#  Photos (optional)
# ─────────────────────────────────────────────────────────────────────────────

if PHOTOS:
    st.markdown('<div class="section-title">Us</div>', unsafe_allow_html=True)
    cols = st.columns(min(3, len(PHOTOS)))
    for i, img in enumerate(PHOTOS):
        with cols[i % len(cols)]:
            cap = PHOTO_CAPTIONS[i] if i < len(PHOTO_CAPTIONS) else None
            try:
                st.image(img, caption=cap, use_container_width=True)
            except Exception:
                st.markdown(f"<p style='text-align:center;'>📷 add <code>{img}</code></p>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  Little notes
# ─────────────────────────────────────────────────────────────────────────────

if LITTLE_NOTES:
    st.markdown('<div class="section-title">Our little universe</div>', unsafe_allow_html=True)
    chips = "".join(f'<span class="note-chip">{n}</span>' for n in LITTLE_NOTES)
    st.markdown(f'<div style="text-align:center;">{chips}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  The sweet ending
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">One last thing…</div>', unsafe_allow_html=True)

if "yes_count" not in st.session_state:
    st.session_state.yes_count = 0

q = f"Will you keep being mine, {HIS_NAME.split()[0]}?"
st.markdown(
    f"<p style='text-align:center;font-family:Cormorant Garamond;font-size:1.9rem;font-style:italic;'>{q}</p>",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns([1, 1.2, 1.2, 1])
with c2:
    if st.button("Yes, always 💛", use_container_width=True):
        st.session_state.yes_count += 1
        st.balloons()
with c3:
    if st.button("Obviously yes 🥹", use_container_width=True):
        st.session_state.yes_count += 1
        st.snow()

if st.session_state.yes_count:
    sweet = [
        "I was hoping you'd say that. 💛",
        "Lucky me. Forever. 🌙",
        "That's all I ever wanted to hear.",
        "You + me. Best decision ever.",
    ]
    msg = sweet[min(st.session_state.yes_count - 1, len(sweet) - 1)]
    st.markdown(
        f"<p style='text-align:center;font-family:Caveat;font-size:1.8rem;color:#e8b96a;'>{msg}</p>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<p style='text-align:center;color:#a98a92;font-family:Nunito Sans;font-weight:300;"
    "font-size:.8rem;margin-top:2.5rem;'>made with 💛, just for you</p>",
    unsafe_allow_html=True,
)
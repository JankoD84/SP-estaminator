"""
Agile Story Point Estimator — Streamlit Web UI Version

Provides a browser-based interface where users move sliders for:
  - Complexity
  - Effort
  - Uncertainty

Clicking "Estimate Story Points" displays the total score and
the corresponding Fibonacci story point value.

Run with:
    streamlit run estimator_app.py
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Mapping: total score -> Fibonacci story points
# ---------------------------------------------------------------------------

SCORE_TO_STORY_POINTS = [
    (range(3, 5),   1),
    (range(5, 7),   2),
    (range(7, 9),   3),
    (range(9, 11),  5),
    (range(11, 13), 8),
    (range(13, 15), 13),
    (range(15, 16), 21),
]

# Human-readable descriptions shown next to each slider value
COMPLEXITY_LABELS  = {1: "Trivial", 2: "Simple", 3: "Moderate", 4: "Complex", 5: "Highly Complex"}
EFFORT_LABELS      = {1: "Hours", 2: "One Day", 3: "Several Days", 4: "Large", 5: "Very Large"}
UNCERTAINTY_LABELS = {1: "Fully Known", 2: "Minor Unknowns", 3: "Some Unknowns", 4: "Significant Unknowns", 5: "Highly Uncertain"}


# ---------------------------------------------------------------------------
# Core calculation logic
# ---------------------------------------------------------------------------

def map_score_to_story_points(score: int) -> int:
    """
    Convert a combined score (3–15) into a Fibonacci story point value.

    Score -> Story Points:
        3–4  -> 1       7–8  -> 3      11–12 -> 8
        5–6  -> 2       9–10 -> 5      13–14 -> 13
                                       15    -> 21
    """
    for score_range, story_points in SCORE_TO_STORY_POINTS:
        if score in score_range:
            return story_points
    raise ValueError(f"Score {score} is outside the valid range (3–15).")


def get_story_point_badge_color(story_points: int) -> str:
    """
    Return a hex color that gives visual weight to higher estimates.
    Low estimates are green, medium are orange, high are red.
    """
    if story_points <= 2:
        return "#2ecc71"   # green
    elif story_points <= 5:
        return "#f39c12"   # orange
    elif story_points <= 13:
        return "#e67e22"   # dark orange
    else:
        return "#e74c3c"   # red


# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Agile Story Point Estimator",
    page_icon="📊",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.title("📊 Agile Story Point Estimator")
st.markdown(
    """
    > **Story points** are relative estimates used in Agile to measure
    > the **effort and complexity** of work. They help teams plan sprints
    > without committing to exact hours.

    Rate each factor from **1** (lowest) to **5** (highest), then click
    **Estimate Story Points** to see your result.
    """
)

st.divider()

# ---------------------------------------------------------------------------
# Criterion sliders
# ---------------------------------------------------------------------------

st.subheader("1. Complexity")
st.caption("How technically difficult is this task?")
complexity = st.slider(
    label="Complexity",
    min_value=1,
    max_value=5,
    value=3,
    label_visibility="collapsed",
)
st.info(f"Selected: **{complexity}** — {COMPLEXITY_LABELS[complexity]}")

st.subheader("2. Effort")
st.caption("How much work is involved?")
effort = st.slider(
    label="Effort",
    min_value=1,
    max_value=5,
    value=3,
    label_visibility="collapsed",
)
st.info(f"Selected: **{effort}** — {EFFORT_LABELS[effort]}")

st.subheader("3. Uncertainty")
st.caption("How well understood is this task?")
uncertainty = st.slider(
    label="Uncertainty",
    min_value=1,
    max_value=5,
    value=3,
    label_visibility="collapsed",
)
st.info(f"Selected: **{uncertainty}** — {UNCERTAINTY_LABELS[uncertainty]}")

st.divider()

# ---------------------------------------------------------------------------
# Estimation button and result
# ---------------------------------------------------------------------------

if st.button("Estimate Story Points", type="primary", use_container_width=True):

    total_score  = complexity + effort + uncertainty
    story_points = map_score_to_story_points(total_score)
    badge_color  = get_story_point_badge_color(story_points)

    st.subheader("Results")

    # Three metric columns: one per criterion
    col1, col2, col3 = st.columns(3)
    col1.metric("Complexity",  complexity)
    col2.metric("Effort",      effort)
    col3.metric("Uncertainty", uncertainty)

    # Total score
    st.metric(label="Total Score", value=total_score, delta=f"out of 15")

    # Story point badge — rendered as a large, coloured HTML block
    st.markdown(
        f"""
        <div style="
            background-color: {badge_color};
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            margin-top: 16px;
        ">
            <p style="color: white; font-size: 18px; margin: 0;">Estimated Story Points</p>
            <p style="color: white; font-size: 64px; font-weight: bold; margin: 0;">
                {story_points} SP
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Explanation of the Fibonacci scale
    st.markdown(
        """
        ---
        **About the Fibonacci scale:**
        Agile teams use Fibonacci numbers (1, 2, 3, 5, 8, 13, 21 …) because the
        increasing gaps naturally reflect the *growing uncertainty* in larger tasks.
        A task estimated at 21 SP is not just "21× harder" than a 1 SP task —
        it signals that the work is large, complex, and should probably be broken down.
        """
    )

# ---------------------------------------------------------------------------
# Sidebar: quick reference table
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("Score Reference")
    st.markdown(
        """
        | Score | Story Points |
        |-------|-------------|
        | 3–4   | 1 SP        |
        | 5–6   | 2 SP        |
        | 7–8   | 3 SP        |
        | 9–10  | 5 SP        |
        | 11–12 | 8 SP        |
        | 13–14 | 13 SP       |
        | 15    | 21 SP       |
        """
    )
    st.divider()
    st.markdown(
        """
        **Score = Complexity + Effort + Uncertainty**

        Each factor is rated 1–5.
        Minimum score: **3** → **1 SP**
        Maximum score: **15** → **21 SP**
        """
    )

"""BHAGE v0.1 — visual dashboard shell.

Only interface elements are implemented. Genomic analysis, model predictions,
and research evaluation will be connected later from modules in bhage/.
"""

import streamlit as st


# ── Page and navigation state ────────────────────────────────────────────────
st.set_page_config(
    page_title="BHAGE | Research Workspace",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PAGES = ("Overview", "Genome Analysis", "Host Prediction", "Research")
if st.session_state.get("bhage_page") not in PAGES:
    st.session_state.bhage_page = "Overview"


def navigate(page: str) -> None:
    """Switch dashboard views without leaving the current Streamlit app."""
    st.session_state.bhage_page = page


# ── Theme and layout ─────────────────────────────────────────────────────────
# Custom CSS is isolated to the dashboard shell and its navigation keys.
# This implements the compact centered style of the BHAGE design mockups.
active_nav_key = {
    "Overview": "overview",
    "Genome Analysis": "genome",
    "Host Prediction": "prediction",
    "Research": "research",
}[st.session_state.bhage_page]

st.markdown(
    """
<style>
    :root {
        --bh-bg: #080909;
        --bh-surface: #0b0d0c;
        --bh-panel: #101411;
        --bh-border: #292e2b;
        --bh-text: #f1f2f1;
        --bh-muted: #a4aaa6;
        --bh-sage: #a3dabc;
        --bh-selected: #293d35;
    }
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background: var(--bh-bg) !important;
        color: var(--bh-text);
    }
    [data-testid="stHeader"] { background: transparent !important; height: 0; }
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    #MainMenu, footer { visibility: hidden; }

    .block-container {
        max-width: 1120px !important;
        padding: 20px 14px 30px !important;
    }
    /* One visual shell contains the entire BHAGE experience. */
    .st-key-bhage_shell {
        border: 1px solid var(--bh-border);
        border-radius: 22px;
        background: #050605;
        padding: 17px 18px 15px;
    }
    /* Remove the default Streamlit's generous vertical spacing in this shell. */
    .st-key-bhage_shell [data-testid="stVerticalBlock"] { gap: .72rem; }
    .st-key-bhage_shell [data-testid="stHorizontalBlock"] { gap: .75rem; }
    .st-key-bhage_shell [data-testid="stMarkdownContainer"] p { margin-bottom: 0; }

    .bh-brandbar { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 4px; }
    .bh-brandgroup { display: flex; gap: 12px; align-items: center; }
    .bh-logo {
        height: 49px; width: 49px; border-radius: 11px;
        background: #213b32; display: flex; justify-content: center;
        align-items: center; color: var(--bh-sage); font-size: 26px;
    }
    .bh-brandname { font-size: 25px; font-weight: 760; line-height: 1.17; letter-spacing: -.03em; }
    .bh-brandcaption { color: var(--bh-muted); font-size: 12px; padding-top: 3px; }
    .bh-version { color: #e2e4e2; background: #202220; border-radius: 999px; padding: 4px 11px; font-size: 13px; font-weight: 650; }

    /* Make the Streamlit buttons look like the mockup's top navigation tiles. */
    .st-key-bhage_shell [class*="st-key-bh_nav_"] button {
        width: 100%; height: 47px; justify-content: flex-start;
        padding: 0 14px; gap: 8px;
        background: #070908; border: 1px solid #232925;
        border-radius: 10px; color: #e9ecea;
        box-shadow: none; transition: border-color .12s, background .12s;
        font-size: 14px; font-weight: 450;
    }
    .st-key-bhage_shell [class*="st-key-bh_nav_"] button:hover {
        background: #17261f; color: white; border-color: #668d76;
    }
    .st-key-bhage_shell [class*="st-key-bh_nav_"] button:focus:not(:active) { color: white; }
    .st-key-bhage_shell [class*="st-key-bh_nav_"] button [data-testid="stIconMaterial"] { color: #bfc9c1; }

    .bh-divider { border-top: 1px solid #232824; margin: 7px 0 18px; }
    .bh-heading { font-size: 24px; letter-spacing: -.025em; font-weight: 750; margin: 3px 0 2px; }
    .bh-description { font-size: 15px; color: #b3b6b3; margin: 0 0 18px; }
    .bh-grid { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 16px 24px; margin-top: 19px; }
    .bh-metric { min-height: 105px; padding: 10px 15px 13px; border-radius: 10px; background: #070908; }
    .bh-metric-label { text-transform: uppercase; color: #c4c8c5; font-size: 12px; letter-spacing: .008em; margin-bottom: 13px; display:flex; align-items:center; justify-content:space-between; }
    .bh-metric-value { color: #f0f1f0; font-weight: 600; font-size: 24px; line-height: 1.15; }
    .bh-metric-note { color: var(--bh-muted); font-size: 15px; margin-top: 11px; }
    .bh-card { border: 1px solid var(--bh-border); border-radius: 17px; padding: 19px 17px; margin-top: 17px; background: #070908; }
    .bh-card-title { font-size: 19px; font-weight: 700; margin-bottom: 12px; }
    .bh-card-text { color: #e1e4e1; font-size: 16px; line-height: 1.6; }
    .bh-section { font-size: 20px; font-weight: 700; margin: 23px 0 12px; }
    .bh-status { color: #b5dfc6; font-size: 15px; display:flex; align-items:center; gap:8px; margin-top:16px; }
    .bh-statusdot { width: 14px; height: 14px; border: 2px solid var(--bh-sage); border-radius: 50%; display: inline-block; box-shadow: inset 0 0 0 3px #070908; background: var(--bh-sage); }
    .bh-center { border: 1px solid var(--bh-border); border-radius: 16px; text-align: center; padding: 28px 22px; background: #060706; }
    .bh-center-icon { color: var(--bh-sage); font-size: 34px; line-height: 1; margin-bottom: 16px; }
    .bh-center-title { color: #f0f2f0; font-size: 21px; font-weight: 720; margin: 5px 0 13px; }
    .bh-center-text { color: #b2b6b3; font-size: 16px; line-height: 1.5; }
    .bh-pill { display:inline-block; margin-top:12px; border-radius: 999px; padding: 4px 12px; background:#232524; color:#e8e8e8; font-weight:600; font-size:13px; }
    .bh-footer { border-top: 1px solid #161a17; padding-top: 16px; margin-top: 24px; display: flex; justify-content: space-between; align-items:center; gap:8px; font-size: 12px; color: #a1a6a2; }
    .bh-footer-dot { background: #a3dabc; width: 13px; height: 13px; display:inline-block; border-radius:50%; vertical-align:middle; margin-right:5px; }

    @media (max-width: 650px) {
        .block-container { padding: 9px 5px 20px !important; }
        .st-key-bhage_shell { padding: 12px 11px; border-radius: 15px; }
        .bh-heading { font-size:22px; }
        .bh-grid { gap: 8px; }
        .bh-metric { padding: 10px 8px; }
        .bh-metric-note { font-size: 12px; }
        .bh-card-text { font-size: 14px; }
        .st-key-bhage_shell [class*="st-key-bh_nav_"] button { padding: 0 7px; font-size: 12px; }
        .bh-brandname {font-size:22px;}
    }
</style>
"""
    + f"""
<style>
    .st-key-bh_nav_{active_nav_key} button {{
        background: #293d35 !important;
        border-color: #6a9880 !important;
        color: #f2f5f2 !important;
        font-weight: 700 !important;
    }}
</style>
""",
    unsafe_allow_html=True,
)


# ── Reusable display-only components ────────────────────────────────────────
def page_heading(title: str, description: str) -> None:
    st.markdown(
        f'<div class="bh-heading">{title}</div>'
        f'<div class="bh-description">{description}</div>',
        unsafe_allow_html=True,
    )


def metric(label: str, note: str = "Awaiting research data", icon: str = "") -> str:
    """Create an empty metric; do not imply zero or fabricated results."""
    return (
        '<div class="bh-metric">'
        f'<div class="bh-metric-label"><span>{label}</span><span>{icon}</span></div>'
        '<div class="bh-metric-value">—</div>'
        f'<div class="bh-metric-note">{note}</div>'
        '</div>'
    )


def metric_grid(items: list[tuple[str, str, str]]) -> None:
    st.markdown(
        '<div class="bh-grid">'
        + ''.join(metric(label, note, icon) for label, note, icon in items)
        + '</div>',
        unsafe_allow_html=True,
    )


def centered_placeholder(icon: str, title: str, message: str, badge: str = "") -> None:
    badge_html = f'<div><span class="bh-pill">{badge}</span></div>' if badge else ''
    st.markdown(
        f'<div class="bh-center"><div class="bh-center-icon">{icon}</div>'
        f'<div class="bh-center-title">{title}</div>'
        f'<div class="bh-center-text">{message}</div>{badge_html}</div>',
        unsafe_allow_html=True,
    )


# ── One centered app shell ───────────────────────────────────────────────────
with st.container(key="bhage_shell"):
    st.markdown(
        '<div class="bh-brandbar">'
        '<div class="bh-brandgroup"><div class="bh-logo">🧬</div>'
        '<div><div class="bh-brandname">BHAGE</div>'
        '<div class="bh-brandcaption">Phage Bot · Research Workspace</div>'
        '</div></div><span class="bh-version">v0.1</span></div>',
        unsafe_allow_html=True,
    )

    # Two columns and two rows, matching the original mockup navigation.
    first, second = st.columns(2)
    with first:
        st.button("Overview", icon=":material/dashboard:", key="bh_nav_overview", use_container_width=True,
                  on_click=navigate, args=("Overview",))
    with second:
        st.button("Genome Analysis", icon=":material/biotech:", key="bh_nav_genome", use_container_width=True,
                  on_click=navigate, args=("Genome Analysis",))
    third, fourth = st.columns(2)
    with third:
        st.button("Host Prediction", icon=":material/adjust:", key="bh_nav_prediction", use_container_width=True,
                  on_click=navigate, args=("Host Prediction",))
    with fourth:
        st.button("Research", icon=":material/science:", key="bh_nav_research", use_container_width=True,
                  on_click=navigate, args=("Research",))

    st.markdown('<div class="bh-divider"></div>', unsafe_allow_html=True)

    if st.session_state.bhage_page == "Overview":
        page_heading("Research Overview", "Your BHAGE research at a glance.")
        metric_grid([
            ("Genomes analyzed", "Awaiting research data", "◫"),
            ("Model accuracy", "Awaiting research data", "▥"),
            ("Host classes", "Awaiting research data", "♧"),
            ("Latest experiment", "Awaiting research data", "⚗"),
        ])
        st.markdown(
            '<div class="bh-card">'
            '<div class="bh-card-title">Current Research Objective</div>'
            '<div class="bh-card-text">Investigate bacterial host-genus prediction '
            'using bacteriophage genomic features.</div>'
            '<div class="bh-status"><span class="bh-statusdot"></span>'
            'Status: Initial development</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    elif st.session_state.bhage_page == "Genome Analysis":
        page_heading("Genome Analysis", "Analyze sequence-derived genomic characteristics.")
        centered_placeholder("⇧", "Upload a FASTA file", "Interface placeholder · Not connected yet")
        metric_grid([
            ("GC content", "Awaiting analysis", ""),
            ("Genome length", "Awaiting analysis", ""),
            ("Nucleotide counts", "Awaiting analysis", ""),
            ("K-mer features", "Planned for v0.2", ""),
        ])

    elif st.session_state.bhage_page == "Host Prediction":
        page_heading("Host Prediction", "Machine learning predictions from genomic data.")
        centered_placeholder(
            "♧", "No trained model available",
            "Predicted bacterial host genera and associated model scores will appear here "
            "once training and evaluation are complete.",
            "Not implemented",
        )
        st.markdown(
            '<div class="bh-card">'
            '<div class="bh-card-title">Planned output</div>'
            '<div class="bh-card-text">Top host label · Alternative labels · '
            'Model information · Prediction limitations</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    else:
        page_heading("Research Evaluation", "Examine how well BHAGE’s models perform.")
        metric_grid([
            ("Accuracy", "Not evaluated", "%"),
            ("Balanced Accuracy", "Not evaluated", "⚖"),
            ("Confusion Matrix", "Not evaluated", "▦"),
            ("Feature Comparison", "Not evaluated", "▥"),
        ])
        st.markdown(
            '<div class="bh-card">'
            '<div class="bh-card-title">Experiment history</div>'
            '<div class="bh-card-text" style="color:#b3b6b3">'
            'No experiments recorded yet.</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="bh-footer"><span>BHAGE · DEVELOPMENT BUILD</span>'
        '<span><i class="bh-footer-dot"></i>Dashboard shell</span></div>',
        unsafe_allow_html=True,
    )

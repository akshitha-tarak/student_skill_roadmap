# import streamlit as st
# import pandas as pd
# import random
# from datetime import date

# st.set_page_config(
#     page_title=" Personalized Skill Roadmap",
#     page_icon="🎯",
#     layout="wide",
# )

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

# :root {
#   --bg:        #020817;
#   --surface:   rgba(15,23,42,0.72);
#   --border:    rgba(99,102,241,0.22);
#   --indigo:    #6366f1;
#   --violet:    #8b5cf6;
#   --emerald:   #34d399;
#   --sky:       #38bdf8;
#   --amber:     #fbbf24;
#   --rose:      #fb7185;
#   --text:      #e2e8f0;
#   --muted:     #64748b;
# }

# html, body, [class*="css"] {
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
#   background: var(--bg) !important;
#   color: var(--text) !important;
# }
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding-top: 0 !important; max-width: 100% !important; }

# ::-webkit-scrollbar { width: 6px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: var(--indigo); border-radius: 99px; }

# /* ── LANDING ── */
# .landing {
#   min-height: 100vh;
#   background:
#     radial-gradient(ellipse 80% 60% at 15% 55%,  rgba(99,102,241,0.38) 0%, transparent 60%),
#     radial-gradient(ellipse 60% 50% at 85% 25%,  rgba(139,92,246,0.30) 0%, transparent 55%),
#     radial-gradient(ellipse 70% 55% at 55% 90%,  rgba(16,185,129,0.18) 0%, transparent 58%),
#     radial-gradient(ellipse 50% 40% at 80% 75%,  rgba(56,189,248,0.12) 0%, transparent 55%),
#     #020817;
#   padding-bottom: 80px;
# }
# .nav {
#   display: flex; align-items: center; justify-content: space-between;
#   padding: 20px 48px;
#   border-bottom: 1px solid rgba(255,255,255,0.06);
# }
# .nav-logo {
#   font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .nav-badge {
#   background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.30);
#   color: #a5b4fc; font-size: 11px; font-weight: 600; padding: 5px 14px;
#   border-radius: 999px; letter-spacing: 0.06em;
# }
# .hero { text-align: center; padding: 72px 24px 48px; }
# .confused-tag {
#   display: inline-block;
#   background: rgba(251,191,36,0.12); border: 1px solid rgba(251,191,36,0.30);
#   color: #fcd34d; font-size: 13px; font-weight: 600;
#   padding: 6px 18px; border-radius: 999px; margin-bottom: 28px;
#   letter-spacing: 0.04em; animation: fadeDown 0.6s ease both;
# }
# @keyframes fadeDown {
#   from { opacity:0; transform:translateY(-12px); }
#   to   { opacity:1; transform:translateY(0); }
# }
# .hero-h1 {
#   font-family: 'Syne', sans-serif;
#   font-size: clamp(32px, 6vw, 60px); font-weight: 800; line-height: 1.08;
#   margin-bottom: 22px; animation: fadeDown 0.7s ease 0.1s both;
# }
# .hero-h1 .line1 {
#   display: block;
#   background: linear-gradient(135deg, #fff 30%, #c7d2fe);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .hero-h1 .line2 {
#   display: block;
#   background: linear-gradient(135deg, #a5b4fc, #34d399 70%);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .hero-sub {
#   font-size: 16px; color: #64748b; max-width: 520px;
#   margin: 0 auto 40px; line-height: 1.7;
#   animation: fadeDown 0.7s ease 0.2s both;
# }
# .quote-card {
#   max-width: 600px; margin: 0 auto 52px;
#   background: rgba(15,23,42,0.70); backdrop-filter: blur(12px);
#   border: 1px solid rgba(99,102,241,0.22); border-left: 4px solid #6366f1;
#   border-radius: 16px; padding: 22px 28px;
#   animation: fadeDown 0.7s ease 0.3s both;
# }
# .quote-text  { font-size: 15px; font-style: italic; color: #e2e8f0; line-height: 1.65; margin-bottom: 10px; }
# .quote-author{ font-size: 12px; color: #6366f1; font-weight: 600; letter-spacing: 0.05em; }
# .img-row {
#   display: flex; justify-content: center; gap: 16px;
#   margin: 0 auto 56px; max-width: 860px; padding: 0 24px;
#   animation: fadeDown 0.7s ease 0.35s both;
# }
# .img-card {
#   flex: 1; min-width: 0; border-radius: 20px; overflow: hidden;
#   border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 8px 32px rgba(0,0,0,0.45);
#   position: relative; transition: transform 0.25s;
# }
# .img-card:hover { transform: translateY(-5px); }
# .img-card img  { width: 100%; height: 200px; object-fit: cover; display: block; filter: brightness(0.82) saturate(1.1); }
# .img-overlay   { position: absolute; bottom:0; left:0; right:0; background: linear-gradient(transparent, rgba(2,8,23,0.85)); padding: 20px 16px 14px; }
# .img-label     { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; color: #fff; }
# .img-sub       { font-size: 11px; color: rgba(255,255,255,0.50); margin-top: 2px; }
# .stats-row {
#   display: flex; justify-content: center; gap: 32px;
#   margin: 0 auto 56px; flex-wrap: wrap;
#   animation: fadeDown 0.7s ease 0.4s both;
# }
# .stat-num {
#   font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .stat-label { font-size: 12px; color: #475569; margin-top: 4px; letter-spacing: 0.04em; text-transform: uppercase; }
# .features {
#   display: flex; justify-content: center; gap: 16px;
#   max-width: 860px; margin: 0 auto 56px; padding: 0 24px; flex-wrap: wrap;
#   animation: fadeDown 0.7s ease 0.45s both;
# }
# .feat-card {
#   flex: 1; min-width: 200px;
#   background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.18);
#   border-radius: 16px; padding: 20px 18px; backdrop-filter: blur(10px);
#   transition: border-color 0.2s, transform 0.2s;
# }
# .feat-card:hover { border-color: rgba(99,102,241,0.45); transform: translateY(-3px); }
# .feat-icon  { font-size: 24px; margin-bottom: 10px; }
# .feat-title { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 6px; }
# .feat-desc  { font-size: 12px; color: #64748b; line-height: 1.6; }

# /* ── CTA button ── */
# div[data-testid="stButton"] > button {
#   background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
#   color: #fff !important; border: none !important; border-radius: 14px !important;
#   padding: 16px 48px !important; font-family: 'Syne', sans-serif !important;
#   font-size: 16px !important; font-weight: 800 !important; letter-spacing: 0.04em !important;
#   box-shadow: 0 6px 28px rgba(99,102,241,0.45) !important;
#   transition: all 0.2s !important; min-width: 260px !important;
# }
# div[data-testid="stButton"] > button:hover {
#   opacity: 0.88 !important; transform: translateY(-3px) !important;
#   box-shadow: 0 12px 36px rgba(99,102,241,0.55) !important;
# }

# /* ── APP PAGE ── */
# .app-header {
#   padding: 20px 48px 18px;
#   border-bottom: 1px solid rgba(99,102,241,0.18);
#   background: rgba(2,8,23,0.97) !important;
#   backdrop-filter: blur(20px);
#   -webkit-backdrop-filter: blur(20px);
#   position: sticky; top: 0; z-index: 100;
# }
# .app-logo {
#   font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .g-card {
#   background: rgba(15,23,42,0.65);
#   border: 1px solid rgba(99,102,241,0.20);
#   border-radius: 20px; padding: 28px 32px;
#   backdrop-filter: blur(14px);
#   margin-bottom: 20px;
#   box-shadow: 0 4px 24px rgba(0,0,0,0.35);
# }
# .g-card-title {
#   font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
#   color: #e2e8f0; margin-bottom: 6px;
# }
# .g-card-sub { font-size: 13px; color: #475569; }
# .sec-pill {
#   display: inline-flex; align-items: center; gap: 8px;
#   background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.28);
#   color: #a5b4fc; font-size: 12px; font-weight: 700;
#   padding: 5px 16px; border-radius: 999px; letter-spacing: 0.06em;
#   margin-bottom: 16px; text-transform: uppercase;
# }
# .goal-item {
#   display: flex; align-items: flex-start; gap: 12px;
#   background: rgba(52,211,153,0.07); border: 1px solid rgba(52,211,153,0.20);
#   border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
# }
# .goal-dot { width: 8px; height: 8px; border-radius: 50%; background: #34d399; margin-top: 5px; flex-shrink: 0; }
# .goal-text { font-size: 14px; color: #e2e8f0; line-height: 1.6; }
# .risk-item {
#   display: flex; align-items: flex-start; gap: 12px;
#   background: rgba(251,113,133,0.08); border: 1px solid rgba(251,113,133,0.22);
#   border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
# }
# .risk-dot { width: 8px; height: 8px; border-radius: 50%; background: #fb7185; margin-top: 5px; flex-shrink: 0; }
# .habit-item {
#   display: flex; align-items: flex-start; gap: 12px;
#   background: rgba(56,189,248,0.07); border: 1px solid rgba(56,189,248,0.20);
#   border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
# }
# .habit-dot { width: 8px; height: 8px; border-radius: 50%; background: #38bdf8; margin-top: 5px; flex-shrink: 0; }
# .step-item {
#   display: flex; align-items: flex-start; gap: 14px;
#   background: rgba(139,92,246,0.07); border: 1px solid rgba(139,92,246,0.20);
#   border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
# }
# .step-num {
#   width: 26px; height: 26px; border-radius: 50%;
#   background: linear-gradient(135deg, #6366f1, #8b5cf6);
#   display: flex; align-items: center; justify-content: center;
#   font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
# }
# .week-card {
#   background: rgba(15,23,42,0.60); border: 1px solid rgba(99,102,241,0.18);
#   border-radius: 16px; padding: 20px 24px; margin-bottom: 16px;
# }
# .week-title {
#   font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 800;
#   margin-bottom: 12px;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .week-bullet {
#   display: flex; align-items: flex-start; gap: 10px;
#   font-size: 13px; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;
# }
# .week-bullet::before { content: '▸'; color: #6366f1; flex-shrink: 0; margin-top: 1px; }
# .proj-card {
#   background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.20);
#   border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
#   display: flex; align-items: center; gap: 12px;
# }
# .proj-icon { font-size: 20px; }
# .proj-name { font-size: 14px; font-weight: 600; color: #fcd34d; }
# .res-card {
#   background: rgba(56,189,248,0.06); border: 1px solid rgba(56,189,248,0.20);
#   border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
#   display: flex; align-items: center; gap: 12px;
# }
# .res-icon { font-size: 18px; }
# .res-name  { font-size: 14px; color: #7dd3fc; }
# .score-ring-wrap { text-align: center; padding: 20px 0; }
# .score-big {
#   font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
#   line-height: 1;
# }
# .score-label { font-size: 13px; color: #475569; margin-top: 4px; letter-spacing: 0.08em; text-transform: uppercase; }
# .score-bar-wrap { margin-bottom: 14px; }
# .score-bar-label {
#   display: flex; justify-content: space-between;
#   font-size: 12px; font-weight: 600; margin-bottom: 5px;
# }
# .score-bar-track {
#   height: 8px; border-radius: 999px; background: rgba(255,255,255,0.08);
#   overflow: hidden;
# }
# .score-bar-fill { height: 100%; border-radius: 999px; }
# .metric-tile {
#   background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.20);
#   border-radius: 16px; padding: 18px 22px; text-align: center;
# }
# .metric-val {
#   font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
#   background: linear-gradient(135deg, #a5b4fc, #34d399);
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .metric-label { font-size: 11px; color: #475569; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; }
# .skill-have {
#   background: rgba(52,211,153,0.10); border: 1px solid rgba(52,211,153,0.30);
#   border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
#   font-size: 13px; color: #6ee7b7; font-weight: 600;
#   display: flex; align-items: center; gap: 8px;
# }
# .skill-need {
#   background: rgba(251,113,133,0.10); border: 1px solid rgba(251,113,133,0.30);
#   border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
#   font-size: 13px; color: #fda4af; font-weight: 600;
#   display: flex; align-items: center; gap: 8px;
# }
# .learn-step {
#   display: flex; align-items: center; gap: 12px;
#   background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.22);
#   border-radius: 12px; padding: 12px 16px; margin-bottom: 8px;
# }
# .learn-step-num {
#   width: 28px; height: 28px; border-radius: 50%;
#   background: linear-gradient(135deg, #8b5cf6, #6366f1);
#   display: flex; align-items: center; justify-content: center;
#   font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
# }
# .learn-step-text { font-size: 14px; color: #c4b5fd; }

# /* ── PROGRESS BAR ── */
# .stProgress > div > div > div > div {
#   background: linear-gradient(90deg, #6366f1, #8b5cf6, #34d399) !important;
#   border-radius: 999px !important;
# }
# .stProgress > div > div > div { background: rgba(255,255,255,0.08) !important; border-radius: 999px !important; }

# /* ════════════════════════════════════════
#    SELECTBOX — ALWAYS VISIBLE (BUG FIX)
#    ════════════════════════════════════════ */
# div[data-baseweb="select"] > div {
#   background: rgba(15,23,42,0.88) !important;
#   border: 1.5px solid rgba(99,102,241,0.55) !important;
#   border-radius: 12px !important;
#   color: #e2e8f0 !important;
#   transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# div[data-baseweb="select"] > div:hover {
#   border-color: rgba(99,102,241,0.90) !important;
#   box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
# }
# div[data-baseweb="select"] > div:focus-within {
#   border-color: #6366f1 !important;
#   box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
# }
# div[data-baseweb="select"] span,
# div[data-baseweb="select"] div[class*="ValueContainer"] {
#   color: #e2e8f0 !important;
#   background: transparent !important;
# }
# div[data-baseweb="select"] svg {
#   fill: #a5b4fc !important;
# }
# ul[data-baseweb="menu"],
# div[data-baseweb="popover"] > div,
# div[role="listbox"] {
#   background-color: #0f172a !important;
#   border: 1px solid rgba(99,102,241,0.35) !important;
#   border-radius: 14px !important;
#   box-shadow: 0 12px 40px rgba(0,0,0,0.60) !important;
#   padding: 6px !important;
# }
# li[role="option"] {
#   background: transparent !important;
#   color: #cbd5e1 !important;
#   font-size: 14px !important;
#   border-radius: 8px !important;
#   padding: 10px 14px !important;
#   transition: background 0.15s !important;
# }
# li[role="option"]:hover {
#   background: rgba(99,102,241,0.22) !important;
#   color: #fff !important;
# }
# li[role="option"][aria-selected="true"] {
#   background: rgba(99,102,241,0.30) !important;
#   color: #c7d2fe !important;
#   font-weight: 600 !important;
# }
# div[data-baseweb="select"] input::placeholder {
#   color: #475569 !important;
# }

# /* ════════════════════════════════════════
#    TEXT INPUT — ALWAYS VISIBLE
#    ════════════════════════════════════════ */
# .stTextInput > div > div > input {
#   background: rgba(15,23,42,0.88) !important;
#   border: 1.5px solid rgba(99,102,241,0.55) !important;
#   border-radius: 12px !important;
#   color: #e2e8f0 !important;
#   font-size: 14px !important;
#   transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# .stTextInput > div > div > input:focus {
#   border-color: #6366f1 !important;
#   box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
#   outline: none !important;
# }
# .stTextInput > div > div > input::placeholder { color: #475569 !important; }

# /* ════════════════════════════════════════
#    NUMBER INPUT — ALWAYS VISIBLE
#    ════════════════════════════════════════ */
# .stNumberInput > div > div > input {
#   background: rgba(15,23,42,0.88) !important;
#   border: 1.5px solid rgba(99,102,241,0.55) !important;
#   border-radius: 12px !important;
#   color: #e2e8f0 !important;
#   font-size: 14px !important;
#   transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# .stNumberInput > div > div > input:focus {
#   border-color: #6366f1 !important;
#   box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
# }
# .stNumberInput button {
#   background: rgba(99,102,241,0.12) !important;
#   border: 1px solid rgba(99,102,241,0.35) !important;
#   color: #a5b4fc !important;
#   border-radius: 8px !important;
# }
# .stNumberInput button:hover {
#   background: rgba(99,102,241,0.28) !important;
# }

# /* ── TABS ── */
# .stTabs [data-baseweb="tab-list"] {
#   background: rgba(15,23,42,0.60) !important;
#   border-radius: 14px !important; padding: 4px !important;
#   gap: 4px !important; border: 1px solid rgba(99,102,241,0.18) !important;
# }
# .stTabs [data-baseweb="tab"] {
#   background: transparent !important; border-radius: 10px !important;
#   color: #64748b !important; font-weight: 600 !important; font-size: 13px !important;
#   padding: 8px 16px !important;
# }
# .stTabs [aria-selected="true"] {
#   background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
#   color: #fff !important; box-shadow: 0 2px 12px rgba(99,102,241,0.40) !important;
# }

# /* ── EXPANDER ── */
# .streamlit-expanderHeader {
#   background: rgba(15,23,42,0.65) !important;
#   border: 1px solid rgba(99,102,241,0.20) !important;
#   border-radius: 12px !important; color: #e2e8f0 !important; font-weight: 600 !important;
# }

# /* ── DOWNLOAD BUTTON ── */
# .stDownloadButton > button {
#   background: linear-gradient(135deg, #059669, #34d399) !important;
#   color: #fff !important; border: none !important; border-radius: 12px !important;
#   font-weight: 700 !important; letter-spacing: 0.04em !important;
#   box-shadow: 0 4px 18px rgba(52,211,153,0.35) !important;
# }

# /* ── WIDGET LABELS ── */
# .stSelectbox label, .stSlider label, .stTextInput label,
# .stNumberInput label, .stMultiSelect label {
#   color: #94a3b8 !important; font-size: 13px !important; font-weight: 600 !important;
# }

# /* ── MULTISELECT tags ── */
# div[data-baseweb="tag"] {
#   background: rgba(99,102,241,0.22) !important;
#   border: 1px solid rgba(99,102,241,0.40) !important;
#   border-radius: 6px !important; color: #c7d2fe !important; font-size: 12px !important;
# }
# div[data-baseweb="tag"] span { color: #c7d2fe !important; }
# div[data-baseweb="tag"] button svg { fill: #a5b4fc !important; }
# div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
#   background: rgba(15,23,42,0.88) !important;
#   border: 1.5px solid rgba(99,102,241,0.55) !important;
#   border-radius: 12px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # SESSION STATE
# # ─────────────────────────────────────────────
# if "page" not in st.session_state:
#     st.session_state.page = "home"
# if "roadmap_data" not in st.session_state:
#     st.session_state.roadmap_data = None
# if "student_info" not in st.session_state:
#     st.session_state.student_info = None
# if "student_name" not in st.session_state:
#     st.session_state.student_name = ""

# # ─────────────────────────────────────────────
# # LANDING PAGE
# # ─────────────────────────────────────────────
# def show_landing_page():
#     QUOTES = [
#         ("\"The secret of getting ahead is getting started.\"", "— Mark Twain"),
#         ("\"Don't watch the clock; do what it does. Keep going.\"", "— Sam Levenson"),
#         ("\"You don't have to be great to start, but you have to start to be great.\"", "— Zig Ziglar"),
#         ("\"Push yourself, because no one else is going to do it for you.\"", "— Anonymous"),
#         ("\"Dream big. Start small. Act now.\"", "— Robin Sharma"),
#         ("\"Your future is created by what you do today, not tomorrow.\"", "— Robert Kiyosaki"),
#         ("\"Success is the sum of small efforts repeated day in and day out.\"", "— Robert Collier"),
#         ("\"Believe you can and you're halfway there.\"", "— Theodore Roosevelt"),
#     ]
#     quote_text, quote_author = random.choice(QUOTES)
#     STUDENT_IMAGES = [
#         "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=400&q=80",
#         "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80",
#         "https://images.unsplash.com/photo-1529390079861-591de354faf5?w=400&q=80",
#     ]
#     st.markdown(f"""
#     <div class="landing">
#       <div class="nav">
#         <div class="nav-logo">🎯  Personalized Skill Roadmap</div>
#       </div>
#       <div class="hero">
#         <div class="confused-tag">😕 &nbsp; Not sure where to start?</div>
#         <h1 class="hero-h1">
#           <span class="line1">Stop feeling lost.</span>
#           <span class="line2">Build your roadmap today.</span>
#         </h1>
#         <p class="hero-sub">
#           Answer a few simple questions about yourself — we'll generate a
#           personalised 4-week learning plan with projects, resources, and a
#           readiness score. Made for engineering students like you.
#         </p>
#         <div class="quote-card">
#           <div class="quote-text">{quote_text}</div>
#           <div class="quote-author">{quote_author}</div>
#         </div>
#       </div>
#       <div class="img-row">
#         <div class="img-card">
#           <img src="{STUDENT_IMAGES[0]}" alt="Students studying"/>
#           <div class="img-overlay"><div class="img-label">Collaborate &amp; Grow</div><div class="img-sub">Learn with peers</div></div>
#         </div>
#         <div class="img-card">
#           <img src="{STUDENT_IMAGES[1]}" alt="Group project"/>
#           <div class="img-overlay"><div class="img-label">Build Real Projects</div><div class="img-sub">Portfolio-grade work</div></div>
#         </div>
#         <div class="img-card">
#           <img src="{STUDENT_IMAGES[2]}" alt="Student laptop"/>
#           <div class="img-overlay"><div class="img-label">Learn at Your Pace</div><div class="img-sub">Structured &amp; clear</div></div>
#         </div>
#       </div>
#       <div class="stats-row">
#         <div class="stat-item"><div class="stat-num">14+</div><div class="stat-label">Learning Tracks</div></div>
#         <div class="stat-item"><div class="stat-num">4</div><div class="stat-label">Week Plan</div></div>
#         <div class="stat-item"><div class="stat-num">50+</div><div class="stat-label">Free Resources</div></div>
#         <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Personalised</div></div>
#       </div>
#       <div class="features">
#         <div class="feat-card"><div class="feat-icon">📊</div><div class="feat-title">Readiness Score</div><div class="feat-desc">Get a breakdown of your academics, skills, routine, and communication.</div></div>
#         <div class="feat-card"><div class="feat-icon">🗓️</div><div class="feat-title">4-Week Plan</div><div class="feat-desc">A clear week-by-week learning roadmap tailored to your interest and level.</div></div>
#         <div class="feat-card"><div class="feat-icon">🧩</div><div class="feat-title">Skill Gap Analysis</div><div class="feat-desc">Pick a job role and instantly see what skills you have and what to learn next.</div></div>
#         <div class="feat-card"><div class="feat-icon">⬇️</div><div class="feat-title">Download Roadmap</div><div class="feat-desc">Save your full roadmap as a Markdown file to keep and revisit anytime.</div></div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2, col3 = st.columns([1, 1.4, 1])
#     with col2:
#         if st.button("🚀  Start My Roadmap", use_container_width=True):
#             st.session_state.page = "app"
#             st.rerun()
#     st.markdown('<p style="text-align:center;color:#334155;font-size:12px;margin-top:8px">Takes less than 2 minutes · No signup needed</p>', unsafe_allow_html=True)


# # ─────────────────────────────────────────────
# # COURSE DATABASE
# # ─────────────────────────────────────────────
# COURSE_DB = {
#     "ML": {
#         "courses": ["Andrew Ng — Machine Learning Specialization (Coursera)", "Krish Naik — Machine Learning Playlist (YouTube)", "fast.ai — Practical Deep Learning for Coders"],
#         "weeks": ["Python + Numpy/Pandas + basics of ML (Regression, metrics).", "Scikit-learn: Decision Trees, Random Forest, model validation.", "Feature engineering + classification + overfitting control.", "Project: Build an end-to-end ML app and deploy via Streamlit."],
#         "projects": ["House Price Predictor", "Student Performance Dashboard + Prediction", "Customer Segmentation (K-Means)"],
#     },
#     "WEB": {
#         "courses": ["The Odin Project (Full Stack foundations)", "FreeCodeCamp — Responsive Web Design", "JavaScript/React Crash Course (YouTube)"],
#         "weeks": ["HTML + CSS (Flex/Grid) + build 1 landing page.", "JavaScript (DOM, ES6, Fetch API) + small interactive UI.", "React basics (components, state, props) + mini app.", "Project: Deploy a portfolio-grade site/app (GitHub Pages/Vercel)."],
#         "projects": ["Portfolio Website (Dark mode + sections)", "To-do App (LocalStorage)", "Mini E-commerce Product Gallery UI"],
#     },
#     "DSA": {
#         "courses": ["Striver A2Z DSA Sheet (TakeUForward)", "NeetCode 150 (structured problems)", "Abdul Bari — Algorithms (YouTube)"],
#         "weeks": ["Arrays/Strings + time complexity + 20 problems.", "Linked List + Stack/Queue + 15 problems.", "Trees + Recursion/Backtracking + 12 problems.", "Sorting/Searching + DP basics + mock interview set."],
#         "projects": ["Sorting Visualizer", "Sudoku Solver", "Pathfinding Visualizer (BFS/Dijkstra)"],
#     },
#     "CYBER": {
#         "courses": ["TryHackMe — Pre Security / Beginner Path", "OverTheWire (Bandit) — Linux basics practice", "YouTube: Networking + Web security basics (OWASP Top 10)"],
#         "weeks": ["Linux + networking basics + command line practice.", "Web fundamentals + OWASP Top 10 (SQLi, XSS, auth issues).", "Hands-on labs (TryHackMe rooms) + write notes.", "Project: Security checklist + demo report (mini pentest style)."],
#         "projects": ["Basic Web Security Audit Report (OWASP checklist)", "Password strength checker + hashing demo", "Phishing awareness mini-site (educational)"],
#     },
#     "ECE": {
#         "courses": ["NPTEL — Digital Circuits / Microprocessors (choose 1)", "Embedded Systems (Arduino/ESP32) playlist (YouTube)", "VLSI Basics / Communication Systems intro (NPTEL/YouTube)"],
#         "weeks": ["Core: C basics + digital logic fundamentals (gates, flip-flops).", "Embedded basics: Arduino/ESP32 + sensors (read data, print/plot).", "Choose one: VLSI basics OR Communication Systems basics.", "Project: Mini IoT/Embedded demo + documentation + results."],
#         "projects": ["IoT Temperature/Humidity Monitor (sensor + dashboard)", "Arduino Sensor Data Logger", "Mini Communication System simulation report (basic)"],
#     },
#     "COMM_SYSTEMS": {
#         "courses": ["NPTEL — Communication Systems", "Signals & Systems basics (YouTube/NPTEL)", "MATLAB/Python signal processing basics (tutorial series)"],
#         "weeks": ["Signals basics: sampling, frequency, noise concept.", "AM/FM basics + modulation/demodulation understanding.", "Digital comm intro: ASK/FSK/PSK concept + simple plots.", "Project: small simulation notebook + report (plots + explanation)."],
#         "projects": ["AM/FM simulation notebook", "Noise impact on signal plots", "Digital modulation demo (basic)"],
#     },
#     "VLSI": {
#         "courses": ["NPTEL — VLSI Design", "Digital Electronics (NPTEL/YouTube)", "Verilog basics playlist (YouTube)"],
#         "weeks": ["Digital design recap + number systems + logic optimization.", "Verilog basics: modules, testbench, simulation flow.", "Combinational + sequential circuits in Verilog.", "Project: design a small digital system + simulate + report."],
#         "projects": ["4-bit ALU in Verilog", "Traffic Light Controller (FSM) in Verilog", "Simple Counter/Shift Register designs"],
#     },
#     "SIGNAL": {
#         "courses": ["NPTEL — Signals and Systems / DSP intro", "Python for Signal Processing (NumPy/Scipy) tutorials", "YouTube: DSP basics (filters, FFT)"],
#         "weeks": ["Signals basics + plotting + basic transforms concept.", "FFT basics + noise removal concept.", "Filters (low/high pass) concept + simple implementations.", "Project: signal cleaning / analysis notebook + report."],
#         "projects": ["Noise filtering demo (FFT + filter)", "Audio signal analysis notebook", "Sensor signal smoothing + plots"],
#     },
#     "IOT": {
#         "courses": ["Arduino/ESP32 IoT playlist (YouTube)", "NPTEL — Introduction to IoT", "Basics of MQTT/HTTP + simple dashboards"],
#         "weeks": ["Microcontroller + sensor basics + read values.", "Send data: serial/log file + basic visualization.", "Add connectivity (Wi-Fi/MQTT/HTTP) basic.", "Project: IoT dashboard demo + short video + README."],
#         "projects": ["Smart home sensor dashboard", "Weather station mini project", "Room monitoring (temp/light) demo"],
#     },
#     "EMBEDDED": {
#         "courses": ["Embedded C basics (YouTube)", "Arduino/ESP32 practical series", "Basics of interrupts/timers (tutorial series)"],
#         "weeks": ["Embedded C: loops, pointers basics, debugging mindset.", "GPIO + sensor interfacing + basic timing.", "Interrupts/timers basics + simple control logic.", "Project: embedded mini demo + documentation."],
#         "projects": ["Digital stopwatch timer", "Sensor-based alert system", "LED patterns with interrupts/timers"],
#     },
#     "EEE": {
#         "courses": ["NPTEL — Power Systems", "NPTEL — Electrical Machines", "Industrial Automation basics (YouTube/NPTEL)"],
#         "weeks": ["Basics: power system components + machines recap.", "Protection & control basics + simple problem practice.", "Renewable/Smart grid basics (choose 1 focus).", "Project: mini case-study/report with calculations + charts."],
#         "projects": ["Load analysis mini report (Excel/Python)", "Renewable energy comparison case study", "Basic fault analysis notes + examples"],
#     },
#     "POWER": {
#         "courses": ["NPTEL — Power Systems (core)", "Protection & Switchgear basics (YouTube/NPTEL)", "Power flow intro (basic concepts)"],
#         "weeks": ["Power system overview + per-unit basics (light).", "Protection basics (relays, faults) + examples.", "Transmission/distribution concepts + reliability.", "Project: load/fault calculation sheet + report."],
#         "projects": ["Fault calculation worksheet + explanation", "Load estimation report for hostel/house", "Transmission line parameter mini notebook"],
#     },
#     "RENEW": {
#         "courses": ["NPTEL — Renewable Energy", "Solar PV basics (YouTube/NPTEL)", "Wind energy basics (tutorial series)"],
#         "weeks": ["Solar PV basics + components + sizing idea.", "Wind/other renewables basics + pros/cons.", "Hybrid systems + storage basics (battery).", "Project: solar sizing calculator + mini report."],
#         "projects": ["Solar sizing calculator (Excel/Python)", "Renewable comparison infographic/report", "Microgrid case study summary"],
#     },
#     "SMARTGRID": {
#         "courses": ["Smart Grid basics (NPTEL/YouTube)", "Power electronics intro (for grid integration)", "SCADA basics overview (intro)"],
#         "weeks": ["Smart grid concept + components + communication basics.", "Demand response + metering + grid monitoring concepts.", "Grid integration of renewables + challenges.", "Project: smart grid concept report + diagram + demo slides."],
#         "projects": ["Smart grid architecture diagram + report", "Demand response mini case study", "Energy monitoring dashboard concept"],
#     },
#     "AUTOMATION": {
#         "courses": ["Industrial Automation basics (YouTube/NPTEL)", "PLC fundamentals (intro course)", "Sensors + actuators basics"],
#         "weeks": ["Automation basics + sensors/actuators overview.", "PLC fundamentals (ladder logic concept).", "Control basics: feedback, stability concept.", "Project: automation workflow diagram + mini case study."],
#         "projects": ["PLC ladder logic mini examples (documented)", "Sensor-actuator workflow demo (simulation/report)", "Industry process automation case study"],
#     },
#     "ELECTRICAL_DESIGN": {
#         "courses": ["Electrical Design basics (YouTube/notes)", "AutoCAD Electrical basics (optional)", "Basics of wiring, safety, standards (overview)"],
#         "weeks": ["Wiring basics + safety + common components.", "Reading single-line diagrams (SLD) basics.", "Load calculation + protection selection basics.", "Project: Create an SLD + load sheet + report."],
#         "projects": ["Single-line diagram + explanation", "Load calculation sheet for a building", "Protection device selection notes"],
#     },
#     "MECH": {
#         "courses": ["CAD basics (Fusion 360/SolidWorks tutorials)", "NPTEL — Manufacturing / Thermal Engineering (choose 1)", "Robotics basics (intro course/playlist)"],
#         "weeks": ["CAD basics: sketches + 3 simple parts.", "Manufacturing basics OR Thermal basics (choose one).", "Robotics basics + mechanisms overview.", "Project: design + report (CAD model + documentation)."],
#         "projects": ["CAD assembly mini project", "Manufacturing process comparison report", "Thermal analysis mini notes + examples"],
#     },
#     "CAD": {
#         "courses": ["Fusion 360 / SolidWorks beginner tutorials", "Engineering drawing basics (YouTube)", "Basic GD&T overview (optional)"],
#         "weeks": ["Sketching + constraints + 3 practice parts.", "3D modeling + assembly basics.", "Drawings + dimensions + tolerances basics.", "Project: model + drawing pack + short explanation."],
#         "projects": ["CAD model of simple machine part", "Assembly of basic mechanism", "Drawing sheet pack (PDF) + notes"],
#     },
#     "ROBOTICS": {
#         "courses": ["Robotics basics playlist (YouTube)", "Arduino basics (for small robotics demos)", "Mechanisms + control intro (overview)"],
#         "weeks": ["Basics: sensors + motors overview + simple control idea.", "Arduino motor control basics + small demo.", "Robot mechanisms + path planning intro (basic).", "Project: mini robot demo plan + documentation/video."],
#         "projects": ["Line follower robot plan/demo", "Obstacle avoidance mini demo", "Robot arm concept + CAD (optional)"],
#     },
#     "AUTO": {
#         "courses": ["Automobile basics (YouTube/NPTEL)", "Engine + transmission basics overview", "Vehicle dynamics intro (basic)"],
#         "weeks": ["Vehicle components + engine basics.", "Transmission + braking + steering basics.", "Vehicle dynamics intro + safety concepts.", "Project: vehicle subsystem report + diagrams."],
#         "projects": ["Vehicle subsystem case study (brakes/engine)", "Maintenance checklist + explanation", "Auto trends summary report"],
#     },
#     "THERMAL": {
#         "courses": ["NPTEL — Thermal Engineering basics", "Heat transfer intro playlist (YouTube)", "Basic thermodynamics notes + problems"],
#         "weeks": ["Thermo basics: laws + properties + simple problems.", "Heat transfer basics (conduction/convection/radiation).", "Cycles overview (Rankine/Brayton) basic.", "Project: mini thermal calculation sheet + report."],
#         "projects": ["Heat loss calculation mini sheet", "Thermal cycle summary report", "Cooling system concept notes"],
#     },
#     "MANUFACTURING": {
#         "courses": ["NPTEL — Manufacturing Processes", "Metrology basics (YouTube/NPTEL)", "Lean manufacturing overview (intro)"],
#         "weeks": ["Manufacturing basics: casting/forming/machining overview.", "Metrology basics + quality concepts.", "Lean basics (5S, waste reduction).", "Project: process comparison + case study report."],
#         "projects": ["Manufacturing process comparison report", "Lean 5S checklist for workshop", "Quality control mini notes + examples"],
#     },
#     "SOFT": {
#         "courses": ["Basic Communication Skills playlist (YouTube)", "TED Talks (practice + notes)", "Resume & Interview basics resources"],
#         "weeks": ["Daily speaking practice + 5–7 lines writing summary.", "Improve vocabulary + clarity + small presentations.", "Mock interview practice + feedback from peers.", "Project: 2-min self intro video + updated resume."],
#         "projects": ["2-min self-introduction video", "Resume + LinkedIn update checklist", "Weekly speaking practice log"],
#     },
# }

# JOB_SKILL_ANALYSIS = {
#     "Software Developer":     {"skills": ["Python / Java", "Data Structures & Algorithms", "HTML, CSS, JavaScript", "Git & GitHub", "Databases (SQL)", "OOPS", "Problem Solving"], "projects": ["Student Management System", "Task Tracker Application", "Portfolio Website", "REST API Mini Project"], "resources": ["NPTEL – Programming & DSA", "YouTube – freeCodeCamp", "GeeksForGeeks – DSA", "GitHub – Open Source Projects"]},
#     "Frontend Developer":     {"skills": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Git & GitHub"], "projects": ["Portfolio Website", "React To-Do App", "UI Clone (Netflix / Amazon)"], "resources": ["MDN Web Docs", "Traversy Media (YouTube)", "React Official Docs"]},
#     "Backend Developer":      {"skills": ["Node.js / Python / Java", "Databases (SQL/NoSQL)", "APIs / RESTful Services", "Git & GitHub", "Authentication & Security"], "projects": ["REST API Project", "E-commerce Backend", "Blog Platform Backend"], "resources": ["Udemy Backend Courses", "YouTube – Tech With Tim / Traversy Media", "MongoDB University"]},
#     "Data Scientist":         {"skills": ["Python", "Statistics", "Pandas & NumPy", "Data Visualization", "Machine Learning Basics"], "projects": ["Student Performance Analysis", "Sales Prediction Model", "EDA Project"], "resources": ["Kaggle Learn", "Krish Naik (YouTube)", "Coursera ML (Audit Mode)"]},
#     "Machine Learning Engineer": {"skills": ["Python", "Linear Algebra & Statistics", "Scikit-learn / TensorFlow / PyTorch", "Data Preprocessing", "Model Deployment"], "projects": ["Predictive Analytics Model", "Image Classification Project", "Recommendation System"], "resources": ["Fast.ai Courses", "DeepLearning.ai (Coursera)", "YouTube – Sentdex / Krish Naik"]},
#     "DevOps Engineer":        {"skills": ["Linux / Shell Scripting", "CI/CD (Jenkins/GitHub Actions)", "Docker / Kubernetes", "Cloud Platforms (AWS / GCP / Azure)", "Monitoring & Logging"], "projects": ["CI/CD Pipeline Setup", "Dockerized Application Deployment", "Cloud Infrastructure Project"], "resources": ["Linux Academy / A Cloud Guru", "YouTube – TechWorld with Nana", "Official Docker & Kubernetes Docs"]},
#     "UI/UX Designer":         {"skills": ["Figma / Adobe XD", "Wireframing & Prototyping", "User Research & Testing", "Responsive Design Principles", "Portfolio Creation"], "projects": ["Mobile App Wireframes", "Website Redesign Project", "Interactive Prototype"], "resources": ["Figma Learn Tutorials", "Coursera UI/UX Courses", "YouTube – DesignCourse / CharliMarieTV"]},
#     "Cybersecurity Analyst":  {"skills": ["Networking Basics", "Linux & Windows Security", "Penetration Testing", "Firewalls & IDS/IPS", "Security Tools (Wireshark, Nmap)"], "projects": ["Vulnerability Assessment", "Phishing Simulation", "Secure Web Application Setup"], "resources": ["TryHackMe / Hack The Box", "Cybrary Courses", "YouTube – NetworkChuck / The Cyber Mentor"]},
#     "Mobile App Developer":   {"skills": ["Java / Kotlin / Swift / Flutter", "UI/UX for Mobile", "APIs & Backend Integration", "App Deployment (Play Store / App Store)", "Debugging & Testing"], "projects": ["Todo App", "Weather Forecast App", "E-commerce Mobile App"], "resources": ["Udemy Mobile App Courses", "YouTube – CodeWithChris / The Net Ninja", "Official Flutter Docs"]},
#     "Cloud Engineer":         {"skills": ["AWS / Azure / GCP", "Cloud Architecture & Design", "Networking & Security", "CI/CD Pipelines", "Infrastructure as Code (Terraform)"], "projects": ["Deploy Web App on Cloud", "Serverless Application Project", "Cloud Monitoring Setup"], "resources": ["AWS / Azure / GCP Official Docs", "A Cloud Guru Courses", "YouTube – TechWorld with Nana"]},
#     "Business Analyst":       {"skills": ["Excel / SQL / Tableau / PowerBI", "Requirement Gathering", "Process Modeling", "Data Analysis & Reporting", "Communication & Presentation"], "projects": ["Sales Dashboard", "Customer Analysis Report", "Process Optimization Project"], "resources": ["Coursera Business Analytics", "Udemy SQL / Tableau Courses", "YouTube – Analytics University"]},
#     "Digital Marketing Specialist": {"skills": ["SEO / SEM", "Google Analytics", "Content Creation", "Social Media Marketing", "Email Marketing"], "projects": ["SEO Campaign Project", "Social Media Ad Campaign", "Email Marketing Automation"], "resources": ["Google Digital Garage", "HubSpot Academy", "YouTube – Neil Patel / Brian Dean"]},
#     "Blockchain Developer":   {"skills": ["Solidity / Ethereum", "Smart Contracts", "Web3.js / Ethers.js", "Blockchain Architecture", "Cryptography Basics"], "projects": ["Smart Contract Deployment", "NFT Minting Platform", "Decentralized App (DApp)"], "resources": ["CryptoZombies.io", "Coursera Blockchain Courses", "YouTube – Dapp University"]},
#     "AI Researcher":          {"skills": ["Python / R", "Mathematics (Linear Algebra, Probability)", "Deep Learning", "NLP / Computer Vision", "Research Paper Reading & Implementation"], "projects": ["Image Captioning Model", "Text Summarization Model", "Custom Neural Network Research"], "resources": ["arXiv Papers", "DeepLearning.ai", "YouTube – Yannic Kilcher / Two Minute Papers"]},
# }

# # ─────────────────────────────────────────────
# # HELPERS
# # ─────────────────────────────────────────────
# def safe_unique(df, col, fallback):
#     if col not in df.columns:
#         return fallback
#     try:
#         vals = df[col].dropna().unique().tolist()
#         vals = [v for v in vals
#                 if v is not None
#                 and str(v).strip() not in ("", "nan", "none", "null", "NaN")]
#         return sorted(vals, key=lambda x: str(x)) if vals else fallback
#     except Exception:
#         return fallback

# def normalize_yes_no(x):
#     return str(x).strip() if x is not None else "Day Scholar"

# def detect_category(interest: str) -> str:
#     s = str(interest).lower()
#     if any(k in s for k in ["ai/ml", "ml", "ai", "data science", "data analysis"]): return "ML"
#     if "web" in s or "app" in s: return "WEB"
#     if "competitive coding" in s: return "DSA"
#     if "cyber" in s: return "CYBER"
#     if "vlsi" in s: return "VLSI"
#     if "iot" in s: return "IOT"
#     if "embedded" in s: return "EMBEDDED"
#     if "signal processing" in s: return "SIGNAL"
#     if "communication systems" in s: return "COMM_SYSTEMS"
#     if "power systems" in s: return "POWER"
#     if "renewable energy" in s: return "RENEW"
#     if "smart grid" in s: return "SMARTGRID"
#     if "industrial automation" in s: return "AUTOMATION"
#     if "electrical design" in s: return "ELECTRICAL_DESIGN"
#     if "robotics" in s: return "ROBOTICS"
#     if "cad design" in s: return "CAD"
#     if "automobile" in s: return "AUTO"
#     if "thermal" in s: return "THERMAL"
#     if "manufacturing" in s: return "MANUFACTURING"
#     if "communication skills" in s: return "SOFT"
#     return "DSA"

# def clamp(x, lo, hi): return max(lo, min(hi, x))

# def level_to_bucket(skill_level: str):
#     s = str(skill_level).lower()
#     if "begin" in s: return "Beginner"
#     if "inter" in s: return "Intermediate"
#     return "Advanced"

# def get_similar_students(df, info):
#     f = df.copy()
#     strict = f[
#         (f["branch"] == info["branch"]) &
#         (f["interest"] == info["interest"])
#     ]
#     if len(strict) >= 5:
#         return strict
#     relaxed = f[f["branch"] == info["branch"]]
#     if len(relaxed) >= 5:
#         return relaxed
#     return f

# def build_week_plan(interest, skill_level, budget_level):
#     cat  = detect_category(interest)
#     data = COURSE_DB.get(cat, COURSE_DB["DSA"])
#     free_note = "Use free resources (YouTube/NPTEL/free audits)." if str(budget_level) == "Low" else "Consider 1 paid course for faster progress."
#     lvl = str(skill_level).lower()
#     practice = "45–60 mins daily practice." if "begin" in lvl else "60–90 mins daily practice."
#     week_plan = []
#     for i in range(4):
#         week_plan.append({
#             "title": f"Week {i+1} — " + ["Foundation", "Core Skills", "Build Projects", "Portfolio & Review"][i],
#             "bullets": [
#                 f"Course focus: {data['courses'][min(i, len(data['courses'])-1)]}",
#                 data["weeks"][i],
#                 practice,
#                 free_note,
#             ],
#         })
#     return week_plan, data["courses"], data["projects"]

# # ─────────────────────────────────────────────
# # ✅ FIXED FUNCTION — only change from original
# # ─────────────────────────────────────────────
# def generate_structured_roadmap(info, df):
#     steps = []; risks = []; habits = []; goals = []
#     sim = get_similar_students(df, info)
#     if len(sim) >= 5:
#         avg_gpa   = sim["gpa"].mean()        if "gpa"         in sim.columns else None
#         avg_study = sim["study_hours"].mean() if "study_hours" in sim.columns else None
#         if avg_gpa is not None and avg_study is not None:
#             sim_note = f"Based on {len(sim)} similar students, avg GPA {avg_gpa:.2f}, avg study hours {avg_study:.1f}/day."
#         else:
#             sim_note = f"Showing general roadmap ({len(sim)} similar students found)."
#     else:
#         sim_note = "Showing a general roadmap based on available data."

#     # ── Safely resolve all fields (fixes budget key mismatch + any None values) ──
#     budget        = str(info.get("budget") or info.get("budget_level") or "Low").strip()
#     gpa           = float(info.get("gpa") or 10)
#     study_hours   = int(info.get("study_hours") or 3)
#     communication = str(info.get("communication") or info.get("communication_level") or "Average").strip()
#     stress_level  = str(info.get("stress_level") or "Medium").strip()
#     confusion     = str(info.get("confusion_level") or "Medium").strip()
#     hostel        = str(info.get("hostel") or "No").strip()
#     family_support = str(info.get("family_support") or "Medium").strip()
#     interest      = str(info.get("interest") or "").strip()
#     skill_level   = str(info.get("skill_level") or "Beginner").strip()

#     # Goals — always at least 1
#     goals.append(f"Build a clear learning path in {interest}.")
#     if gpa < 6.0:
#         goals.append("Improve academic consistency (target +0.5 GPA next semester).")
#     if study_hours < 3:
#         goals.append("Increase study hours gradually to a sustainable level.")
#     if communication in ("Poor", "Low"):
#         goals.append("Improve communication through weekly speaking/writing practice.")

#     # Risks
#     if stress_level == "High" or confusion == "High":
#         risks.append("High stress/confusion detected — use weekly planning + short focused sessions.")
#         habits.append("10 min breathing/meditation + 25/5 Pomodoro (2 cycles).")

#     # Habits — always at least 1
#     habits.append(
#         "Hostel routine: fixed sleep + fixed study slot + limit late-night scrolling."
#         if hostel == "Yes"
#         else "Home routine: fixed study slot + communicate study time to family."
#     )
#     habits.append("Review your week every Sunday — 15 min planning saves hours of confusion.")

#     # Steps — always at least 2
#     steps.append(
#         "Get external support: mentor/teacher/peer group + online communities."
#         if family_support == "Low"
#         else "Use family support: share weekly goals and ask for accountability."
#     )
#     steps.append(
#         "Use free resources first + build projects (proof > certificates)."
#         if budget == "Low"
#         else "Pick 1 high-quality paid course OR mentorship for faster progress."
#     )
#     if study_hours < 3:
#         steps.append("Study plan: add +30 mins/week until you reach 3–4 hours/day.")
#     if gpa < 6.0:
#         steps.append("Academics: revise daily + weekly tests + focus on weak subjects.")
#     if communication in ("Poor", "Low"):
#         steps.append("Communication: 2 short talks/week + write 1 summary/day (5–7 lines).")

#     week_plan, course_resources, course_projects = build_week_plan(
#         interest, skill_level, budget
#     )

#     return {
#         "similar_note": sim_note,
#         "goals":    [x for x in goals  if x],
#         "risks":    [x for x in risks  if x],
#         "habits":   [x for x in habits if x],
#         "steps":    [x for x in steps  if x],
#         "week_plan":  week_plan,
#         "resources":  course_resources,
#         "projects":   course_projects,
#     }

# def readiness_breakdown(info):
#     g = float(info.get("gpa", 0))
#     academics = 30 if g>=8 else 26 if g>=7 else 20 if g>=6 else 14 if g>=5 else 8
#     lvl  = level_to_bucket(info.get("skill_level","Beginner"))
#     sh   = int(info.get("study_hours",0))
#     base = 12 if lvl=="Beginner" else 20 if lvl=="Intermediate" else 26
#     bonus= 6 if sh>=4 else 3 if sh>=3 else 1
#     skills = clamp(base+bonus, 0, 30)
#     sleep    = int(info.get("sleep_hours",6))
#     stress   = info.get("stress_level","Medium")
#     confusion= info.get("confusion_level","Medium")
#     routine  = (8 if sleep>=7 else 5 if sleep>=6 else 2) + (6 if stress=="Low" else 4 if stress=="Medium" else 2) + (6 if confusion=="Low" else 4 if confusion=="Medium" else 2)
#     routine  = clamp(routine, 0, 20)
#     comm  = str(info.get("communication","Average"))
#     communication = 20 if comm in ("Good","High") else 14 if comm in ("Average","Medium") else 8
#     return {"Academics": academics, "Skills": skills, "Routine": routine, "Communication": communication, "Total": clamp(academics+skills+routine+communication, 0, 100)}

# def roadmap_to_markdown(name, info, roadmap):
#     def s(x):
#         try:
#             if pd.isna(x): return ""
#         except Exception: pass
#         return str(x)
    
#     lines = [
#         f"# Personalised Roadmap for {s(name) or 'Student'}", 
#         f"**Generated:** {date.today().isoformat()}", 
#         "", 
#         "## Profile"
#     ]
    
#     for k in ["year","branch","interest","skill_level","budget","hostel","study_hours","gpa","stress_level","confusion_level","communication","family_support"]:
#         lines.append(f"- **{k.replace('_',' ').title()}**: {s(info.get(k))}")
    
#     lines += ["", "## Data Insight", s(roadmap.get("similar_note","")), "", "## Goals"]
    
#     # Corrected: Use standard for loops instead of list comprehensions
#     for g in roadmap.get("goals", []):
#         lines.append(f"- {s(g)}")
    
#     if roadmap.get("risks"):
#         lines += ["", "## Risks"]
#         for r in roadmap["risks"]:
#             lines.append(f"- {s(r)}")
            
#     lines += ["", "## Daily Habits"]
#     for h in roadmap.get("habits", []):
#         lines.append(f"- {s(h)}")
        
#     lines += ["", "## Action Steps"]
#     for step in roadmap.get("steps", []):
#         lines.append(f"- {s(step)}")
        
#     lines += ["", "## 4-Week Plan"]
#     for w in roadmap.get("week_plan", []):
#         lines += [f"### {s(w['title'])}"]
#         for b in w.get("bullets", []):
#             lines.append(f"- {s(b)}")
#         lines += [""]
        
#     lines += ["## Suggested Projects"]
#     for p in roadmap.get("projects", []):
#         lines.append(f"- {s(p)}")
        
#     lines += ["", "## Resources"]
#     for r in roadmap.get("resources", []):
#         lines.append(f"- {s(r)}")
        
#     return "\n".join(lines)

# def compute_skill_gap(required, known):
#     have    = [s for s in required if s in known]
#     missing = [s for s in required if s not in known]
#     return have, missing


# # ─────────────────────────────────────────────
# # ROUTING
# # ─────────────────────────────────────────────
# if st.session_state.page == "home":
#     show_landing_page()
#     st.stop()

# # ═══════════════════════════════════════════════
# #  APP PAGE
# # ═══════════════════════════════════════════════
# @st.cache_data
# def load_data():
#     df = pd.read_csv("student_performance_final.csv")
#     df.columns = df.columns.str.lower()
#     if "hostel" in df.columns:
#         df["hostel"] = df["hostel"].astype(str).str.strip().str.lower()
#         df["hostel"] = df["hostel"].replace({
#             "day scholar": "No",
#             "dayscholar":  "No",
#             "hosteler":    "Yes",
#             "hosteller":   "Yes"
#         })
#     df = df.dropna(subset=["year", "branch", "interest", "skill_level",
#                             "budget_level", "stress_level",
#                             "confusion_level", "communication_level"])
#     df = df.reset_index(drop=True)
#     return df

# data = load_data()

# st.markdown("""
# <div class="app-header">
#   <div style="display:flex;align-items:center;justify-content:space-between;">
#     <div class="app-logo">🎯 Skill Roadmap</div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# col_back, _ = st.columns([1, 8])
# with col_back:
#     if st.button("← Back"):
#         st.session_state.page = "home"
#         st.session_state.roadmap_data = None
#         st.rerun()

# st.markdown("<br>", unsafe_allow_html=True)

# years        = [1, 2, 3, 4]
# branches     = ["CSE", "ECE", "EEE", "IT", "Mechanical"]
# interests    = sorted(data["interest"].dropna().unique().tolist())
# budgets      = ["High", "Low", "Medium"]
# skill_levels = ["Beginner", "Intermediate"]
# stress_lvls  = ["High", "Low", "Medium"]
# conf_lvls    = ["High", "Low", "Medium"]
# comm_lvls    = ["Average", "Good", "Poor"]
# hostel_display = ["Yes", "No"]

# st.markdown('<div class="g-card"><div class="g-card-title">📋 Your Profile</div><div class="g-card-sub">Fill your details to generate a personalised roadmap + readiness score + skill gap analysis.</div></div>', unsafe_allow_html=True)

# with st.form("profile_form"):
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         name         = st.text_input("👤 Student Name", "")
#         year         = st.selectbox("📅 Year", years)
#         branch       = st.selectbox("🏛️ Branch", branches)
#         gpa          = st.slider("🎓 GPA", 0.0, 10.0, 7.0, 0.1)
#         study_hours  = st.slider("📖 Daily Study Hours", 0, 12, 3)
#     with col2:
#         failures     = st.number_input("❌ Number of Failures", min_value=0, max_value=10, value=0)
#         hostel       = st.selectbox("🏠 Hostel?", hostel_display)
#         sleep_hours  = st.slider("😴 Daily Sleep Hours", 0, 12, 7)
#         family_support = st.selectbox("👨‍👩‍👦 Family Support", ["Low","Medium","High"])
#         interest     = st.selectbox("💡 Primary Interest", interests)
#     with col3:
#         budget       = st.selectbox("💰 Budget Level", budgets)
#         skill_level  = st.selectbox("🛠️ Skill Level", skill_levels)
#         stress_level = st.selectbox("😰 Stress Level", stress_lvls)
#         confusion_level = st.selectbox("🤔 Confusion Level", conf_lvls)
#         communication   = st.selectbox("🗣️ Communication Level", comm_lvls)

#     submitted = st.form_submit_button("🔍  Generate My Roadmap", use_container_width=True)

# if submitted:
#     st.session_state.student_name = name
#     st.session_state.student_info = {
#         "year": year, "branch": branch, "gpa": float(gpa),
#         "study_hours": int(study_hours), "failures": int(failures),
#         "hostel": hostel, "sleep_hours": int(sleep_hours),
#         "family_support": family_support, "interest": interest,
#         "budget": budget, "skill_level": skill_level,
#         "stress_level": stress_level, "confusion_level": confusion_level,
#         "communication": communication,
#     }
#     st.session_state.roadmap_data = generate_structured_roadmap(st.session_state.student_info, data)

# if st.session_state.roadmap_data is not None:
#     roadmap = st.session_state.roadmap_data
#     info    = st.session_state.student_info
#     sname   = st.session_state.student_name

#     st.markdown("<br>", unsafe_allow_html=True)
#     st.markdown(f'<div style="text-align:center;font-family:Syne,sans-serif;font-size:22px;font-weight:800;background:linear-gradient(135deg,#a5b4fc,#34d399);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:24px;">✅ Roadmap Generated for {sname or "Student"}</div>', unsafe_allow_html=True)

#     score = readiness_breakdown(info)
#     c1,c2,c3,c4,c5 = st.columns(5)
#     tiles = [
#         ("GPA", f"{info['gpa']:.1f}"),
#         ("Study hrs/day", str(info["study_hours"])),
#         ("Sleep hrs", str(info["sleep_hours"])),
#         ("Readiness", f"{score['Total']}/100"),
#         ("Skill Level", info["skill_level"]),
#     ]
#     for col, (label, val) in zip([c1,c2,c3,c4,c5], tiles):
#         col.markdown(f'<div class="metric-tile"><div class="metric-val">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     with st.expander("📊  Readiness Score Breakdown", expanded=True):
#         col_score, col_bars = st.columns([1, 2])
#         with col_score:
#             st.markdown(f'<div class="score-ring-wrap"><div class="score-big">{score["Total"]}</div><div class="score-label">out of 100</div></div>', unsafe_allow_html=True)
#         with col_bars:
#             bar_config = [
#                 ("Academics",     score["Academics"],     30,  "linear-gradient(90deg,#6366f1,#818cf8)"),
#                 ("Skills",        score["Skills"],        30,  "linear-gradient(90deg,#8b5cf6,#a78bfa)"),
#                 ("Routine",       score["Routine"],       20,  "linear-gradient(90deg,#0ea5e9,#38bdf8)"),
#                 ("Communication", score["Communication"], 20,  "linear-gradient(90deg,#34d399,#6ee7b7)"),
#             ]
#             for label, val, mx, grad in bar_config:
#                 pct = int(val/mx*100)
#                 st.markdown(f"""
#                 <div class="score-bar-wrap">
#                   <div class="score-bar-label">
#                     <span style="color:#e2e8f0">{label}</span>
#                     <span style="color:#6366f1">{val}/{mx}</span>
#                   </div>
#                   <div class="score-bar-track">
#                     <div class="score-bar-fill" style="width:{pct}%;background:{grad}"></div>
#                   </div>
#                 </div>""", unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧭 Roadmap", "🗓️ 4-Week Plan", "🚀 Projects", "📚 Resources", "🧩 Skill Gap"])

#     with tab1:
#         st.markdown(f'<div style="background:rgba(99,102,241,0.10);border:1px solid rgba(99,102,241,0.28);border-radius:14px;padding:16px 20px;font-size:14px;color:#a5b4fc;margin-bottom:20px;">💡 {roadmap["similar_note"]}</div>', unsafe_allow_html=True)
#         st.markdown('<div class="sec-pill">🎯 Goals</div>', unsafe_allow_html=True)
#         for g in roadmap["goals"]:
#             st.markdown(f'<div class="goal-item"><div class="goal-dot"></div><div class="goal-text">{g}</div></div>', unsafe_allow_html=True)
#         if roadmap["risks"]:
#             st.markdown('<br><div class="sec-pill">⚠️ Risks to Watch</div>', unsafe_allow_html=True)
#             for r in roadmap["risks"]:
#                 st.markdown(f'<div class="risk-item"><div class="risk-dot"></div><div class="goal-text">{r}</div></div>', unsafe_allow_html=True)
#         st.markdown('<br><div class="sec-pill">🧠 Daily Habits</div>', unsafe_allow_html=True)
#         for h in roadmap["habits"]:
#             st.markdown(f'<div class="habit-item"><div class="habit-dot"></div><div class="goal-text">{h}</div></div>', unsafe_allow_html=True)
#         st.markdown('<br><div class="sec-pill">✅ Action Steps</div>', unsafe_allow_html=True)
#         for i, step in enumerate(roadmap["steps"], 1):
#             st.markdown(f'<div class="step-item"><div class="step-num">{i}</div><div class="goal-text">{step}</div></div>', unsafe_allow_html=True)

#     with tab2:
#         for w in roadmap["week_plan"]:
#             bullets_html = "".join(f'<div class="week-bullet">{b}</div>' for b in w["bullets"])
#             st.markdown(f'<div class="week-card"><div class="week-title">{w["title"]}</div>{bullets_html}</div>', unsafe_allow_html=True)

#     with tab3:
#         st.markdown('<div class="sec-pill">🚀 Suggested Projects</div>', unsafe_allow_html=True)
#         icons = ["🔵","🟣","🟡","🟢","🔴"]
#         for i, p in enumerate(roadmap["projects"]):
#             st.markdown(f'<div class="proj-card"><div class="proj-icon">{icons[i%len(icons)]}</div><div class="proj-name">{p}</div></div>', unsafe_allow_html=True)
#         st.markdown('<p style="font-size:12px;color:#475569;margin-top:12px;">Tip: Add screenshots + README + clear results. That makes your project look strong.</p>', unsafe_allow_html=True)

#     with tab4:
#         st.markdown('<div class="sec-pill">📚 Recommended Resources</div>', unsafe_allow_html=True)
#         res_icons = ["🎥","📖","🌐"]
#         for i, r in enumerate(roadmap["resources"]):
#             st.markdown(f'<div class="res-card"><div class="res-icon">{res_icons[i%len(res_icons)]}</div><div class="res-name">{r}</div></div>', unsafe_allow_html=True)

#     with tab5:
#         st.markdown('<div class="sec-pill">🧩 Skill Gap Analysis</div>', unsafe_allow_html=True)
#         st.markdown("""<p style='font-size:14px;color:#64748b;margin-bottom:20px;'>Select a job role, then tick the skills you already know — we will show your match % and what to learn next.</p>""", unsafe_allow_html=True)
#         job_roles = ["— Select a role —"] + list(JOB_SKILL_ANALYSIS.keys())
#         job_choice = st.selectbox("🎯 Target Job Role", job_roles, key="sg_role_tab")
#         if job_choice != "— Select a role —":
#             job_info = JOB_SKILL_ANALYSIS[job_choice]
#             col_left, col_right = st.columns([1, 1])
#             with col_left:
#                 st.markdown('<div class="sec-pill">🧠 Required Skills</div>', unsafe_allow_html=True)
#                 for sk in job_info["skills"]:
#                     st.markdown(f'<div style="background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.22);border-radius:10px;padding:8px 14px;margin-bottom:6px;font-size:13px;color:#c7d2fe;">• {sk}</div>', unsafe_allow_html=True)
#             with col_right:
#                 st.markdown('<div class="sec-pill">🧪 Sample Projects</div>', unsafe_allow_html=True)
#                 for p in job_info["projects"]:
#                     st.markdown(f'<div class="proj-card" style="margin-bottom:6px;"><div class="proj-name" style="color:#fcd34d;">{p}</div></div>', unsafe_allow_html=True)
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<div class="sec-pill">✅ Mark Skills You Already Know</div>', unsafe_allow_html=True)
#             known_skills = st.multiselect("Select skills you already have:", options=job_info["skills"], key="sg_known_tab")
#             have, missing = compute_skill_gap(job_info["skills"], known_skills)
#             pct = int(len(have) / len(job_info["skills"]) * 100) if job_info["skills"] else 0
#             st.markdown("<br>", unsafe_allow_html=True)
#             bar_color = "#34d399" if pct >= 70 else "#fbbf24" if pct >= 40 else "#fb7185"
#             st.markdown(f"""
#             <div style="margin-bottom:8px;">
#               <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;">
#                 <span style="color:#e2e8f0;font-weight:700;">📊 Skill Match</span>
#                 <span style="color:{bar_color};font-weight:800;">{pct}%</span>
#               </div>
#               <div style="height:12px;border-radius:999px;background:rgba(255,255,255,0.08);overflow:hidden;">
#                 <div style="height:100%;width:{pct}%;background:{bar_color};border-radius:999px;transition:width 0.5s ease;"></div>
#               </div>
#               <div style="font-size:12px;color:#475569;margin-top:6px;">
#                 {"🟢 Strong match — ready to apply!" if pct>=70 else "🟡 Getting there — keep building!" if pct>=40 else "🔴 Start learning — you've got this!"}
#               </div>
#             </div>
#             """, unsafe_allow_html=True)
#             st.markdown("<br>", unsafe_allow_html=True)
#             col_h, col_m = st.columns(2)
#             with col_h:
#                 st.markdown('<div class="sec-pill" style="background:rgba(52,211,153,0.12);border-color:rgba(52,211,153,0.35);color:#6ee7b7;">✅ Skills You Have</div>', unsafe_allow_html=True)
#                 if have:
#                     for sk in have:
#                         st.markdown(f'<div class="skill-have">✅ {sk}</div>', unsafe_allow_html=True)
#                 else:
#                     st.markdown('<p style="font-size:13px;color:#475569;">Select skills you know above.</p>', unsafe_allow_html=True)
#             with col_m:
#                 st.markdown('<div class="sec-pill" style="background:rgba(251,113,133,0.12);border-color:rgba(251,113,133,0.35);color:#fda4af;">🔴 Skills to Learn</div>', unsafe_allow_html=True)
#                 if missing:
#                     for sk in missing:
#                         st.markdown(f'<div class="skill-need">🔴 {sk}</div>', unsafe_allow_html=True)
#                 else:
#                     st.markdown('<div style="background:rgba(52,211,153,0.10);border:1px solid rgba(52,211,153,0.30);border-radius:12px;padding:14px;font-size:14px;color:#6ee7b7;font-weight:700;">🎉 You have all required skills!</div>', unsafe_allow_html=True)
#             if missing:
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 st.markdown('<div class="sec-pill">🛣️ Recommended Learning Order</div>', unsafe_allow_html=True)
#                 for i, sk in enumerate(missing, 1):
#                     st.markdown(f'<div class="learn-step"><div class="learn-step-num">{i}</div><div class="learn-step-text">Learn <strong style="color:#e2e8f0">{sk}</strong></div></div>', unsafe_allow_html=True)
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.markdown('<div class="sec-pill">📚 Resources for this Role</div>', unsafe_allow_html=True)
#             for r in job_info["resources"]:
#                 st.markdown(f'<div class="res-card"><div class="res-icon">📌</div><div class="res-name">{r}</div></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)
#     md = roadmap_to_markdown(sname, info, roadmap)
#     st.download_button(
#         label="⬇️  Download Full Roadmap (Markdown)",
#         data=md.encode("utf-8"),
#         file_name=f"roadmap_{(sname or 'student').replace(' ','_').lower()}.md",
#         mime="text/markdown",
#         use_container_width=True,
#     )

# st.markdown("<br>", unsafe_allow_html=True)
# with st.expander("📊  Sample Student Dataset (Preview)"):
#     st.dataframe(data, use_container_width=True)

# st.markdown('<p style="text-align:center;font-size:11px;color:#1e293b;margin-top:32px;">Student Skill Roadmap · Streamlit</p>', unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import random
from datetime import date

st.set_page_config(
    page_title="Personalized Skill Roadmap",
    page_icon="🎯",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

:root {
  --bg:        #020817;
  --surface:   rgba(15,23,42,0.72);
  --border:    rgba(99,102,241,0.22);
  --indigo:    #6366f1;
  --violet:    #8b5cf6;
  --emerald:   #34d399;
  --sky:       #38bdf8;
  --amber:     #fbbf24;
  --rose:      #fb7185;
  --text:      #e2e8f0;
  --muted:     #64748b;
}

html, body, [class*="css"] {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--indigo); border-radius: 99px; }

/* ── LANDING ── */
.landing {
  min-height: 100vh;
  background:
    radial-gradient(ellipse 80% 60% at 15% 55%,  rgba(99,102,241,0.38) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 25%,  rgba(139,92,246,0.30) 0%, transparent 55%),
    radial-gradient(ellipse 70% 55% at 55% 90%,  rgba(16,185,129,0.18) 0%, transparent 58%),
    radial-gradient(ellipse 50% 40% at 80% 75%,  rgba(56,189,248,0.12) 0%, transparent 55%),
    #020817;
  padding-bottom: 80px;
}
.nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 20px 48px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.nav-logo {
  font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.nav-badge {
  background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.30);
  color: #a5b4fc; font-size: 11px; font-weight: 600; padding: 5px 14px;
  border-radius: 999px; letter-spacing: 0.06em;
}
.hero { text-align: center; padding: 72px 24px 48px; }
.confused-tag {
  display: inline-block;
  background: rgba(251,191,36,0.12); border: 1px solid rgba(251,191,36,0.30);
  color: #fcd34d; font-size: 13px; font-weight: 600;
  padding: 6px 18px; border-radius: 999px; margin-bottom: 28px;
  letter-spacing: 0.04em; animation: fadeDown 0.6s ease both;
}
@keyframes fadeDown {
  from { opacity:0; transform:translateY(-12px); }
  to   { opacity:1; transform:translateY(0); }
}
.hero-h1 {
  font-family: 'Syne', sans-serif;
  font-size: clamp(32px, 6vw, 60px); font-weight: 800; line-height: 1.08;
  margin-bottom: 22px; animation: fadeDown 0.7s ease 0.1s both;
}
.hero-h1 .line1 {
  display: block;
  background: linear-gradient(135deg, #fff 30%, #c7d2fe);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-h1 .line2 {
  display: block;
  background: linear-gradient(135deg, #a5b4fc, #34d399 70%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-sub {
  font-size: 16px; color: #64748b; max-width: 520px;
  margin: 0 auto 40px; line-height: 1.7;
  animation: fadeDown 0.7s ease 0.2s both;
}
.quote-card {
  max-width: 600px; margin: 0 auto 52px;
  background: rgba(15,23,42,0.70); backdrop-filter: blur(12px);
  border: 1px solid rgba(99,102,241,0.22); border-left: 4px solid #6366f1;
  border-radius: 16px; padding: 22px 28px;
  animation: fadeDown 0.7s ease 0.3s both;
}
.quote-text  { font-size: 15px; font-style: italic; color: #e2e8f0; line-height: 1.65; margin-bottom: 10px; }
.quote-author{ font-size: 12px; color: #6366f1; font-weight: 600; letter-spacing: 0.05em; }
.img-row {
  display: flex; justify-content: center; gap: 16px;
  margin: 0 auto 56px; max-width: 860px; padding: 0 24px;
  animation: fadeDown 0.7s ease 0.35s both;
}
.img-card {
  flex: 1; min-width: 0; border-radius: 20px; overflow: hidden;
  border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 8px 32px rgba(0,0,0,0.45);
  position: relative; transition: transform 0.25s;
}
.img-card:hover { transform: translateY(-5px); }
.img-card img  { width: 100%; height: 200px; object-fit: cover; display: block; filter: brightness(0.82) saturate(1.1); }
.img-overlay   { position: absolute; bottom:0; left:0; right:0; background: linear-gradient(transparent, rgba(2,8,23,0.85)); padding: 20px 16px 14px; }
.img-label     { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; color: #fff; }
.img-sub       { font-size: 11px; color: rgba(255,255,255,0.50); margin-top: 2px; }
.stats-row {
  display: flex; justify-content: center; gap: 32px;
  margin: 0 auto 56px; flex-wrap: wrap;
  animation: fadeDown 0.7s ease 0.4s both;
}
.stat-num {
  font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-label { font-size: 12px; color: #475569; margin-top: 4px; letter-spacing: 0.04em; text-transform: uppercase; }
.features {
  display: flex; justify-content: center; gap: 16px;
  max-width: 860px; margin: 0 auto 56px; padding: 0 24px; flex-wrap: wrap;
  animation: fadeDown 0.7s ease 0.45s both;
}
.feat-card {
  flex: 1; min-width: 200px;
  background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.18);
  border-radius: 16px; padding: 20px 18px; backdrop-filter: blur(10px);
  transition: border-color 0.2s, transform 0.2s;
}
.feat-card:hover { border-color: rgba(99,102,241,0.45); transform: translateY(-3px); }
.feat-icon  { font-size: 24px; margin-bottom: 10px; }
.feat-title { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 700; color: #e2e8f0; margin-bottom: 6px; }
.feat-desc  { font-size: 12px; color: #64748b; line-height: 1.6; }

/* ── CTA button ── */
div[data-testid="stButton"] > button {
  background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
  color: #fff !important; border: none !important; border-radius: 14px !important;
  padding: 16px 48px !important; font-family: 'Syne', sans-serif !important;
  font-size: 16px !important; font-weight: 800 !important; letter-spacing: 0.04em !important;
  box-shadow: 0 6px 28px rgba(99,102,241,0.45) !important;
  transition: all 0.2s !important; min-width: 260px !important;
}
div[data-testid="stButton"] > button:hover {
  opacity: 0.88 !important; transform: translateY(-3px) !important;
  box-shadow: 0 12px 36px rgba(99,102,241,0.55) !important;
}

/* ── APP PAGE ── */
.app-header {
  padding: 20px 48px 18px;
  border-bottom: 1px solid rgba(99,102,241,0.18);
  background: rgba(2,8,23,0.97) !important;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  position: sticky; top: 0; z-index: 100;
}
.app-logo {
  font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.g-card {
  background: rgba(15,23,42,0.65);
  border: 1px solid rgba(99,102,241,0.20);
  border-radius: 20px; padding: 28px 32px;
  backdrop-filter: blur(14px);
  margin-bottom: 20px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.35);
}
.g-card-title {
  font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 800;
  color: #e2e8f0; margin-bottom: 6px;
}
.g-card-sub { font-size: 13px; color: #475569; }

/* ── FORM SECTION HEADER ── */
.form-section-header {
  display: flex; align-items: center; gap: 10px;
  padding: 12px 0 10px;
  border-bottom: 1px solid rgba(99,102,241,0.18);
  margin-bottom: 16px; margin-top: 8px;
}
.form-section-icon {
  width: 32px; height: 32px; border-radius: 8px;
  background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(139,92,246,0.25));
  border: 1px solid rgba(99,102,241,0.35);
  display: flex; align-items: center; justify-content: center;
  font-size: 15px;
}
.form-section-title {
  font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 800;
  color: #a5b4fc; letter-spacing: 0.04em; text-transform: uppercase;
}
.form-section-badge {
  font-size: 11px; color: #475569; font-weight: 500; margin-left: auto;
}

.sec-pill {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.28);
  color: #a5b4fc; font-size: 12px; font-weight: 700;
  padding: 5px 16px; border-radius: 999px; letter-spacing: 0.06em;
  margin-bottom: 16px; text-transform: uppercase;
}
.goal-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(52,211,153,0.07); border: 1px solid rgba(52,211,153,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.goal-dot { width: 8px; height: 8px; border-radius: 50%; background: #34d399; margin-top: 5px; flex-shrink: 0; }
.goal-text { font-size: 14px; color: #e2e8f0; line-height: 1.6; }
.risk-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(251,113,133,0.08); border: 1px solid rgba(251,113,133,0.22);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.risk-dot { width: 8px; height: 8px; border-radius: 50%; background: #fb7185; margin-top: 5px; flex-shrink: 0; }
.habit-item {
  display: flex; align-items: flex-start; gap: 12px;
  background: rgba(56,189,248,0.07); border: 1px solid rgba(56,189,248,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.habit-dot { width: 8px; height: 8px; border-radius: 50%; background: #38bdf8; margin-top: 5px; flex-shrink: 0; }
.step-item {
  display: flex; align-items: flex-start; gap: 14px;
  background: rgba(139,92,246,0.07); border: 1px solid rgba(139,92,246,0.20);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 10px;
}
.step-num {
  width: 26px; height: 26px; border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
}
.week-card {
  background: rgba(15,23,42,0.60); border: 1px solid rgba(99,102,241,0.18);
  border-radius: 16px; padding: 20px 24px; margin-bottom: 16px;
}
.week-title {
  font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 800;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.week-bullet {
  display: flex; align-items: flex-start; gap: 10px;
  font-size: 13px; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;
}
.week-bullet::before { content: '▸'; color: #6366f1; flex-shrink: 0; margin-top: 1px; }
.proj-card {
  background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.20);
  border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
  display: flex; align-items: center; gap: 12px;
}
.proj-icon { font-size: 20px; }
.proj-name { font-size: 14px; font-weight: 600; color: #fcd34d; }
.proj-desc { font-size: 12px; color: #64748b; margin-top: 3px; }
.res-card {
  background: rgba(56,189,248,0.06); border: 1px solid rgba(56,189,248,0.20);
  border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;
  display: flex; align-items: center; gap: 12px;
}
.res-icon { font-size: 18px; }
.res-name  { font-size: 14px; color: #7dd3fc; }
.res-tag   { font-size: 11px; color: #34d399; font-weight: 600; margin-top: 3px; }
.score-ring-wrap { text-align: center; padding: 20px 0; }
.score-big {
  font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  line-height: 1;
}
.score-label { font-size: 13px; color: #475569; margin-top: 4px; letter-spacing: 0.08em; text-transform: uppercase; }
.score-bar-wrap { margin-bottom: 14px; }
.score-bar-label {
  display: flex; justify-content: space-between;
  font-size: 12px; font-weight: 600; margin-bottom: 5px;
}
.score-bar-track {
  height: 8px; border-radius: 999px; background: rgba(255,255,255,0.08);
  overflow: hidden;
}
.score-bar-fill { height: 100%; border-radius: 999px; }
.metric-tile {
  background: rgba(15,23,42,0.65); border: 1px solid rgba(99,102,241,0.20);
  border-radius: 16px; padding: 18px 22px; text-align: center;
}
.metric-val {
  font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #34d399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.metric-label { font-size: 11px; color: #475569; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; }
.skill-have {
  background: rgba(52,211,153,0.10); border: 1px solid rgba(52,211,153,0.30);
  border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
  font-size: 13px; color: #6ee7b7; font-weight: 600;
  display: flex; align-items: center; gap: 8px;
}
.skill-need {
  background: rgba(251,113,133,0.10); border: 1px solid rgba(251,113,133,0.30);
  border-radius: 10px; padding: 10px 16px; margin-bottom: 8px;
  font-size: 13px; color: #fda4af; font-weight: 600;
  display: flex; align-items: center; gap: 8px;
}
.learn-step {
  display: flex; align-items: center; gap: 12px;
  background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.22);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 8px;
}
.learn-step-num {
  width: 28px; height: 28px; border-radius: 50%;
  background: linear-gradient(135deg, #8b5cf6, #6366f1);
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #fff; flex-shrink: 0;
}
.learn-step-text { font-size: 14px; color: #c4b5fd; }

/* ── LEVEL BADGE ── */
.level-beginner {
  display: inline-block; background: rgba(251,191,36,0.15);
  border: 1px solid rgba(251,191,36,0.35); color: #fcd34d;
  font-size: 11px; font-weight: 700; padding: 3px 10px;
  border-radius: 999px; margin-left: 8px;
}
.level-intermediate {
  display: inline-block; background: rgba(99,102,241,0.15);
  border: 1px solid rgba(99,102,241,0.35); color: #a5b4fc;
  font-size: 11px; font-weight: 700; padding: 3px 10px;
  border-radius: 999px; margin-left: 8px;
}

/* ── PROGRESS BAR ── */
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, #6366f1, #8b5cf6, #34d399) !important;
  border-radius: 999px !important;
}
.stProgress > div > div > div { background: rgba(255,255,255,0.08) !important; border-radius: 999px !important; }

/* ── SELECTBOX ── */
div[data-baseweb="select"] > div {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-baseweb="select"] > div:hover {
  border-color: rgba(99,102,241,0.90) !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}
div[data-baseweb="select"] > div:focus-within {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
}
div[data-baseweb="select"] span,
div[data-baseweb="select"] div[class*="ValueContainer"] {
  color: #e2e8f0 !important;
  background: transparent !important;
}
div[data-baseweb="select"] svg { fill: #a5b4fc !important; }
ul[data-baseweb="menu"],
div[data-baseweb="popover"] > div,
div[role="listbox"] {
  background-color: #0f172a !important;
  border: 1px solid rgba(99,102,241,0.35) !important;
  border-radius: 14px !important;
  box-shadow: 0 12px 40px rgba(0,0,0,0.60) !important;
  padding: 6px !important;
}
li[role="option"] {
  background: transparent !important;
  color: #cbd5e1 !important;
  font-size: 14px !important;
  border-radius: 8px !important;
  padding: 10px 14px !important;
  transition: background 0.15s !important;
}
li[role="option"]:hover { background: rgba(99,102,241,0.22) !important; color: #fff !important; }
li[role="option"][aria-selected="true"] {
  background: rgba(99,102,241,0.30) !important;
  color: #c7d2fe !important; font-weight: 600 !important;
}

/* ── TEXT INPUT ── */
.stTextInput > div > div > input {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  font-size: 14px !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
  outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: #475569 !important; }

/* ── NUMBER INPUT ── */
.stNumberInput > div > div > input {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
  color: #e2e8f0 !important;
  font-size: 14px !important;
}
.stNumberInput > div > div > input:focus {
  border-color: #6366f1 !important;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.22) !important;
}
.stNumberInput button {
  background: rgba(99,102,241,0.12) !important;
  border: 1px solid rgba(99,102,241,0.35) !important;
  color: #a5b4fc !important; border-radius: 8px !important;
}
.stNumberInput button:hover { background: rgba(99,102,241,0.28) !important; }

/* ── SLIDER ── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
  background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
  border: 2px solid rgba(165,180,252,0.5) !important;
  box-shadow: 0 0 10px rgba(99,102,241,0.5) !important;
}
.stSlider [data-testid="stTickBar"] { color: #475569 !important; }
.stSlider [data-baseweb="slider"] div[class*="Track"] > div {
  background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
  background: rgba(15,23,42,0.60) !important;
  border-radius: 14px !important; padding: 4px !important;
  gap: 4px !important; border: 1px solid rgba(99,102,241,0.18) !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important; border-radius: 10px !important;
  color: #64748b !important; font-weight: 600 !important; font-size: 13px !important;
  padding: 8px 16px !important;
}
.stTabs [aria-selected="true"] {
  background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
  color: #fff !important; box-shadow: 0 2px 12px rgba(99,102,241,0.40) !important;
}

/* ── EXPANDER ── */
.streamlit-expanderHeader {
  background: rgba(15,23,42,0.65) !important;
  border: 1px solid rgba(99,102,241,0.20) !important;
  border-radius: 12px !important; color: #e2e8f0 !important; font-weight: 600 !important;
}

/* ── DOWNLOAD BUTTON ── */
.stDownloadButton > button {
  background: linear-gradient(135deg, #059669, #34d399) !important;
  color: #fff !important; border: none !important; border-radius: 12px !important;
  font-weight: 700 !important; letter-spacing: 0.04em !important;
  box-shadow: 0 4px 18px rgba(52,211,153,0.35) !important;
}

/* ── WIDGET LABELS ── */
.stSelectbox label, .stSlider label, .stTextInput label,
.stNumberInput label, .stMultiSelect label {
  color: #94a3b8 !important; font-size: 13px !important; font-weight: 600 !important;
}

/* ── MULTISELECT ── */
div[data-baseweb="tag"] {
  background: rgba(99,102,241,0.22) !important;
  border: 1px solid rgba(99,102,241,0.40) !important;
  border-radius: 6px !important; color: #c7d2fe !important; font-size: 12px !important;
}
div[data-baseweb="tag"] span { color: #c7d2fe !important; }
div[data-baseweb="tag"] button svg { fill: #a5b4fc !important; }
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
  background: rgba(15,23,42,0.88) !important;
  border: 1.5px solid rgba(99,102,241,0.55) !important;
  border-radius: 12px !important;
}

/* ── FORM SUBMIT ── */
div[data-testid="stForm"] {
  background: rgba(15,23,42,0.50) !important;
  border: 1px solid rgba(99,102,241,0.20) !important;
  border-radius: 20px !important;
  padding: 28px 32px !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "roadmap_data" not in st.session_state:
    st.session_state.roadmap_data = None
if "student_info" not in st.session_state:
    st.session_state.student_info = None
if "student_name" not in st.session_state:
    st.session_state.student_name = ""

# ─────────────────────────────────────────────
# LANDING PAGE
# ─────────────────────────────────────────────
def show_landing_page():
    QUOTES = [
        ("\"The secret of getting ahead is getting started.\"", "— Mark Twain"),
        ("\"Don't watch the clock; do what it does. Keep going.\"", "— Sam Levenson"),
        ("\"You don't have to be great to start, but you have to start to be great.\"", "— Zig Ziglar"),
        ("\"Push yourself, because no one else is going to do it for you.\"", "— Anonymous"),
        ("\"Dream big. Start small. Act now.\"", "— Robin Sharma"),
        ("\"Your future is created by what you do today, not tomorrow.\"", "— Robert Kiyosaki"),
        ("\"Success is the sum of small efforts repeated day in and day out.\"", "— Robert Collier"),
        ("\"Believe you can and you're halfway there.\"", "— Theodore Roosevelt"),
    ]
    quote_text, quote_author = random.choice(QUOTES)
    STUDENT_IMAGES = [
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=400&q=80",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80",
        "https://images.unsplash.com/photo-1529390079861-591de354faf5?w=400&q=80",
    ]
    st.markdown(f"""
    <div class="landing">
      <div class="nav">
        <div class="nav-logo">🎯  Personalized Skill Roadmap</div>
        <div class="nav-badge">Beta v1.0</div>
      </div>
      <div class="hero">
        <div class="confused-tag">😕 &nbsp; Not sure where to start?</div>
        <h1 class="hero-h1">
          <span class="line1">Stop feeling lost.</span>
          <span class="line2">Build your roadmap today.</span>
        </h1>
        <p class="hero-sub">
          Answer a few simple questions about yourself — we'll generate a
          personalised 4-week learning plan with projects, resources, and a
          readiness score. Made for engineering students like you.
        </p>
        <div class="quote-card">
          <div class="quote-text">{quote_text}</div>
          <div class="quote-author">{quote_author}</div>
        </div>
      </div>
      <div class="img-row">
        <div class="img-card">
          <img src="{STUDENT_IMAGES[0]}" alt="Students studying"/>
          <div class="img-overlay"><div class="img-label">Collaborate &amp; Grow</div><div class="img-sub">Learn with peers</div></div>
        </div>
        <div class="img-card">
          <img src="{STUDENT_IMAGES[1]}" alt="Group project"/>
          <div class="img-overlay"><div class="img-label">Build Real Projects</div><div class="img-sub">Portfolio-grade work</div></div>
        </div>
        <div class="img-card">
          <img src="{STUDENT_IMAGES[2]}" alt="Student laptop"/>
          <div class="img-overlay"><div class="img-label">Learn at Your Pace</div><div class="img-sub">Structured &amp; clear</div></div>
        </div>
      </div>
      <div class="stats-row">
        <div class="stat-item"><div class="stat-num">14+</div><div class="stat-label">Learning Tracks</div></div>
        <div class="stat-item"><div class="stat-num">4</div><div class="stat-label">Week Plan</div></div>
        <div class="stat-item"><div class="stat-num">50+</div><div class="stat-label">Free Resources</div></div>
        <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Personalised</div></div>
      </div>
      <div class="features">
        <div class="feat-card"><div class="feat-icon">📊</div><div class="feat-title">Readiness Score</div><div class="feat-desc">Get a breakdown of your academics, skills, routine, and communication.</div></div>
        <div class="feat-card"><div class="feat-icon">🗓️</div><div class="feat-title">4-Week Plan</div><div class="feat-desc">A clear week-by-week roadmap tailored to your level — beginner or intermediate.</div></div>
        <div class="feat-card"><div class="feat-icon">🧩</div><div class="feat-title">Skill Gap Analysis</div><div class="feat-desc">Pick a job role and instantly see what skills you have and what to learn next.</div></div>
        <div class="feat-card"><div class="feat-icon">⬇️</div><div class="feat-title">Download Roadmap</div><div class="feat-desc">Save your full roadmap as a Markdown file to keep and revisit anytime.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        if st.button("🚀  Start My Roadmap", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()
    st.markdown('<p style="text-align:center;color:#334155;font-size:12px;margin-top:8px">Takes less than 2 minutes · No signup needed</p>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# COURSE DATABASE  — Beginner & Intermediate tracks
# ─────────────────────────────────────────────
COURSE_DB = {
    "ML": {
        "courses_free":  [
            "🎥 Krish Naik — ML Playlist (YouTube, Free)",
            "📖 Kaggle Learn — Intro to ML + Pandas (Free)",
            "🌐 fast.ai — Practical Deep Learning for Coders (Free)",
        ],
        "courses_paid":  [
            "🎥 Andrew Ng — ML Specialization (Coursera ~₹3k/mo)",
            "📖 Udemy — ML A-Z: AI, Python & R (Paid, watch for sales)",
            "🌐 fast.ai — Practical Deep Learning for Coders (Free)",
        ],
        "weeks_beginner": [
            ["Set up Python environment (Anaconda/VS Code).", "Learn Python basics: lists, dicts, loops, functions — 2 hrs/day.", "Complete Kaggle's 'Intro to Python' + 'Intro to Pandas' micro-courses (free).", "Daily target: 1 topic + 1 notebook exercise."],
            ["Watch Krish Naik's Linear/Logistic Regression videos.", "Code from scratch: implement regression with NumPy (no Scikit).", "Understand train/test split, accuracy, confusion matrix.", "Practice: 1 Kaggle Titanic-style mini problem."],
            ["Learn Scikit-learn: Decision Tree, Random Forest, basic pipelines.", "Feature engineering basics: handle missing values, encode categories.", "Run your first cross-validation + plot feature importance.", "Submit 1 Kaggle beginner competition."],
            ["Build end-to-end project: data → model → Streamlit app.", "Write a README + upload to GitHub.", "Record a 2-min demo video (phone camera is fine).", "Review all concepts + list your 3 weakest areas for next month."],
        ],
        "weeks_intermediate": [
            ["Revise Pandas profiling + advanced feature engineering techniques.", "Implement pipelines with ColumnTransformer + custom transformers.", "Study Bias-Variance trade-off deeply + regularization (L1/L2).", "Reproduce 1 Kaggle top-10 notebook and improve it."],
            ["Dive into ensemble methods: XGBoost, LightGBM, CatBoost.", "Hyperparameter tuning: Optuna or GridSearchCV deep-dive.", "Build a model comparison dashboard (Streamlit or Plotly Dash).", "Understand SHAP values for model explainability."],
            ["Intro to Neural Networks: PyTorch or TensorFlow basics.", "Train your first CNN on image data (CIFAR-10 or custom).", "Experiment with learning rate schedulers + batch norm.", "Implement early stopping + model checkpointing."],
            ["Deploy an ML API: FastAPI + Docker basics.", "Build a portfolio project with a live demo (HuggingFace Spaces free).", "Write a technical blog post about your approach.", "Explore MLflow or Weights & Biases for experiment tracking."],
        ],
        "projects_beginner":     [("🏠 House Price Predictor", "Regression + EDA + Streamlit UI"), ("📊 Student Score Dashboard", "Classify pass/fail + visualize with Plotly"), ("🛍️ Customer Segmentation", "K-Means clustering on retail data")],
        "projects_intermediate": [("⚡ Real-time Sentiment Analyser", "Twitter API + NLP pipeline + dashboard"), ("🖼️ Image Classifier App", "CNN + HuggingFace deploy + REST API"), ("📈 Stock Price Forecasting", "LSTM + feature engineering + backtesting")],
    },
    "WEB": {
        "courses_free":  [
            "🎥 The Odin Project — Full Stack Foundations (Free)",
            "📖 FreeCodeCamp — Responsive Web Design (Free)",
            "🌐 JavaScript.info — Modern JS Tutorial (Free)",
        ],
        "courses_paid":  [
            "🎥 Traversy Media — Web Dev Bootcamp (Udemy, paid)",
            "📖 Scrimba — Frontend Career Path (Paid with free tier)",
            "🌐 The Odin Project — Full Stack Foundations (Free)",
        ],
        "weeks_beginner": [
            ["Learn HTML5 structure: semantic tags, forms, tables.", "CSS basics: box model, Flexbox layout, colours, fonts.", "Build 1 landing page (your own topic — not a clone).", "Goal: page looks good on laptop and phone."],
            ["JavaScript: variables, loops, functions, DOM manipulation.", "Build 2 interactive mini-projects: colour picker + simple calculator.", "Learn Git: init, add, commit, push to GitHub.", "Daily: 30 mins reading + 30 mins coding."],
            ["React basics: components, props, useState, useEffect.", "Build a to-do app with local state (no backend).", "Style with Tailwind CSS or CSS modules.", "Deploy to GitHub Pages or Vercel (free)."],
            ["Add a contact form + smooth scroll to your portfolio site.", "Polish 2 projects: write READMEs + add screenshots.", "Learn localStorage basics (save to-dos without backend).", "Share your GitHub link — peer review with 1 friend."],
        ],
        "weeks_intermediate": [
            ["React advanced: Context API, custom hooks, lazy loading.", "Set up ESLint + Prettier + absolute imports in a CRA/Vite project.", "Build a multi-page app with React Router v6.", "Optimize with React.memo + useMemo where needed."],
            ["Node.js + Express: REST API with full CRUD.", "Connect to MongoDB (Atlas free tier) using Mongoose.", "Add JWT authentication (login/register flow).", "Test API with Postman + document with README."],
            ["Full-stack project: React frontend + Express backend + MongoDB.", "Add image upload (Cloudinary free tier) + pagination.", "Handle errors globally: error boundaries + Express middleware.", "Write basic unit tests (Jest + React Testing Library)."],
            ["Deploy full-stack: Railway/Render (backend) + Vercel (frontend).", "Add CI/CD with GitHub Actions (auto-deploy on push).", "Performance audit with Lighthouse: target 90+ score.", "Write a case study post on your project decisions."],
        ],
        "projects_beginner":     [("🌐 Portfolio Website", "Responsive, dark mode, smooth scroll"), ("✅ Interactive To-Do App", "LocalStorage + filtering + animations"), ("🎨 CSS Art / UI Clone", "Pick a site and recreate the UI")],
        "projects_intermediate": [("🛒 Full-Stack E-commerce", "Cart, auth, MongoDB, Stripe sandbox"), ("💬 Real-time Chat App", "Socket.io + React + Node.js"), ("📰 Blog CMS", "Rich text editor + admin panel + public feed")],
    },
    "DSA": {
        "courses_free":  [
            "🎥 Striver A2Z DSA Sheet — TakeUForward (YouTube + free)",
            "📖 NeetCode.io — 150 structured problems (Free)",
            "🌐 Abdul Bari — Algorithms playlist (YouTube, Free)",
        ],
        "courses_paid":  [
            "🎥 Love Babbar — DSA Supreme 2.0 (Paid course)",
            "📖 AlgoExpert (Paid, good explanations)",
            "🌐 Striver A2Z Sheet — TakeUForward (YouTube + free)",
        ],
        "weeks_beginner": [
            ["Pick one language: Python or Java (stick to it for DSA).", "Arrays + Strings: 2-pointer, sliding window — 20 easy problems (LeetCode).", "Understand Big-O notation: O(n), O(n²), O(log n).", "Goal: solve 3 problems/day comfortably."],
            ["Linked List: insert, delete, reverse, detect cycle.", "Stack + Queue: implementation + bracket matching problems.", "15 problems covering these topics on LeetCode Easy.", "Time yourself: try to solve in under 20 minutes."],
            ["Binary Tree: traversals (in/pre/post/level order).", "Recursion basics: factorial, Fibonacci, power, subsets.", "12 tree + recursion problems (LeetCode Easy–Medium).", "Write your solutions in your own words — teach someone."],
            ["Sorting: Merge Sort + Quick Sort implementation from scratch.", "Binary Search on arrays + answers.", "Do a 1-hour mock interview (use NeetCode mock or Pramp).", "Review all weak areas + plan next 30 days."],
        ],
        "weeks_intermediate": [
            ["Dynamic Programming: memoization → tabulation pattern.", "Classic DP: knapsack, LCS, coin change — 10 problems.", "Graphs: BFS/DFS on adjacency list, detect cycle.", "Do 2 LeetCode Mediums per day minimum."],
            ["Backtracking: N-Queens, permutations, sudoku solver.", "Heaps + Priority Queue: top-K problems, merge K sorted.", "Segment Tree or Fenwick Tree basics (if targeting product companies).", "Attempt 1 LeetCode contest per week."],
            ["Advanced Graphs: Dijkstra, Bellman-Ford, Topological sort.", "Tries: implement + word search + autocomplete problems.", "2 LeetCode Mediums + 1 Hard per day.", "Review your contest mistakes and rewrite solutions."],
            ["Full mock interview set: 2 rounds × 3 problems under 90 mins.", "Revise all pattern cheat-sheets (sliding window, two-pointer etc.).", "Create your DSA revision notes doc.", "Apply to internship with your GitHub (DSA notes + mini projects)."],
        ],
        "projects_beginner":     [("📊 Sorting Visualiser", "Bubble, Selection, Merge in HTML+JS"), ("🔢 Sudoku Solver", "Backtracking with step-by-step UI"), ("📝 DSA Revision Tracker", "Track solved problems with progress bar")],
        "projects_intermediate": [("🗺️ Pathfinding Visualiser", "BFS/Dijkstra on grid + animated"), ("📈 Contest Rating Tracker", "Scrape LeetCode + Codeforces, plot trends"), ("🧩 DSA Flashcard App", "Spaced-repetition system for patterns")],
    },
    "CYBER": {
        "courses_free":  [
            "🎥 TryHackMe — Pre-Security + Jr Pentester Path (Free tier)",
            "📖 OverTheWire Bandit — Linux wargame (Free)",
            "🌐 OWASP Top 10 — official docs + YouTube walkthroughs (Free)",
        ],
        "courses_paid":  [
            "🎥 TCM Security — Practical Ethical Hacking (Paid, high quality)",
            "📖 INE / eJPT — Entry-level pentesting (Paid)",
            "🌐 TryHackMe — Pre-Security Path (Free tier available)",
        ],
        "weeks_beginner": [
            ["Linux basics: file system, permissions, common commands.", "Networking: IP, TCP/UDP, DNS, HTTP — conceptual understanding.", "Complete TryHackMe 'Pre-Security' path rooms (free).", "Goal: get comfortable with terminal, ping, traceroute, curl."],
            ["OWASP Top 10: understand SQLi, XSS, IDOR, auth flaws.", "Practice on DVWA (Damn Vulnerable Web App) locally.", "Learn Burp Suite Community Edition basics (intercept, repeater).", "Attempt 3 easy TryHackMe web rooms."],
            ["Hands-on labs: TryHackMe 'Jr Pentester' intro rooms.", "Wireshark basics: capture + filter HTTP/DNS traffic.", "Understand firewalls, IDS/IPS at concept level.", "Write notes for each room (your personal security handbook)."],
            ["Mini project: OWASP checklist audit on a demo site.", "Create a security report template (executive summary + findings).", "Practice 2 more TryHackMe rooms of your choice.", "Set up a home lab: Kali VM + vulnerable target (VulnHub)."],
        ],
        "weeks_intermediate": [
            ["Active recon: Nmap scans, enum4linux, Gobuster directory brute-force.", "Exploitation basics: Metasploit Framework — search, use, run.", "Complete TryHackMe 'Steel Mountain' or 'Blue' room.", "Read 2 CVE writeups and understand the vulnerability chain."],
            ["Web app pentesting deep-dive: SQL injection (manual + sqlmap).", "XSS: reflected, stored, DOM-based — exploit each on DVWA.", "Directory traversal + IDOR + broken auth labs.", "Write a full pentest report for 1 box (methodical format)."],
            ["Privilege escalation: Linux (GTFOBins) + Windows (WinPEAS).", "Hash cracking: Hashcat + John the Ripper + rainbow tables.", "Complete 2 HackTheBox Easy machines.", "Study CVE writeup + reproduce the exploit in your lab."],
            ["Build portfolio: 3 documented HTB/THM writeups on GitHub.", "Learn report writing: executive summary + risk rating + remediation.", "Attempt 1 CTF competition (CTFtime.org upcoming events).", "Explore bug bounty programs (HackerOne, Bugcrowd — read-only first)."],
        ],
        "projects_beginner":     [("🔍 OWASP Audit Report", "Checklist-based audit on demo site"), ("🔐 Password Strength Tool", "Entropy check + bcrypt hash demo in Python"), ("🌐 Phishing Awareness Site", "Educational mini-site on spotting phishing")],
        "projects_intermediate": [("🏴 CTF Writeup Portfolio", "3 documented HTB/THM writeups on GitHub"), ("🔓 Vuln Scanner Script", "Python script using Nmap + CVE lookup"), ("📋 Pentest Report Template", "Professional report for 1 HTB/THM machine")],
    },
    "VLSI": {
        "courses_free":  ["🎥 NPTEL — VLSI Design (Free audit)", "📖 Nandland — FPGA/Verilog tutorials (Free)", "🌐 YouTube — Digital Design with Verilog playlist"],
        "courses_paid":  ["🎥 NPTEL VLSI Design (Free)", "📖 Udemy — Complete Verilog HDL (Paid)", "🌐 Nandland FPGA/Verilog (Free)"],
        "weeks_beginner": [
            ["Number systems recap + Boolean algebra + logic minimization (K-map).", "Combinational circuits: MUX, decoder, adder from scratch.", "Verilog: module, wire, reg, basic assign + always blocks.", "Simulate 2 simple circuits using EDA Playground (free online)."],
            ["Sequential circuits: D flip-flop, JK flip-flop, registers.", "Verilog behavioral modeling: if-else, case statements.", "Write and simulate a 4-bit counter in Verilog.", "Draw timing diagrams for your circuits — builds intuition."],
            ["Finite State Machines (FSM): Moore vs Mealy, traffic light design.", "Implement FSM in Verilog + write a testbench.", "Understand synthesis flow (concept level): RTL → netlist → layout.", "Attempt 2 design problems from NPTEL assignments."],
            ["Project: design a small digital system (ALU or controller).", "Write a testbench covering corner cases.", "Simulate, document waveforms, write a 2-page report.", "Review and note 3 things you would do differently."],
        ],
        "weeks_intermediate": [
            ["Advanced Verilog: tasks, functions, parameterized modules.", "Pipelining: implement a pipelined adder/multiplier.", "Timing analysis concepts: setup time, hold time, critical path.", "Reproduce a textbook design and optimize it."],
            ["Low-power design techniques: clock gating, power domains.", "Memory design: SRAM, DRAM concepts + Verilog model.", "Understand DFT basics: scan chain, BIST concept.", "Complete a Verilog project and peer-review with classmate."],
            ["Physical design flow: floorplan → P&R → STA overview.", "Open-source tools: OpenROAD or Qflow — run a small design.", "Study 1 published VLSI paper and summarize it.", "Focus on area/power trade-offs in your design."],
            ["Portfolio project: 4-bit processor or custom controller.", "Document: block diagram + FSM + waveforms + area/power report.", "Upload to GitHub with README + simulation screenshots.", "Prepare 5-min project walkthrough for interviews."],
        ],
        "projects_beginner":     [("⚙️ 4-bit ALU in Verilog", "Add, sub, AND, OR operations + testbench"), ("🚦 Traffic Light FSM", "3-state controller with timing"), ("🔢 Shift Register", "SISO/SIPO with Verilog simulation")],
        "projects_intermediate": [("🖥️ 4-bit Processor", "Fetch-decode-execute + instruction set"), ("📊 UART Controller", "Serial communication in Verilog"), ("⚡ Pipelined Multiplier", "4-stage pipeline + area analysis")],
    },
    "IOT": {
        "courses_free":  ["🎥 Arduino + ESP32 IoT playlist (YouTube, Free)", "📖 NPTEL — Introduction to IoT (Free audit)", "🌐 Random Nerd Tutorials — ESP32 guides (Free)"],
        "courses_paid":  ["🎥 Udemy — IoT with ESP32 (Paid)", "📖 NPTEL IoT (Free)", "🌐 Random Nerd Tutorials (Free)"],
        "weeks_beginner": [
            ["Set up Arduino IDE + install ESP32 board package.", "GPIO basics: digital read/write, LED blink, button press.", "Connect a temperature sensor (DHT11/DHT22) — read and print values.", "Log sensor data to Serial Monitor and observe."],
            ["Analog sensors: LDR (light), potentiometer — map values.", "Display data on 16×2 LCD or OLED screen.", "Build a sensor data logger to SD card or Serial.", "Daily: wire 1 new sensor, read datasheet, test it."],
            ["Wi-Fi basics: connect ESP32 to network, send HTTP GET.", "Post sensor data to a free dashboard (ThingSpeak or Adafruit IO).", "Set up MQTT basics: broker, publish, subscribe (Mosquitto local).", "Trigger an LED/buzzer based on sensor threshold (cloud command)."],
            ["Project: IoT dashboard — ESP32 + 2 sensors + live web chart.", "Write a README with circuit diagram (use Fritzing).", "Record a 1-min demo video of data flowing to the dashboard.", "Note improvements: battery life, Wi-Fi reconnect logic."],
        ],
        "weeks_intermediate": [
            ["Deep-sleep + wake on interrupt for battery optimization.", "OTA (Over-The-Air) firmware updates with ESP32.", "MQTT + TLS security: encrypted communication.", "Store data locally (SPIFFS/LittleFS) when offline + sync later."],
            ["Build a RESTful API on the device (ESPAsyncWebServer).", "JSON parsing: ArduinoJSON library for structured data.", "Multi-task with FreeRTOS: separate sensor, display, Wi-Fi tasks.", "Implement watchdog timer + robust error recovery."],
            ["Edge ML: TensorFlow Lite Micro — gesture or keyword detection.", "LoRa basics: long-range low-power comm concept + simple demo.", "Node-RED: visual IoT pipeline on local server.", "Integrate 2 different protocols in 1 project."],
            ["End-to-end project: ESP32 + cloud + web dashboard + mobile alert.", "PCB design intro: EasyEDA schematic for your circuit (free online).", "Document architecture diagram + BOM + power budget.", "GitHub portfolio: code + wiring diagram + demo GIF."],
        ],
        "projects_beginner":     [("🌡️ Smart Weather Station", "Temp/humidity/light + ThingSpeak dashboard"), ("🚨 Smart Alert System", "Threshold breach → buzzer + LED + serial log"), ("📊 Sensor Data Logger", "SD card logging + CSV export")],
        "projects_intermediate": [("🏠 Home Automation Hub", "MQTT + mobile app control + schedules"), ("🌱 Smart Plant Monitor", "Soil moisture + auto-watering + Telegram alerts"), ("📡 LoRa Sensor Node", "Long-range data + gateway + dashboard")],
    },
    "SOFT": {
        "courses_free":  ["🎥 Basic Communication Skills (YouTube, Free)", "📖 TED Talks — watch 1/day + take notes (Free)", "🌐 Grammarly Blog + writing exercises (Free)"],
        "courses_paid":  ["🎥 Coursera — English Communication Skills (Paid/Audit)", "📖 Udemy — Public Speaking Mastery (Paid)", "🌐 TED Talks + Grammarly (Free)"],
        "weeks_beginner": [
            ["Read 1 article/day — summarise it in 5–7 lines in your own words.", "Practice 5 minutes of spoken English daily (record on phone).", "Learn 5 new professional words per day + use them in sentences.", "Goal: write 1 email draft (even imaginary) with formal tone."],
            ["Watch 1 TED Talk/day — note 3 key ideas + how speaker delivers.", "Practice introducing yourself confidently (2-min script, memorise).", "Improve clarity: short sentences, active voice, no filler words.", "Write a short paragraph every day (topic: your day or a skill you learned)."],
            ["Mock interview: ask a friend to give you 2 HR questions + respond.", "Focus: eye contact, posture, pace of speaking (no rushing).", "Give a 3-minute presentation on any topic to a friend or mirror.", "Collect feedback + note 2 specific things to improve."],
            ["Record a 2-minute self-introduction video — watch it critically.", "Update your resume using a clean template (NovoResume free).", "Write a professional LinkedIn 'About' section.", "Do 1 more mock interview — compare to week 1 recording."],
        ],
        "weeks_intermediate": [
            ["Study persuasion techniques: storytelling, data + story combo.", "Give a 5-minute structured presentation (Problem–Solution–Benefit).", "Practice disagreeing politely + suggesting alternatives in conversation.", "Read 1 chapter of a communication book (eg. 'Talk Like TED')."],
            ["Group discussion practice: join or simulate a GD with peers.", "Practice giving and receiving constructive feedback.", "Technical writing: write a 1-page project summary clearly.", "Record a GD session and self-review."],
            ["Advanced email: write a persuasive proposal or request email.", "Practise negotiation: salary negotiation or resource request role-play.", "Host a mini Q&A session — answer questions on your project.", "LinkedIn: post 1 short professional update or insight."],
            ["Final project: film a 3-min video demo of one of your tech projects.", "Focus on clear explanation, pace, confidence — no script needed.", "Get 3 peer reviews + incorporate feedback.", "Upload to LinkedIn — professional communication is your new habit."],
        ],
        "projects_beginner":     [("🎥 Self-Intro Video", "2-min confident intro + upload to drive"), ("📄 Resume Rebuild", "Clean template + tailored to 1 job role"), ("📝 Daily Writing Log", "7-day challenge: 1 paragraph/day")],
        "projects_intermediate": [("🎤 5-min Tech Talk", "Present your best project clearly on video"), ("📋 Project Case Study", "Written report: problem, approach, outcome"), ("🤝 Mock GD Documentation", "Record + review a group discussion session")],
    },
}

# Fill remaining categories with a simpler template
_SIMPLE_CATS = {
    "ECE": ("ECE / Electronics",
        ["🎥 NPTEL — Digital Circuits / Microprocessors (Free)", "📖 YouTube — Arduino/ESP32 Embedded series (Free)", "🌐 NPTEL — VLSI or Communication Systems (choose 1, Free)"],
        ["🎥 NPTEL Core + Udemy Embedded (Paid)", "📖 YouTube — Arduino/ESP32 series (Free)", "🌐 NPTEL VLSI/Comm Systems (Free)"]),
    "EEE": ("EEE / Electrical",
        ["🎥 NPTEL — Power Systems (Free)", "📖 NPTEL — Electrical Machines (Free)", "🌐 YouTube — Industrial Automation intro (Free)"],
        ["🎥 NPTEL + Udemy Power Systems (Paid)", "📖 NPTEL Electrical Machines (Free)", "🌐 Industrial Automation (YouTube)"]),
    "MECH": ("Mechanical",
        ["🎥 Fusion 360 / SolidWorks tutorials (YouTube, Free)", "📖 NPTEL — Manufacturing or Thermal Engineering (Free)", "🌐 YouTube — Robotics basics playlist (Free)"],
        ["🎥 Udemy — SolidWorks or AutoCAD (Paid)", "📖 NPTEL Manufacturing (Free)", "🌐 YouTube Robotics (Free)"]),
    "EMBEDDED": ("Embedded Systems",
        ["🎥 YouTube — Embedded C / ARM Cortex tutorials (Free)", "📖 Arduino/ESP32 practical series (YouTube, Free)", "🌐 NPTEL — Embedded Systems (Free audit)"],
        ["🎥 Udemy — Embedded C + RTOS (Paid)", "📖 YouTube Embedded C (Free)", "🌐 NPTEL Embedded (Free)"]),
    "SIGNAL": ("Signal Processing",
        ["🎥 NPTEL — Signals and Systems (Free)", "📖 YouTube — DSP basics (FFT, filters) (Free)", "🌐 Python + SciPy signal processing tutorials (Free)"],
        ["🎥 NPTEL Signals + Coursera DSP (Paid)", "📖 YouTube DSP (Free)", "🌐 SciPy docs (Free)"]),
    "COMM_SYSTEMS": ("Communication Systems",
        ["🎥 NPTEL — Communication Systems (Free)", "📖 YouTube — Signals & Systems basics (Free)", "🌐 MATLAB/Python signal basics tutorial (Free)"],
        ["🎥 NPTEL Comm Sys + Udemy (Paid)", "📖 YouTube Signals (Free)", "🌐 MATLAB/Python basics (Free)"]),
    "POWER": ("Power Systems",
        ["🎥 NPTEL — Power Systems (Free)", "📖 YouTube — Protection & Switchgear basics (Free)", "🌐 Excel/Python for power flow calculations (Free)"],
        ["🎥 NPTEL Power Sys + Udemy (Paid)", "📖 YouTube Protection (Free)", "🌐 Power flow tools (Free)"]),
    "RENEW": ("Renewable Energy",
        ["🎥 NPTEL — Renewable Energy (Free)", "📖 YouTube — Solar PV basics + sizing (Free)", "🌐 YouTube — Wind energy basics (Free)"],
        ["🎥 NPTEL Renewable + Coursera (Paid)", "📖 YouTube Solar PV (Free)", "🌐 Wind energy YouTube (Free)"]),
    "AUTOMATION": ("Industrial Automation",
        ["🎥 YouTube — PLC basics / ladder logic (Free)", "📖 NPTEL — Industrial Automation (Free)", "🌐 YouTube — SCADA basics overview (Free)"],
        ["🎥 Udemy — PLC Programming (Paid)", "📖 NPTEL Automation (Free)", "🌐 YouTube SCADA (Free)"]),
    "CAD": ("CAD Design",
        ["🎥 Fusion 360 beginner tutorials (YouTube, Free)", "📖 Engineering Drawing basics (YouTube, Free)", "🌐 GrabCAD community + tutorials (Free)"],
        ["🎥 Udemy — SolidWorks / AutoCAD (Paid)", "📖 YouTube Engineering Drawing (Free)", "🌐 GrabCAD community (Free)"]),
    "ROBOTICS": ("Robotics",
        ["🎥 YouTube — Robotics basics playlist (Free)", "📖 Arduino motor control series (YouTube, Free)", "🌐 ROS (Robot Operating System) beginner tutorials (Free)"],
        ["🎥 Udemy — Robotics + ROS (Paid)", "📖 YouTube Robotics (Free)", "🌐 ROS official docs (Free)"]),
    "AUTO": ("Automobile Engineering",
        ["🎥 YouTube — Automobile basics / engine fundamentals (Free)", "📖 NPTEL — Automobile Engineering (Free audit)", "🌐 YouTube — Vehicle dynamics intro (Free)"],
        ["🎥 NPTEL Auto + Udemy (Paid)", "📖 YouTube Engine basics (Free)", "🌐 Vehicle dynamics YouTube (Free)"]),
    "THERMAL": ("Thermal Engineering",
        ["🎥 NPTEL — Thermal Engineering basics (Free)", "📖 YouTube — Heat transfer intro (Free)", "🌐 Python for thermodynamics calculations (Free)"],
        ["🎥 NPTEL Thermal + Udemy (Paid)", "📖 YouTube Heat Transfer (Free)", "🌐 Python thermo tools (Free)"]),
    "MANUFACTURING": ("Manufacturing",
        ["🎥 NPTEL — Manufacturing Processes (Free)", "📖 YouTube — Metrology basics (Free)", "🌐 YouTube — Lean/5S manufacturing intro (Free)"],
        ["🎥 NPTEL Manufacturing + Udemy (Paid)", "📖 YouTube Metrology (Free)", "🌐 Lean YouTube (Free)"]),
    "SMARTGRID": ("Smart Grid",
        ["🎥 YouTube — Smart Grid basics (Free)", "📖 NPTEL — Smart Grid (Free audit)", "🌐 IEEE Spectrum — Smart Grid articles (Free)"],
        ["🎥 NPTEL Smart Grid + Coursera (Paid)", "📖 YouTube Smart Grid (Free)", "🌐 IEEE articles (Free)"]),
    "ELECTRICAL_DESIGN": ("Electrical Design",
        ["🎥 YouTube — Electrical Design basics (Free)", "📖 YouTube — AutoCAD Electrical intro (Free)", "🌐 IEC/IS standards overview (Free)"],
        ["🎥 Udemy — AutoCAD Electrical (Paid)", "📖 YouTube Electrical Design (Free)", "🌐 Standards overview (Free)"]),
}

_GENERIC_BEGINNER_WEEKS = [
    ["Set up your tools + explore the domain fundamentals.", "Complete introductory exercises or tutorials (2 hrs/day).", "Read/watch 1 core concept per day — take brief notes.", "Goal: understand the basic vocabulary of your field."],
    ["Go deeper on 2–3 core topics identified in Week 1.", "Practice with guided examples + replicate them independently.", "Identify 1 area you find hardest — spend extra time there.", "Daily: 1 concept + 1 small exercise."],
    ["Apply concepts: start your first mini project.", "Follow a tutorial step-by-step, then modify it to make it your own.", "Document what you build — a short README counts.", "Share with a peer for feedback."],
    ["Complete and polish your mini project.", "Write a concise summary: what you learned + what you'd do differently.", "Plan your next 30 days based on gaps discovered.", "Upload to GitHub + update your resume/LinkedIn."],
]
_GENERIC_INTERMEDIATE_WEEKS = [
    ["Review fundamentals at speed — focus on gaps not basics.", "Choose 1 advanced topic and go deep (not broad).", "Read documentation or a reference book chapter.", "Attempt 1 challenging problem or exercise."],
    ["Build a non-trivial project incorporating advanced techniques.", "Follow industry standards: documentation, version control, testing.", "Get peer feedback or post in a community (Reddit, Discord).", "Compare your approach to an expert solution."],
    ["Optimize: improve performance, readability, or scalability.", "Add 1 advanced feature or integration to your project.", "Write a technical blog post or internal doc about your approach.", "Benchmark or measure your work quantitatively."],
    ["Final portfolio project: end-to-end, production-quality.", "Record a 3-min walkthrough or write a detailed case study.", "Upload to GitHub with full documentation.", "Plan your next skill (adjacent domain or deeper specialization)."],
]

for _cat, (_title, _free, _paid) in _SIMPLE_CATS.items():
    if _cat not in COURSE_DB:
        # simple projects
        _bp = [("📋 Mini Concept Report", "Document + diagrams + examples"), ("🛠️ Hands-on Lab Demo", "Simple implementation + screenshot"), ("📊 Comparison Study", "Research + structured report")]
        _ip = [("⚡ Advanced Project", "Full-featured implementation + documentation"), ("🔬 Simulation / Analysis", "Quantitative results + report"), ("📑 Technical Case Study", "Industry-relevant problem + solution")]
        COURSE_DB[_cat] = {
            "courses_free": _free,
            "courses_paid": _paid,
            "weeks_beginner": _GENERIC_BEGINNER_WEEKS,
            "weeks_intermediate": _GENERIC_INTERMEDIATE_WEEKS,
            "projects_beginner": _bp,
            "projects_intermediate": _ip,
        }


JOB_SKILL_ANALYSIS = {
    "Software Developer":     {"skills": ["Python / Java", "Data Structures & Algorithms", "HTML, CSS, JavaScript", "Git & GitHub", "Databases (SQL)", "OOPS", "Problem Solving"], "projects": ["Student Management System", "Task Tracker Application", "Portfolio Website", "REST API Mini Project"], "resources": ["NPTEL – Programming & DSA", "YouTube – freeCodeCamp", "GeeksForGeeks – DSA", "GitHub – Open Source Projects"]},
    "Frontend Developer":     {"skills": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Git & GitHub"], "projects": ["Portfolio Website", "React To-Do App", "UI Clone (Netflix / Amazon)"], "resources": ["MDN Web Docs", "Traversy Media (YouTube)", "React Official Docs"]},
    "Backend Developer":      {"skills": ["Node.js / Python / Java", "Databases (SQL/NoSQL)", "APIs / RESTful Services", "Git & GitHub", "Authentication & Security"], "projects": ["REST API Project", "E-commerce Backend", "Blog Platform Backend"], "resources": ["Udemy Backend Courses", "YouTube – Tech With Tim / Traversy Media", "MongoDB University"]},
    "Data Scientist":         {"skills": ["Python", "Statistics", "Pandas & NumPy", "Data Visualization", "Machine Learning Basics"], "projects": ["Student Performance Analysis", "Sales Prediction Model", "EDA Project"], "resources": ["Kaggle Learn", "Krish Naik (YouTube)", "Coursera ML (Audit Mode)"]},
    "Machine Learning Engineer": {"skills": ["Python", "Linear Algebra & Statistics", "Scikit-learn / TensorFlow / PyTorch", "Data Preprocessing", "Model Deployment"], "projects": ["Predictive Analytics Model", "Image Classification Project", "Recommendation System"], "resources": ["Fast.ai Courses", "DeepLearning.ai (Coursera)", "YouTube – Sentdex / Krish Naik"]},
    "DevOps Engineer":        {"skills": ["Linux / Shell Scripting", "CI/CD (Jenkins/GitHub Actions)", "Docker / Kubernetes", "Cloud Platforms (AWS / GCP / Azure)", "Monitoring & Logging"], "projects": ["CI/CD Pipeline Setup", "Dockerized Application Deployment", "Cloud Infrastructure Project"], "resources": ["Linux Academy / A Cloud Guru", "YouTube – TechWorld with Nana", "Official Docker & Kubernetes Docs"]},
    "UI/UX Designer":         {"skills": ["Figma / Adobe XD", "Wireframing & Prototyping", "User Research & Testing", "Responsive Design Principles", "Portfolio Creation"], "projects": ["Mobile App Wireframes", "Website Redesign Project", "Interactive Prototype"], "resources": ["Figma Learn Tutorials", "Coursera UI/UX Courses", "YouTube – DesignCourse / CharliMarieTV"]},
    "Cybersecurity Analyst":  {"skills": ["Networking Basics", "Linux & Windows Security", "Penetration Testing", "Firewalls & IDS/IPS", "Security Tools (Wireshark, Nmap)"], "projects": ["Vulnerability Assessment", "Phishing Simulation", "Secure Web Application Setup"], "resources": ["TryHackMe / Hack The Box", "Cybrary Courses", "YouTube – NetworkChuck / The Cyber Mentor"]},
    "Mobile App Developer":   {"skills": ["Java / Kotlin / Swift / Flutter", "UI/UX for Mobile", "APIs & Backend Integration", "App Deployment (Play Store / App Store)", "Debugging & Testing"], "projects": ["Todo App", "Weather Forecast App", "E-commerce Mobile App"], "resources": ["Udemy Mobile App Courses", "YouTube – CodeWithChris / The Net Ninja", "Official Flutter Docs"]},
    "Cloud Engineer":         {"skills": ["AWS / Azure / GCP", "Cloud Architecture & Design", "Networking & Security", "CI/CD Pipelines", "Infrastructure as Code (Terraform)"], "projects": ["Deploy Web App on Cloud", "Serverless Application Project", "Cloud Monitoring Setup"], "resources": ["AWS / Azure / GCP Official Docs", "A Cloud Guru Courses", "YouTube – TechWorld with Nana"]},
    "Business Analyst":       {"skills": ["Excel / SQL / Tableau / PowerBI", "Requirement Gathering", "Process Modeling", "Data Analysis & Reporting", "Communication & Presentation"], "projects": ["Sales Dashboard", "Customer Analysis Report", "Process Optimization Project"], "resources": ["Coursera Business Analytics", "Udemy SQL / Tableau Courses", "YouTube – Analytics University"]},
    "Digital Marketing Specialist": {"skills": ["SEO / SEM", "Google Analytics", "Content Creation", "Social Media Marketing", "Email Marketing"], "projects": ["SEO Campaign Project", "Social Media Ad Campaign", "Email Marketing Automation"], "resources": ["Google Digital Garage", "HubSpot Academy", "YouTube – Neil Patel / Brian Dean"]},
    "Blockchain Developer":   {"skills": ["Solidity / Ethereum", "Smart Contracts", "Web3.js / Ethers.js", "Blockchain Architecture", "Cryptography Basics"], "projects": ["Smart Contract Deployment", "NFT Minting Platform", "Decentralized App (DApp)"], "resources": ["CryptoZombies.io", "Coursera Blockchain Courses", "YouTube – Dapp University"]},
    "AI Researcher":          {"skills": ["Python / R", "Mathematics (Linear Algebra, Probability)", "Deep Learning", "NLP / Computer Vision", "Research Paper Reading & Implementation"], "projects": ["Image Captioning Model", "Text Summarization Model", "Custom Neural Network Research"], "resources": ["arXiv Papers", "DeepLearning.ai", "YouTube – Yannic Kilcher / Two Minute Papers"]},
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def clamp(x, lo, hi): return max(lo, min(hi, x))

def detect_category(interest: str) -> str:
    s = str(interest).lower()
    if any(k in s for k in ["ai/ml", "ml", "ai", "data science", "data analysis", "machine learning"]): return "ML"
    if any(k in s for k in ["web", "app development", "frontend", "backend", "full stack"]): return "WEB"
    if any(k in s for k in ["competitive coding", "dsa", "algorithms", "data structures"]): return "DSA"
    if "cyber" in s: return "CYBER"
    if "vlsi" in s: return "VLSI"
    if "iot" in s: return "IOT"
    if "embedded" in s: return "EMBEDDED"
    if "signal processing" in s: return "SIGNAL"
    if "communication systems" in s: return "COMM_SYSTEMS"
    if "power systems" in s: return "POWER"
    if "renewable energy" in s: return "RENEW"
    if "smart grid" in s: return "SMARTGRID"
    if "industrial automation" in s: return "AUTOMATION"
    if "electrical design" in s: return "ELECTRICAL_DESIGN"
    if "robotics" in s: return "ROBOTICS"
    if "cad design" in s or "cad" in s: return "CAD"
    if "automobile" in s: return "AUTO"
    if "thermal" in s: return "THERMAL"
    if "manufacturing" in s: return "MANUFACTURING"
    if any(k in s for k in ["communication skill", "soft skill", "english", "presentation"]): return "SOFT"
    if "ece" in s or "electronics" in s: return "ECE"
    if "eee" in s or "electrical" in s: return "EEE"
    if "mechanical" in s or "mech" in s: return "MECH"
    return "DSA"

def get_similar_students(df, info):
    strict = df[(df["branch"] == info["branch"]) & (df["interest"] == info["interest"])]
    if len(strict) >= 5: return strict
    relaxed = df[df["branch"] == info["branch"]]
    if len(relaxed) >= 5: return relaxed
    return df

def build_week_plan(interest, skill_level, budget):
    cat   = detect_category(interest)
    data  = COURSE_DB.get(cat, COURSE_DB["DSA"])
    is_beginner = "begin" in str(skill_level).lower()
    is_free     = str(budget).lower() in ("low",)

    resources = data["courses_free"] if is_free else data["courses_paid"]
    week_data = data["weeks_beginner"] if is_beginner else data["weeks_intermediate"]
    projects  = data["projects_beginner"] if is_beginner else data["projects_intermediate"]

    week_titles_beginner     = ["Foundation & Setup", "Core Concepts", "Build & Practice", "Portfolio & Review"]
    week_titles_intermediate = ["Advanced Concepts", "Project Deep-Dive", "Optimization & Quality", "Portfolio & Next Steps"]
    titles = week_titles_beginner if is_beginner else week_titles_intermediate

    week_plan = []
    for i in range(4):
        week_plan.append({
            "title": f"Week {i+1} — {titles[i]}",
            "bullets": week_data[i],
            "level": "Beginner" if is_beginner else "Intermediate",
        })
    return week_plan, resources, projects


def generate_structured_roadmap(info, df):
    budget        = str(info.get("budget") or info.get("budget_level") or "Low").strip()
    gpa           = float(info.get("gpa") or 7.0)
    study_hours   = int(info.get("study_hours") or 3)
    sleep_hours   = int(info.get("sleep_hours") or 7)
    failures      = int(info.get("failures") or 0)
    communication = str(info.get("communication") or info.get("communication_level") or "Average").strip()
    stress_level  = str(info.get("stress_level") or "Medium").strip()
    confusion     = str(info.get("confusion_level") or "Medium").strip()
    hostel        = str(info.get("hostel") or "No").strip()
    family_support = str(info.get("family_support") or "Medium").strip()
    interest      = str(info.get("interest") or "").strip()
    skill_level   = str(info.get("skill_level") or "Beginner").strip()
    year          = int(info.get("year") or 2)
    branch        = str(info.get("branch") or "").strip()
    is_beginner   = "begin" in skill_level.lower()

    sim = get_similar_students(df, info)
    if len(sim) >= 5:
        avg_gpa   = sim["gpa"].mean()        if "gpa"         in sim.columns else None
        avg_study = sim["study_hours"].mean() if "study_hours" in sim.columns else None
        if avg_gpa is not None and avg_study is not None:
            gpa_compare = "above" if gpa > avg_gpa else "below"
            sim_note = (f"Among {len(sim)} {branch} students interested in {interest}: "
                        f"avg GPA is {avg_gpa:.2f} (you are {gpa_compare} average) and "
                        f"avg study time is {avg_study:.1f} hrs/day.")
        else:
            sim_note = f"Showing roadmap based on {len(sim)} similar {branch} students."
    else:
        sim_note = "Personalised roadmap generated based on your profile inputs."

    # ── GOALS (dynamic, multi-condition) ──
    goals = [f"Build a solid foundation in {interest} over the next 4 weeks."]

    if is_beginner:
        goals.append("Focus on understanding concepts before rushing to advanced topics.")
    else:
        goals.append("Deepen your expertise and build portfolio-grade projects.")

    if gpa >= 8.0:
        goals.append("Leverage your strong academics — combine theory with implementation projects.")
    elif gpa >= 6.0:
        goals.append("Maintain academic consistency while growing technical skills in parallel.")
    else:
        goals.append(f"Target +0.5 GPA improvement next semester alongside skill building.")

    if study_hours >= 5:
        goals.append("You study well — channel those hours into 1 focused project per week.")
    elif study_hours >= 3:
        goals.append("Use your 3+ daily study hours with a structured daily plan (no random browsing).")
    else:
        goals.append("Build a consistent study habit: even 90 focused minutes/day creates momentum.")

    if year == 1:
        goals.append("Year 1 priority: build strong fundamentals + explore interests widely.")
    elif year == 2:
        goals.append("Year 2 priority: pick 1 domain, go deep, complete 2 projects for your portfolio.")
    elif year == 3:
        goals.append("Year 3 priority: internship-ready projects + technical skill + communication.")
    else:
        goals.append("Year 4 priority: polish portfolio, prepare for placements/higher studies.")

    if communication in ("Poor",):
        goals.append("Improve communication to complement your technical skills (top hiring factor).")

    # ── RISKS (detailed) ──
    risks = []
    if stress_level == "High" and confusion == "High":
        risks.append("High stress + confusion is a dangerous combo — leads to burnout and avoidance. Break work into 25-min focused sessions (Pomodoro). Take Sundays off completely.")
    elif stress_level == "High":
        risks.append("High stress detected. Sustainable learning beats intense sprints. Cap study at 5–6 hrs with breaks; maintain sleep ≥ 7 hrs.")
    elif confusion == "High":
        risks.append("High confusion means you may be skipping fundamentals. Slow down — spend extra time on Week 1 basics before progressing.")

    if failures > 0:
        risks.append(f"{'1 academic failure' if failures == 1 else f'{failures} academic failures'} noted — don't let past results define direction. Identify the root cause (study method? attendance? concepts?) and fix that first.")

    if sleep_hours < 6:
        risks.append(f"Only {sleep_hours} hrs of sleep is hurting memory consolidation and focus. Aim for 7–8 hrs — this single change can improve your performance more than 1 extra study hour.")

    if study_hours < 2 and stress_level == "High":
        risks.append("Studying very little but feeling stressed — the anxiety comes from not starting. Even 30 mins of focused work breaks the cycle.")

    if budget == "Low" and not is_beginner:
        risks.append("Low budget + intermediate goals: use free resources strategically (fast.ai, Kaggle, NPTEL) — they are genuinely high quality. Build projects over certificates.")

    # ── HABITS (personalised) ──
    habits = []
    if hostel == "Yes":
        habits.append("Hostel advantage: fixed schedule matters more than hours. Set a hard study start time (e.g., 9 PM daily) and stick to it. Avoid late-night phone scrolling past midnight.")
    else:
        habits.append("Home advantage: fewer distractions if you communicate your study time to family. Use a dedicated study corner and treat it like college hours.")

    if study_hours < 3:
        habits.append("Start small: 2 × 45-minute focused blocks (Pomodoro) per day. No multitasking during blocks. Phone face-down, notifications off.")
    else:
        habits.append("Maintain your study streak: track daily with a simple habit tracker (even a paper checkmark). Don't break the chain.")

    if sleep_hours >= 7:
        habits.append("Great sleep habit — protect it. Sleep consistency (same bed/wake time) improves focus more than caffeine.")
    else:
        habits.append(f"Prioritize sleep: shift from {sleep_hours} hrs to 7 hrs. Avoid screens 30 mins before bed. Sleep quality = learning quality.")

    habits.append("Weekly review every Sunday: 15 mins — what did I learn? What's stuck? What's next week's goal? This prevents drifting.")

    if communication in ("Poor", "Average"):
        habits.append("Communication habit: write 1 short summary of what you learned today (5–7 sentences). This builds both writing and retention.")

    # ── STEPS (specific + conditional) ──
    steps = []
    if family_support == "Low":
        steps.append("External support matters: find an online community (Reddit r/learnprogramming, Discord study servers) or 1 peer with similar goals. Accountability works.")
    elif family_support == "High":
        steps.append("Use family support actively: share your weekly goal with them on Sunday. External accountability boosts follow-through by ~65%.")
    else:
        steps.append("Build a small study group (2–3 people from your class). Even 1 hour of collaborative problem-solving per week accelerates learning.")

    if budget == "Low":
        steps.append("Free resources are more than enough to start. Sequence: YouTube fundamentals → Kaggle/FreeCodeCamp practicals → GitHub projects. Build proof, not certificates.")
    else:
        steps.append("Budget tip: buy 1 high-quality course (not 10 cheap ones). Focus on finishing it. Udemy sales bring courses to ₹499. Pair with free docs and practice.")

    if is_beginner:
        steps.append("Beginner rule: do NOT jump to advanced topics. Finish Week 1 basics before touching Week 2 material — confusion at early stages is solved by slowing down, not skipping ahead.")
    else:
        steps.append("Intermediate strategy: find your knowledge gaps first (do a mini assessment or attempt a medium-difficulty project). Build up from there — don't re-learn basics you know.")

    if gpa < 6.0:
        steps.append("Academic recovery: revise 1 subject topic daily + do weekly self-tests. Correlate weak subjects with your career interest — knowing 'why it matters' helps retention.")

    if communication in ("Poor",):
        steps.append("Communication fix: 2 speaking practices/week (talk about your tech project to a friend or record yourself). Technical ability + clear communication = internship-ready.")

    if year >= 3:
        steps.append("Placement prep: start applying to internships even if you feel 'not ready'. Rejections teach you more than preparation alone. 2 live applications per week.")

    steps.append(f"Track your 4-week journey: mark each week's tasks in a Notion or paper tracker. Visible progress is a powerful motivator.")

    week_plan, resources, projects = build_week_plan(interest, skill_level, budget)

    return {
        "similar_note": sim_note,
        "goals":    goals,
        "risks":    risks,
        "habits":   habits,
        "steps":    steps,
        "week_plan":  week_plan,
        "resources":  resources,
        "projects":   projects,
        "is_beginner": is_beginner,
        "budget": budget,
    }


def readiness_breakdown(info):
    g = float(info.get("gpa", 0))
    academics = 30 if g >= 8 else 26 if g >= 7 else 20 if g >= 6 else 14 if g >= 5 else 8
    lvl  = str(info.get("skill_level", "Beginner")).lower()
    sh   = int(info.get("study_hours", 0))
    base = 12 if "begin" in lvl else 22
    bonus = 8 if sh >= 5 else 6 if sh >= 4 else 3 if sh >= 3 else 1
    skills = clamp(base + bonus, 0, 30)
    sleep  = int(info.get("sleep_hours", 6))
    stress = info.get("stress_level", "Medium")
    conf   = info.get("confusion_level", "Medium")
    failures = int(info.get("failures", 0))
    routine = (
        (8 if sleep >= 7 else 5 if sleep >= 6 else 2) +
        (6 if stress == "Low" else 4 if stress == "Medium" else 2) +
        (6 if conf == "Low" else 4 if conf == "Medium" else 2) -
        min(failures, 4)
    )
    routine = clamp(routine, 0, 20)
    comm = str(info.get("communication", "Average"))
    communication = 20 if comm in ("Good", "High") else 14 if comm in ("Average", "Medium") else 8
    total = clamp(academics + skills + routine + communication, 0, 100)
    return {"Academics": academics, "Skills": skills, "Routine": routine, "Communication": communication, "Total": total}


def roadmap_to_markdown(name, info, roadmap):
    def s(x):
        try:
            if pd.isna(x): return ""
        except Exception: pass
        return str(x)
    lines = [
        f"# Personalised Roadmap for {s(name) or 'Student'}",
        f"**Generated:** {date.today().isoformat()}",
        f"**Level:** {'Beginner' if roadmap.get('is_beginner') else 'Intermediate'}",
        f"**Budget Mode:** {roadmap.get('budget','Low')}",
        "", "## Profile"
    ]
    for k in ["year", "branch", "interest", "skill_level", "budget", "hostel",
              "study_hours", "gpa", "sleep_hours", "failures",
              "stress_level", "confusion_level", "communication", "family_support"]:
        lines.append(f"- **{k.replace('_',' ').title()}**: {s(info.get(k))}")
    lines += ["", "## Data Insight", s(roadmap.get("similar_note", "")), "", "## Goals"]
    for g in roadmap.get("goals", []):
        lines.append(f"- {s(g)}")
    if roadmap.get("risks"):
        lines += ["", "## Risks & Warnings"]
        for r in roadmap["risks"]:
            lines.append(f"- ⚠️ {s(r)}")
    lines += ["", "## Daily Habits"]
    for h in roadmap.get("habits", []):
        lines.append(f"- {s(h)}")
    lines += ["", "## Action Steps"]
    for i, step in enumerate(roadmap.get("steps", []), 1):
        lines.append(f"{i}. {s(step)}")
    lines += ["", "## 4-Week Plan"]
    for w in roadmap.get("week_plan", []):
        lines += [f"### {s(w['title'])} [{w.get('level','')}]"]
        for b in w.get("bullets", []):
            lines.append(f"- {s(b)}")
        lines.append("")
    lines += ["## Suggested Projects"]
    for p in roadmap.get("projects", []):
        name_p, desc_p = (p[0], p[1]) if isinstance(p, (list, tuple)) and len(p) > 1 else (str(p), "")
        lines.append(f"- **{s(name_p)}**: {s(desc_p)}")
    lines += ["", "## Resources"]
    for r in roadmap.get("resources", []):
        lines.append(f"- {s(r)}")
    return "\n".join(lines)


def compute_skill_gap(required, known):
    have    = [s for s in required if s in known]
    missing = [s for s in required if s not in known]
    return have, missing


# ─────────────────────────────────────────────
# ROUTING
# ─────────────────────────────────────────────
if st.session_state.page == "home":
    show_landing_page()
    st.stop()

# ═══════════════════════════════════════════════
#  APP PAGE
# ═══════════════════════════════════════════════
@st.cache_data
def load_data():
    df = pd.read_csv("student_performance_final.csv")
    df.columns = df.columns.str.lower()
    if "hostel" in df.columns:
        df["hostel"] = df["hostel"].astype(str).str.strip().str.lower()
        df["hostel"] = df["hostel"].replace({
            "day scholar": "No", "dayscholar": "No",
            "hosteler": "Yes", "hosteller": "Yes"
        })
    df = df.dropna(subset=["year", "branch", "interest", "skill_level",
                            "budget_level", "stress_level",
                            "confusion_level", "communication_level"])
    df = df.reset_index(drop=True)
    return df

data = load_data()

# App header
st.markdown("""
<div class="app-header">
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div class="app-logo">🎯 Skill Roadmap</div>
    <div style="font-size:12px;color:#334155;">Personalised · 4 Weeks · Free Resources Available</div>
  </div>
</div>
""", unsafe_allow_html=True)

col_back, _ = st.columns([1, 8])
with col_back:
    if st.button("← Back"):
        st.session_state.page = "home"
        st.session_state.roadmap_data = None
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Interests from dataset
interests = sorted(data["interest"].dropna().unique().tolist())

# ── Profile Card ──
st.markdown("""
<div class="g-card">
  <div class="g-card-title">📋 Tell Us About Yourself</div>
  <div class="g-card-sub">Fill all sections — your roadmap, week plan, and resources are personalised based on every answer.</div>
</div>
""", unsafe_allow_html=True)

with st.form("profile_form"):

    # ── Section 1: Personal Info ──
    st.markdown("""
    <div class="form-section-header">
      <div class="form-section-icon">🧑</div>
      <div class="form-section-title">Personal Info</div>
      <div class="form-section-badge">Basic details</div>
    </div>
    """, unsafe_allow_html=True)
    pc1, pc2, pc3, pc4 = st.columns([2, 1, 1, 1])
    with pc1:
        name   = st.text_input("👤 Full Name", placeholder="e.g. Priya Sharma")
    with pc2:
        year   = st.selectbox("📅 Year", [1, 2, 3, 4])
    with pc3:
        branch = st.selectbox("🏛️ Branch", ["CSE", "ECE", "EEE", "IT", "Mechanical"])
    with pc4:
        hostel = st.selectbox("🏠 Hostel?", ["Yes", "No"])

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── Section 2: Academics ──
    st.markdown("""
    <div class="form-section-header">
      <div class="form-section-icon">📚</div>
      <div class="form-section-title">Academics & Routine</div>
      <div class="form-section-badge">Shapes your readiness score</div>
    </div>
    """, unsafe_allow_html=True)
    ac1, ac2, ac3, ac4 = st.columns(4)
    with ac1:
        gpa          = st.slider("🎓 Current GPA", 0.0, 10.0, 7.0, 0.1)
    with ac2:
        study_hours  = st.slider("📖 Study hrs / day", 0, 12, 3)
    with ac3:
        sleep_hours  = st.slider("😴 Sleep hrs / day", 4, 12, 7)
    with ac4:
        failures     = st.number_input("❌ Failures (backlogs)", min_value=0, max_value=10, value=0)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── Section 3: Wellbeing & Support ──
    st.markdown("""
    <div class="form-section-header">
      <div class="form-section-icon">💬</div>
      <div class="form-section-title">Wellbeing & Support</div>
      <div class="form-section-badge">Shapes your habits & risk flags</div>
    </div>
    """, unsafe_allow_html=True)
    wc1, wc2, wc3 = st.columns(3)
    with wc1:
        stress_level    = st.selectbox("😰 Stress Level",    ["Low", "Medium", "High"])
    with wc2:
        confusion_level = st.selectbox("🤔 Confusion Level", ["Low", "Medium", "High"])
    with wc3:
        family_support  = st.selectbox("👨‍👩‍👦 Family Support",  ["Low", "Medium", "High"])

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── Section 4: Skills & Preferences ──
    st.markdown("""
    <div class="form-section-header">
      <div class="form-section-icon">⚙️</div>
      <div class="form-section-title">Skills & Learning Preferences</div>
      <div class="form-section-badge">Drives your week plan & resources</div>
    </div>
    """, unsafe_allow_html=True)
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        interest     = st.selectbox("💡 Primary Interest", interests)
    with sc2:
        skill_level  = st.selectbox("🛠️ Skill Level", ["Beginner", "Intermediate"])
    with sc3:
        budget       = st.selectbox("💰 Budget Level", ["Low", "Medium", "High"])
    with sc4:
        communication = st.selectbox("🗣️ Communication", ["Poor", "Average", "Good"])

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍  Generate My Personalised Roadmap", use_container_width=True)

if submitted:
    st.session_state.student_name = name
    st.session_state.student_info = {
        "year": year, "branch": branch, "gpa": float(gpa),
        "study_hours": int(study_hours), "sleep_hours": int(sleep_hours),
        "failures": int(failures), "hostel": hostel,
        "family_support": family_support, "interest": interest,
        "budget": budget, "skill_level": skill_level,
        "stress_level": stress_level, "confusion_level": confusion_level,
        "communication": communication,
    }
    st.session_state.roadmap_data = generate_structured_roadmap(st.session_state.student_info, data)

# ─────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────
if st.session_state.roadmap_data is not None:
    roadmap = st.session_state.roadmap_data
    info    = st.session_state.student_info
    sname   = st.session_state.student_name
    is_beg  = roadmap.get("is_beginner", True)

    st.markdown("<br>", unsafe_allow_html=True)

    level_badge = '<span class="level-beginner">Beginner Track</span>' if is_beg else '<span class="level-intermediate">Intermediate Track</span>'
    budget_tag = "🆓 Free Resources" if roadmap.get("budget") == "Low" else "💳 Paid + Free Mix"
    st.markdown(
        f'<div style="text-align:center;font-family:Syne,sans-serif;font-size:22px;font-weight:800;'
        f'background:linear-gradient(135deg,#a5b4fc,#34d399);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:8px;">'
        f'✅ Roadmap Generated for {sname or "Student"}</div>'
        f'<div style="text-align:center;margin-bottom:24px;">{level_badge}&nbsp;&nbsp;'
        f'<span style="font-size:12px;color:#475569;">{budget_tag}</span></div>',
        unsafe_allow_html=True
    )

    score = readiness_breakdown(info)
    c1, c2, c3, c4, c5 = st.columns(5)
    tiles = [
        ("GPA", f"{info['gpa']:.1f}"),
        ("Study hrs/day", str(info["study_hours"])),
        ("Sleep hrs", str(info["sleep_hours"])),
        ("Readiness", f"{score['Total']}/100"),
        ("Skill Level", info["skill_level"]),
    ]
    for col, (label, val) in zip([c1, c2, c3, c4, c5], tiles):
        col.markdown(f'<div class="metric-tile"><div class="metric-val">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📊  Readiness Score Breakdown", expanded=True):
        col_score, col_bars = st.columns([1, 2])
        with col_score:
            score_color = "#34d399" if score["Total"] >= 70 else "#fbbf24" if score["Total"] >= 45 else "#fb7185"
            verdict = "🟢 Strong foundation!" if score["Total"] >= 70 else "🟡 Good start — keep building!" if score["Total"] >= 45 else "🔴 Need to build momentum"
            st.markdown(f'<div class="score-ring-wrap"><div class="score-big" style="-webkit-text-fill-color:{score_color}">{score["Total"]}</div><div class="score-label">out of 100</div><div style="font-size:13px;margin-top:8px;color:{score_color}">{verdict}</div></div>', unsafe_allow_html=True)
        with col_bars:
            bar_config = [
                ("Academics",     score["Academics"],     30, "linear-gradient(90deg,#6366f1,#818cf8)"),
                ("Skills",        score["Skills"],        30, "linear-gradient(90deg,#8b5cf6,#a78bfa)"),
                ("Routine",       score["Routine"],       20, "linear-gradient(90deg,#0ea5e9,#38bdf8)"),
                ("Communication", score["Communication"], 20, "linear-gradient(90deg,#34d399,#6ee7b7)"),
            ]
            for label, val, mx, grad in bar_config:
                pct = int(val / mx * 100)
                st.markdown(f"""
                <div class="score-bar-wrap">
                  <div class="score-bar-label">
                    <span style="color:#e2e8f0">{label}</span>
                    <span style="color:#6366f1">{val}/{mx}</span>
                  </div>
                  <div class="score-bar-track">
                    <div class="score-bar-fill" style="width:{pct}%;background:{grad}"></div>
                  </div>
                </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧭 Roadmap", "🗓️ 4-Week Plan", "🚀 Projects", "📚 Resources", "🧩 Skill Gap"])

    with tab1:
        st.markdown(f'<div style="background:rgba(99,102,241,0.10);border:1px solid rgba(99,102,241,0.28);border-radius:14px;padding:16px 20px;font-size:14px;color:#a5b4fc;margin-bottom:20px;">💡 {roadmap["similar_note"]}</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-pill">🎯 Goals</div>', unsafe_allow_html=True)
        for g in roadmap["goals"]:
            st.markdown(f'<div class="goal-item"><div class="goal-dot"></div><div class="goal-text">{g}</div></div>', unsafe_allow_html=True)
        if roadmap["risks"]:
            st.markdown('<br><div class="sec-pill" style="background:rgba(251,113,133,0.12);border-color:rgba(251,113,133,0.35);color:#fda4af;">⚠️ Risks to Watch</div>', unsafe_allow_html=True)
            for r in roadmap["risks"]:
                st.markdown(f'<div class="risk-item"><div class="risk-dot"></div><div class="goal-text">{r}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="sec-pill" style="background:rgba(56,189,248,0.12);border-color:rgba(56,189,248,0.35);color:#7dd3fc;">🧠 Daily Habits</div>', unsafe_allow_html=True)
        for h in roadmap["habits"]:
            st.markdown(f'<div class="habit-item"><div class="habit-dot"></div><div class="goal-text">{h}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="sec-pill">✅ Action Steps</div>', unsafe_allow_html=True)
        for i, step in enumerate(roadmap["steps"], 1):
            st.markdown(f'<div class="step-item"><div class="step-num">{i}</div><div class="goal-text">{step}</div></div>', unsafe_allow_html=True)

    with tab2:
        lv = roadmap["week_plan"][0].get("level", "Beginner") if roadmap["week_plan"] else "Beginner"
        lv_badge = f'<span class="level-{"beginner" if lv == "Beginner" else "intermediate"}">{lv} Track</span>'
        st.markdown(f'<p style="font-size:13px;color:#64748b;margin-bottom:16px;">Your week plan is tailored to {lv_badge} level. Each week builds on the previous.</p>', unsafe_allow_html=True)
        for w in roadmap["week_plan"]:
            bullets_html = "".join(f'<div class="week-bullet">{b}</div>' for b in w["bullets"])
            st.markdown(f'<div class="week-card"><div class="week-title">{w["title"]}</div>{bullets_html}</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="sec-pill">🚀 Suggested Projects</div>', unsafe_allow_html=True)
        icons = ["🔵", "🟣", "🟡", "🟢", "🔴"]
        for i, p in enumerate(roadmap["projects"]):
            p_name = p[0] if isinstance(p, (list, tuple)) else str(p)
            p_desc = p[1] if isinstance(p, (list, tuple)) and len(p) > 1 else ""
            st.markdown(f'<div class="proj-card"><div class="proj-icon">{icons[i % len(icons)]}</div><div><div class="proj-name">{p_name}</div><div class="proj-desc">{p_desc}</div></div></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:12px;color:#475569;margin-top:12px;">💡 Tip: Add screenshots + README + clear results to GitHub. That makes your project look strong in interviews.</p>', unsafe_allow_html=True)

    with tab4:
        budget_note = "🆓 Showing <strong>free resources only</strong> based on your Low budget setting." if roadmap.get("budget") == "Low" else "💳 Showing <strong>paid + free resources</strong> based on your budget setting."
        st.markdown(f'<div style="background:rgba(52,211,153,0.08);border:1px solid rgba(52,211,153,0.22);border-radius:12px;padding:12px 18px;font-size:13px;color:#6ee7b7;margin-bottom:16px;">{budget_note}</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-pill">📚 Recommended Resources</div>', unsafe_allow_html=True)
        res_icons = ["🎥", "📖", "🌐"]
        for i, r in enumerate(roadmap["resources"]):
            tag = "Free" if "free" in str(r).lower() or budget == "Low" else "Paid"
            tag_color = "#34d399" if tag == "Free" else "#fbbf24"
            st.markdown(f'<div class="res-card"><div class="res-icon">{res_icons[i % len(res_icons)]}</div><div><div class="res-name">{r}</div><div class="res-tag" style="color:{tag_color}">{tag}</div></div></div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="sec-pill">🧩 Skill Gap Analysis</div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px;color:#64748b;margin-bottom:20px;">Select a job role, then tick the skills you already have — see your match % and exact skills to learn next.</p>', unsafe_allow_html=True)
        job_roles  = ["— Select a role —"] + list(JOB_SKILL_ANALYSIS.keys())
        job_choice = st.selectbox("🎯 Target Job Role", job_roles, key="sg_role_tab")
        if job_choice != "— Select a role —":
            job_info = JOB_SKILL_ANALYSIS[job_choice]
            col_left, col_right = st.columns([1, 1])
            with col_left:
                st.markdown('<div class="sec-pill">🧠 Required Skills</div>', unsafe_allow_html=True)
                for sk in job_info["skills"]:
                    st.markdown(f'<div style="background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.22);border-radius:10px;padding:8px 14px;margin-bottom:6px;font-size:13px;color:#c7d2fe;">• {sk}</div>', unsafe_allow_html=True)
            with col_right:
                st.markdown('<div class="sec-pill">🧪 Sample Projects</div>', unsafe_allow_html=True)
                for p in job_info["projects"]:
                    st.markdown(f'<div class="proj-card" style="margin-bottom:6px;"><div class="proj-name" style="color:#fcd34d;">{p}</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="sec-pill">✅ Mark Skills You Already Know</div>', unsafe_allow_html=True)
            known_skills = st.multiselect("Select skills you already have:", options=job_info["skills"], key="sg_known_tab")
            have, missing = compute_skill_gap(job_info["skills"], known_skills)
            pct = int(len(have) / len(job_info["skills"]) * 100) if job_info["skills"] else 0
            st.markdown("<br>", unsafe_allow_html=True)
            bar_color = "#34d399" if pct >= 70 else "#fbbf24" if pct >= 40 else "#fb7185"
            st.markdown(f"""
            <div style="margin-bottom:8px;">
              <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;">
                <span style="color:#e2e8f0;font-weight:700;">📊 Skill Match</span>
                <span style="color:{bar_color};font-weight:800;">{pct}%</span>
              </div>
              <div style="height:12px;border-radius:999px;background:rgba(255,255,255,0.08);overflow:hidden;">
                <div style="height:100%;width:{pct}%;background:{bar_color};border-radius:999px;transition:width 0.5s ease;"></div>
              </div>
              <div style="font-size:12px;color:#475569;margin-top:6px;">
                {"🟢 Strong match — ready to apply!" if pct >= 70 else "🟡 Getting there — keep building!" if pct >= 40 else "🔴 Start learning — you've got this!"}
              </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            col_h, col_m = st.columns(2)
            with col_h:
                st.markdown('<div class="sec-pill" style="background:rgba(52,211,153,0.12);border-color:rgba(52,211,153,0.35);color:#6ee7b7;">✅ Skills You Have</div>', unsafe_allow_html=True)
                if have:
                    for sk in have:
                        st.markdown(f'<div class="skill-have">✅ {sk}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="font-size:13px;color:#475569;">Select skills you know above.</p>', unsafe_allow_html=True)
            with col_m:
                st.markdown('<div class="sec-pill" style="background:rgba(251,113,133,0.12);border-color:rgba(251,113,133,0.35);color:#fda4af;">🔴 Skills to Learn</div>', unsafe_allow_html=True)
                if missing:
                    for sk in missing:
                        st.markdown(f'<div class="skill-need">🔴 {sk}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="background:rgba(52,211,153,0.10);border:1px solid rgba(52,211,153,0.30);border-radius:12px;padding:14px;font-size:14px;color:#6ee7b7;font-weight:700;">🎉 You have all required skills!</div>', unsafe_allow_html=True)
            if missing:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="sec-pill">🛣️ Recommended Learning Order</div>', unsafe_allow_html=True)
                for i, sk in enumerate(missing, 1):
                    st.markdown(f'<div class="learn-step"><div class="learn-step-num">{i}</div><div class="learn-step-text">Learn <strong style="color:#e2e8f0">{sk}</strong></div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="sec-pill">📚 Resources for this Role</div>', unsafe_allow_html=True)
            for r in job_info["resources"]:
                st.markdown(f'<div class="res-card"><div class="res-icon">📌</div><div class="res-name">{r}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    md = roadmap_to_markdown(sname, info, roadmap)
    st.download_button(
        label="⬇️  Download Full Roadmap (Markdown)",
        data=md.encode("utf-8"),
        file_name=f"roadmap_{(sname or 'student').replace(' ', '_').lower()}.md",
        mime="text/markdown",
        use_container_width=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📊  Sample Student Dataset (Preview)"):
    st.dataframe(data, use_container_width=True)

st.markdown('<p style="text-align:center;font-size:11px;color:#1e293b;margin-top:32px;">Student Skill Roadmap · Streamlit</p>', unsafe_allow_html=True)

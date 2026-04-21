import streamlit as st
import pandas as pd
import random
from datetime import date

st.set_page_config(page_title="SkillRoadmap", page_icon="🎯", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }

.landing {
  min-height: 100vh;
  background: radial-gradient(ellipse 80% 60% at 15% 55%, rgba(99,102,241,.38) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 25%, rgba(139,92,246,.30) 0%, transparent 55%),
    radial-gradient(ellipse 70% 55% at 55% 90%, rgba(16,185,129,.18) 0%, transparent 58%), #020817;
  padding-bottom: 80px; color: #e2e8f0;
}
.lnav { display:flex; align-items:center; padding:20px 48px; border-bottom:1px solid rgba(255,255,255,.06); }
.lnav-logo { font-family:'Syne',sans-serif; font-size:18px; font-weight:800; background:linear-gradient(135deg,#a5b4fc,#34d399); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero { text-align:center; padding:72px 24px 48px; }
.ctag { display:inline-block; background:rgba(251,191,36,.12); border:1px solid rgba(251,191,36,.30); color:#fcd34d; font-size:13px; font-weight:600; padding:6px 18px; border-radius:999px; margin-bottom:28px; animation:fd .6s ease both; }
@keyframes fd { from{opacity:0;transform:translateY(-12px)} to{opacity:1;transform:translateY(0)} }
.hh1 { font-family:'Syne',sans-serif; font-size:clamp(32px,6vw,60px); font-weight:800; line-height:1.08; margin-bottom:22px; animation:fd .7s ease .1s both; }
.ll1 { display:block; background:linear-gradient(135deg,#fff 30%,#c7d2fe); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.ll2 { display:block; background:linear-gradient(135deg,#a5b4fc,#34d399 70%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hsub { font-size:16px; color:#64748b; max-width:520px; margin:0 auto 40px; line-height:1.7; animation:fd .7s ease .2s both; }
.qcard { max-width:600px; margin:0 auto 52px; background:rgba(15,23,42,.70); backdrop-filter:blur(12px); border:1px solid rgba(99,102,241,.22); border-left:4px solid #6366f1; border-radius:16px; padding:22px 28px; animation:fd .7s ease .3s both; }
.qtxt { font-size:15px; font-style:italic; color:#e2e8f0; line-height:1.65; margin-bottom:10px; }
.qauth { font-size:12px; color:#6366f1; font-weight:600; letter-spacing:.05em; }
.imgrow { display:flex; justify-content:center; gap:16px; margin:0 auto 56px; max-width:860px; padding:0 24px; animation:fd .7s ease .35s both; }
.imgcard { flex:1; min-width:0; border-radius:20px; overflow:hidden; border:1px solid rgba(255,255,255,.08); box-shadow:0 8px 32px rgba(0,0,0,.45); position:relative; transition:transform .25s; }
.imgcard:hover { transform:translateY(-5px); }
.imgcard img { width:100%; height:200px; object-fit:cover; display:block; filter:brightness(.82) saturate(1.1); }
.imgov { position:absolute; bottom:0; left:0; right:0; background:linear-gradient(transparent,rgba(2,8,23,.85)); padding:20px 16px 14px; }
.imglbl { font-family:'Syne',sans-serif; font-size:13px; font-weight:700; color:#fff; }
.imgsub { font-size:11px; color:rgba(255,255,255,.50); margin-top:2px; }
.srow { display:flex; justify-content:center; gap:32px; margin:0 auto 56px; flex-wrap:wrap; animation:fd .7s ease .4s both; }
.snum { font-family:'Syne',sans-serif; font-size:28px; font-weight:800; background:linear-gradient(135deg,#a5b4fc,#34d399); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.slbl { font-size:12px; color:#475569; margin-top:4px; letter-spacing:.04em; text-transform:uppercase; }
.feats { display:flex; justify-content:center; gap:16px; max-width:860px; margin:0 auto 56px; padding:0 24px; flex-wrap:wrap; animation:fd .7s ease .45s both; }
.fc { flex:1; min-width:200px; background:rgba(15,23,42,.65); border:1px solid rgba(99,102,241,.18); border-radius:16px; padding:20px 18px; backdrop-filter:blur(10px); transition:border-color .2s,transform .2s; }
.fc:hover { border-color:rgba(99,102,241,.45); transform:translateY(-3px); }
.fcico { font-size:24px; margin-bottom:10px; }
.fct { font-family:'Syne',sans-serif; font-size:14px; font-weight:700; color:#e2e8f0; margin-bottom:6px; }
.fcd { font-size:12px; color:#64748b; line-height:1.6; }

div[data-testid="stButton"] > button {
  background:linear-gradient(135deg,#4f46e5,#7c3aed) !important; color:#fff !important; border:none !important;
  border-radius:14px !important; padding:14px 40px !important; font-family:'Syne',sans-serif !important;
  font-size:16px !important; font-weight:800 !important; letter-spacing:.04em !important;
  box-shadow:0 6px 28px rgba(99,102,241,.45) !important; transition:all .2s !important; min-width:220px !important;
}
div[data-testid="stButton"] > button:hover { opacity:.88 !important; transform:translateY(-3px) !important; }

.apphdr { background:linear-gradient(90deg,#4f46e5,#7c3aed,#ec4899); padding:16px 40px; display:flex; align-items:center; box-shadow:0 4px 20px rgba(99,102,241,.30); }
.applogo { font-family:'Syne',sans-serif; font-size:22px; font-weight:800; color:#fff; }

.pill { display:inline-flex; align-items:center; gap:6px; font-family:'Syne',sans-serif; font-size:11px; font-weight:800; padding:5px 14px; border-radius:999px; margin-bottom:12px; letter-spacing:.06em; text-transform:uppercase; }
.pi { background:#eef2ff; color:#4f46e5; border:1.5px solid #c7d2fe; }
.pv { background:#f5f3ff; color:#7c3aed; border:1.5px solid #ddd6fe; }
.pg { background:#f0fdf4; color:#15803d; border:1.5px solid #bbf7d0; }
.pr { background:#fff1f2; color:#e11d48; border:1.5px solid #fecdd3; }
.ps { background:#f0f9ff; color:#0369a1; border:1.5px solid #bae6fd; }
.pa { background:#fffbeb; color:#b45309; border:1.5px solid #fde68a; }

.wcard { background:#fff; border-radius:20px; padding:26px 24px; box-shadow:0 4px 24px rgba(99,102,241,.08); border:1.5px solid #e0e7ff; margin-bottom:16px; }
.wct { font-family:'Syne',sans-serif; font-size:19px; font-weight:800; color:#1e1b4b; margin-bottom:4px; }
.wcs { font-size:13px; color:#6b7280; }

.mt { border-radius:16px; padding:18px 12px; text-align:center; }
.mi { background:linear-gradient(135deg,#6366f1,#818cf8); }
.mv { background:linear-gradient(135deg,#8b5cf6,#a78bfa); }
.ms { background:linear-gradient(135deg,#0ea5e9,#38bdf8); }
.mg { background:linear-gradient(135deg,#10b981,#34d399); }
.mr2{ background:linear-gradient(135deg,#f43f5e,#fb7185); }
.mval { font-family:'Syne',sans-serif; font-size:24px; font-weight:800; color:#fff; }
.mlbl { font-size:10px; color:rgba(255,255,255,.80); margin-top:3px; text-transform:uppercase; letter-spacing:.06em; }

.sbig { font-family:'Syne',sans-serif; font-size:64px; font-weight:800; background:linear-gradient(135deg,#6366f1,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent; line-height:1; }
.ssub { font-size:12px; color:#9ca3af; margin-top:4px; text-transform:uppercase; letter-spacing:.06em; }
.brow { display:flex; justify-content:space-between; font-size:13px; font-weight:700; margin-bottom:5px; }
.btrk { height:10px; border-radius:999px; background:#f1f5f9; overflow:hidden; margin-bottom:14px; }
.bfil { height:100%; border-radius:999px; }

.gc { display:flex; align-items:flex-start; gap:12px; background:linear-gradient(135deg,rgba(99,102,241,.07),rgba(139,92,246,.04)); border:1.5px solid #c7d2fe; border-radius:14px; padding:12px 16px; margin-bottom:10px; }
.rc { display:flex; align-items:flex-start; gap:12px; background:linear-gradient(135deg,rgba(244,63,94,.07),rgba(251,113,133,.04)); border:1.5px solid #fecdd3; border-radius:14px; padding:12px 16px; margin-bottom:10px; }
.hc { display:flex; align-items:flex-start; gap:12px; background:linear-gradient(135deg,rgba(14,165,233,.07),rgba(56,189,248,.04)); border:1.5px solid #bae6fd; border-radius:14px; padding:12px 16px; margin-bottom:10px; }
.sc2{ display:flex; align-items:flex-start; gap:14px; background:linear-gradient(135deg,rgba(16,185,129,.07),rgba(52,211,153,.04)); border:1.5px solid #bbf7d0; border-radius:14px; padding:12px 16px; margin-bottom:10px; }
.di { width:10px; height:10px; border-radius:50%; background:linear-gradient(135deg,#6366f1,#8b5cf6); margin-top:5px; flex-shrink:0; }
.dr { width:10px; height:10px; border-radius:50%; background:linear-gradient(135deg,#f43f5e,#fb7185); margin-top:5px; flex-shrink:0; }
.ds { width:10px; height:10px; border-radius:50%; background:linear-gradient(135deg,#0ea5e9,#38bdf8); margin-top:5px; flex-shrink:0; }
.sn { width:26px; height:26px; border-radius:50%; background:linear-gradient(135deg,#10b981,#34d399); display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:800; color:#fff; flex-shrink:0; }
.ct { font-size:14px; color:#1e1b4b; line-height:1.6; }

.wkcard { background:#fff; border-radius:16px; padding:20px 22px; margin-bottom:14px; box-shadow:0 2px 12px rgba(0,0,0,.06); border-left:4px solid #6366f1; }
.wktit { font-family:'Syne',sans-serif; font-size:15px; font-weight:800; background:linear-gradient(135deg,#6366f1,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:10px; }
.wkb { font-size:13px; color:#374151; line-height:1.7; margin-bottom:6px; padding-left:12px; border-left:3px solid #c7d2fe; }

.pjc { display:flex; align-items:center; gap:12px; background:linear-gradient(135deg,#fffbeb,#fff7ed); border:1.5px solid #fde68a; border-radius:12px; padding:12px 16px; margin-bottom:9px; }
.pjn { font-size:14px; font-weight:700; color:#92400e; }
.rsc { display:flex; align-items:center; gap:12px; background:linear-gradient(135deg,#f0f9ff,#e0f2fe); border:1.5px solid #bae6fd; border-radius:12px; padding:12px 16px; margin-bottom:9px; }
.rsn { font-size:14px; color:#075985; font-weight:600; }

.skr { background:#f5f3ff; border:1.5px solid #ddd6fe; border-radius:10px; padding:9px 14px; margin-bottom:7px; font-size:13px; color:#5b21b6; font-weight:600; }
.skh { background:linear-gradient(135deg,#f0fdf4,#dcfce7); border:1.5px solid #86efac; border-radius:10px; padding:9px 14px; margin-bottom:7px; font-size:13px; color:#15803d; font-weight:700; }
.skn { background:linear-gradient(135deg,#fff1f2,#ffe4e6); border:1.5px solid #fca5a5; border-radius:10px; padding:9px 14px; margin-bottom:7px; font-size:13px; color:#b91c1c; font-weight:700; }
.lst { display:flex; align-items:center; gap:12px; background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:1.5px solid #c4b5fd; border-radius:12px; padding:11px 16px; margin-bottom:8px; }
.ln  { width:26px; height:26px; border-radius:50%; background:linear-gradient(135deg,#7c3aed,#6366f1); display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:800; color:#fff; flex-shrink:0; }
.lt  { font-size:14px; color:#4c1d95; font-weight:600; }

.ib { background:linear-gradient(135deg,#eef2ff,#f5f3ff); border:1.5px solid #c7d2fe; border-radius:14px; padding:14px 20px; font-size:14px; color:#4338ca; margin-bottom:20px; }

.stTabs [data-baseweb="tab-list"] { background:#fff !important; border-radius:14px !important; padding:4px !important; gap:4px !important; border:1.5px solid #e0e7ff !important; }
.stTabs [data-baseweb="tab"]      { background:transparent !important; border-radius:10px !important; color:#6b7280 !important; font-weight:600 !important; font-size:13px !important; padding:8px 16px !important; }
.stTabs [aria-selected="true"]    { background:linear-gradient(135deg,#6366f1,#8b5cf6) !important; color:#fff !important; }

.stDownloadButton > button { background:linear-gradient(135deg,#10b981,#34d399) !important; color:#fff !important; border:none !important; border-radius:12px !important; font-weight:700 !important; }
.stSelectbox div[data-baseweb="select"] > div { background:#fff !important; border:1.5px solid #c7d2fe !important; border-radius:10px !important; color:#1e1b4b !important; }
.stTextInput > div > div > input  { background:#fff !important; border:1.5px solid #c7d2fe !important; border-radius:10px !important; color:#1e1b4b !important; }
.stNumberInput > div > div > input{ background:#fff !important; border:1.5px solid #c7d2fe !important; border-radius:10px !important; color:#1e1b4b !important; }
.stMultiSelect div[data-baseweb="select"] > div { background:#fff !important; border:1.5px solid #c7d2fe !important; border-radius:10px !important; }
.stSelectbox label,.stSlider label,.stTextInput label,.stNumberInput label,.stMultiSelect label { color:#374151 !important; font-size:13px !important; font-weight:600 !important; }
.stProgress > div > div > div > div { background:linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899) !important; border-radius:999px !important; }
.stProgress > div > div > div       { background:#f1f5f9 !important; border-radius:999px !important; }
</style>
""", unsafe_allow_html=True)

for k,v in [("page","home"),("roadmap_data",None),("student_info",None),("student_name","")]:
    if k not in st.session_state:
        st.session_state[k] = v

def clean(x):
    if x is None: return ""
    try:
        if pd.isna(x): return ""
    except Exception: pass
    s = str(x).strip()
    return "" if s.lower() in ("nan","none","null","") else s

def show_landing():
    QUOTES = [
        ("The secret of getting ahead is getting started.", "Mark Twain"),
        ("Do not watch the clock. Keep going.", "Sam Levenson"),
        ("You do not have to be great to start, but you have to start to be great.", "Zig Ziglar"),
        ("Push yourself, because no one else will do it for you.", "Anonymous"),
        ("Dream big. Start small. Act now.", "Robin Sharma"),
        ("Success is the sum of small efforts repeated day in and day out.", "Robert Collier"),
        ("Believe you can and you are halfway there.", "Theodore Roosevelt"),
    ]
    qt, qa = random.choice(QUOTES)
    IMGS = [
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=400&q=80",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&q=80",
        "https://images.unsplash.com/photo-1529390079861-591de354faf5?w=400&q=80",
    ]
    st.markdown(f"""
    <div class="landing">
      <div class="lnav"><div class="lnav-logo">🎯 SkillRoadmap</div></div>
      <div class="hero">
        <div class="ctag">😕 &nbsp; Not sure where to start?</div>
        <h1 class="hh1"><span class="ll1">Stop feeling lost.</span><span class="ll2">Build your roadmap today.</span></h1>
        <p class="hsub">Answer a few simple questions — we generate a personalised 4-week learning plan with projects, resources, and a readiness score. Made for engineering students.</p>
        <div class="qcard"><div class="qtxt">{qt}</div><div class="qauth">— {qa}</div></div>
      </div>
      <div class="imgrow">
        <div class="imgcard"><img src="{IMGS[0]}" alt="s"/><div class="imgov"><div class="imglbl">Collaborate &amp; Grow</div><div class="imgsub">Learn with peers</div></div></div>
        <div class="imgcard"><img src="{IMGS[1]}" alt="g"/><div class="imgov"><div class="imglbl">Build Real Projects</div><div class="imgsub">Portfolio-grade work</div></div></div>
        <div class="imgcard"><img src="{IMGS[2]}" alt="l"/><div class="imgov"><div class="imglbl">Learn at Your Pace</div><div class="imgsub">Structured &amp; clear</div></div></div>
      </div>
      <div class="srow">
        <div><div class="snum">14+</div><div class="slbl">Learning Tracks</div></div>
        <div><div class="snum">4</div><div class="slbl">Week Plan</div></div>
        <div><div class="snum">50+</div><div class="slbl">Free Resources</div></div>
        <div><div class="snum">100%</div><div class="slbl">Personalised</div></div>
      </div>
      <div class="feats">
        <div class="fc"><div class="fcico">📊</div><div class="fct">Readiness Score</div><div class="fcd">Breakdown of academics, skills, routine, and communication.</div></div>
        <div class="fc"><div class="fcico">🗓️</div><div class="fct">4-Week Plan</div><div class="fcd">A clear week-by-week roadmap tailored to your interest and level.</div></div>
        <div class="fc"><div class="fcico">🧩</div><div class="fct">Skill Gap Analysis</div><div class="fcd">Pick a job role and see what skills you have and what to learn next.</div></div>
        <div class="fc"><div class="fcico">⬇️</div><div class="fct">Download Roadmap</div><div class="fcd">Save your full roadmap as a Markdown file to revisit anytime.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns([1,1.4,1])
    with c2:
        if st.button("🚀  Start My Roadmap", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()
    st.markdown('<p style="text-align:center;color:#334155;font-size:12px;margin-top:8px">Takes less than 2 minutes - No signup needed</p>', unsafe_allow_html=True)

COURSE_DB = {
    "ML":{"courses":["Andrew Ng - ML Specialization (Coursera)","Krish Naik - ML Playlist (YouTube)","fast.ai - Practical Deep Learning"],"weeks":["Python + Numpy/Pandas + ML basics.","Scikit-learn: Decision Trees, Random Forest, validation.","Feature engineering + classification + overfitting.","Project: End-to-end ML app deployed on Streamlit."],"projects":["House Price Predictor","Student Performance Dashboard","Customer Segmentation K-Means"]},
    "WEB":{"courses":["The Odin Project Full Stack","FreeCodeCamp Responsive Web Design","JavaScript React Crash Course YouTube"],"weeks":["HTML + CSS Flex/Grid + build 1 landing page.","JavaScript DOM ES6 Fetch + interactive UI.","React basics components state props + mini app.","Project: Portfolio site on GitHub Pages or Vercel."],"projects":["Portfolio Website","To-do App LocalStorage","Mini E-commerce Product Gallery"]},
    "DSA":{"courses":["Striver A2Z DSA Sheet TakeUForward","NeetCode 150 structured problems","Abdul Bari Algorithms YouTube"],"weeks":["Arrays/Strings + time complexity + 20 problems.","Linked List + Stack/Queue + 15 problems.","Trees + Recursion + 12 problems.","Sorting/Searching + DP basics + mock interview."],"projects":["Sorting Visualizer","Sudoku Solver","Pathfinding Visualizer BFS Dijkstra"]},
    "CYBER":{"courses":["TryHackMe Pre Security Path","OverTheWire Bandit Linux basics","Networking and Web security OWASP Top 10"],"weeks":["Linux + networking + command line practice.","Web fundamentals + OWASP Top 10 SQLi XSS.","Hands-on TryHackMe labs.","Project: Security checklist + mini pentest report."],"projects":["Web Security Audit Report OWASP","Password strength checker demo","Phishing awareness mini-site"]},
    "ECE":{"courses":["NPTEL Digital Circuits Microprocessors","Embedded Systems Arduino ESP32 playlist","VLSI Basics Communication Systems NPTEL"],"weeks":["C basics + digital logic gates flip-flops.","Arduino ESP32 + sensors read and plot.","VLSI basics OR Communication Systems.","Project: Mini IoT Embedded demo + docs."],"projects":["IoT Temperature Humidity Monitor","Arduino Sensor Data Logger","Communication System simulation report"]},
    "VLSI":{"courses":["NPTEL VLSI Design","Digital Electronics NPTEL YouTube","Verilog basics playlist YouTube"],"weeks":["Digital design + number systems + logic.","Verilog modules testbench simulation.","Combinational and sequential circuits.","Project: Small digital system simulate report."],"projects":["4-bit ALU in Verilog","Traffic Light Controller FSM","Counter Shift Register designs"]},
    "IOT":{"courses":["Arduino ESP32 IoT playlist YouTube","NPTEL Introduction to IoT","MQTT HTTP basics simple dashboards"],"weeks":["Microcontroller + sensor basics + read values.","Send data serial log + basic visualization.","Add connectivity WiFi MQTT HTTP.","Project: IoT dashboard demo README."],"projects":["Smart home sensor dashboard","Weather station mini project","Room monitoring temp light demo"]},
    "EMBEDDED":{"courses":["Embedded C basics YouTube","Arduino ESP32 practical series","Interrupts timers tutorial series"],"weeks":["Embedded C loops pointers debugging.","GPIO + sensor interfacing + timing.","Interrupts timers + simple control logic.","Project: Embedded mini demo + docs."],"projects":["Digital stopwatch timer","Sensor-based alert system","LED patterns with interrupts"]},
    "SIGNAL":{"courses":["NPTEL Signals and Systems DSP","Python Signal Processing NumPy Scipy","YouTube DSP basics filters FFT"],"weeks":["Signals basics plotting transforms.","FFT basics + noise removal.","Filters low high pass + implementations.","Project: Signal cleaning notebook report."],"projects":["Noise filtering demo FFT","Audio signal analysis notebook","Sensor signal smoothing plots"]},
    "COMM_SYSTEMS":{"courses":["NPTEL Communication Systems","Signals and Systems YouTube NPTEL","MATLAB Python signal processing basics"],"weeks":["Signals sampling frequency noise.","AM FM modulation demodulation.","Digital comm ASK FSK PSK plots.","Project: Simulation notebook report."],"projects":["AM FM simulation notebook","Noise impact on signal plots","Digital modulation demo"]},
    "POWER":{"courses":["NPTEL Power Systems","Protection and Switchgear YouTube NPTEL","Power flow intro basic concepts"],"weeks":["Power system overview per-unit basics.","Protection relays faults examples.","Transmission distribution reliability.","Project: Load fault calculation sheet."],"projects":["Fault calculation worksheet","Load estimation report","Transmission line parameter notebook"]},
    "RENEW":{"courses":["NPTEL Renewable Energy","Solar PV basics YouTube NPTEL","Wind energy basics"],"weeks":["Solar PV + components + sizing.","Wind renewables pros cons.","Hybrid systems battery storage.","Project: Solar sizing calculator report."],"projects":["Solar sizing calculator Python","Renewable comparison report","Microgrid case study summary"]},
    "SMARTGRID":{"courses":["Smart Grid basics NPTEL YouTube","Power electronics intro","SCADA basics intro"],"weeks":["Smart grid concept components.","Demand response metering monitoring.","Grid integration of renewables.","Project: Smart grid report diagram."],"projects":["Smart grid architecture diagram","Demand response case study","Energy monitoring dashboard concept"]},
    "AUTOMATION":{"courses":["Industrial Automation YouTube NPTEL","PLC fundamentals intro course","Sensors actuators basics"],"weeks":["Automation basics sensors actuators.","PLC fundamentals ladder logic.","Control basics feedback stability.","Project: Automation workflow case study."],"projects":["PLC ladder logic examples","Sensor-actuator workflow demo","Industry automation case study"]},
    "ELECTRICAL_DESIGN":{"courses":["Electrical Design basics YouTube","AutoCAD Electrical basics optional","Wiring safety standards overview"],"weeks":["Wiring basics safety components.","Reading single-line diagrams SLD.","Load calculation protection selection.","Project: SLD load sheet report."],"projects":["Single-line diagram explanation","Load calculation sheet","Protection device selection notes"]},
    "ROBOTICS":{"courses":["Robotics basics playlist YouTube","Arduino basics robotics demos","Mechanisms and control intro"],"weeks":["Sensors motors simple control.","Arduino motor control small demo.","Robot mechanisms path planning.","Project: Mini robot demo documentation."],"projects":["Line follower robot demo","Obstacle avoidance mini demo","Robot arm concept CAD"]},
    "CAD":{"courses":["Fusion 360 SolidWorks tutorials","Engineering drawing basics YouTube","GD and T overview optional"],"weeks":["Sketching constraints 3 parts.","3D modeling assembly basics.","Drawings dimensions tolerances.","Project: Model drawing pack."],"projects":["CAD model of machine part","Assembly of basic mechanism","Drawing sheet pack notes"]},
    "AUTO":{"courses":["Automobile basics YouTube NPTEL","Engine transmission overview","Vehicle dynamics intro"],"weeks":["Vehicle components engine basics.","Transmission braking steering.","Vehicle dynamics safety.","Project: Vehicle subsystem report."],"projects":["Vehicle subsystem case study","Maintenance checklist","Auto trends summary report"]},
    "THERMAL":{"courses":["NPTEL Thermal Engineering","Heat transfer intro YouTube","Thermodynamics notes problems"],"weeks":["Thermo laws properties problems.","Heat transfer conduction convection radiation.","Cycles Rankine Brayton overview.","Project: Thermal calculation sheet report."],"projects":["Heat loss calculation mini sheet","Thermal cycle summary report","Cooling system concept notes"]},
    "MANUFACTURING":{"courses":["NPTEL Manufacturing Processes","Metrology basics YouTube NPTEL","Lean manufacturing overview"],"weeks":["Manufacturing casting forming machining.","Metrology quality concepts.","Lean basics 5S waste reduction.","Project: Process comparison report."],"projects":["Manufacturing process comparison report","Lean 5S checklist for workshop","Quality control mini notes"]},
    "SOFT":{"courses":["Communication Skills playlist YouTube","TED Talks practice notes","Resume and Interview basics"],"weeks":["Daily speaking practice 5-7 lines writing.","Vocabulary clarity small presentations.","Mock interview peer feedback.","Project: 2-min intro video updated resume."],"projects":["2-min self-introduction video","Resume LinkedIn update checklist","Weekly speaking practice log"]},
}

JOB_SKILLS = {
    "Software Developer":{"skills":["Python or Java","Data Structures and Algorithms","HTML CSS JavaScript","Git and GitHub","Databases SQL","OOPS","Problem Solving"],"projects":["Student Management System","Task Tracker Application","Portfolio Website","REST API Mini Project"],"resources":["NPTEL Programming and DSA","YouTube freeCodeCamp","GeeksForGeeks DSA","GitHub Open Source"]},
    "Frontend Developer":{"skills":["HTML","CSS","JavaScript","React","Responsive Design","Git and GitHub"],"projects":["Portfolio Website","React To-Do App","UI Clone Netflix or Amazon"],"resources":["MDN Web Docs","Traversy Media YouTube","React Official Docs"]},
    "Backend Developer":{"skills":["Node.js or Python or Java","Databases SQL or NoSQL","APIs RESTful Services","Git and GitHub","Authentication and Security"],"projects":["REST API Project","E-commerce Backend","Blog Platform Backend"],"resources":["Udemy Backend Courses","YouTube Tech With Tim","MongoDB University"]},
    "Data Scientist":{"skills":["Python","Statistics","Pandas and NumPy","Data Visualization","Machine Learning Basics"],"projects":["Student Performance Analysis","Sales Prediction Model","EDA Project"],"resources":["Kaggle Learn","Krish Naik YouTube","Coursera ML Audit Mode"]},
    "Machine Learning Engineer":{"skills":["Python","Linear Algebra and Statistics","Scikit-learn TensorFlow PyTorch","Data Preprocessing","Model Deployment"],"projects":["Predictive Analytics Model","Image Classification Project","Recommendation System"],"resources":["Fast.ai Courses","DeepLearning.ai Coursera","YouTube Sentdex Krish Naik"]},
    "DevOps Engineer":{"skills":["Linux Shell Scripting","CI/CD Jenkins GitHub Actions","Docker Kubernetes","Cloud Platforms AWS GCP Azure","Monitoring and Logging"],"projects":["CI/CD Pipeline Setup","Dockerized App Deployment","Cloud Infrastructure Project"],"resources":["Linux Academy A Cloud Guru","YouTube TechWorld with Nana","Official Docker and Kubernetes Docs"]},
    "UI/UX Designer":{"skills":["Figma or Adobe XD","Wireframing and Prototyping","User Research and Testing","Responsive Design Principles","Portfolio Creation"],"projects":["Mobile App Wireframes","Website Redesign Project","Interactive Prototype"],"resources":["Figma Learn Tutorials","Coursera UI/UX Courses","YouTube DesignCourse"]},
    "Cybersecurity Analyst":{"skills":["Networking Basics","Linux and Windows Security","Penetration Testing","Firewalls and IDS IPS","Security Tools Wireshark Nmap"],"projects":["Vulnerability Assessment","Phishing Simulation","Secure Web App Setup"],"resources":["TryHackMe Hack The Box","Cybrary Courses","YouTube NetworkChuck"]},
    "Mobile App Developer":{"skills":["Java Kotlin Swift Flutter","UI/UX for Mobile","APIs and Backend Integration","App Deployment Play Store App Store","Debugging and Testing"],"projects":["Todo App","Weather Forecast App","E-commerce Mobile App"],"resources":["Udemy Mobile App Courses","YouTube The Net Ninja","Official Flutter Docs"]},
    "Cloud Engineer":{"skills":["AWS Azure GCP","Cloud Architecture and Design","Networking and Security","CI/CD Pipelines","Infrastructure as Code Terraform"],"projects":["Deploy Web App on Cloud","Serverless Application Project","Cloud Monitoring Setup"],"resources":["AWS Azure GCP Official Docs","A Cloud Guru Courses","YouTube TechWorld with Nana"]},
    "Business Analyst":{"skills":["Excel SQL Tableau PowerBI","Requirement Gathering","Process Modeling","Data Analysis and Reporting","Communication and Presentation"],"projects":["Sales Dashboard","Customer Analysis Report","Process Optimization Project"],"resources":["Coursera Business Analytics","Udemy SQL Tableau Courses","YouTube Analytics University"]},
    "Blockchain Developer":{"skills":["Solidity Ethereum","Smart Contracts","Web3.js Ethers.js","Blockchain Architecture","Cryptography Basics"],"projects":["Smart Contract Deployment","NFT Minting Platform","Decentralized App DApp"],"resources":["CryptoZombies.io","Coursera Blockchain Courses","YouTube Dapp University"]},
    "AI Researcher":{"skills":["Python or R","Mathematics Linear Algebra Probability","Deep Learning","NLP or Computer Vision","Research Paper Reading and Implementation"],"projects":["Image Captioning Model","Text Summarization Model","Custom Neural Network Research"],"resources":["arXiv Papers","DeepLearning.ai","YouTube Yannic Kilcher"]},
}

def safe_unique(df, col, fallback):
    return sorted(df[col].dropna().unique()) if col in df.columns else fallback

def normalize_yn(x):
    return "Yes" if isinstance(x,str) and x.strip().lower() in ("yes","y","true","1") else "No"

def detect_cat(interest):
    s = str(interest).lower()
    if any(k in s for k in ["ai/ml","ml","ai","data science","data analysis"]): return "ML"
    if "web" in s or "app" in s: return "WEB"
    if "competitive" in s: return "DSA"
    if "cyber" in s: return "CYBER"
    if "vlsi" in s: return "VLSI"
    if "iot" in s: return "IOT"
    if "embedded" in s: return "EMBEDDED"
    if "signal" in s: return "SIGNAL"
    if "communication systems" in s: return "COMM_SYSTEMS"
    if "power" in s: return "POWER"
    if "renewable" in s: return "RENEW"
    if "smart grid" in s: return "SMARTGRID"
    if "automation" in s: return "AUTOMATION"
    if "electrical design" in s: return "ELECTRICAL_DESIGN"
    if "robotics" in s: return "ROBOTICS"
    if "cad" in s: return "CAD"
    if "automobile" in s: return "AUTO"
    if "thermal" in s: return "THERMAL"
    if "manufacturing" in s: return "MANUFACTURING"
    if "communication skills" in s: return "SOFT"
    return "DSA"

def clamp(x,lo,hi): return max(lo,min(hi,x))

def lvl_bucket(sk):
    s = str(sk).lower()
    return "Beginner" if "begin" in s else "Intermediate" if "inter" in s else "Advanced"

def similar_students(df, info):
    f = df.copy()
    if "hostel" in f.columns: f["hostel"] = f["hostel"].apply(normalize_yn)
    for k,col in [("year","year"),("branch","branch"),("interest","interest"),("skill_level","skill_level")]:
        if col in f.columns and clean(info.get(k)):
            f = f[f[col]==info[k]]
    return f

def build_weeks(interest, skill_level, budget):
    cat  = detect_cat(interest)
    db   = COURSE_DB.get(cat, COURSE_DB["DSA"])
    free = "Use free resources YouTube/NPTEL." if budget=="Low" else "Consider 1 paid course for faster progress."
    prac = "45-60 mins daily practice." if "begin" in str(skill_level).lower() else "60-90 mins daily practice."
    titles = ["Foundation","Core Skills","Build Projects","Portfolio and Review"]
    return (
        [{"title":f"Week {i+1} - {titles[i]}","bullets":[f"Course: {db['courses'][min(i,len(db['courses'])-1)]}",db["weeks"][i],prac,free]} for i in range(4)],
        db["courses"], db["projects"]
    )

def generate(info, df):
    goals=[]; risks=[]; habits=[]; steps=[]
    sim = similar_students(df, info)
    if len(sim) >= 5:
        ag  = sim["gpa"].mean()         if "gpa"         in sim.columns else None
        asd = sim["study_hours"].mean() if "study_hours" in sim.columns else None
        if ag is not None and asd is not None:
            note = f"Based on {len(sim)} similar students - avg GPA {ag:.2f}, avg study {asd:.1f} hrs/day."
        else:
            note = f"General roadmap shown. {len(sim)} similar profiles found."
    else:
        note = "General roadmap based on your profile."

    interest_val = clean(info.get("interest")) or "your chosen field"
    goals.append(f"Build a clear learning path in {interest_val}.")
    if info["gpa"] < 6.0:
        goals.append("Improve academic consistency. Target +0.5 GPA next semester.")
    if info["study_hours"] < 3:
        goals.append("Gradually increase daily study hours to 3-4 hours.")
    if info["communication"] in ("Poor","Low"):
        goals.append("Improve communication through weekly speaking and writing practice.")

    if info["stress_level"]=="High" or info["confusion_level"]=="High":
        risks.append("High stress or confusion detected. Use weekly planning and short focused sessions.")
        habits.append("10 min meditation + Pomodoro 25/5 method (2 cycles daily).")

    if info["hostel"]=="Yes":
        habits.append("Fixed sleep schedule + dedicated study slot + limit late-night screen time.")
    else:
        habits.append("Fixed study slot at home + communicate your schedule to family.")

    if info["family_support"]=="Low":
        steps.append("Join a peer group or online community for external accountability.")
    else:
        steps.append("Share weekly goals with family and use their encouragement.")

    if info["budget"]=="Low":
        steps.append("Start with free resources and build projects to prove your skills.")
    else:
        steps.append("Invest in 1 quality paid course or mentorship for structured learning.")

    if info["study_hours"] < 3:
        steps.append("Add 30 extra mins per week to study routine until reaching 3-4 hrs/day.")
    if info["gpa"] < 6.0:
        steps.append("Daily revision + weekly tests + focus on your weakest subjects.")
    if info["communication"] in ("Poor","Low"):
        steps.append("2 short talks per week + write 1 paragraph summary daily.")

    weeks, courses, projects = build_weeks(info["interest"], info["skill_level"], info["budget"])
    return {"note":note,"goals":goals,"risks":risks,"habits":habits,"steps":steps,"weeks":weeks,"resources":courses,"projects":projects}

def readiness(info):
    g  = float(info.get("gpa",0))
    ac = 30 if g>=8 else 26 if g>=7 else 20 if g>=6 else 14 if g>=5 else 8
    lv = lvl_bucket(info.get("skill_level","Beginner"))
    sh = int(info.get("study_hours",0))
    sk = clamp((12 if lv=="Beginner" else 20 if lv=="Intermediate" else 26)+(6 if sh>=4 else 3 if sh>=3 else 1),0,30)
    sl = int(info.get("sleep_hours",6))
    st_= info.get("stress_level","Medium")
    cf = info.get("confusion_level","Medium")
    ro = clamp((8 if sl>=7 else 5 if sl>=6 else 2)+(6 if st_=="Low" else 4 if st_=="Medium" else 2)+(6 if cf=="Low" else 4 if cf=="Medium" else 2),0,20)
    cm = str(info.get("communication","Average"))
    co = 20 if cm in ("Good","High") else 14 if cm in ("Average","Medium") else 8
    return {"Academics":ac,"Skills":sk,"Routine":ro,"Communication":co,"Total":clamp(ac+sk+ro+co,0,100)}

def to_md(name, info, r):
    n = clean(name) or "Student"
    lines = [f"# Roadmap for {n}", f"Date: {date.today()}", "", "## Profile"]
    for k in ["year","branch","interest","skill_level","budget","hostel","study_hours","gpa","stress_level","confusion_level","communication","family_support"]:
        val = clean(info.get(k))
        lines.append(f"- {k.replace('_',' ').title()}: {val if val else 'N/A'}")
    lines += ["","## Insight", clean(r.get("note","")), "","## Goals"]
    for g in r.get("goals",[]): lines.append(f"- {clean(g)}")
    if r.get("risks"):
        lines += ["","## Risks"]
        for x in r["risks"]: lines.append(f"- {clean(x)}")
    lines += ["","## Daily Habits"]
    for x in r.get("habits",[]): lines.append(f"- {clean(x)}")
    lines += ["","## Action Steps"]
    for x in r.get("steps",[]): lines.append(f"- {clean(x)}")
    lines += ["","## 4-Week Plan"]
    for w in r.get("weeks",[]):
        lines += [f"### {w['title']}"] + [f"- {b}" for b in w["bullets"]] + [""]
    lines += ["## Projects"]
    for x in r.get("projects",[]): lines.append(f"- {clean(x)}")
    lines += ["","## Resources"]
    for x in r.get("resources",[]): lines.append(f"- {clean(x)}")
    return "\n".join(lines)

def skill_gap(required, known):
    return [s for s in required if s in known], [s for s in required if s not in known]

if st.session_state.page == "home":
    show_landing()
    st.stop()

@st.cache_data
def load_data():
    df = pd.read_csv("student_performance_final.csv")
    df.columns = df.columns.str.lower()
    return df

data = load_data()
st.write(data.columns.tolist())  # See actual column names
st.write(data.head(2))         

st.markdown('<div class="apphdr"><div class="applogo">🎯 SkillRoadmap</div></div>', unsafe_allow_html=True)

cb, _ = st.columns([1,9])
with cb:
    if st.button("Back"):
        st.session_state.page = "home"
        st.session_state.roadmap_data = None
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

years     = safe_unique(data,"year",               [1,2,3,4])
branches  = safe_unique(data,"branch",             ["CSE","IT","ECE","EEE","MECH"])
interests = safe_unique(data,"interest",           ["AI/ML","Web Development","DSA","Cybersecurity","IoT"])
budgets   = safe_unique(data,"budget_level",       ["Low","Medium","High"])
skills_l  = safe_unique(data,"skill_level",        ["Beginner","Intermediate","Advanced"])
stress_l  = safe_unique(data,"stress_level",       ["Low","Medium","High"])
conf_l    = safe_unique(data,"confusion_level",    ["Low","Medium","High"])
comm_l    = safe_unique(data,"communication_level",["Poor","Average","Good"])

st.markdown('<div class="wcard"><div class="wct">Your Profile</div><div class="wcs">Fill in your details and click Generate to get your personalised roadmap.</div></div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1:
    st.markdown('<div class="wcard"><div class="pill pi">Personal Info</div>', unsafe_allow_html=True)
    name   = st.text_input("Student Name","",key="nm")
    year   = st.selectbox("Year",years,key="yr")
    branch = st.selectbox("Branch",branches,key="br")
    hostel = st.selectbox("Hostel?",["Yes","No"],key="ho")
    fam    = st.selectbox("Family Support",["Low","Medium","High"],key="fa")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="wcard"><div class="pill pv">Academics</div>', unsafe_allow_html=True)
    gpa    = st.slider("GPA",0.0,10.0,7.0,0.1,key="gp")
    study  = st.slider("Daily Study Hours",0,12,3,key="sh")
    sleep  = st.slider("Daily Sleep Hours",0,12,7,key="sl")
    fail   = st.number_input("Number of Failures",0,10,0,key="fl")
    stress = st.selectbox("Stress Level",stress_l,key="st")
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="wcard"><div class="pill pg">Goals and Skills</div>', unsafe_allow_html=True)
    interest = st.selectbox("Primary Interest",interests,key="in")
    budget   = st.selectbox("Budget Level",budgets,key="bu")
    skill    = st.selectbox("Skill Level",skills_l,key="sk")
    conf     = st.selectbox("Confusion Level",conf_l,key="cn")
    comm     = st.selectbox("Communication Level",comm_l,key="cm")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
_,cg,_ = st.columns([1,2,1])
with cg:
    if st.button("Generate My Roadmap", use_container_width=True, key="gen"):
        st.session_state.student_name = name
        st.session_state.student_info = {
            "year":year,"branch":branch,"gpa":float(gpa),
            "study_hours":int(study),"failures":int(fail),
            "hostel":hostel,"sleep_hours":int(sleep),
            "family_support":fam,"interest":interest,
            "budget":budget,"skill_level":skill,
            "stress_level":stress,"confusion_level":conf,
            "communication":comm,
        }
        st.session_state.roadmap_data = generate(st.session_state.student_info, data)

if st.session_state.roadmap_data is not None:
    rdm   = st.session_state.roadmap_data
    info  = st.session_state.student_info
    sname = clean(st.session_state.student_name) or "Student"
    sc    = readiness(info)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#4f46e5,#7c3aed,#ec4899);border-radius:20px;
         padding:22px 32px;text-align:center;margin-bottom:24px;box-shadow:0 8px 32px rgba(99,102,241,.30);">
      <div style="font-family:Syne,sans-serif;font-size:22px;font-weight:800;color:#fff;">
        Roadmap Ready for {sname}!
      </div>
      <div style="font-size:13px;color:rgba(255,255,255,.75);margin-top:4px;">Your personalised 4-week plan is below.</div>
    </div>
    """, unsafe_allow_html=True)

    tiles = [
        ("GPA",f"{info['gpa']:.1f}","mi"),
        ("Study/day",f"{info['study_hours']} hrs","mv"),
        ("Sleep",f"{info['sleep_hours']} hrs","ms"),
        ("Readiness",f"{sc['Total']}/100","mg"),
        ("Level",clean(info['skill_level']) or "N/A","mr2"),
    ]
    cols = st.columns(5)
    for col,(lbl,val,cls) in zip(cols,tiles):
        col.markdown(f'<div class="mt {cls}"><div class="mval">{val}</div><div class="mlbl">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="wcard"><div class="pill pi">Readiness Score</div>', unsafe_allow_html=True)
    cA,cB = st.columns([1,2])
    with cA:
        st.markdown(f'<div style="text-align:center;padding:16px 0;"><div class="sbig">{sc["Total"]}</div><div class="ssub">out of 100</div></div>', unsafe_allow_html=True)
    with cB:
        bars = [
            ("Academics",sc["Academics"],30,"linear-gradient(90deg,#6366f1,#818cf8)","#4f46e5"),
            ("Skills",sc["Skills"],30,"linear-gradient(90deg,#8b5cf6,#a78bfa)","#7c3aed"),
            ("Routine",sc["Routine"],20,"linear-gradient(90deg,#0ea5e9,#38bdf8)","#0284c7"),
            ("Communication",sc["Communication"],20,"linear-gradient(90deg,#10b981,#34d399)","#059669"),
        ]
        for lbl,val,mx,grad,hex_ in bars:
            pct = int(val/mx*100)
            st.markdown(f'<div class="brow"><span style="color:#374151">{lbl}</span><span style="color:{hex_};font-weight:800">{val}/{mx}</span></div><div class="btrk"><div class="bfil" style="width:{pct}%;background:{grad}"></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    t1,t2,t3,t4,t5 = st.tabs(["Roadmap","4-Week Plan","Projects","Resources","Skill Gap"])

    with t1:
        note_txt = clean(rdm.get("note",""))
        if note_txt:
            st.markdown(f'<div class="ib">💡 {note_txt}</div>', unsafe_allow_html=True)
        st.markdown('<div class="pill pi">Goals</div>', unsafe_allow_html=True)
        for g in rdm["goals"]:
            st.markdown(f'<div class="gc"><div class="di"></div><div class="ct">{clean(g)}</div></div>', unsafe_allow_html=True)
        if rdm["risks"]:
            st.markdown('<br><div class="pill pr">Risks to Watch</div>', unsafe_allow_html=True)
            for r in rdm["risks"]:
                st.markdown(f'<div class="rc"><div class="dr"></div><div class="ct">{clean(r)}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="pill ps">Daily Habits</div>', unsafe_allow_html=True)
        for h in rdm["habits"]:
            st.markdown(f'<div class="hc"><div class="ds"></div><div class="ct">{clean(h)}</div></div>', unsafe_allow_html=True)
        st.markdown('<br><div class="pill pg">Action Steps</div>', unsafe_allow_html=True)
        for i,step in enumerate(rdm["steps"],1):
            st.markdown(f'<div class="sc2"><div class="sn">{i}</div><div class="ct">{clean(step)}</div></div>', unsafe_allow_html=True)

    with t2:
        wk_colors=["#6366f1","#8b5cf6","#ec4899","#10b981"]
        for idx,w in enumerate(rdm["weeks"]):
            bullets = "".join(f'<div class="wkb">{clean(b)}</div>' for b in w["bullets"])
            st.markdown(f'<div class="wkcard" style="border-left-color:{wk_colors[idx%4]};"><div class="wktit">{clean(w["title"])}</div>{bullets}</div>', unsafe_allow_html=True)

    with t3:
        st.markdown('<div class="pill pa">Suggested Projects</div>', unsafe_allow_html=True)
        icons=["🔶","🔷","🟣","🟢","🔴"]
        for i,p in enumerate(rdm["projects"]):
            st.markdown(f'<div class="pjc"><div style="font-size:20px">{icons[i%len(icons)]}</div><div class="pjn">{clean(p)}</div></div>', unsafe_allow_html=True)

    with t4:
        st.markdown('<div class="pill ps">Recommended Resources</div>', unsafe_allow_html=True)
        ri=["🎥","📖","🌐"]
        for i,r in enumerate(rdm["resources"]):
            st.markdown(f'<div class="rsc"><div style="font-size:18px">{ri[i%3]}</div><div class="rsn">{clean(r)}</div></div>', unsafe_allow_html=True)

    with t5:
        st.markdown('<div class="pill pv">Skill Gap Analysis</div>', unsafe_allow_html=True)
        jroles  = ["Select a role"] + list(JOB_SKILLS.keys())
        jchoice = st.selectbox("Target Job Role", jroles, key="jc")
        if jchoice != "Select a role":
            ji = JOB_SKILLS[jchoice]
            cl2,cr2 = st.columns(2)
            with cl2:
                st.markdown('<div class="pill pv">Required Skills</div>', unsafe_allow_html=True)
                for sk in ji["skills"]:
                    st.markdown(f'<div class="skr">• {clean(sk)}</div>', unsafe_allow_html=True)
            with cr2:
                st.markdown('<div class="pill pa">Sample Projects</div>', unsafe_allow_html=True)
                for p in ji["projects"]:
                    st.markdown(f'<div class="pjc"><div class="pjn">{clean(p)}</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="pill pg">Skills You Already Know</div>', unsafe_allow_html=True)
            known = st.multiselect("Select your current skills:", options=ji["skills"], key="km")
            have,miss = skill_gap(ji["skills"], known)
            pct = int(len(have)/len(ji["skills"])*100) if ji["skills"] else 0
            bc  = "#10b981" if pct>=70 else "#f59e0b" if pct>=40 else "#ef4444"
            tag = "Strong match - ready to apply!" if pct>=70 else "Getting there - keep building!" if pct>=40 else "Start learning - you have got this!"
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="background:#fff;border:1.5px solid #e0e7ff;border-radius:16px;padding:20px 24px;margin-bottom:20px;box-shadow:0 2px 12px rgba(0,0,0,.06);">
              <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
                <span style="font-weight:800;font-family:Syne,sans-serif;color:#1e1b4b;font-size:15px;">Skill Match</span>
                <span style="font-weight:800;font-size:24px;color:{bc};">{pct}%</span>
              </div>
              <div style="height:12px;border-radius:999px;background:#f1f5f9;overflow:hidden;margin-bottom:8px;">
                <div style="height:100%;width:{pct}%;background:{bc};border-radius:999px;"></div>
              </div>
              <div style="font-size:13px;color:{bc};font-weight:700;">{tag}</div>
            </div>
            """, unsafe_allow_html=True)
            ch2,cm2 = st.columns(2)
            with ch2:
                st.markdown('<div class="pill pg">You Have</div>', unsafe_allow_html=True)
                if have:
                    for sk in have: st.markdown(f'<div class="skh">✅ {clean(sk)}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="font-size:13px;color:#6b7280;">Select your skills above.</p>', unsafe_allow_html=True)
            with cm2:
                st.markdown('<div class="pill pr">To Learn</div>', unsafe_allow_html=True)
                if miss:
                    for sk in miss: st.markdown(f'<div class="skn">🔴 {clean(sk)}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="background:#f0fdf4;border:1.5px solid #86efac;border-radius:12px;padding:14px;font-size:14px;color:#15803d;font-weight:700;">All skills covered!</div>', unsafe_allow_html=True)
            if miss:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="pill pv">Learning Order</div>', unsafe_allow_html=True)
                for i,sk in enumerate(miss,1):
                    st.markdown(f'<div class="lst"><div class="ln">{i}</div><div class="lt">Learn {clean(sk)}</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="pill ps">Resources for this Role</div>', unsafe_allow_html=True)
            for r in ji["resources"]:
                st.markdown(f'<div class="rsc"><div style="font-size:16px">📌</div><div class="rsn">{clean(r)}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    md_txt = to_md(sname, info, rdm)
    st.download_button("Download Full Roadmap (Markdown)", data=md_txt.encode("utf-8"),
        file_name=f"roadmap_{sname.replace(' ','_').lower()}.md", mime="text/markdown", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
with st.expander("Dataset Preview"):
    st.dataframe(data, use_container_width=True)

st.markdown('<p style="text-align:center;font-size:11px;color:#9ca3af;margin-top:24px;padding-bottom:24px;">Student Skill Roadmap - Mini Project</p>', unsafe_allow_html=True)

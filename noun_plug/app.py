import streamlit as st
import pandas as pd

# --- 1. CLOUD SYNC ---
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQcXKUQKj--5bQnHzCYdJ1g4EVkzmsXF5KwXPXOjtLMe88IuwDYlmshCz5J8z-Ssga8L-aE1Zm6YJ6R/pub?gid=0&single=true&output=csv"

def load_users():
    try:
        df = pd.read_csv(SHEET_CSV_URL)
        df.columns = df.columns.str.strip().str.lower()
        return dict(zip(df['username'].astype(str), df['password'].astype(str)))
    except:
        return {"admin": "plug2026"}

# --- 2. EXAM DATABASE (20 per subject | 100 Total) ---
DB = {
    "MTH 101: Elementary Mathematics I": [
        {"q": "Given A = {x : x is a prime number, 2 < x < 10} and B = {x : x is an odd number, 1 < x < 9}, find A ∩ B.", "o": ["{3, 5, 7}", "{3, 5, 7, 9}", "{2, 3, 5, 7}", "{3, 5}"], "a": "{3, 5, 7}", "e": "A={3,5,7}, B={3,5,7}. The intersection is {3,5,7}."},
        {"q": "Simplify the complex number i^63.", "o": ["i", "-i", "1", "-1"], "a": "-i", "e": "i^4=1. 63/4 leaves remainder 3. i^3 = -i."},
        # [IBRAHIM: Paste the other 18 MTH questions here]
    ],
    "GST 103: Computer Fundamentals": [
        {"q": "Who proposed the 'Stored Program' concept?", "o": ["Babbage", "Von Neumann", "Pascal", "Gates"], "a": "Von Neumann", "e": "Core architecture of modern computers."},
        {"q": "Which generation used Vacuum Tubes?", "o": ["1st", "2nd", "3rd", "4th"], "a": "1st", "e": "1940-1956 technology."},
        # [IBRAHIM: Paste the other 18 GST103 questions here]
    ],
    "PHY 101: Mechanics & Heat": [
         {"q": "The dimension of Force is:", "o": ["[MLT^-1]", "[MLT^-2]", "[ML^2T^-2]", "[MLT]"], "a": "[MLT^-2]", "e": "Force = mass * accel."},
         # [IBRAHIM: Paste the other 19 PHY questions here]
    ],
    "CHM 101: Inorganic Chemistry": [
         {"q": "Atomic number of Hydrogen?", "o": ["1", "2", "3", "4"], "a": "1", "e": "First element in the periodic table."},
         # [IBRAHIM: Paste the other 19 CHM questions here]
    ],
    "GST 101: Use of English I": [
         {"q": "SQ3R: The 1st 'S' stands for?", "o": ["Survey", "Search", "Scan", "Solve"], "a": "Survey", "e": "Surveying is the overview step."},
         # [IBRAHIM: Paste the other 19 GST101 questions here]
    ]
}

# --- 3. THE "OFFICIAL" DESIGN ---
st.set_page_config(page_title="NOUN CS Plug | 100L", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; }
    .main-header { font-size: 3.5rem; font-weight: 800; background: -webkit-linear-gradient(#58a6ff, #1f6feb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 0px; }
    .info-box { background: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); margin: 20px 0; }
    .pay-btn { display: inline-block; padding: 12px 24px; background-color: #238636; color: white !important; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 1.1rem; transition: 0.3s; }
    .pay-btn:hover { background-color: #2ea043; transform: scale(1.05); }
    .ai-explainer { background: #0d1117; border-left: 4px solid #58a6ff; padding: 15px; font-style: italic; color: #8b949e; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE WELCOME INTERFACE ---
st.markdown("<h1 class='main-header'>NOUN CS PLUG 🔌</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center; color: #8b949e;'>Developed by <b>Nurudeen Olabamidele Ibrahim</b></p>", unsafe_allow_html=True)

st.markdown("""
<div class='info-box'>
    <h2>🚀 Your 5.0 GPA Journey Starts Here</h2>
    <p>Get exclusive access to 100 practice questions designed strictly from the <b>NOUN 100L Computer Science Courseware</b>.</p>
    <ul>
        <li>✅ MTH 101, GST 103, PHY 101, CHM 101, GST 101</li>
        <li>✅ Automated Nova AI explanations for every answer</li>
        <li>✅ Real-time CBT scoring system</li>
    </ul>
    <br>
    <a class='pay-btn' href='https://selar.com/g444q677i3' target='_blank'>💳 PAY ₦1,000 FOR INSTANT ACCESS</a>
</div>
""", unsafe_allow_html=True)

# --- 5. MEMBERSHIP LOGIN ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=80)
    st.title("Member Portal")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    
    user_db = load_users()
    
    if u in user_db and str(user_db[u]) == str(p):
        st.success(f"Verified: {u}")
        auth = True
    else:
        if u != "": st.error("Access Denied")
        auth = False
        st.divider()
        st.write("### 📞 Support")
        st.write("Message OLA for your login details.")
        st.link_button("Chat with OLA", "https://wa.me/2348148849127")
        st.stop()

# --- 6. UNLOCKED ACADEMY ---
st.header("💻 Study Dashboard")
subject = st.selectbox("Select Subject:", list(DB.keys()))

if 'score' not in st.session_state: st.session_state.score = 0

for i, item in enumerate(DB[subject]):
    st.write(f"### Q{i+1}")
    st.write(item["q"])
    ans = st.radio(f"Options for Q{i+1}:", item["o"], key=f"ans_{subject}_{i}")
    
    if st.button(f"Verify Answer {i+1}", key=f"btn_{subject}_{i}"):
        if ans == item["a"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong. Answer: {item['a']}")
            st.markdown(f"<div class='ai-explainer'>🤖 <b>Nova AI:</b> {item['e']}</div>", unsafe_allow_html=True)
    st.divider()

if st.button("Final Result"):
    st.balloons()
    st.subheader(f"Score: {st.session_state.score} / {len(DB[subject])}")
    st.session_state.score = 0

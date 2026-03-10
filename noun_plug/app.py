import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN CS Plug | 100L", layout="wide", page_icon="💻")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .main-header { font-size: 3rem; font-weight: bold; color: #58a6ff; text-align: center; margin-bottom: 0; }
    .sub-header { font-size: 1.2rem; text-align: center; color: #8b949e; margin-bottom: 2rem; }
    .payment-card { background-color: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: center; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #238636; color: white; font-weight: bold; height: 3em; }
    .ai-box { background-color: #0d1117; border-left: 5px solid #58a6ff; padding: 15px; border-radius: 5px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE (SHRINKED FOR THE EXAMPLE, KEEP YOUR FULL DB HERE) ---
DB = {
    "MTH 101: Elementary Mathematics I": [
        {"q": "Given A = {x : x is a prime number, 2 < x < 10} and B = {x : x is an odd number, 1 < x < 9}, find A ∩ B.", "o": ["{3, 5, 7}", "{3, 5, 7, 9}", "{2, 3, 5, 7}", "{3, 5}"], "a": "{3, 5, 7}", "e": "A={3,5,7}, B={3,5,7}. The intersection is {3,5,7}."},
        # ... [Keep the 20 questions I gave you in the previous turn here]
    ],
    # ... [Keep all other course banks here]
}

# --- SIDEBAR ACCESS CONTROL ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/checked-user-male.png", width=80)
    st.title("Admin Access")
    access_code = st.text_input("Enter 1k Access Code:", type="password")
    st.divider()
    st.write("### 📞 Help & Support")
    st.write("Creator: **Nurudeen Olabamidele Ibrahim**")
    st.link_button("Chat on WhatsApp", "https://wa.me/2348148849127")

# --- MAIN PAGE LOGIC ---
if not access_code or access_code != "PLUG2026":
    # --- WELCOME / LANDING PAGE ---
    st.markdown("<h1 class='main-header'>NOUN CS PLUG 🔌</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>The Ultimate 100L Computer Science Exam Prep Tool</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("### Why use NOUN CS Plug?")
        st.write("✅ **Courseware-Based:** Questions are strictly from NOUN study materials.")
        st.write("✅ **Detailed Explanations:** Our Nova AI breaks down complex math and science logic.")
        st.write("✅ **Exam Simulation:** Real CBT-style interface to build your confidence.")
        st.write("✅ **5.0 GPA Focus:** Designed by Ibrahim to help you ace your TMAs and e-Exams.")
        
    with col2:
        st.markdown("""
            <div class='payment-card'>
                <h4>🔓 Unlock Full Access</h4>
                <p>Get the 1k access code to unlock all 100 questions across 5 core subjects.</p>
                <h2 style='color: #238636;'>₦1,000</h2>
            </div>
            """, unsafe_allow_html=True)
        # REPLACE THE LINK BELOW WITH YOUR ACTUAL PAYMENT LINK (Selar, Paystack, etc.)
        st.link_button("💳 Pay Online to Get Code", "https://selar.co/your-link-here")
        st.info("After payment, message Ibrahim on WhatsApp to get your unique code.")

    st.divider()
    st.image("https://img.icons8.com/fluency/48/info.png", width=30)
    st.write("**Note:** This app covers MTH 101, GST 103, PHY 101, CHM 101, and GST 101 with 20 high-standard questions each.")

else:
    # --- ACTUAL STUDY PORTAL (Unlocked) ---
    st.title("💻 NOUN CS 100L Academy")
    subject = st.selectbox("Select Subject:", list(DB.keys()))
    
    if 'score' not in st.session_state: st.session_state.score = 0
    
    for i, item in enumerate(DB[subject]):
        st.subheader(f"Question {i+1}")
        st.write(item["q"])
        user_ans = st.radio(f"Select your answer for Q{i+1}:", item["o"], key=f"q_{subject}_{i}")
        
        if st.button(f"Verify Answer {i+1}", key=f"btn_{subject}_{i}"):
            if user_ans == item["a"]:
                st.success("🎯 Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. The answer is: {item['a']}")
                st.markdown(f"<div class='ai-box'>🤖 <b>Nova AI:</b> {item['e']}</div>", unsafe_allow_html=True)
        st.divider()

    if st.button("Generate Final Result"):
        st.balloons()
        st.header(f"Final Score: {st.session_state.score} / {len(DB[subject])}")
        st.session_state.score = 0

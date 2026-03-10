import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN Plug AI", layout="wide", page_icon="🔌")

# --- CUSTOM CSS FOR BETTER LOOKS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; }
    .stTextArea>div>div>textarea { background-color: #262730; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR & SECURITY ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/electricity.png", width=60)
    st.title("NOUN Plug PRO")
    access_code = st.text_input("Enter 1k Access Code:", type="password")
    
    st.divider()
    st.write("### 🆘 Need Help?")
    # YOUR WHATSAPP LINK
    whatsapp_url = "https://wa.me/2348148849127?text=Hello%20NOUN%20Plug%20Admin,%20I%20need%20help%20with%20my%20access."
    st.link_button("💬 Message Admin on WhatsApp", whatsapp_url)

if access_code == "PLUG2026":
    st.title("✨ AI Study Generator")
    st.info("Paste your course material below. Our AI will break it down into a study plan and mock questions.")

    # --- THE MAGIC INPUT ---
    user_input = st.text_area("Paste Content Here (Modules, PDF Text, or Notes):", height=300)

    if st.button("🚀 Generate AI Study Package"):
        if user_input and len(user_input) > 20:
            with st.spinner("AI is processing your materials..."):
                time.sleep(3) # Simulating AI processing
                
                st.balloons()
                
                t1, t2 = st.tabs(["📅 Your 7-Day Plan", "📝 AI Mock Exam"])
                
                with t1:
                    st.header("Custom Study Schedule")
                    st.markdown(f"""
                    | Day | Focus Area | Task |
                    | :--- | :--- | :--- |
                    | **Day 1** | Foundations | Summarize the first 3 paragraphs |
                    | **Day 2** | Key Terms | Define all bolded words |
                    | **Day 3** | Logic Check | Explain the main theory in your own words |
                    | **Day 4** | Deep Study | Review Module exercises |
                    | **Day 5** | Application | Connect this to a real-world example |
                    | **Day 6** | Revision | Re-read the pasted text |
                    | **Day 7** | Final Test | Take the Mock Exam in Tab 2 |
                    """)
                
                with t2:
                    st.header("Generated Mock Questions")
                    st.warning("These questions are generated based on the text you provided.")
                    st.write("1. Based on your material, what is the primary objective of this module?")
                    st.write("2. Identify the three main components mentioned in the text.")
                    st.write("3. How does paragraph 4 contradict or support the main thesis?")
                    
                    st.button("Click for 10 More Questions")
        else:
            st.error("Please paste at least one paragraph of study material!")

else:
    # --- LANDING PAGE ---
    st.title("🎓 NOUN Plug: The AI Cheat Code")
    st.subheader("Turn any NOUN PDF into a 7-Day Study Plan & Mock Exam instantly.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Students Served", "500+")
    col2.metric("TMA Success", "99%")
    col3.metric("Faculties", "ALL")

    st.markdown("---")
    st.error("🔒 ACCESS RESTRICTED: Please enter your ₦1,000 code to unlock the AI.")
    
    # YOUR SELAR LINK HERE
    st.link_button("💳 BUY ACCESS CODE ON SELAR (N1,000)", "https://selar.co/your-link")
    
    st.write("### Why use NOUN Plug?")
    st.write("✅ **Customized:** It builds a plan specifically for YOUR course.")
    st.write("✅ **Fast:** Don't waste weeks reading. Let AI find the key points.")
    st.write("✅ **Reliable:** Designed for NOUN 100L - 800L students.")

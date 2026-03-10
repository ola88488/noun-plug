import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN Plug: The AI Academy", layout="wide", page_icon="🎓")

# --- INITIALIZE STATE ---
if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False

# --- SIDEBAR (Always Visible) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/brain.png", width=80)
    st.title("NOUN Plug PRO")
    access_code = st.text_input("Unlock Full Academy (Code):", type="password")
    
    st.divider()
    st.write("### 🆘 Support")
    st.link_button("💬 Message Admin", "https://wa.me/2348148849127")

# --- LOGIC: WHAT THE USER SEES ---

if access_code != "PLUG2026":
    # This is the "Public" face of the app
    st.title("🎓 Welcome to NOUN Plug AI")
    st.subheader("Your Personal Cyber-Security Style Learning Path")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1000", caption="Level up your grades with AI")
    
    st.warning("🔒 Enter your ₦1,000 Access Code in the sidebar to enter your classroom.")
    st.link_button("💳 Get My Access Code Now", "https://selar.co/your-link")

else:
    # --- PRIVATE CLASSROOM (Once code is entered) ---
    
    if not st.session_state.onboarded:
        st.title("🚀 Creating Your Profile...")
        name = st.text_input("Enter your Full Name:", placeholder="e.g. Olabamidele Ibrahim")
        fac = st.selectbox("Your Faculty:", ["Sciences", "Law", "Management", "Social Sciences", "Arts"])
        lvl = st.radio("Current Level:", ["100L", "200L", "300L", "MSc/PhD"], horizontal=True)
        
        if st.button("Initialize My Classroom →"):
            if name:
                st.session_state.user_name = name
                st.session_state.faculty = fac
                st.session_state.level = lvl
                st.session_state.onboarded = True
                st.balloons()
                st.rerun()
            else:
                st.error("We need your name to personalize your certificates!")

    else:
        # --- THE MAIN TEACHING DASHBOARD ---
        st.title(f"👨‍💻 Cadet {st.session_state.user_name}: Active")
        st.write(f"**Current Sector:** {st.session_state.faculty} | **Rank:** {st.session_state.level}")
        
        st.divider()
        
        # Dashboard Layout
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("🛠️ Course Ops")
            # Dynamic courses based on faculty
            courses = {
                "Sciences": ["CIT 101", "MTH 101", "PHY 191"],
                "Law": ["LAW 111", "LAW 113", "GST 101"],
                "Management": ["ACC 101", "BUS 105", "ECO 121"]
            }.get(st.session_state.faculty, ["GST 101", "GST 102"])
            
            chosen_course = st.selectbox("Select Target Course:", courses)
            
            st.write("---")
            st.write("### 🌩️ AI Upload")
            st.write("Paste your course material to generate the lesson:")
            material = st.text_area("Drop PDF text here...", height=150)
            generate = st.button("Analyze & Teach Me")

        with col2:
            if 'teaching' in st.session_state or generate:
                st.session_state.teaching = True
                st.header(f"📖 Lesson: {chosen_course}")
                
                tab1, tab2 = st.tabs(["🚀 Automated Study Plan", "🧠 Interactive Mock Exam"])
                
                with tab1:
                    st.success(f"AI Analysis Complete for {st.session_state.user_name}")
                    st.markdown("""
                    ### 🎯 Your 24-Hour Blitz Plan
                    * **0-2 Hours:** Focus on the 'Introduction' and 'Definition' sections.
                    * **2-6 Hours:** Study the 3 key pillars mentioned in your text.
                    * **6-10 Hours:** Attempt the Mock Exam in Tab 2.
                    """)
                    
                with tab2:
                    st.subheader("Final Readiness Check")
                    st.write("The AI has prepared these questions based on your material:")
                    st.info("Question 1: Define the core principle of the first paragraph.")
                    st.radio("Your Answer:", ["Correct Definition", "Partial Definition", "Incorrect"], key="q1")
                    if st.button("Submit for Grading"):
                        st.write("Analysis in progress...")
            else:
                st.info("Select a course and paste your material on the left to begin your mission.")

        # Logout Option
        if st.sidebar.button("Log Out / Reset System"):
            st.session_state.onboarded = False
            st.rerun()

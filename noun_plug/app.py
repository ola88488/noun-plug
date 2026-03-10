import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN Plug: My Classroom", layout="wide", page_icon="🎓")

# --- INITIALIZE SESSION STATE ---
if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- ACCESS CONTROL ---
with st.sidebar:
    st.title("🔑 Security")
    access_code = st.text_input("Enter 1k Access Code:", type="password")
    st.divider()
    if access_code == "PLUG2026":
        st.success("Access Granted")
    else:
        st.warning("Locked")
        st.stop() # Stops the app here if code is wrong

# --- STEP 1: ONBOARDING MENU ---
if not st.session_state.onboarded:
    st.title("🚀 Welcome to NOUN Plug")
    st.subheader("Let's set up your personalized classroom.")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("What is your name?")
        faculty = st.selectbox("Select your Faculty:", ["Sciences", "Law", "Management Sciences", "Social Sciences", "Education", "Health Sciences"])
    with col2:
        level = st.selectbox("What is your Level?", ["100L", "200L", "300L", "400L", "500L", "800L"])
        goal = st.selectbox("What is your target GPA?", ["First Class (4.5+)", "2.1 (3.5 - 4.4)", "2.2 (2.4 - 3.4)"])

    if st.button("Start Learning Now →"):
        if name:
            st.session_state.user_name = name
            st.session_state.faculty = faculty
            st.session_state.level = level
            st.session_state.onboarded = True
            st.rerun()
        else:
            st.error("Please enter your name to continue.")

# --- STEP 2: THE MAIN DASHBOARD (The "Alive" Part) ---
else:
    st.title(f"👋 Welcome back, {st.session_state.user_name}!")
    st.write(f"**Path:** {st.session_state.faculty} | **Level:** {st.session_state.level}")
    
    # --- DYNAMIC COURSE GENERATION ---
    st.header("📚 Your Learning Path")
    
    # Simulating a professional "Learning Card" look
    courses = {
        "Sciences": ["CIT 101", "MTH 101", "STT 102", "PHY 191"],
        "Law": ["LAW 111", "LAW 113", "GST 101", "LAW 101"],
        "Management Sciences": ["ACC 101", "BUS 105", "ECO 121", "GST 107"]
    }.get(st.session_state.faculty, ["GST 101", "GST 102", "GST 107"])

    cols = st.columns(len(courses))
    
    for i, course_code in enumerate(courses):
        with cols[i]:
            with st.container(border=True):
                st.subheader(course_code)
                st.write("Progress: 0%")
                if st.button(f"Enter {course_code}", key=course_code):
                    st.session_state.current_course = course_code
    
    st.divider()

    # --- THE TEACHING INTERFACE (Cyber Security Style) ---
    if 'current_course' in st.session_state:
        st.header(f"📍 Currently Studying: {st.session_state.current_course}")
        
        tab1, tab2, tab3 = st.tabs(["📖 Lessons", "🧠 Interactive Lab", "📝 Final Mock Exam"])
        
        with tab1:
            st.markdown(f"""
            ### Module 1: Introduction to {st.session_state.current_course}
            In this section, you will learn the fundamental principles required for your TMA.
            
            **Key Concept:** The most important thing to remember is...
            """)
            st.info("💡 Pro Tip: 80% of exam questions come from this paragraph.")
            
        with tab2:
            st.subheader("Interactive Lab")
            st.write("Paste a paragraph from your material to generate a breakdown:")
            ai_input = st.text_area("Drop text here...", height=100)
            if st.button("Analyze Content"):
                with st.spinner("Breaking it down..."):
                    time.sleep(2)
                    st.success("Concept Simplified: This means that...")

        with tab3:
            st.subheader("Exam Readiness Test")
            st.write("Test your knowledge before the real TMA.")
            q1 = st.radio("Sample Question: Which of these is a primary source?", ["Option A", "Option B", "Option C"])
            if st.button("Submit Answer"):
                st.write("Processing result...")

    # --- SIDEBAR SUPPORT ---
    st.sidebar.divider()
    whatsapp_url = "https://wa.me/2348148849127?text=Hi%20Admin,%20I'm%20on%20the%20app!"
    st.sidebar.link_button("💬 Chat with Admin", whatsapp_url)
    if st.sidebar.button("Log Out / Reset"):
        st.session_state.onboarded = False
        st.rerun()

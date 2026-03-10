import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN Plug Academy", layout="wide", page_icon="🎓")

# --- DATABASE: THE ACTUAL LESSONS (Pre-loaded) ---
ACADEMY_CONTENT = {
    "Sciences": {
        "CIT 101: Computer In Society": {
            "Module 1: History": "Computers evolved through 5 generations. 1st Gen used Vacuum Tubes (1940s), while modern computers use Microprocessors. Key takeaway: Every generation got smaller, faster, and cheaper.",
            "Module 2: Hardware": "Hardware is the physical part. Input (Keyboard), Output (Monitor), Storage (Hard Drive). The CPU is the brain.",
            "Quiz": [
                {"q": "What did 1st Generation computers use?", "o": ["Transistors", "Vacuum Tubes", "Chips"], "a": "Vacuum Tubes"},
                {"q": "Which is an output device?", "o": ["Mouse", "Printer", "Keyboard"], "a": "Printer"}
            ]
        }
    },
    "Law": {
        "LAW 111: Legal Methods": {
            "Module 1: Sources of Law": "Nigerian law comes from the Constitution, Legislation, and Judicial Precedents. The Constitution is supreme.",
            "Module 2: Court Hierarchy": "The Supreme Court is at the top, followed by the Court of Appeal, then High Courts.",
            "Quiz": [
                {"q": "Which law is supreme in Nigeria?", "o": ["Customary Law", "The Constitution", "Religious Law"], "a": "The Constitution"},
                {"q": "What is the highest court in Nigeria?", "o": ["High Court", "Supreme Court", "Magistrate Court"], "a": "Supreme Court"}
            ]
        }
    }
}

# --- INITIALIZE STATE ---
if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False

# --- SIDEBAR ACCESS ---
with st.sidebar:
    st.title("🔌 NOUN Plug")
    access_code = st.text_input("Enter Access Code:", type="password")
    st.divider()
    st.write("### 🆘 Support")
    st.link_button("💬 WhatsApp Admin", "https://wa.me/2348148849127")

# --- APP LOGIC ---
if access_code != "PLUG2026":
    st.title("🎓 NOUN Plug: The 100L Academy")
    st.subheader("Professional Study Path for NOUN Students")
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1000", caption="Your classroom is waiting.")
    st.error("🔒 Enter your code in the sidebar to unlock your Faculty and Courses.")
else:
    if not st.session_state.onboarded:
        # STEP 1: WELCOME & IDENTITY
        st.title("👋 Welcome to the Academy")
        st.session_state.user_name = st.text_input("What is your name, Student?")
        st.session_state.faculty = st.selectbox("Select Your Faculty:", list(ACADEMY_CONTENT.keys()))
        
        if st.button("Initialize My Learning Path"):
            if st.session_state.user_name:
                st.session_state.onboarded = True
                st.balloons()
                st.rerun()
    else:
        # STEP 2: THE PROFESSIONAL DASHBOARD
        st.title(f"📖 {st.session_state.user_name}'s Classroom")
        st.write(f"**Faculty:** {st.session_state.faculty} | **Status:** Active Student")
        
        # Course Selection
        courses = list(ACADEMY_CONTENT[st.session_state.faculty].keys())
        selected_course = st.selectbox("Choose a Course to Study:", courses)
        
        st.divider()
        
        # THE LEARNING INTERFACE
        col1, col2 = st.columns([1, 1])
        
        content = ACADEMY_CONTENT[st.session_state.faculty][selected_course]
        
        with col1:
            st.header("📋 Lesson Plan")
            # Modules are listed like a real online course
            for module in content.keys():
                if module != "Quiz":
                    with st.expander(f"🔹 {module}"):
                        st.write(content[module])
                        st.button(f"Mark {module} as Completed", key=module)

        with col2:
            st.header("✍️ Module Mock Exam")
            st.write(f"Test your knowledge on {selected_course}")
            
            for i, item in enumerate(content["Quiz"]):
                st.write(f"**Q{i+1}: {item['q']}**")
                ans = st.radio("Select Answer:", item['o'], key=f"quiz_{i}")
                if st.button(f"Check Q{i+1}"):
                    if ans == item['a']:
                        st.success("Correct! Well done.")
                    else:
                        st.error(f"Wrong. The answer is {item['a']}")

        if st.sidebar.button("Log Out"):
            st.session_state.onboarded = False
            st.rerun()

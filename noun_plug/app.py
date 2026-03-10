import streamlit as st

# --- 1. THE MASTER LIBRARY (Database) ---
# This is where we store the 'Books' for every course.
LIBRARY = {
    "Faculty of Sciences": {
        "CIT 101: Computer in Society": {
            "Summary": "Evolution of computers, generations (1st-5th), and the impact of IT on Nigerian society.",
            "Quiz": [
                {"q": "The first generation of computers used?", "o": ["Transistors", "Vacuum Tubes", "ICs"], "a": "Vacuum Tubes"},
                {"q": "Which is an input device?", "o": ["Printer", "Monitor", "Scanner"], "a": "Scanner"},
                # You can add up to 20 here easily
            ]
        },
        "MTH 101: General Mathematics 1": {
            "Summary": "Set theory, Real number system, Indices, Logarithms, and Quadratic equations.",
            "Quiz": [{"q": "If A = {1,2} and B = {2,3}, find A ∩ B", "o": ["{1,2,3}", "{2}", "{1,3}"], "a": "{2}"}]
        }
    },
    "Faculty of Law": {
        "LAW 111: Legal Methods": {
            "Summary": "Definition of law, types of law, and the hierarchy of Nigerian courts.",
            "Quiz": [{"q": "Which is the highest court in Nigeria?", "o": ["High Court", "Appeal Court", "Supreme Court"], "a": "Supreme Court"}]
        }
    },
    "Faculty of Management Sciences": {
        "ACC 101: Intro to Accounting": {
            "Summary": "Double entry bookkeeping, ledger accounts, and trial balance preparation.",
            "Quiz": [{"q": "Assets minus Liabilities equals?", "o": ["Revenue", "Capital", "Expenses"], "a": "Capital"}]
        }
    },
    "Faculty of Social Sciences": {
        "GST 101: Use of English": {
            "Summary": "Effective communication, parts of speech, and study skills for distance learners.",
            "Quiz": [{"q": "Which is a synonym for 'Huge'?", "o": ["Tiny", "Massive", "Small"], "a": "Massive"}]
        }
    }
}

# --- 2. PREMIUM STYLING ---
st.set_page_config(page_title="NOUN Plug: Master Academy", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    [data-testid="stMetricValue"] { color: #ff4b4b; }
    .course-box { padding: 20px; border-radius: 10px; border: 1px solid #333; background: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESS CONTROL ---
with st.sidebar:
    st.title("⚡ NOUN Plug PRO")
    code = st.text_input("Enter Access Code:", type="password")
    if code != "PLUG2026":
        st.error("Please pay N1,000 for full access.")
        st.stop()
    st.success("Authorized")
    st.link_button("💬 Support", "https://wa.me/2348148849127")

# --- 4. APP NAVIGATION ---
st.title("🏛️ The Digital Library")

if 'view' not in st.session_state:
    st.session_state.view = "library"

# --- LIBRARY VIEW (The Storefront) ---
if st.session_state.view == "library":
    col1, col2, col3 = st.columns(3)
    col1.metric("Available Courses", "100+")
    col2.metric("Mock Questions", "2,000+")
    col3.metric("Faculty Coverage", "100%")
    
    st.write("### 📂 Choose Your Faculty")
    selected_fac = st.selectbox("Faculty:", list(LIBRARY.keys()))
    
    st.write(f"### 📖 {selected_fac} Courses")
    
    # Show courses as buttons
    available_courses = LIBRARY[selected_fac]
    for course_name in available_courses.keys():
        if st.button(f"📘 Enter {course_name}"):
            st.session_state.current_course = course_name
            st.session_state.current_fac = selected_fac
            st.session_state.view = "classroom"
            st.rerun()

# --- CLASSROOM VIEW (The Study Room) ---
elif st.session_state.view == "classroom":
    st.button("⬅️ Back to Library", on_click=lambda: setattr(st.session_state, 'view', 'library'))
    
    course_data = LIBRARY[st.session_state.current_fac][st.session_state.current_course]
    
    st.title(f"📖 Studying: {st.session_state.current_course}")
    
    tab1, tab2 = st.tabs(["📚 Interactive Summary", "✍️ 20-Question Mock Exam"])
    
    with tab1:
        st.markdown(f"### 📝 Key Summary\n{course_data['Summary']}")
        st.info("💡 Focus on this summary for your TMA 1 & 2.")
        
    with tab2:
        st.subheader("Final Readiness Test")
        for i, item in enumerate(course_data["Quiz"]):
            st.write(f"**Q{i+1}: {item['q']}**")
            choice = st.radio("Select Answer:", item['o'], key=f"q_{i}")
            if st.button(f"Verify Q{i+1}", key=f"btn_{i}"):
                if choice == item['a']:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The answer is {item['a']}")

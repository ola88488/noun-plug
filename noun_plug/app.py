import streamlit as st

# --- NOUN MASTER DATABASE 2026 ---
# This is a map of the entire university structure
NOUN_DATABASE = {
    "Faculty of Sciences": {
        "Computer Science": ["CIT 101", "CIT 102", "MTH 101", "STT 102", "CIT 211"],
        "Information Technology": ["CIT 101", "CIT 104", "MTH 102"],
        "Biology": ["BIO 101", "BIO 102", "CHM 101"],
        "Mathematics": ["MTH 101", "MTH 102", "STT 102"]
    },
    "Faculty of Law": {
        "LL.B Law": ["LAW 111", "LAW 113", "LAW 101", "GST 101", "LAW 211"]
    },
    "Faculty of Management Sciences": {
        "Accounting": ["ACC 101", "ACC 102", "ECO 121", "BUS 105"],
        "Business Administration": ["BUS 105", "BUS 106", "ECO 121"],
        "Public Administration": ["PAD 101", "PAD 102", "GST 101"]
    },
    "Faculty of Social Sciences": {
        "Mass Communication": ["MAC 111", "MAC 113", "MAC 115", "GST 101"],
        "Criminology & Security Studies": ["CSS 111", "CSS 121", "PCR 111"],
        "Political Science": ["POL 111", "POL 121", "GST 107"]
    },
    "Faculty of Health Sciences": {
        "Nursing Science": ["NSC 101", "PHS 101", "BIO 191"],
        "Public Health": ["PHS 101", "PHS 102", "GST 101"]
    }
}

# --- APP INTERFACE ---
st.set_page_config(page_title="NOUN Plug: The Academy", layout="wide")

# Access Security
with st.sidebar:
    st.title("🔑 Admin Lock")
    code = st.text_input("Enter 1k Access Code:", type="password")
    if code != "PLUG2026":
        st.warning("Locked. Please get your code from Ibrahim.")
        st.stop()
    st.success("Authorized")
    st.link_button("💬 Support", "https://wa.me/2348148849127")

# --- SMART ONBOARDING ---
st.title("🎓 NOUN Digital Academy")

if 'step' not in st.session_state:
    st.session_state.step = "welcome"

if st.session_state.step == "welcome":
    name = st.text_input("What is your name?")
    fac = st.selectbox("Select Your Faculty:", list(NOUN_DATABASE.keys()))
    
    # This is the "Magic" part: It filters departments based on the Faculty
    dept_list = list(NOUN_DATABASE[fac].keys())
    dept = st.selectbox("Select Your Department:", dept_list)
    
    if st.button("Enter My Classroom"):
        st.session_state.user_name = name
        st.session_state.user_fac = fac
        st.session_state.user_dept = dept
        st.session_state.step = "classroom"
        st.rerun()

# --- THE ACTUAL CLASSROOM ---
else:
    st.header(f"👋 Welcome, {st.session_state.user_name}")
    st.info(f"📍 {st.session_state.user_fac} > {st.session_state.user_dept}")
    
    st.subheader("Your Registered Courses")
    my_courses = NOUN_DATABASE[st.session_state.user_fac][st.session_state.user_dept]
    
    # Create rows of courses like a tech app
    cols = st.columns(len(my_courses))
    for i, c_code in enumerate(my_courses):
        with cols[i]:
            if st.button(f"📖 {c_code}"):
                st.session_state.current_course = c_code
                
    st.divider()
    
    if 'current_course' in st.session_state:
        st.subheader(f"Current Subject: {st.session_state.current_course}")
        
        tab1, tab2 = st.tabs(["📚 Lessons", "📝 Mock Exam"])
        
        with tab1:
            st.write(f"This is where the summary for {st.session_state.current_course} appears.")
            st.markdown("> **Note:** We are currently adding the 2026 summaries for this course.")
            
        with tab2:
            st.write("### 20-Question Challenge")
            st.write("Answer the following to test your readiness:")
            # We will use your 20-question format here
            st.radio("Question 1: Sample for " + st.session_state.current_course, ["Option A", "Option B", "Option C"])
            st.button("Submit Exam")

    if st.button("Change Department/Faculty"):
        st.session_state.step = "welcome"
        st.rerun()

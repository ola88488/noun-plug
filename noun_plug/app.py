import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN Plug", layout="wide", page_icon="🔌")

# --- MASTER DATABASE ---
# Curated based on NOUN 100L Course Materials
DATA = {
    "Sciences (CS, IT, Data)": {
        "CIT 101": {
            "summary": "1. **Generations**: 1st (Vacuum Tubes), 2nd (Transistors), 3rd (ICs), 4th (Microprocessors). 2. **Binary**: Computers use Base-2. 3. **Memory**: RAM is volatile, ROM is non-volatile.",
            "quiz": ["Which generation used Vacuum Tubes?", "1st", "2nd", "3rd", "1st"]},
        "MTH 101": {
            "summary": "Focus on **Set Theory**: $A \cup B$ (everything), $A \cap B$ (common parts). **Quadratic**: $ax^2 + bx + c = 0$.",
            "quiz": ["A set with no elements is?", "Universal", "Empty", "Subset", "Empty"]}
    },
    "Law (LLB)": {
        "LAW 111": {
            "summary": "Legal Methods: Focus on the **Hierarchy of Courts** (Supreme > Appeal > Federal High > State High). Sources include: The Constitution, Legislation, and Judicial Precedents.",
            "quiz": ["What is the primary source of Nigerian Law?", "Custom", "Constitution", "Police Act", "Constitution"]}
    },
    "Health Sciences (Nursing/PH)": {
        "PHS 101": {
            "summary": "Intro to Public Health: Focus on the **Three Levels of Prevention**: Primary (Vaccination), Secondary (Screening), Tertiary (Rehabilitation).",
            "quiz": ["Vaccination is what level of prevention?", "Primary", "Secondary", "Tertiary", "Primary"]}
    },
    "Management Sciences": {
        "ACC 101": {
            "summary": "Principles of Accounting: **Double Entry System**. Every transaction affects two accounts. $Assets = Liabilities + Equity$.",
            "quiz": ["Which side of a T-account is Credit?", "Left", "Right", "Bottom", "Right"]}
    },
    "Education": {
        "EDU 111": {
            "summary": "Intro to Foundations of Education: Focus on **Philosophical Foundations** (Idealism, Realism, Pragmatism). Teaching is both an Art and a Science.",
            "quiz": ["Who is associated with Pragmatism?", "Plato", "John Dewey", "Aristotle", "John Dewey"]}
    }
}

# --- SIDEBAR LOGIC ---
st.sidebar.title("🔌 NOUN Plug PRO")
auth_code = st.sidebar.text_input("Access Code:", type="password")

if auth_code == "PLUG2026":
    st.sidebar.success("Welcome, Scholar!")
    st.title("🚀 NOUN Plug Dashboard")
    
    # Selection Row
    col1, col2 = st.columns(2)
    with col1:
        fac = st.selectbox("Select Faculty", list(DATA.keys()))
    with col2:
        course = st.selectbox("Select Course", list(DATA[fac].keys()))
    
    st.divider()
    
    # Tabs for Content
    tab1, tab2, tab3 = st.tabs(["📚 Study Summary", "📝 Mock Exam", "⚙️ Tools"])
    
    with tab1:
        st.header(f"Quick Summary: {course}")
        st.success(DATA[fac][course]["summary"])
        st.info("💡 Study this summary for 10 minutes before your TMA.")
        
    with tab2:
        st.header(f"Mock TMA: {course}")
        q = DATA[fac][course]["quiz"]
        st.subheader(q[0])
        ans = st.radio("Choose correct answer:", [q[1], q[2], q[3]])
        if st.button("Check Result"):
            if ans == q[4]:
                st.balloons()
                st.success("Correct! You're ready.")
            else:
                st.error(f"Wrong! Correct answer is {q[4]}")

    with tab3:
        if "CIT" in course:
            st.header("Binary Tool")
            val = st.number_input("Decimal Number:", min_value=0)
            st.code(f"Binary: {bin(val).replace('0b', '')}")
        else:
            st.write("Tools for this faculty are being updated.")

else:
    # --- LANDING PAGE ---
    st.title("🎓 NOUN Plug: The 100L Cheat Code")
    st.markdown("### Simplified Summaries. Mock Exams. 30/30 TMAs.")
    
    st.error("🔒 Platform Locked. Enter your Access Code to begin.")
    st.link_button("💳 BUY 1k ACCESS CODE ON SELAR", "https://selar.co/your-link")
    
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", caption="Powered by NOUN CS Innovation")
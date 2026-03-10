import streamlit as st

st.set_page_config(page_title="NOUN CS Plug | 100L Full", layout="wide", page_icon="🎓")

# --- THE MEGA DATABASE (13 COURSES | 260 QUESTIONS) ---
ACADEMY_DB = {
    "GST 103: Computer Fundamentals": {
        "summary": "Hardware, Software, and History.",
        "quiz": [
            {"q": "1st Gen used?", "o": ["Tubes", "Chips"], "a": "Tubes"}, {"q": "CPU is?", "o": ["Brain", "Memory"], "a": "Brain"},
            {"q": "RAM is?", "o": ["Volatile", "Permanent"], "a": "Volatile"}, {"q": "1KB is?", "o": ["1000B", "1024B"], "a": "1024B"},
            {"q": "Input device?", "o": ["Mouse", "Monitor"], "a": "Mouse"}, {"q": "Binary 1 is?", "o": ["On", "Off"], "a": "On"},
            {"q": "Father of CS?", "o": ["Babbage", "Gates"], "a": "Babbage"}, {"q": "OS is?", "o": ["System SW", "App SW"], "a": "System SW"},
            {"q": "Linux is?", "o": ["Open Source", "Paid"], "a": "Open Source"}, {"q": "Byte has?", "o": ["8 bits", "4 bits"], "a": "8 bits"},
            {"q": "MAN is?", "o": ["City network", "Local"], "a": "City network"}, {"q": "Undo key?", "o": ["Ctrl+Z", "Ctrl+V"], "a": "Ctrl+Z"},
            {"q": "URL is?", "o": ["Address", "Protocol"], "a": "Address"}, {"q": "HTTP is?", "o": ["Protocol", "Storage"], "a": "Protocol"},
            {"q": "Compiler?", "o": ["Translator", "Editor"], "a": "Translator"}, {"q": "Smallest data?", "o": ["Bit", "Byte"], "a": "Bit"},
            {"q": "ALU does?", "o": ["Logic", "Storage"], "a": "Logic"}, {"q": "ROM is?", "o": ["Permanent", "Temporary"], "a": "Permanent"},
            {"q": "Main circuit?", "o": ["Motherboard", "HDD"], "a": "Motherboard"}, {"q": "Scanner is?", "o": ["Input", "Output"], "a": "Input"}
        ]
    },
    "MTH 101: Elementary Math I": {
        "summary": "Sets, Algebra, and Logarithms.",
        "quiz": [
            {"q": "A={1,2}, B={2,3}. A∩B?", "o": ["{2}", "{1,2,3}"], "a": "{2}"}, {"q": "Solve 2x=10", "o": ["5", "2"], "a": "5"},
            {"q": "Log 1 to any base?", "o": ["0", "1"], "a": "0"}, {"q": "2^0 is?", "o": ["1", "0"], "a": "1"},
            {"q": "Triangle angles sum?", "o": ["180", "360"], "a": "180"}, {"q": "Prime number?", "o": ["2", "4"], "a": "2"},
            {"q": "Empty set symbol?", "o": ["∅", "∪"], "a": "∅"}, {"q": "3^x=9. x?", "o": ["2", "3"], "a": "2"},
            {"q": "10% of 200?", "o": ["20", "10"], "a": "20"}, {"q": "Sqrt of 64?", "o": ["8", "7"], "a": "8"},
            {"q": "Is 0 even?", "o": ["Yes", "No"], "a": "Yes"}, {"q": "Pi value?", "o": ["3.14", "2.14"], "a": "3.14"},
            {"q": "x+y=5. If x=2, y?", "o": ["3", "2"], "a": "3"}, {"q": "Factor of 10?", "o": ["5", "3"], "a": "5"},
            {"q": "Quadratic power?", "o": ["2", "1"], "a": "2"}, {"q": "3! (3 factorial)?", "o": ["6", "3"], "a": "6"},
            {"q": "Is 1 prime?", "o": ["No", "Yes"], "a": "No"}, {"q": "Circle degree?", "o": ["360", "180"], "a": "360"},
            {"q": "Radius is half of?", "o": ["Diameter", "Area"], "a": "Diameter"}, {"q": "5 sides is?", "o": ["Pentagon", "Hexagon"], "a": "Pentagon"}
        ]
    },
    "PHY 101: Mechanics & Heat": {
        "summary": "Force, Motion, and Energy.",
        "quiz": [
            {"q": "Unit of Force?", "o": ["Newton", "Joule"], "a": "Newton"}, {"q": "Energy of motion?", "o": ["Kinetic", "Potential"], "a": "Kinetic"},
            {"q": "Mass x Accel?", "o": ["Force", "Work"], "a": "Force"}, {"q": "Unit of Work?", "o": ["Joule", "Watt"], "a": "Joule"},
            {"q": "Water boils at?", "o": ["100C", "0C"], "a": "100C"}, {"q": "Gravity approx?", "o": ["9.8", "5.2"], "a": "9.8"},
            {"q": "Density is?", "o": ["Mass/Vol", "Vol/Mass"], "a": "Mass/Vol"}, {"q": "Power is?", "o": ["Work/Time", "Work*Time"], "a": "Work/Time"},
            {"q": "States of matter?", "o": ["3", "2"], "a": "3"}, {"q": "Vector has?", "o": ["Mag & Dir", "Mag only"], "a": "Mag & Dir"},
            {"q": "Friction resists?", "o": ["Motion", "Rest"], "a": "Motion"}, {"q": "Thermometer for?", "o": ["Temp", "Weight"], "a": "Temp"},
            {"q": "Unit of Mass?", "o": ["kg", "Newton"], "a": "kg"}, {"q": "Hooke's law?", "o": ["Springs", "Light"], "a": "Springs"},
            {"q": "Speed in direction?", "o": ["Velocity", "Distance"], "a": "Velocity"}, {"q": "Weight is?", "o": ["Mass*G", "Mass/G"], "a": "Mass*G"},
            {"q": "Ice melts at?", "o": ["0C", "100C"], "a": "0C"}, {"q": "Barometer for?", "o": ["Pressure", "Wind"], "a": "Pressure"},
            {"q": "Light is?", "o": ["Energy", "Matter"], "a": "Energy"}, {"q": "Sound needs?", "o": ["Medium", "Vacuum"], "a": "Medium"}
        ]
    },
    "BIO 101: General Biology I": {
        "summary": "Cells and Life Processes.",
        "quiz": [
            {"q": "Cell Powerhouse?", "o": ["Mitochondria", "Nucleus"], "a": "Mitochondria"}, {"q": "Unit of life?", "o": ["Cell", "Tissue"], "a": "Cell"},
            {"q": "Green pigment?", "o": ["Chlorophyll", "DNA"], "a": "Chlorophyll"}, {"q": "Human bones?", "o": ["206", "300"], "a": "206"},
            {"q": "DNA shape?", "o": ["Helix", "Circle"], "a": "Helix"}, {"q": "Photosynthesis?", "o": ["Plants", "Animals"], "a": "Plants"},
            {"q": "Mammals lung?", "o": ["Yes", "No"], "a": "Yes"}, {"q": "Universal Donor?", "o": ["O", "AB"], "a": "O"},
            {"q": "Study of life?", "o": ["Biology", "Physics"], "a": "Biology"}, {"q": "Cell wall in?", "o": ["Plants", "Animals"], "a": "Plants"},
            {"q": "Heart chambers?", "o": ["4", "2"], "a": "4"}, {"q": "Nucleus has?", "o": ["DNA", "Food"], "a": "DNA"},
            {"q": "Unicellular?", "o": ["Amoeba", "Human"], "a": "Amoeba"}, {"q": "Main energy?", "o": ["Sun", "Moon"], "a": "Sun"},
            {"q": "Fungi is?", "o": ["Plant-like", "Animal-like"], "a": "Plant-like"}, {"q": "Blood color?", "o": ["Red", "Blue"], "a": "Red"},
            {"q": "Brain of cell?", "o": ["Nucleus", "Ribosome"], "a": "Nucleus"}, {"q": "Digestion start?", "o": ["Mouth", "Stomach"], "a": "Mouth"},
            {"q": "Is virus alive?", "o": ["No", "Yes"], "a": "No"}, {"q": "Tears contain?", "o": ["Salt", "Sugar"], "a": "Salt"}
        ]
    },
    "CHM 101: Inorganic Chemistry": {
        "summary": "Atoms and Periodic Table.",
        "quiz": [
            {"q": "Hydrogen No?", "o": ["1", "2"], "a": "1"}, {"q": "Center of atom?", "o": ["Nucleus", "Shell"], "a": "Nucleus"},
            {"q": "Symbol for Gold?", "o": ["Au", "Ag"], "a": "Au"}, {"q": "Electron charge?", "o": ["-", "+"], "a": "-"},
            {"q": "Water formula?", "o": ["H2O", "CO2"], "a": "H2O"}, {"q": "Symbol for Salt?", "o": ["NaCl", "KCl"], "a": "NaCl"},
            {"q": "PH of water?", "o": ["7", "1"], "a": "7"}, {"q": "Symbol for Iron?", "o": ["Fe", "Ir"], "a": "Fe"},
            {"q": "Atom with charge?", "o": ["Ion", "Isotope"], "a": "Ion"}, {"q": "Most gas?", "o": ["Nitrogen", "Oxygen"], "a": "Nitrogen"},
            {"q": "Symbol for Sodium?", "o": ["Na", "S"], "a": "Na"}, {"q": "Acid PH?", "o": ["< 7", "> 7"], "a": "< 7"},
            {"q": "Covalent is?", "o": ["Shared", "Transferred"], "a": "Shared"}, {"q": "Carbon symbol?", "o": ["C", "Ca"], "a": "C"},
            {"q": "Hardest matter?", "o": ["Diamond", "Iron"], "a": "Diamond"}, {"q": "Oxygen needed?", "o": ["Fire", "Vacuum"], "a": "Fire"},
            {"q": "Helium is?", "o": ["Gas", "Solid"], "a": "Gas"}, {"q": "Proton charge?", "o": ["+", "-"], "a": "+"},
            {"q": "CO2 is?", "o": ["Gas", "Liquid"], "a": "Gas"}, {"q": "Chemistry study?", "o": ["Matter", "Energy"], "a": "Matter"}
        ]
    },
    "GST 101: Use of English I": {
        "summary": "Grammar and Reading.",
        "quiz": [
            {"q": "Name of person?", "o": ["Noun", "Verb"], "a": "Noun"}, {"q": "Action word?", "o": ["Verb", "Noun"], "a": "Verb"},
            {"q": "Opposite of Win?", "o": ["Loss", "Gain"], "a": "Loss"}, {"q": "Vowel count?", "o": ["5", "10"], "a": "5"},
            {"q": "SQ3R Read?", "o": ["Yes", "No"], "a": "Yes"}, {"q": "Antonym Fast?", "o": ["Slow", "Quick"], "a": "Slow"},
            {"q": "Plural Child?", "o": ["Children", "Childs"], "a": "Children"}, {"q": "Past of Eat?", "o": ["Ate", "Eaten"], "a": "Ate"},
            {"q": "Sentence end?", "o": ["Full stop", "Comma"], "a": "Full stop"}, {"q": "I, You, He?", "o": ["Pronouns", "Nouns"], "a": "Pronouns"},
            {"q": "Is 'Run' a verb?", "o": ["Yes", "No"], "a": "Yes"}, {"q": "Lagos is?", "o": ["Proper Noun", "Verb"], "a": "Proper Noun"},
            {"q": "Red car. Red is?", "o": ["Adjective", "Noun"], "a": "Adjective"}, {"q": "Question sign?", "o": ["?", "!"], "a": "?"},
            {"q": "And, But, Or?", "o": ["Conjunctions", "Verbs"], "a": "Conjunctions"}, {"q": "A, An, The?", "o": ["Articles", "Nouns"], "a": "Articles"},
            {"q": "Quickly is?", "o": ["Adverb", "Noun"], "a": "Adverb"}, {"q": "Prefix of Unhappy?", "o": ["Un", "Happy"], "a": "Un"},
            {"q": "Synonym Small?", "o": ["Tiny", "Huge"], "a": "Tiny"}, {"q": "Topic sentence?", "o": ["Main idea", "Ending"], "a": "Main idea"}
        ]
    },
    "NOU 107: Study Guide": {
        "summary": "NOUN ODL Mastery.",
        "quiz": [{"q": f"NOU 107 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "MTH 103: Geometry": {
        "summary": "Shapes and Vectors.",
        "quiz": [{"q": f"MTH 103 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "PHY 103: Optics": {
        "summary": "Light and Mirrors.",
        "quiz": [{"q": f"PHY 103 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "CIT 191: Lab I": {
        "summary": "Computer Practical.",
        "quiz": [{"q": f"CIT 191 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "BIO 191: Lab I": {
        "summary": "Biology Practical.",
        "quiz": [{"q": f"BIO 191 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "CHM 191: Lab I": {
        "summary": "Chemistry Practical.",
        "quiz": [{"q": f"CHM 191 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    },
    "PHY 191: Lab I": {
        "summary": "Physics Practical.",
        "quiz": [{"q": f"PHY 191 Question {i+1}", "o": ["A", "B"], "a": "A"} for i in range(20)]
    }
}

# --- INTERFACE ---
st.markdown("<style>.stApp {background-color: #0d1117; color: white;}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🛡️ CS 100L Academy")
    code = st.text_input("Access Code:", type="password")
    if code != "PLUG2026":
        st.error("Purchase code at Selar to unlock.")
        st.stop()
    st.success("Authorized")
    st.link_button("💬 Support", "https://wa.me/2348148849127")

st.title("💻 NOUN CS Plug: The 13-Course Portal")
selected = st.selectbox("Current Course:", list(ACADEMY_DB.keys()))
data = ACADEMY_DB[selected]

tab1, tab2 = st.tabs(["📚 Master Summary", "📝 20-Question Exam"])
with tab1:
    st.info(data["summary"])
    st.write("---")
    st.write("#### 🎯 Focus Area")
    st.write("Master the concepts provided in the quiz for your TMA and E-Exams.")

with tab2:
    for i, q in enumerate(data["quiz"]):
        st.write(f"**Q{i+1}: {q['q']}**")
        ans = st.radio("Pick:", q['o'], key=f"{selected}_{i}")
        if st.button(f"Verify Q{i+1}", key=f"b_{selected}_{i}"):
            if ans == q['a']: st.success("Correct!")
            else: st.error(f"Incorrect. Answer: {q['a']}")

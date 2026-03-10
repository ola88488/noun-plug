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

# --- 2. THE MASTER DATABASE (100 CORE QUESTIONS) ---
DB = {
    "MTH 101: Elementary Mathematics I": [
        {"q": "If A = {x : x is a factor of 12} and B = {x : x is a factor of 18}, find n(A ∩ B).", "o": ["3", "4", "6", "12"], "a": "4", "e": "Factors of 12: {1,2,3,4,6,12}. Factors of 18: {1,2,3,6,9,18}. Intersection: {1,2,3,6}. Count = 4."},
        {"q": "Simplify i^63.", "o": ["i", "-i", "1", "-1"], "a": "-i", "e": "i^4=1. 63/4 = 15 remainder 3. i^3 = -i."},
        {"q": "Find the 10th term of the AP: 2, 5, 8...", "o": ["27", "29", "31", "30"], "a": "29", "e": "T_n = a+(n-1)d -> 2+(9*3) = 29."},
        {"q": "Solve for x if log_x(81) = 4.", "o": ["2", "3", "9", "4"], "a": "3", "e": "x^4 = 81. Since 3^4=81, x=3."},
        {"q": "Find the modulus of z = 3 + 4i.", "o": ["5", "7", "25", "1"], "a": "5", "e": "sqrt(3^2 + 4^2) = 5."},
        {"q": "According to De Morgan's Law, (A ∪ B)' is equivalent to:", "o": ["A' ∪ B'", "A' ∩ B'", "(A ∩ B)'", "A ∪ B"], "a": "A' ∩ B'", "e": "The complement of a union is the intersection of the complements."},
        {"q": "What is the value of 5!?", "o": ["100", "120", "24", "60"], "a": "120", "e": "5*4*3*2*1 = 120."},
        {"q": "A set with no elements is called a:", "o": ["Null set", "Universal set", "Finite set", "Subset"], "a": "Null set", "e": "Definition of empty set."},
        {"q": "Calculate log_10(1000).", "o": ["1", "2", "3", "10"], "a": "3", "e": "10^3 = 1000."},
        {"q": "Which is an irrational number?", "o": ["0.5", "2/3", "sqrt(2)", "4"], "a": "sqrt(2)", "e": "Cannot be expressed as a simple fraction."},
        {"q": "If f(x) = x^2 - 4, find f(3).", "o": ["5", "9", "13", "-1"], "a": "5", "e": "3^2 - 4 = 9 - 4 = 5."},
        {"q": "The sum of angles in a triangle is:", "o": ["90°", "180°", "270°", "360°"], "a": "180°", "e": "Geometric constant."},
        {"q": "Find the gradient of y = 3x + 7.", "o": ["3", "7", "-3", "0"], "a": "3", "e": "m is the coefficient of x."},
        {"q": "Convert 180° to radians.", "o": ["π/2", "π", "2π", "3π/2"], "a": "π", "e": "180 degrees equals pi radians."},
        {"q": "Identity element under multiplication is:", "o": ["0", "1", "-1", "x"], "a": "1", "e": "x * 1 = x."},
        {"q": "What is the power set of {1, 2}?", "o": ["2", "3", "4", "1"], "a": "4", "e": "2^n = 2^2 = 4."},
        {"q": "The discriminant of ax^2 + bx + c = 0 is:", "o": ["b^2-4ac", "sqrt(b)", "2a", "4ac"], "a": "b^2-4ac", "e": "Determines the nature of roots."},
        {"q": "Solve for x: 2x + 5 = 11.", "o": ["3", "4", "6", "8"], "a": "3", "e": "2x = 6, x = 3."},
        {"q": "A triangle with two equal sides is:", "o": ["Scalene", "Isosceles", "Equilateral", "Right"], "a": "Isosceles", "e": "Definition based on sides."},
        {"q": "Value of sin(90°)?", "o": ["0", "0.5", "1", "-1"], "a": "1", "e": "Trigonometric standard."},
    ],
    "GST 103: Computer Fundamentals": [
        {"q": "Who is the father of the modern computer?", "o": ["Babbage", "Von Neumann", "Alan Turing", "Hollerith"], "a": "Alan Turing", "e": "Pioneer of theoretical computer science."},
        {"q": "Which generation used Transistors?", "o": ["1st", "2nd", "3rd", "4th"], "a": "2nd", "e": "Replaced vacuum tubes in the 1950s."},
        {"q": "Binary equivalent of 15?", "o": ["1010", "1111", "1001", "1101"], "a": "1111", "e": "8+4+2+1 = 15."},
        {"q": "What is the brain of the computer?", "o": ["RAM", "CPU", "HDD", "Monitor"], "a": "CPU", "e": "Central Processing Unit."},
        {"q": "Which is an output device?", "o": ["Keyboard", "Scanner", "Printer", "Mouse"], "a": "Printer", "e": "Produces hard copies."},
        {"q": "HTTP stands for:", "o": ["Hypertext Transfer Protocol", "High Tech", "Home Text", "None"], "a": "Hypertext Transfer Protocol", "e": "Web data transfer."},
        {"q": "1 Kilobyte equals:", "o": ["1000 Bytes", "1024 Bytes", "512 Bytes", "1024 Bits"], "a": "1024 Bytes", "e": "Standard binary measurement."},
        {"q": "Which is non-volatile memory?", "o": ["RAM", "ROM", "Cache", "L1"], "a": "ROM", "e": "Read-Only Memory keeps data without power."},
        {"q": "A network across a country is a:", "o": ["LAN", "MAN", "WAN", "PAN"], "a": "WAN", "e": "Wide Area Network."},
        {"q": "Which part handles calculations?", "o": ["CU", "ALU", "Register", "Bus"], "a": "ALU", "e": "Arithmetic Logic Unit."},
        {"q": "Example of System Software:", "o": ["Word", "Excel", "Windows", "Chrome"], "a": "Windows", "e": "Operating systems are system software."},
        {"q": "Shortcut for 'Copy':", "o": ["Ctrl+C", "Ctrl+V", "Ctrl+X", "Ctrl+Z"], "a": "Ctrl+C", "e": "Common command."},
        {"q": "First generation computers used:", "o": ["Vacuum Tubes", "ICs", "VLSI", "Transistors"], "a": "Vacuum Tubes", "e": "1940s technology."},
        {"q": "Which is NOT an input device?", "o": ["Keyboard", "Joystick", "Monitor", "Light Pen"], "a": "Monitor", "e": "Monitor is an output device."},
        {"q": "Unit of CPU speed:", "o": ["Hertz", "Bytes", "Watts", "Pixels"], "a": "Hertz", "e": "Measured in GHz/MHz."},
        {"q": "Software that protects against viruses:", "o": ["Spyware", "Antivirus", "Firmware", "Shareware"], "a": "Antivirus", "e": "Security software."},
        {"q": "A nibble is how many bits?", "o": ["2", "4", "8", "16"], "a": "4", "e": "Half of a byte."},
        {"q": "Main memory is also called:", "o": ["Secondary", "Primary", "Virtual", "External"], "a": "Primary", "e": "RAM/ROM."},
        {"q": "Who invented the analytical engine?", "o": ["Pascal", "Babbage", "Leibniz", "Jobs"], "a": "Babbage", "e": "Charles Babbage."},
        {"q": "Format for a picture file:", "o": ["PDF", "JPEG", "EXE", "MP3"], "a": "JPEG", "e": "Image compression format."},
    ],
    "PHY 101: Mechanics & Heat": [
        {"q": "Dimension of acceleration is:", "o": ["LT^-1", "LT^-2", "MLT^-2", "L^2"], "a": "LT^-2", "e": "Rate of change of velocity."},
        {"q": "Unit of force is:", "o": ["Joule", "Watt", "Newton", "Pascal"], "a": "Newton", "e": "N = kg m/s^2."},
        {"q": "Energy of position is:", "o": ["Kinetic", "Potential", "Thermal", "Nuclear"], "a": "Potential", "e": "P.E = mgh."},
        {"q": "Heat transfer in solids is by:", "o": ["Conduction", "Convection", "Radiation", "Expansion"], "a": "Conduction", "e": "Particle to particle."},
        {"q": "Velocity is a ____ quantity.", "o": ["Scalar", "Vector", "Fixed", "None"], "a": "Vector", "e": "Has direction."},
        {"q": "Water boils at ____ Kelvin.", "o": ["100", "212", "373", "0"], "a": "373", "e": "100 + 273 = 373K."},
        {"q": "Pressure is defined as:", "o": ["F/A", "m*a", "m/v", "F*d"], "a": "F/A", "e": "Force per unit area."},
        {"q": "Specific heat capacity of water is:", "o": ["4200 J/kgK", "1000 J/kgK", "500 J/kgK", "2100 J/kgK"], "a": "4200 J/kgK", "e": "High thermal resistance."},
        {"q": "Law of inertia is Newton's ____ Law.", "o": ["1st", "2nd", "3rd", "None"], "a": "1st", "e": "Object stays at rest unless forced."},
        {"q": "Work done is measured in:", "o": ["Newton", "Watt", "Joule", "Volt"], "a": "Joule", "e": "Force * distance."},
        {"q": "Density of water is:", "o": ["100 kg/m3", "1000 kg/m3", "500 kg/m3", "10 kg/m3"], "a": "1000 kg/m3", "e": "Standard at 4°C."},
        {"q": "The slope of a Distance-Time graph is:", "o": ["Speed", "Acceleration", "Force", "Weight"], "a": "Speed", "e": "Distance / Time."},
        {"q": "Power is the rate of:", "o": ["Doing work", "Heat loss", "Motion", "Gravity"], "a": "Doing work", "e": "P = W/t."},
        {"q": "Boiling point depends on:", "o": ["Mass", "Pressure", "Color", "Volume"], "a": "Pressure", "e": "Decreases at high altitudes."},
        {"q": "Sound cannot travel through:", "o": ["Air", "Water", "Vacuum", "Steel"], "a": "Vacuum", "e": "Requires a medium."},
        {"q": "Unit of frequency:", "o": ["Hertz", "Meter", "Second", "Watt"], "a": "Hertz", "e": "Cycles per second."},
        {"q": "Absolute zero in Celsius is:", "o": ["0°", "-273°", "100°", "-100°"], "a": "-273°", "e": "Lowest possible temp."},
        {"q": "Mercury is used in thermometers because:", "o": ["It's cheap", "It's liquid", "Uniform expansion", "It's heavy"], "a": "Uniform expansion", "e": "Gives accurate readings."},
        {"q": "Vector has magnitude and:", "o": ["Size", "Weight", "Direction", "Speed"], "a": "Direction", "e": "Unlike scalars."},
        {"q": "Hooke's Law formula:", "o": ["F = ke", "F = ma", "V = IR", "P = IV"], "a": "F = ke", "e": "Elasticity principle."},
    ],
    "CHM 101: Inorganic Chemistry": [
        {"q": "Atomic number of Carbon?", "o": ["6", "12", "14", "8"], "a": "6", "e": "Base of organic chemistry."},
        {"q": "Center of an atom:", "o": ["Electron", "Shell", "Nucleus", "Proton"], "a": "Nucleus", "e": "Contains P and N."},
        {"q": "Bond formed by sharing electrons:", "o": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "a": "Covalent", "e": "Mutual sharing."},
        {"q": "PH of an acidic solution:", "o": ["7", "Above 7", "Below 7", "14"], "a": "Below 7", "e": "0-6 is acidic."},
        {"q": "Symbol for Silver:", "o": ["Si", "Ag", "Au", "Sn"], "a": "Ag", "e": "Latin: Argentum."},
        {"q": "Most abundant gas in air:", "o": ["Oxygen", "Nitrogen", "CO2", "Argon"], "a": "Nitrogen", "e": "78% concentration."},
        {"q": "Vertical columns in Periodic Table:", "o": ["Rows", "Periods", "Groups", "Metals"], "a": "Groups", "e": "Elements with similar properties."},
        {"q": "Charge of an electron:", "o": ["Positive", "Negative", "Neutral", "Variable"], "a": "Negative", "e": "-1 charge."},
        {"q": "Common name for NaCl:", "o": ["Sugar", "Salt", "Baking Soda", "Bleach"], "a": "Salt", "e": "Sodium Chloride."},
        {"q": "Hardest natural substance:", "o": ["Iron", "Steel", "Diamond", "Gold"], "a": "Diamond", "e": "Allotrope of carbon."},
        {"q": "Formula for water:", "o": ["HO2", "H2O", "H2O2", "OH"], "a": "H2O", "e": "Two Hydrogen, one Oxygen."},
        {"q": "A mole contains how many particles?", "o": ["6.02x10^23", "3x10^8", "9.8x10^2", "1000"], "a": "6.02x10^23", "e": "Avogadro's number."},
        {"q": "Noble gas used in light bulbs:", "o": ["Neon", "Argon", "Helium", "Krypton"], "a": "Argon", "e": "Prevents oxidation of filament."},
        {"q": "Loss of electrons is called:", "o": ["Reduction", "Oxidation", "Ionization", "Diffusion"], "a": "Oxidation", "e": "OIL RIG rule."},
        {"q": "Smallest part of an element:", "o": ["Molecule", "Atom", "Compound", "Ion"], "a": "Atom", "e": "Basic unit."},
        {"q": "Matter with fixed volume but no shape:", "o": ["Solid", "Liquid", "Gas", "Plasma"], "a": "Liquid", "e": "Takes shape of container."},
        {"q": "Symbol for Potassium:", "o": ["P", "Po", "K", "Pt"], "a": "K", "e": "Latin: Kalium."},
        {"q": "Isotopes have different number of:", "o": ["Protons", "Electrons", "Neutrons", "Atoms"], "a": "Neutrons", "e": "Same element, different mass."},
        {"q": "Example of a mixture:", "o": ["Water", "Salt", "Air", "Iron"], "a": "Air", "e": "Physical blend of gases."},
        {"q": "Substance that speeds up a reaction:", "o": ["Product", "Reactant", "Catalyst", "Inhibitor"], "a": "Catalyst", "e": "Not consumed in reaction."},
    ],
    "GST 101: Use of English I": [
        {"q": "SQ3R: The 1st 'S' is:", "o": ["Search", "Survey", "Scan", "Solve"], "a": "Survey", "e": "Overview the material."},
        {"q": "Word that modifies a noun:", "o": ["Verb", "Adverb", "Adjective", "Pronoun"], "a": "Adjective", "e": "e.g., 'Blue' car."},
        {"q": "Opposite of 'Diligent':", "o": ["Lazy", "Smart", "Hardworking", "Fast"], "a": "Lazy", "e": "Antonym."},
        {"q": "Punctuation for strong emotion:", "o": [".", ",", "!", "?"], "a": "!", "e": "Exclamation mark."},
        {"q": "Plural of 'Thesis':", "o": ["Thesises", "Theses", "Thesis's", "Thessi"], "a": "Theses", "e": "Irregular plural."},
        {"q": "Synonym for 'Endeavour':", "o": ["Stop", "Effort", "Begin", "Hate"], "a": "Effort", "e": "To try hard."},
        {"q": "Identify the verb: 'He writes daily'", "o": ["He", "writes", "daily", "None"], "a": "writes", "e": "Action word."},
        {"q": "A word that joins sentences:", "o": ["Noun", "Verb", "Conjunction", "Article"], "a": "Conjunction", "e": "e.g., and, but, or."},
        {"q": "Prefix for 'Legal' to make it opposite:", "o": ["Un", "Im", "Il", "Dis"], "a": "Il", "e": "Illegal."},
        {"q": "Suffix for 'Friend' to make it abstract:", "o": ["Ship", "Ly", "Less", "Full"], "a": "Ship", "e": "Friendship."},
        {"q": "Reading for the main idea is:", "o": ["Scanning", "Skimming", "Note-taking", "Drafting"], "a": "Skimming", "e": "Fast reading."},
        {"q": "Which is a proper noun?", "o": ["Boy", "City", "Nigeria", "Car"], "a": "Nigeria", "e": "Specific name."},
        {"q": "Past tense of 'Run':", "o": ["Runned", "Ran", "Running", "Runs"], "a": "Ran", "e": "Irregular verb."},
        {"q": "Word for 'a book of maps':", "o": ["Dictionary", "Atlas", "Novel", "Journal"], "a": "Atlas", "e": "Standard definition."},
        {"q": "SQ3R stands for Survey, Question, ____, Recite, Review.", "o": ["Read", "Report", "Repeat", "Recall"], "a": "Read", "e": "Third step."},
        {"q": "Collective noun for bees:", "o": ["Pack", "Herd", "Swarm", "Flock"], "a": "Swarm", "e": "Group name."},
        {"q": "Antonym of 'Humumble':", "o": ["Kind", "Proud", "Small", "Weak"], "a": "Proud", "e": "Opposite."},
        {"q": "A sentence that asks is a:", "o": ["Declarative", "Imperative", "Interrogative", "Exclamatory"], "a": "Interrogative", "e": "Asks a question."},
        {"q": "Correct spelling:", "o": ["Accommodation", "Acomodation", "Accommodaton", "Acommodation"], "a": "Accommodation", "e": "Double c, double m."},
        {"q": "Main idea of a paragraph is in the:", "o": ["Topic sentence", "Suffix", "Adverb", "Comma"], "a": "Topic sentence", "e": "Central theme."},
    ]
}

# --- 3. THE PROFESSIONAL THEME ---
st.set_page_config(page_title="NOUN CS Plug | 100L Academy", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; font-family: 'Segoe UI', sans-serif; }
    .main-header { font-size: 3.5rem; font-weight: 800; background: -webkit-linear-gradient(#58a6ff, #1f6feb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .info-box { background: #161b22; border: 1px solid #30363d; padding: 30px; border-radius: 12px; margin: 20px 0; border-left: 6px solid #58a6ff; }
    .pay-btn { display: inline-block; padding: 15px 30px; background-color: #238636; color: white !important; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.2rem; }
    .ai-explainer { background: #010409; border-left: 4px solid #58a6ff; padding: 15px; font-style: italic; color: #8b949e; margin-top: 10px; border-radius: 0 8px 8px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. LANDING PAGE ---
st.markdown("<h1 class='main-header'>NOUN CS PLUG 🔌</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center; color: #8b949e;'>Developed by <b>Nurudeen Olabamidele Ibrahim</b></p>", unsafe_allow_html=True)

st.markdown("""
<div class='info-box'>
    <h2>🚀 Direct From Study Materials</h2>
    <p>Prepare with <b>100 real questions</b> extracted directly from NOUN 100L Computer Science Courseware.</p>
    <a class='pay-btn' href='https://selar.com/g444q677i3' target='_blank'>💳 PAY ₦1,000 FOR YOUR UNIQUE PASSWORD</a>
</div>
""", unsafe_allow_html=True)

# --- 5. MEMBERSHIP LOGIN ---
with st.sidebar:
    st.title("🛡️ Member Access")
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
        st.write("### 📞 Contact OLA")
        st.write("Message for your login password.")
        st.link_button("WhatsApp OLA", "https://wa.me/2348148849127")
        st.stop()

# --- 6. EXAM PORTAL ---
st.header("💻 CBT Simulator")
subject = st.selectbox("Choose Your Subject:", list(DB.keys()))
questions = DB[subject]

if 'score' not in st.session_state: st.session_state.score = 0

for i, item in enumerate(questions):
    st.write(f"### Question {i+1} of 20")
    st.write(f"**{item['q']}**")
    ans = st.radio(f"Select answer:", item["o"], key=f"ans_{subject}_{i}")
    
    if st.button(f"Verify Answer {i+1}", key=f"btn_{subject}_{i}"):
        if ans == item["a"]:
            st.success("🎯 Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. Correct Answer: {item['a']}")
            st.markdown(f"<div class='ai-explainer'>🤖 <b>Nova AI Explain:</b> {item['e']}</div>", unsafe_allow_html=True)
    st.divider()

if st.button("🏁 Submit Final Result"):
    st.balloons()
    st.subheader(f"Your Total Score for {subject}: {st.session_state.score} / 20")
    if st.session_state.score >= 15: st.success("Excellent! You are ready for the exam.")
    else: st.warning("You might need to study the courseware more.")
    st.session_state.score = 0

import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="NOUN CS Plug | 100L Academy", layout="wide")

# --- DATABASE: REAL NOUN EXAM CONTENT ---
DB = {
    "MTH 101: Elementary Mathematics I": [
        {"q": "Given A = {x : x is a prime number, 2 < x < 10} and B = {x : x is an odd number, 1 < x < 9}, find A ∩ B.", "o": ["{3, 5, 7}", "{3, 5, 7, 9}", "{2, 3, 5, 7}", "{3, 5}"], "a": "{3, 5, 7}", "e": "A={3,5,7}, B={3,5,7}. The intersection is {3,5,7}."},
        {"q": "Simplify the complex number i^63.", "o": ["i", "-i", "1", "-1"], "a": "-i", "e": "i^4=1. 63/4 leaves remainder 3. i^3 = -i."},
        {"q": "Find the 10th term of an Arithmetic Progression (AP) where a=2 and d=3.", "o": ["27", "29", "31", "33"], "a": "29", "e": "T10 = a+(n-1)d = 2+(9*3) = 29."},
        {"q": "Solve for x if log_x(81) = 4.", "o": ["2", "3", "9", "4"], "a": "3", "e": "x^4 = 81. Since 3^4=81, x=3."},
        {"q": "What is the modulus of the complex number z = 3 + 4i?", "o": ["5", "7", "25", "1"], "a": "5", "e": "Modulus = sqrt(3^2 + 4^2) = 5."},
        {"q": "According to De Morgan's Law, (A ∪ B)' is equivalent to:", "o": ["A' ∪ B'", "A' ∩ B'", "(A ∩ B)'", "A ∪ B"], "a": "A' ∩ B'", "e": "The complement of a union is the intersection of the complements."},
        {"q": "A set with no elements is called a ______.", "o": ["Finite set", "Infinite set", "Null set", "Universal set"], "a": "Null set", "e": "Also known as an empty set."},
        {"q": "Calculate the value of 5! (5 factorial).", "o": ["100", "120", "24", "60"], "a": "120", "e": "5*4*3*2*1 = 120."},
        {"q": "The quadratic formula to find roots is:", "o": ["-b ± sqrt(b^2-4ac) / 2a", "b ± sqrt(b^2-4ac)", "x + y", "b/a"], "a": "-b ± sqrt(b^2-4ac) / 2a", "e": "Standard quadratic solution."},
        {"q": "Which is an irrational number?", "o": ["0.5", "2/3", "sqrt(2)", "4"], "a": "sqrt(2)", "e": "Cannot be expressed as a simple fraction."},
        {"q": "Find the sum of the first 5 terms of AP: 1, 3, 5...", "o": ["20", "25", "15", "30"], "a": "25", "e": "S5 = 5/2(2(1) + 4(2)) = 25."},
        {"q": "The power set of a set with 3 elements has how many members?", "o": ["3", "6", "8", "9"], "a": "8", "e": "2^n = 2^3 = 8."},
        {"q": "Calculate log_10(1000).", "o": ["1", "2", "3", "10"], "a": "3", "e": "10^3 = 1000."},
        {"q": "Find the gradient of the line y = 2x + 5.", "o": ["2", "5", "-2", "0"], "a": "2", "e": "In y=mx+c, m is the gradient."},
        {"q": "What is the identity element under addition?", "o": ["1", "0", "-1", "x"], "a": "0", "e": "Any number + 0 = the number."},
        {"q": "A triangle with all sides equal is:", "o": ["Isosceles", "Scalene", "Equilateral", "Right"], "a": "Equilateral", "e": "Definition of equilateral."},
        {"q": "Convert 2π radians to degrees.", "o": ["90", "180", "270", "360"], "a": "360", "e": "2π = 360°."},
        {"q": "The set of natural numbers is denoted by:", "o": ["N", "Z", "Q", "R"], "a": "N", "e": "Standard mathematical notation."},
        {"q": "If f(x) = x^2, find f(3).", "o": ["6", "9", "3", "12"], "a": "9", "e": "3^2 = 9."},
        {"q": "Which is a proper subset of {1, 2}?", "o": ["{1}", "{1,2}", "{1,2,3}", "{4}"], "a": "{1}", "e": "Proper subset has fewer elements."}
    ],
    "GST 103: Computer Fundamentals": [
        {"q": "Who proposed the 'Stored Program' concept?", "o": ["Babbage", "Von Neumann", "Pascal", "Gates"], "a": "Von Neumann", "e": "Core architecture of modern computers."},
        {"q": "Which generation used Vacuum Tubes?", "o": ["1st", "2nd", "3rd", "4th"], "a": "1st", "e": "1940-1956 technology."},
        {"q": "Binary equivalent of decimal 10?", "o": ["1010", "1111", "1001", "1100"], "a": "1010", "e": "8+2 = 10."},
        {"q": "Which is an Operating System?", "o": ["Word", "Linux", "Chrome", "Excel"], "a": "Linux", "e": "System software."},
        {"q": "What does ALU stand for?", "o": ["Arithmetic Logic Unit", "All Logic Unit", "Array Link", "None"], "a": "Arithmetic Logic Unit", "e": "Handles calculations."},
        {"q": "1 Gigabyte is:", "o": ["1024MB", "1000MB", "1024KB", "1024B"], "a": "1024MB", "e": "Binary measurement."},
        {"q": "Which is non-volatile memory?", "o": ["RAM", "ROM", "Cache", "Register"], "a": "ROM", "e": "Retains data without power."},
        {"q": "A network spanning a city is:", "o": ["LAN", "MAN", "WAN", "PAN"], "a": "MAN", "e": "Metropolitan Area Network."},
        {"q": "The brain of the computer is the:", "o": ["ALU", "CPU", "RAM", "HDD"], "a": "CPU", "e": "Central Processing Unit."},
        {"q": "HTTP stands for:", "o": ["Hypertext Transfer Protocol", "High Tech", "Home Text", "None"], "a": "Hypertext Transfer Protocol", "e": "Web foundation."},
        {"q": "Smallest unit of data:", "o": ["Bit", "Byte", "Nibble", "Word"], "a": "Bit", "e": "Binary digit."},
        {"q": "Which generation used ICs?", "o": ["1st", "2nd", "3rd", "4th"], "a": "3rd", "e": "Integrated Circuits."},
        {"q": "Which is an input device?", "o": ["Monitor", "Printer", "Scanner", "Speaker"], "a": "Scanner", "e": "Captures physical data."},
        {"q": "ASCII has how many bits?", "o": ["7", "16", "32", "64"], "a": "7", "e": "Standard ASCII is 7-bit."},
        {"q": "Which software manages hardware?", "o": ["Application", "Operating System", "Utility", "Browser"], "a": "Operating System", "e": "System intermediary."},
        {"q": "Shortcut for 'Undo':", "o": ["Ctrl+Z", "Ctrl+Y", "Ctrl+C", "Ctrl+V"], "a": "Ctrl+Z", "e": "Standard command."},
        {"q": "First Gen language:", "o": ["Assembly", "Machine", "C", "Basic"], "a": "Machine", "e": "Binary 0s and 1s."},
        {"q": "Which is NOT hardware?", "o": ["Mouse", "Windows", "CPU", "Keyboard"], "a": "Windows", "e": "Windows is software."},
        {"q": "A collection of 8 bits:", "o": ["Bit", "Byte", "KB", "Nibble"], "a": "Byte", "e": "8 bits = 1 byte."},
        {"q": "VLSI was used in which generation?", "o": ["3rd", "4th", "5th", "2nd"], "a": "4th", "e": "Very Large Scale Integration."}
    ],
    "PHY 101: Mechanics & Heat": [
        {"q": "The dimension of Force is:", "o": ["[MLT^-1]", "[MLT^-2]", "[ML^2T^-2]", "[MLT]"], "a": "[MLT^-2]", "e": "Force = mass * accel."},
        {"q": "Unit of work is:", "o": ["Newton", "Watt", "Joule", "Pascal"], "a": "Joule", "e": "Work = Force * Distance."},
        {"q": "Acceleration due to gravity is approx:", "o": ["8.9", "9.8", "10.5", "7.2"], "a": "9.8", "e": "Standard g value on Earth."},
        {"q": "Energy of motion is called:", "o": ["Potential", "Kinetic", "Thermal", "Chemical"], "a": "Kinetic", "e": "1/2 mv^2."},
        {"q": "Velocity is a ____ quantity.", "o": ["Scalar", "Vector", "Dimensionless", "Fixed"], "a": "Vector", "e": "Has magnitude and direction."},
        {"q": "Water boils at ____ Celsius.", "o": ["0", "50", "100", "212"], "a": "100", "e": "Standard boiling point."},
        {"q": "Density = Mass / ____.", "o": ["Weight", "Area", "Volume", "Speed"], "a": "Volume", "e": "ρ = m/V."},
        {"q": "Power is measured in:", "o": ["Joules", "Watts", "Newtons", "Amps"], "a": "Watts", "e": "Rate of doing work."},
        {"q": "Matter exists in how many main states?", "o": ["1", "2", "3", "4"], "a": "3", "e": "Solid, Liquid, Gas."},
        {"q": "Resistance to motion is:", "o": ["Inertia", "Friction", "Gravity", "Velocity"], "a": "Friction", "e": "Opposes relative motion."},
        {"q": "Hooke's law deals with:", "o": ["Light", "Elasticity", "Fluids", "Heat"], "a": "Elasticity", "e": "F = ke."},
        {"q": "Instrument to measure temp:", "o": ["Barometer", "Thermometer", "Ammeter", "Scalpel"], "a": "Thermometer", "e": "Thermal measurement."},
        {"q": "Weight = Mass * ____.", "o": ["Gravity", "Velocity", "Time", "Speed"], "a": "Gravity", "e": "W = mg."},
        {"q": "Speed in a direction is:", "o": ["Velocity", "Motion", "Accel", "Force"], "a": "Velocity", "e": "Vector speed."},
        {"q": "Unit of power is:", "o": ["Watt", "Joule", "Newton", "Volt"], "a": "Watt", "e": "J/s."},
        {"q": "Vector has magnitude and ____.", "o": ["Speed", "Direction", "Mass", "Size"], "a": "Direction", "e": "Definition of vector."},
        {"q": "Push or pull is a:", "o": ["Work", "Energy", "Force", "Power"], "a": "Force", "e": "Definition of force."},
        {"q": "Sound travels fastest in:", "o": ["Air", "Water", "Steel", "Vacuum"], "a": "Steel", "e": "Travels fastest in solids."},
        {"q": "Is light matter?", "o": ["Yes", "No", "Only at night", "Maybe"], "a": "No", "e": "Light is electromagnetic energy."},
        {"q": "Force per unit area is:", "o": ["Work", "Power", "Pressure", "Stress"], "a": "Pressure", "e": "P = F/A."}
    ],
    "CHM 101: Inorganic Chemistry": [
        {"q": "Atomic number of Hydrogen?", "o": ["1", "2", "3", "4"], "a": "1", "e": "First element."},
        {"q": "Center of an atom is the:", "o": ["Electron", "Nucleus", "Proton", "Neutron"], "a": "Nucleus", "e": "Contains protons and neutrons."},
        {"q": "Symbol for Gold?", "o": ["Gd", "Ag", "Au", "Fe"], "a": "Au", "e": "From Latin Aurum."},
        {"q": "Negative subatomic particle?", "o": ["Proton", "Neutron", "Electron", "Ion"], "a": "Electron", "e": "Surrounds nucleus."},
        {"q": "PH of pure water?", "o": ["1", "7", "14", "0"], "a": "7", "e": "Neutral PH."},
        {"q": "Symbol for Sodium?", "o": ["S", "So", "Na", "Sn"], "a": "Na", "e": "From Latin Natrium."},
        {"q": "Bond where electrons are shared?", "o": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "a": "Covalent", "e": "Mutual sharing."},
        {"q": "Most abundant gas in atmosphere?", "o": ["Oxygen", "Nitrogen", "Argon", "CO2"], "a": "Nitrogen", "e": "Approx 78%."},
        {"q": "Symbol for Carbon?", "o": ["Ca", "C", "Cr", "Co"], "a": "C", "e": "Standard symbol."},
        {"q": "Atomic mass of Carbon?", "o": ["6", "12", "14", "16"], "a": "12", "e": "Approx 12 amu."},
        {"q": "Charge of a proton?", "o": ["Positive", "Negative", "Neutral", "Zero"], "a": "Positive", "e": "+1 charge."},
        {"q": "Water is made of Hydrogen and ____.", "o": ["Nitrogen", "Oxygen", "Helium", "Neon"], "a": "Oxygen", "e": "H2O."},
        {"q": "Chemical formula for Salt?", "o": ["NaCl", "KCl", "H2O", "CO2"], "a": "NaCl", "e": "Sodium Chloride."},
        {"q": "Isotope has different number of ____.", "o": ["Protons", "Electrons", "Neutrons", "Atoms"], "a": "Neutrons", "e": "Same atomic number, diff mass."},
        {"q": "Noble gas used in balloons:", "o": ["Oxygen", "Helium", "Neon", "Argon"], "a": "Helium", "e": "Lighter than air."},
        {"q": "Matter with fixed shape/volume:", "o": ["Solid", "Liquid", "Gas", "Plasma"], "a": "Solid", "e": "Fixed structure."},
        {"q": "Atom with a charge is an:", "o": ["Isotope", "Ion", "Molecule", "Crystal"], "a": "Ion", "e": "Gained or lost electrons."},
        {"q": "Symbol for Iron?", "o": ["Ir", "Fe", "In", "I"], "a": "Fe", "e": "From Latin Ferrum."},
        {"q": "Process of solid to gas:", "o": ["Melting", "Sublimation", "Evaporation", "Freezing"], "a": "Sublimation", "e": "Direct phase change."},
        {"q": "Hardest natural substance:", "o": ["Iron", "Steel", "Diamond", "Gold"], "a": "Diamond", "e": "Carbon allotrope."}
    ],
    "GST 101: Use of English I": [
        {"q": "Word that describes a verb:", "o": ["Adjective", "Adverb", "Noun", "Pronoun"], "a": "Adverb", "e": "Modifies a verb."},
        {"q": "Opposite of 'Success':", "o": ["Win", "Failure", "Growth", "Good"], "a": "Failure", "e": "Antonym."},
        {"q": "SQ3R: The 1st 'S' stands for?", "o": ["Survey", "Search", "Scan", "Solve"], "a": "Survey", "e": "Overview step."},
        {"q": "Plural of 'Child':", "o": ["Childs", "Children", "Childrens", "Childies"], "a": "Children", "e": "Irregular plural."},
        {"q": "Synonym for 'Fast':", "o": ["Slow", "Quick", "Lazy", "Angry"], "a": "Quick", "e": "Similar meaning."},
        {"q": "A, An, The are called:", "o": ["Verbs", "Articles", "Nouns", "Adverbs"], "a": "Articles", "e": "Grammar category."},
        {"q": "Identify the verb: 'He runs fast'", "o": ["He", "runs", "fast", "None"], "a": "runs", "e": "Action word."},
        {"q": "Sentence ender for a question:", "o": [".", ",", "?", "!"], "a": "?", "e": "Question mark."},
        {"q": "Prefix for 'Unhappy':", "o": ["Un", "Happy", "Py", "Hap"], "a": "Un", "e": "Added at the start."},
        {"q": "Suffix for 'Careless':", "o": ["Care", "Less", "C", "S"], "a": "Less", "e": "Added at the end."},
        {"q": "Punctuation for strong emotion:", "o": [".", "?", "!", ","], "a": "!", "e": "Exclamation mark."},
        {"q": "Noun name for a person/place:", "o": ["Common", "Proper", "Abstract", "Verb"], "a": "Proper", "e": "e.g., Lagos, Ibrahim."},
        {"q": "Identify the adjective: 'The red car'", "o": ["The", "red", "car", "is"], "a": "red", "e": "Describes the noun."},
        {"q": "Past tense of 'Go':", "o": ["Goed", "Went", "Gone", "Going"], "a": "Went", "e": "Irregular verb."},
        {"q": "Main idea of a paragraph:", "o": ["Topic sentence", "Suffix", "Adverb", "Title"], "a": "Topic sentence", "e": "Central theme."},
        {"q": "Is 'Happiness' an abstract noun?", "o": ["Yes", "No", "Maybe", "Sometimes"], "a": "Yes", "e": "Cannot be touched."},
        {"q": "What is 'skimming'?", "o": ["Deep reading", "Fast reading for gist", "Writing", "Singing"], "a": "Fast reading for gist", "e": "Reading technique."},
        {"q": "Collective noun for sheep:", "o": ["Pack", "Flock", "Herd", "School"], "a": "Flock", "e": "Group name."},
        {"q": "Antonym of 'Beautiful':", "o": ["Pretty", "Nice", "Ugly", "Small"], "a": "Ugly", "e": "Opposite."},
        {"q": "A word used to join sentences:", "o": ["Verb", "Conjunction", "Noun", "Preposition"], "a": "Conjunction", "e": "e.g., and, but, or."}
    ]
}

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #238636; color: white; font-weight: bold; }
    .ai-box { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🔑 Student Access")
    code = st.text_input("Access Code:", type="password")
    if code != "PLUG2026":
        st.warning("Enter code to unlock.")
        st.stop()
    st.success("Welcome, Ibrahim")
    st.divider()
    st.link_button("💬 Support", "https://wa.me/2348148849127")

# --- MAIN INTERFACE ---
st.title("💻 NOUN CS 100L Academy")
st.write("Targeting 5.0 GPA through Exam Simulation.")

subject = st.selectbox("Select Subject:", list(DB.keys()))
questions = DB[subject]

if 'score' not in st.session_state: st.session_state.score = 0

for i, item in enumerate(questions):
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
    st.header(f"Final Score: {st.session_state.score} / 20")
    st.session_state.score = 0 # Reset for next attempt

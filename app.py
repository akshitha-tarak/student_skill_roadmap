import streamlit as st
import pandas as pd

# --- Page configuration ---
st.set_page_config(
    page_title="Student Skill Roadmap",
    layout="centered"
)

# --- Load dataset ---
@st.cache_data
def load_data():
    return pd.read_csv("student_performance_extended.csv")  # your dataset filename

data = load_data()

# --- Title ---
st.title("🎓 Personalized Student Skill Roadmap Web App")
st.write("Interactive web application to guide students in planning their skills, career, and personal development.")

st.divider()

# --- User Input ---
st.header("📋 Enter Your Details")

name = st.text_input("Student Name", "")
year = st.selectbox("Year", sorted(data["year"].unique()))
branch = st.selectbox("Branch", sorted(data["branch"].unique()))
gpa = st.slider("GPA", 0.0, 10.0, 7.0, 0.1)
study_hours = st.slider("Daily Study Hours", 0, 12, 3)
failures = st.number_input("Number of Failures", min_value=0, max_value=10, value=0)
hostel = st.selectbox("Hostel?", ["Yes", "No"])
sleep_hours = st.slider("Daily Sleep Hours", 0, 12, 6)
family_support = st.selectbox("Family Support Level", ["Low", "Medium", "High"])
interest = st.selectbox("Primary Interest", sorted(data["interest"].unique()))
budget = st.selectbox("Budget Level", sorted(data["budget_level"].unique()))
skill_level = st.selectbox("Skill Level", sorted(data["skill level"].unique()))
stress_level = st.selectbox("Stress Level", sorted(data["stress level"].unique()))
confusion_level = st.selectbox("Confusion Level", sorted(data["confusion  level"].unique()))
communication = st.selectbox("Communication Level", sorted(data["communication"].unique()))

st.divider()

# --- Recommendation Logic ---
def generate_roadmap(info):
    steps = []

    # Skill improvement
    if info['skill_level'] == "Beginner":
        steps.append("Start with basics of your interest area and practice small projects.")
    else:
        steps.append("Focus on advanced projects, real-world applications, and certifications.")

    # Study & GPA
    if info['study_hours'] < 3 or info['gpa'] < 6.0:
        steps.append("Increase study hours and follow a structured learning schedule.")

    # Hostel / Sleep
    if info['hostel'] == "Yes":
        steps.append("Maintain a healthy routine: proper sleep, food, and time management in hostel.")
    else:
        steps.append("Balance family responsibilities with studies and skill building.")

    # Stress & Confusion
    if info['stress_level'] == "High" or info['confusion_level'] == "High":
        steps.append("Adopt stress management techniques: meditation, time management, and counseling.")

    # Family Support
    if info['family_support'] == "Low":
        steps.append("Seek mentors, peer groups, or online communities for guidance.")

    # Communication
    if info['communication'] == "Poor":
        steps.append("Work on communication skills through speaking, writing, and online workshops.")

    # Interest-based learning
    steps.append(f"Follow curated courses, books, and online tutorials for {info['interest']}.")

    # Budget
    if info['budget'] == "Low":
        steps.append("Use free resources: YouTube tutorials, free MOOCs, and open-source materials.")
    else:
        steps.append("Consider paid courses, mentorship, or workshops for faster learning.")

    return steps

# --- Generate Roadmap Button ---
if st.button("🔍 Generate My Roadmap"):
    student_info = {
        'skill_level': skill_level,
        'interest': interest,
        'study_hours': study_hours,
        'gpa': gpa,
        'stress_level': stress_level,
        'confusion_level': confusion_level,
        'hostel': hostel,
        'communication': communication,
        'budget': budget,
        'family_support': family_support
    }

    roadmap = generate_roadmap(student_info)
    st.success(f"✅ Roadmap Generated for {name}")
    
    st.subheader("📌 Suggested Steps:")
    for i, step in enumerate(roadmap, 1):
        st.write(f"{i}. {step}")

    st.subheader("📚 Recommended Resources:")
    st.markdown("""
    - **Free Courses:** YouTube, NPTEL, Coursera free courses  
    - **Paid Courses:** Udemy, Coursera, edX  
    - **Practice & Projects:** HackerRank, LeetCode, GitHub  
    - **Soft Skills & Communication:** Toastmasters, online workshops
    """)

st.divider()

# --- Display Dataset Preview ---
st.header("📊 Sample Student Dataset")
st.dataframe(data)

st.caption("Mini Project | Student Skill Roadmap | Streamlit Web App")



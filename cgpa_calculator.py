import streamlit as st

GRADE_POINTS = {
    "A": 4.0,  "A-": 3.7,
    "B+": 3.3, "B": 3.0,  "B-": 2.7,
    "C+": 2.3, "C": 2.0,  "C-": 1.7,
    "D+": 1.3, "D": 1.0,
    "F": 0.0
}

CREDIT_OPTIONS = [1, 1.5, 3]

st.set_page_config(page_title="NSU CGPA Calculator 🎓", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'>📘 NSU CGPA Calculator</h1>
    <p style='text-align: center; font-size: 18px;'>
    Calculate your <b>updated CGPA</b> and <b>semester CGPA</b> based on North South University grading policy.
    </p>
    """,
    unsafe_allow_html=True,
)

# Input Previous CGPA & Credits
with st.container():
    st.subheader("🔢 Current CGPA and Credits Completed")
    prev_cgpa = st.number_input("Current CGPA", min_value=0.0, max_value=4.0, step=0.01, help="Your CGPA before this semester")
    prev_credits = st.number_input("Total Completed Credits", min_value=0.0, step=0.5, help="Total credits completed before this semester")

st.markdown("---")

# Initialize session state variables for dynamic course list
if "courses" not in st.session_state:
    st.session_state.courses = []

def add_course():
    st.session_state.courses.append({"grade": "A", "credit": 1})

# Add course button
st.subheader("🆕 Enter This Semester Courses")
st.button("➕ Add Course", on_click=add_course)

# Show all courses input dynamically
for idx, course in enumerate(st.session_state.courses):
    col1, col2, col3 = st.columns([4, 2, 1])
    with col1:
        course["grade"] = st.selectbox(f"Course {idx+1} Grade", list(GRADE_POINTS.keys()), index=list(GRADE_POINTS.keys()).index(course["grade"]), key=f"grade_{idx}")
    with col2:
        course["credit"] = st.selectbox(f"Course {idx+1} Credit Hours", CREDIT_OPTIONS, index=CREDIT_OPTIONS.index(course["credit"]), key=f"credit_{idx}")
    with col3:
        if st.button("❌", key=f"remove_{idx}"):
            st.session_state.courses.pop(idx)
            st.experimental_rerun()

st.markdown("---")

# Calculate button and logic
if st.button("🎯 Calculate CGPA"):
    if not st.session_state.courses:
        st.error("Please add at least one course.")
    else:
        sem_points = sum(GRADE_POINTS[c['grade']] * c['credit'] for c in st.session_state.courses)
        sem_credits = sum(c['credit'] for c in st.session_state.courses)

        if sem_credits == 0:
            st.error("Total semester credits cannot be zero.")
        else:
            semester_cgpa = sem_points / sem_credits
            total_credits = prev_credits + sem_credits
            total_points = (prev_cgpa * prev_credits) + sem_points
            updated_cgpa = total_points / total_credits

            st.success("✅ Calculation Complete!")
            st.markdown(f"<h3 style='color: green;'>🎓 This Semester CGPA: <code>{semester_cgpa:.2f}</code></h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: blue;'>📌 Updated Total CGPA: <code>{updated_cgpa:.2f}</code></h3>", unsafe_allow_html=True)
            st.markdown(f"<h4>📚 Total Credits Now: <code>{total_credits}</code></h4>", unsafe_allow_html=True)

import streamlit as st
st.title("Profile Shortlist Application")

user_name = st.text_input("Candidate Name: ", value="John Doe")
exp = st.slider("Experience (in years): ", min_value=0, max_value=20, value=2)
role = st.selectbox("Role: ",["Data Scientist", "Software Engineer", "Product Manager"])


st.write(f"Profile: {user_name}, {role} {exp}")

st.divider()
#st.subheader("Shortlist Candidate")

#shortlisted_list = []

#if st.button("Shortlist This Candidate"):
    #candidate_summary = f" {user_name} ({role})"
    #shortlisted_list.append(candidate_summary)


#st.write(f"Total Shortlisted Candidates: {len(shortlisted_list)}")
#st.write(shortlisted_list)

if "shortlisted_list" not in st.session_state:
    st.session_state.shortlisted_list =[]

col1, col2 = st.columns([1,1])

with col1:
    if st.button("shortlist this candidate", type = "primary"):
        candidate_summary = f"{user_name} ({role})"
        st.session_state.shortlisted_list.append(candidate_summary)

with col2:
    if st.button("Clear candidate list"):
        st.session_state.shortlisted_list=[]


st.write(f"Total Shortlisted Candidates: {len(st.session_state.shortlisted_list)}")
for idx, candidate in enumerate(st.session_state.shortlisted_list, start=1):
    st.write(f"{idx}. {candidate}")


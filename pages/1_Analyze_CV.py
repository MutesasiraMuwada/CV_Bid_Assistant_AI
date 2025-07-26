import streamlit as st
from utils.cv_parser import analyze_cv_against_jd

st.set_page_config(page_title="Analyze CV", page_icon="🔍")

st.title("🔍 Analyze Single CV")
st.markdown("Upload a CV and paste the job description. We'll highlight strengths and improvement areas.")

uploaded_file = st.file_uploader("Upload a CV (DOCX only)", type=["docx"])
job_description = st.text_area("Paste the Job Description here")

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        # Call your processing function
        result = analyze_cv_against_jd(uploaded_file, job_description)
        st.success("✅ Analysis Complete")
        st.write(result)
else:
    st.info("Please upload a CV and paste a job description to begin.")

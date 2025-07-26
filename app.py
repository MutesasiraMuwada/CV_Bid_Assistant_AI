import streamlit as st
from utils.cv_scoring import analyze_cv  # assuming you have a function like this
from utils.helpers import extract_text_from_docx  # or your own text extractor

# --- PAGE CONFIG ---
st.set_page_config(page_title="KCL CV Analyzer", page_icon="📄", layout="wide")

# --- CUSTOM HEADER ---
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #1a73e8;
        }
        .sub-title {
            font-size: 18px;
            color: gray;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("klc_logo.jpg", use_container_width=True)
st.sidebar.title("Navigation")
st.sidebar.markdown("🚀 Upload CVs and Job Descriptions to get started.")
st.sidebar.markdown("🔍 Analyze and improve to meet bid requirements.")

# --- MAIN CONTENT ---
st.markdown("<div class='main-title'>📄 CV Analyzer for Technical Bids</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Tailor your CVs to meet bid specifications and win more consultancy projects.</div>", unsafe_allow_html=True)

st.write("---")

# --- FILE UPLOAD SECTION ---
cv_file = st.file_uploader("📤 Upload CV (DOCX format only)", type=["docx"], help="Drop your CV here for analysis.")
job_desc = st.text_area("📝 Paste the Job Description or Terms of Reference", height=250)

if st.button("Analyze CV"):
    if cv_file and job_desc:
        cv_text = extract_text_from_docx(cv_file)
        report = analyze_cv(cv_text, job_desc)
        st.success("✅ CV Analysis Complete")
        st.write(report)
    else:
        st.warning("Please upload a CV and paste a job description.")


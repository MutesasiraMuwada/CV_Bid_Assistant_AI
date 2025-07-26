# utils/cv_parser.py

def analyze_cv_against_jd(cv_file, jd_text):
    import docx2txt
    cv_text = docx2txt.process(cv_file)

    # Basic match keywords (for example purposes)
    jd_keywords = set(jd_text.lower().split())
    cv_keywords = set(cv_text.lower().split())

    matched = jd_keywords & cv_keywords
    missing = jd_keywords - cv_keywords

    return {
        "✅ Matched Keywords": list(matched)[:30],  # limit for display
        "❌ Missing Keywords (Add to CV)": list(missing)[:30]
    }

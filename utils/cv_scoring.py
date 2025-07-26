import re
from collections import Counter

def analyze_cv(cv_text, job_text):
    # Lowercase + tokenize both texts
    cv_words = re.findall(r'\w+', cv_text.lower())
    job_words = re.findall(r'\w+', job_text.lower())

    # Count word matches
    cv_word_counts = Counter(cv_words)
    job_word_counts = Counter(job_words)

    matched_keywords = [word for word in set(job_words) if word in cv_word_counts]
    total_keywords = len(set(job_words))
    matched_count = len(matched_keywords)

    # Basic score out of 100
    match_score = int((matched_count / total_keywords) * 100) if total_keywords > 0 else 0

    # Feedback
    missing_keywords = [word for word in set(job_words) if word not in cv_word_counts]

    feedback = {
        "Match Score": f"{match_score}%",
        "Matched Keywords": matched_keywords[:20],  # limit display
        "Missing Keywords (Consider adding)": missing_keywords[:20]
    }

    return feedback

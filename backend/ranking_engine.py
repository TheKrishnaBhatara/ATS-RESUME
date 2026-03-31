from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_embedding, jd_embedding):
    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return float(score)


def skill_overlap_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0

    overlap = set(resume_skills).intersection(set(jd_skills))
    return len(overlap) / len(jd_skills)


def final_ranking_score(similarity, skill_score):
    return (0.7 * similarity) + (0.3 * skill_score)

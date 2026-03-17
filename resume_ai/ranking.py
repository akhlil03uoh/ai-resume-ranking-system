def score_candidate(skill_match, exp, edu, loc):

    score = (
        skill_match * 0.5 +
        exp * 0.25 +
        edu * 0.10 +
        loc * 0.15
    )

    return round(score, 2)
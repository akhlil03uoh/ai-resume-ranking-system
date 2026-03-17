skills_list = [
    "python",
    "java",
    "sql",
    "machine learning",
    "data analysis",
    "aws",
    "docker",
    "react",
    "node",
    "flask",
    "django"
]


def extract_skills(text):

    found = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found.append(skill)

    return found
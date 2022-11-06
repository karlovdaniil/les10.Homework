from flask import Flask

from utils import get_all, format_candidate, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all()
    result: str = format_candidate(candidates)
    return result


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidates: dict = get_by_pk(uid)
    result = f'<img src="{candidates["picture"]}">'
    result += format_candidate([candidates])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """Поиск кандидата по навыку"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_by_skill(skill_lower)
    result: str = format_candidate(candidates)
    return result


app.run()

import json


def load_candidates() -> list[dict]:
    """Загружает данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def format_candidate(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            Имя кандидата - {candidate["name"]}\n
            Позиция - {candidate["position"]}\n
            Навыки - {candidate["skills"]}\n
        """
    result += '</pre>'
    return result


def get_all() -> list[dict]:
    """Покажет всех кандидатов"""
    return load_candidates()


def get_by_pk(uid: int) -> dict | None:
    """Вернет кандидата по pk"""
    candidates = get_all()
    for candidate in candidates:
        if candidate['pk'] == uid:
            return candidate
    return None


def get_by_skill(skill: str) -> list[dict]:
    """Вернет кандидатов по навыку"""
    result = []
    candidates = get_all()
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

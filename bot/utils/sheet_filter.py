from bot.loader import get_sheet_data


def get_next_parameters(current: list[str] = None) -> list[str]:
    """
    Возвращает возможные параметры в зависимости от предыдущих выборов для следущей стадии опроса
    :param current: Текущий ряд параметров, например: ["Мтс", "От агента"]
    :return: Варианты ответов со следующей стадии, например: []
    """
    if not current: current = []
    l = len(current)
    res = {x[l] for x in get_sheet_data()[1:] if current == x[:l]}
    return list(res)

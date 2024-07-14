def filter_by_state(list_of_dicts: list[dict[str, str | int]], state: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция сортирует словари в списках по значению ключа state."""
    result_list: list[dict[str, str | int]] = []
    for item in list_of_dicts:
        if item["state"] == state:
            result_list.append(item)
    return result_list


def sort_by_date(list_of_dicts: list[dict[str, str | int]], ascending: bool = False) -> list[dict[str, str | int]]:
    """Функция возвращающая список словарей отсортированных по дате"""
    list_of_dicts.sort(key=lambda x: x["date"], reverse=not ascending)
    return list_of_dicts

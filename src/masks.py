def get_mask_card_number(card_number: str) -> str:
    """Payment card number"""
    if len(card_number) < 16 or len(card_number) > 16:
        raise ValueError("Неверная длина карты")

    if len(card_number) == 0:
        raise ValueError("Пустая строка")

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Номер счета"""
    if len(account_number) < 20 or len(account_number) > 20:
        raise ValueError("Неверная длина номера счета")

    if len(account_number) == 0:
        raise ValueError("Пустая строка")

    return f"**{account_number[-4:]}"

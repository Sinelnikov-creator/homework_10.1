def get_mask_card_number(card_number: str) -> str:
    """Payment card number"""
    if len(card_number) < 16:
        raise ValueError("Неверная длина карты")

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Номер счета"""
    if len(account_number) < 20:
        raise ValueError("Неверная длина номера счета")

    return f"**{account_number[-4:]}"

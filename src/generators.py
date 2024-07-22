import re

from typing import Any
from collections.abc import Iterator, Generator


def filter_by_currency(transactions: list[dict[str, Any]], currency) -> Iterator[dict[str, Any]]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции. Функция должна возвращать
    итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""

    currency_code = []

    for current_data in transactions:
        if amount := current_data.get("operationAmount"):
            currency_ = amount.get("currency")
            code = currency_.get("code") if currency_ else None
            if code == currency.value:
                currency_code.append(current_data)
    return iter(currency_code)


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """Функция-генератор transaction_descriptions, который принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    for transactions_ in transactions:
        descriptions: str | None = transactions_.get("descriptions")
        if descriptions:
            yield descriptions


def card_number_generator(start: int = 1, finish: int = 9999999999999999) -> Generator[str]:
    """Функция-генератор card_number_generator, который выдает номера банковских карт в формат XXXX-XXXX-XXXX-XXXX
     где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
     от 0000-0000-0000-0001 до 9999-9999-9999-9999. Генератор должен принимать начальное и конечное значения для
     генерации диапазона номеров."""
    while True:
        if start >= finish:
            break
        start = str(start)
        not_formated_card = start.rjust(16,"0")
        card_number_list = re.findall(r"(\d{4})", not_formated_card)
        yield " ".join(card_number_list)
        start += 1

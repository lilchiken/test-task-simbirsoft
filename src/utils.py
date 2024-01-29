from typing import List, Tuple

from src_lib.transactions import TransactionData


def save_csv(data: List[Tuple[str, str, str]]):
    tr_data = TransactionData(data=data)
    tr_data.to_csv()

from typing import List, Tuple
import datetime

from src_lib.transactions import TransactionData
from src_lib.consts import TRANSACTION_DATE_FORMAT


def save_csv(data: List[Tuple[str, str, str]]):
    tr_data = TransactionData(data=data)
    tr_data.to_csv()


def get_time_now() -> str:
    timezone = datetime.timezone(
        offset=datetime.timedelta()
    )
    time_now = datetime.datetime.now(tz=timezone) \
        .strftime(TRANSACTION_DATE_FORMAT)
    return time_now

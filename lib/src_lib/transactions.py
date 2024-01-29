from typing import List, Tuple
from dataclasses import dataclass
import csv


__all__ = ['TransactionData']


@dataclass
class TransactionData:
    data: List[Tuple[str, str, str]]

    def to_csv(self):
        with open('allure-data.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(self.data)

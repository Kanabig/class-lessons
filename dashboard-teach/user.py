from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    pw: str
    bank_account: str

    memos: list[tuple]
    todoList: list[tuple]

    def __post_init__(self):
        self._validate()

    def _validate(self):
        pass

from typing import NamedTuple

class Point(NamedTuple):
    """To store point of next move"""
    row: str
    column: int

    def __repr__(self):
        return str(self.row) + str(self.column)

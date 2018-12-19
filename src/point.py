from typing import NamedTuple

class Point(NamedTuple):
    """To store point of next move"""
    column: str
    row: int

    def __repr__(self):
        return str(self.column) + str(self.row)

    def get_column(self):
        """Returns column number"""
        return ord(self.column) - 97 # TOOD: will this return correct column?

    def get_row(self):
        """Returns row number"""
        return self.row

from typing import NamedTuple

class Point(NamedTuple):
    x: str
    y: int

    def __repr__(self):
        return str(self.x) + str(self.y)

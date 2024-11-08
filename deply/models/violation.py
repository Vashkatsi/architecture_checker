from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Violation:
    file: Path
    element_name: str
    element_type: str  # 'class', 'function', or 'variable'
    line: int
    column: int
    message: str

    def __eq__(self, other):
        return (
                self.file == other.file and
                self.line == other.line and
                self.column == other.column and
                self.message == other.message
        )

    def __hash__(self):
        return hash((self.file, self.line, self.column, self.message))

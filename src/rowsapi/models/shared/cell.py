import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils


@dataclass_json
@dataclasses.dataclass
class Cell:
    r"""Cell
    Cell values and formulas
    """
    
    col: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('col') }})
    formula: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('formula') }})
    row: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('row') }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

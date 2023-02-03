import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import cell as shared_cell


@dataclass_json
@dataclasses.dataclass
class RangeList:
    r"""RangeList
    Data inside a table range as a list of cells grouped by row.
    """
    
    items: Optional[list[list[shared_cell.Cell]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    

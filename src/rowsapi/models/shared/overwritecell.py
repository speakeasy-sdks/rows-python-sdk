import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils


@dataclass_json
@dataclasses.dataclass
class OverwriteCell:
    r"""OverwriteCell
    Cell values and formulas
    """
    
    formula: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('formula') }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    

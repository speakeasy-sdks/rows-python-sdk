import dataclasses
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import overwritecell as shared_overwritecell


@dataclass_json
@dataclasses.dataclass
class OverwriteCells:
    r"""OverwriteCells
    Data inside a table range to be written. This is a list of cells grouped by row.
    
    To set a cell to an empty value, set the value to an empty string.
    
    """
    
    cells: list[list[shared_overwritecell.OverwriteCell]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('cells') }})
    

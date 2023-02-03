import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import spreadsheet as shared_spreadsheet


@dataclass_json
@dataclasses.dataclass
class SpreadsheetsList:
    r"""SpreadsheetsList
    Array of spreadsheets
    """
    
    items: Optional[list[shared_spreadsheet.Spreadsheet]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    next_page_results: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_page_results') }})
    

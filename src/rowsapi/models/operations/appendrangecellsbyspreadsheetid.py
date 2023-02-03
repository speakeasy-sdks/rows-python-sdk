import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import appendvalues as shared_appendvalues
from ..shared import error as shared_error


@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetIDPathParams:
    range: str = dataclasses.field(metadata={'path_param': { 'field_name': 'range', 'style': 'simple', 'explode': False }})
    spreadsheet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'spreadsheet_id', 'style': 'simple', 'explode': False }})
    table_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'table_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON1:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON1
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON2:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON2
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON3:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON3
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON4:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON4
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON5:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON5
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON6:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON6
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON7:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON7
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetID400ApplicationJSON8:
    r"""AppendRangeCellsBySpreadsheetID400ApplicationJSON8
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetIDRequest:
    path_params: AppendRangeCellsBySpreadsheetIDPathParams = dataclasses.field()
    request: shared_appendvalues.AppendValues = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AppendRangeCellsBySpreadsheetIDResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    append_range_cells_by_spreadsheet_id_400_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    

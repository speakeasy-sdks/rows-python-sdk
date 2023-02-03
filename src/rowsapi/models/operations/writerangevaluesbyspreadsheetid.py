import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import overwritecells as shared_overwritecells
from ..shared import error as shared_error


@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetIDPathParams:
    range: str = dataclasses.field(metadata={'path_param': { 'field_name': 'range', 'style': 'simple', 'explode': False }})
    spreadsheet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'spreadsheet_id', 'style': 'simple', 'explode': False }})
    table_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'table_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON1:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON1
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON2:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON2
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON3:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON3
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON4:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON4
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON5:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON5
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON6:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON6
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON7:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON7
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON8:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON8
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetID400ApplicationJSON9:
    r"""WriteRangeValuesBySpreadsheetID400ApplicationJSON9
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetIDRequest:
    path_params: WriteRangeValuesBySpreadsheetIDPathParams = dataclasses.field()
    request: shared_overwritecells.OverwriteCells = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class WriteRangeValuesBySpreadsheetIDResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    write_range_values_by_spreadsheet_id_400_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    

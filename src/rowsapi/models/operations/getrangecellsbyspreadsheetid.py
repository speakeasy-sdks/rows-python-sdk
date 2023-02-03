import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import error as shared_error
from ..shared import rangelist as shared_rangelist


@dataclasses.dataclass
class GetRangeCellsBySpreadsheetIDPathParams:
    range: str = dataclasses.field(metadata={'path_param': { 'field_name': 'range', 'style': 'simple', 'explode': False }})
    spreadsheet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'spreadsheet_id', 'style': 'simple', 'explode': False }})
    table_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'table_id', 'style': 'simple', 'explode': False }})
    
class GetRangeCellsBySpreadsheetIDMajorDimensionEnum(str, Enum):
    ROW = "ROW"
    COLUMN = "COLUMN"

class GetRangeCellsBySpreadsheetIDValueRenderOptionEnum(str, Enum):
    FORMATTED = "FORMATTED"
    RAW = "RAW"


@dataclasses.dataclass
class GetRangeCellsBySpreadsheetIDQueryParams:
    major_dimension: Optional[GetRangeCellsBySpreadsheetIDMajorDimensionEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'major_dimension', 'style': 'form', 'explode': True }})
    value_render_option: Optional[GetRangeCellsBySpreadsheetIDValueRenderOptionEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'value_render_option', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeCellsBySpreadsheetID400ApplicationJSON1:
    r"""GetRangeCellsBySpreadsheetID400ApplicationJSON1
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeCellsBySpreadsheetID400ApplicationJSON2:
    r"""GetRangeCellsBySpreadsheetID400ApplicationJSON2
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeCellsBySpreadsheetID400ApplicationJSON3:
    r"""GetRangeCellsBySpreadsheetID400ApplicationJSON3
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeCellsBySpreadsheetID400ApplicationJSON4:
    r"""GetRangeCellsBySpreadsheetID400ApplicationJSON4
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetRangeCellsBySpreadsheetIDRequest:
    path_params: GetRangeCellsBySpreadsheetIDPathParams = dataclasses.field()
    query_params: GetRangeCellsBySpreadsheetIDQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetRangeCellsBySpreadsheetIDResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    range_list: Optional[shared_rangelist.RangeList] = dataclasses.field(default=None)
    get_range_cells_by_spreadsheet_id_400_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    

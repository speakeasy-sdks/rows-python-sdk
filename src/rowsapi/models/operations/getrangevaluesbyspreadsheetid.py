import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import error as shared_error


@dataclasses.dataclass
class GetRangeValuesBySpreadsheetIDPathParams:
    range: str = dataclasses.field(metadata={'path_param': { 'field_name': 'range', 'style': 'simple', 'explode': False }})
    spreadsheet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'spreadsheet_id', 'style': 'simple', 'explode': False }})
    table_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'table_id', 'style': 'simple', 'explode': False }})
    
class GetRangeValuesBySpreadsheetIDMajorDimensionEnum(str, Enum):
    ROW = "ROW"
    COLUMN = "COLUMN"

class GetRangeValuesBySpreadsheetIDValueRenderOptionEnum(str, Enum):
    FORMATTED = "FORMATTED"
    RAW = "RAW"


@dataclasses.dataclass
class GetRangeValuesBySpreadsheetIDQueryParams:
    major_dimension: Optional[GetRangeValuesBySpreadsheetIDMajorDimensionEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'major_dimension', 'style': 'form', 'explode': True }})
    value_render_option: Optional[GetRangeValuesBySpreadsheetIDValueRenderOptionEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'value_render_option', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeValuesBySpreadsheetID200ApplicationJSON:
    items: Optional[list[list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeValuesBySpreadsheetID400ApplicationJSON1:
    r"""GetRangeValuesBySpreadsheetID400ApplicationJSON1
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeValuesBySpreadsheetID400ApplicationJSON2:
    r"""GetRangeValuesBySpreadsheetID400ApplicationJSON2
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeValuesBySpreadsheetID400ApplicationJSON3:
    r"""GetRangeValuesBySpreadsheetID400ApplicationJSON3
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclass_json
@dataclasses.dataclass
class GetRangeValuesBySpreadsheetID400ApplicationJSON4:
    r"""GetRangeValuesBySpreadsheetID400ApplicationJSON4
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

@dataclasses.dataclass
class GetRangeValuesBySpreadsheetIDRequest:
    path_params: GetRangeValuesBySpreadsheetIDPathParams = dataclasses.field()
    query_params: GetRangeValuesBySpreadsheetIDQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetRangeValuesBySpreadsheetIDResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get_range_values_by_spreadsheet_id_200_application_json_object: Optional[GetRangeValuesBySpreadsheetID200ApplicationJSON] = dataclasses.field(default=None)
    get_range_values_by_spreadsheet_id_400_application_json_one_of: Optional[Any] = dataclasses.field(default=None)
    

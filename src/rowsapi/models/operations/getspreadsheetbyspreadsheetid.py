import dataclasses
from typing import Optional
from ..shared import error as shared_error
from ..shared import spreadsheetdetail as shared_spreadsheetdetail


@dataclasses.dataclass
class GetSpreadsheetBySpreadsheetIDPathParams:
    spreadsheet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'spreadsheet_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSpreadsheetBySpreadsheetIDRequest:
    path_params: GetSpreadsheetBySpreadsheetIDPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSpreadsheetBySpreadsheetIDResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    spreadsheet_detail: Optional[shared_spreadsheetdetail.SpreadsheetDetail] = dataclasses.field(default=None)
    

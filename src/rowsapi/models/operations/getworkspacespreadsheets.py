import dataclasses
from typing import Optional
from ..shared import error as shared_error
from ..shared import spreadsheetslist as shared_spreadsheetslist


@dataclasses.dataclass
class GetWorkspaceSpreadsheetsQueryParams:
    folder_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'folder_id', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetWorkspaceSpreadsheetsRequest:
    query_params: GetWorkspaceSpreadsheetsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkspaceSpreadsheetsResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    spreadsheets_list: Optional[shared_spreadsheetslist.SpreadsheetsList] = dataclasses.field(default=None)
    

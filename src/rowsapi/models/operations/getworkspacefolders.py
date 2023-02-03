import dataclasses
from typing import Optional
from ..shared import error as shared_error
from ..shared import folderlist as shared_folderlist


@dataclasses.dataclass
class GetWorkspaceFoldersQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetWorkspaceFoldersRequest:
    query_params: GetWorkspaceFoldersQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetWorkspaceFoldersResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    folder_list: Optional[shared_folderlist.FolderList] = dataclasses.field(default=None)
    

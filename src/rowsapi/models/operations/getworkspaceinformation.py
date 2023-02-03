import dataclasses
from typing import Optional
from ..shared import error as shared_error
from ..shared import workspace as shared_workspace


@dataclasses.dataclass
class GetWorkspaceInformationResponse:
    content_type: str = dataclasses.field()
    headers: dict[str, list[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    workspace: Optional[shared_workspace.Workspace] = dataclasses.field(default=None)
    

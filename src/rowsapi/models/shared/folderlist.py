import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils
from ..shared import folder as shared_folder


@dataclass_json
@dataclasses.dataclass
class FolderList:
    r"""FolderList
    Array of folders
    """
    
    items: Optional[list[shared_folder.Folder]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('items') }})
    next_page_results: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_page_results') }})
    

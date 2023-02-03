import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from rowsapi import utils


@dataclass_json
@dataclasses.dataclass
class Error:
    r"""Error
    The Error details JSON Object.
    """
    
    code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('code') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    

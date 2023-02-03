import dataclasses
from dataclasses_json import dataclass_json
from rowsapi import utils


@dataclass_json
@dataclasses.dataclass
class AppendValues:
    values: list[list[str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('values') }})
    

from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ApiResponse:
    code: str
    msg: str
    data: object

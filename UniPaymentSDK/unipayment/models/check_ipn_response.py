from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CheckIpnResponse:
    code: str
    msg: str
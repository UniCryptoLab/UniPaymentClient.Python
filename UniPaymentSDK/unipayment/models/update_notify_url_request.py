from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UpdateNotifyURLRequest:
    notify_url: str

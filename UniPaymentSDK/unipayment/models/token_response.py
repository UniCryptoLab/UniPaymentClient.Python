from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TokenResponse:
    access_token: str
    expires_in: int
    token_type: str
    scope: str

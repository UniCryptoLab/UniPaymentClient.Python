from dataclasses import dataclass
from typing import List, TypeVar, Generic

from dataclasses_json import dataclass_json

T = TypeVar('T')


@dataclass_json
@dataclass
class QueryResult(Generic[T]):
    models: List[T]
    page_no: int
    total: int
    page_count: int
    page_size: int

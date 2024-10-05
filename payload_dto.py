import json
from dataclasses import dataclass, field, asdict
from typing import Dict


@dataclass
class PayloadDto:
    event: str  # should come from enum
    url: str
    body: any
    headers: Dict[str, str] = field(default_factory=lambda: {})

    def to_dict(self) -> Dict:
        return asdict(self)

    def to_json(self, sort_keys: bool = False, indent: None | int | str = None) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=sort_keys, indent=indent)

from dataclasses import dataclass
from typing import Optional

@dataclass
class visitorDTO:
    id: int
    name: str
    email: str
    registration_date: Optional[str] = None

@dataclass
class SkiPassDTO:
    id: int
    visitor_id: int
    type: str
    valid_from: str
    valid_to: str

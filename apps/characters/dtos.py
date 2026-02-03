from dataclasses import dataclass
from typing import Optional,List

@dataclass
class CharacterCreateDTO:
    name: str
    bio: str
    image1: Optional[str] = None
    image2: Optional[str] = None
    image3: Optional[str] = None
    is_alive: bool = True

@dataclass
class CharacterResponseDTO:
    id: int
    name: str
    bio: str
    images: list[str]
    is_alive: bool


@dataclass
class CharacterListCursorDTO:
    results: List[CharacterResponseDTO]
    next_cursor: Optional[int] = None
from .dtos import CharacterCreateDTO,CharacterListCursorDTO
from .mappers import CharacterMapper
from .queries import CharacterQuery
from .exceptions import CharacterInvalidDataException

class CharacterServiceCreate:
    @staticmethod
    def create_character(dto: CharacterCreateDTO):
        if not dto.name or not dto.bio:
            raise CharacterInvalidDataException("Name and bio are required")
        character = CharacterMapper.to_model(dto)
        character.save()
        return character
    
class CharacterServiceList:
    @staticmethod
    def list_characters(limit: int = 10, cursor: int = None, is_alive: bool = None) -> CharacterListCursorDTO:
        characters, next_cursor = CharacterQuery.get_all_cursor(limit=limit, cursor=cursor, is_alive=is_alive)
        dtos = [CharacterMapper.to_dto(c) for c in characters]
        return CharacterListCursorDTO(results=dtos, next_cursor=next_cursor)
    

class CharacterByIDService:
    @staticmethod
    def get_character_by_id(character_id: int):
        character = CharacterQuery.get_by_id(character_id)
        return CharacterMapper.to_dto(character)

    

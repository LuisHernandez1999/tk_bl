from .models import Character
from .dtos import CharacterCreateDTO, CharacterResponseDTO

class CharacterMapper:

    @staticmethod
    def to_model(dto: CharacterCreateDTO) -> Character:
        return Character(
            name=dto.name,
            bio=dto.bio,
            image1=dto.image1,
            image2=dto.image2,
            image3=dto.image3,
            is_alive=dto.is_alive
        )

    @staticmethod
    def to_dto(character: Character) -> CharacterResponseDTO:
        images = [img for img in [character.image1, character.image2, character.image3] if img]
        return CharacterResponseDTO(
            id=character.id,
            name=character.name,
            bio=character.bio,
            images=images,
            is_alive=character.is_alive
        )

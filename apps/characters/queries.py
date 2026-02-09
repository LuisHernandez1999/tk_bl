from .models import Character
from .exceptions import CharacterNotFoundException

class CharacterQuery:
    @staticmethod
    def get_all_cursor(limit: int = 10, cursor: int = None, is_alive: bool = None):
        qs = Character.objects.only('id', 'name', 'bio', 'image1', 'image2', 'image3', 'is_alive') \
                              .order_by('id')
        if is_alive is not None:
            qs = qs.filter(is_alive=is_alive)
        if cursor:
            qs = qs.filter(id__gt=cursor)
        items = list(qs[:limit])
        if items:
            remaining = qs.filter(id__gt=items[-1].id).exists()
            next_cursor = items[-1].id if remaining else None
        else:
            next_cursor = None
        
        return items, next_cursor


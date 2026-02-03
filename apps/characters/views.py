from dataclasses import asdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views import View
from .services import CharacterServiceCreate,CharacterServiceList,CharacterByIDService
from .dtos import CharacterCreateDTO
from .mappers import CharacterMapper
from .exceptions import CharacterInvalidDataException, CharacterNotFoundException
import json

class CharacterCreateAPIView(APIView):
    def post(self, request):
        try:
            dto = CharacterCreateDTO(**request.data)
            character = CharacterServiceCreate.create_character(dto)
            return Response(asdict(CharacterMapper.to_dto(character)), status=status.HTTP_201_CREATED)
        except CharacterInvalidDataException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CharacterListView(View):
    def get(self, request):
        try:
            limit = int(request.GET.get('limit', 10))
            cursor = request.GET.get('cursor')
            is_alive = request.GET.get('is_alive')
            cursor = int(cursor) if cursor else None
            is_alive = is_alive.lower() == 'true' if is_alive is not None else None
            response_dto = CharacterServiceList.list_characters(limit=limit, cursor=cursor, is_alive=is_alive)
            return JsonResponse(asdict(response_dto), safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



class CharacterDetailView(View):
    def get(self, request, pk):
        try:
            character = CharacterByIDService.get_character_by_id(pk)
            return JsonResponse(asdict(character))
        except CharacterNotFoundException as e:
            return JsonResponse({'error': str(e)}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Word
from .serializers import WordSerializer


class WordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (AllowAny,)

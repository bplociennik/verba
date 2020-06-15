from rest_framework.viewsets import ModelViewSet

from .models import Sentence
from .serializers import SentenceSerializer


class SentenceViewSet(ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

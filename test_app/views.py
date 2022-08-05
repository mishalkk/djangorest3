from test_app.models import TestModel
from test_app.serializer import SimpleSerializer
from rest_framework import generics, viewsets


class Simple(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer



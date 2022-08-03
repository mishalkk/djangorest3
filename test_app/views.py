from django.http import JsonResponse, response
from rest_framework.views import APIView
from test_app.models import TestModel
from test_app.serializer import SimpleSerializer
from rest_framework import generics


class SimpleGenerics(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer


class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"

# class Simple(APIView):
#
#     def post(self, request):
#         serializer = SimpleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse({"data": serializer.data})
#
#     def get(self, request):
#         content = TestModel.objects.all()
#         data = SimpleSerializer(content, many=True).data
#         return JsonResponse({"data": data})
#
#     def put(self, request, *args, **kwargs):
#         model_id = kwargs.get("id", None)
#         if not model_id:
#             return JsonResponse({"error": "method /PUT/ not allowed"})
#         try:
#             instance = TestModel.objects.get(id=model_id)
#         except:
#             return JsonResponse({"error": "Object does not exist"})
#
#         serializer = SimpleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse({"data": serializer.data})


from django.http import JsonResponse, response
from rest_framework.views import APIView
from test_app.models import TestModel


class SimpleView(APIView):

    def post(self, request):
        new_test_content = TestModel.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            phone=request.data["phone_number"],
            is_alive=request.data["is_alive"],
            amount=request.data["amount"],
        )

        return JsonResponse({"data": [1, 2, 3, 4]})

    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data": list(content)})

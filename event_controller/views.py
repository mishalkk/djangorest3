from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from event_controller.serializers import (EventMain, EventMainSerializer, AddressGlobal, AddressGlobalSerializer,
                                          EventFeatureSerializer, EventAttender, EventAttenderSerializer)
from rest_framework.response import Response


class EventMainView(ModelViewSet):
    serializer_class = EventMainSerializer
    queryset = EventMain.objects.select_related("author", "address_info",).prefetch_related("event_feature")

    def create(self, request, *args, **kwargs):
        address_serializer = AddressGlobalSerializer(data=request.data)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        data = {**request.data, "address_info_id": address_serializer.data["id"]}

        event_serializer = self.serializer_class(data=data)
        if not event_serializer.is_valid():
            AddressGlobal.objects.filter(id=address_serializer.data["id"]).delete()
            raise Exception(event_serializer.errors)
        event_serializer.save()

        features = request.data.get("features", None)

        if not features:
            raise Exception("features field is required")

        if not isinstance(features, list):
            features = [features]

        data = []

        for f in features:
            if not isinstance(f, dict):
                AddressGlobal.objects.filter(id=address_serializer.data["id"]).delete()
                raise Exception("Feature instance must be an Object")
            data.append({**f, "event_main_id": event_serializer.data["id"]})

        feature_serializer = EventFeatureSerializer(data=data, many=True)

        if not feature_serializer.is_valid():
            AddressGlobal.objects.filter(id=address_serializer.data["id"]).delete()
            raise Exception(feature_serializer.errors)

        feature_serializer.save()

        return Response(self.serializer_class(self.get_queryset().get(id=event_serializer.data["id"])),
                        status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)

        event_serializer = self.serializer_class(data=request.data, instance=instance, partial=True)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save()

        address_serializer = AddressGlobalSerializer(data=request.data, instance=instance.address_info, partial=True)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        features = request.data.get("features", None)
        if features:
            if not isinstance(features, list):
                features = [features]
            data = []
            for f in features:
                if not isinstance(f, dict):
                    raise Exception("Feature instance must be an object")
                data.append({**f, "event_main_id": event_serializer.data["id"]})

            feature_serializer = EventFeatureSerializer(data=data, many=True)
            feature_serializer.is_valid(raise_exception=True)
            feature_serializer.save()

        return Response(self.serializer_class(self.get_object()).data)


class EventAttenderView(ModelViewSet):
    queryset = EventAttender.objects.select_related("user", "event_main")
    serializer_class = EventAttenderSerializer

    def create(self, request, *args, **kwargs):
        attender_serializer = self.serializer_class(data=request.data)
        attender_serializer.is_valid(raise_exception=True)

        event = EventMainView.queryset.filter(id=attender_serializer.validated_data["event_main_id"])

        if not event:
            raise Exception("Event does not exist.")

        event = event[0]

        # check if the maximum seat have not reached
        attender_count = self.queryset.filter(event_main_id=event.id).count()
        if not attender_count < event.max_seat:
            raise Exception("Maximum seat booked")

        # check attending time
        attend_time = attender_serializer.validated_data["time"]
        if attend_time < event.time:
            raise Exception("You are too early")

        attender_serializer.save()
        return Response(attender_serializer.data, status=status.HTTP_201_CREATED)




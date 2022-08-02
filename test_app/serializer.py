from rest_framework import serializers


class SimpleObject(serializers):

    def __int__(self, name):
        self.name = name


class SimpleObjectSerializer(serializers.Serializer):
    name = serializers.CharField()



def run_data():
    simple_var = SimpleObject("Henry")
    simple_var_serializer = SimpleObjectSerializer(simple_var)
    simple_var_serializer.data
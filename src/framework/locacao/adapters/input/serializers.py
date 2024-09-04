from rest_framework import serializers
class LocacaoSerializer(serializers.Serializer):
    id = serializers.CharField()
    data = serializers.DateField()
    itens = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(),
        ),
    )



class ItemLocacaoSerializer(serializers.Serializer):
    id = serializers.CharField()
    quantidade = serializers.IntegerField()
    dias = serializers.IntegerField()
    locacao = 


class CreateLocacaoRequestSerializer(serializers.Serializer):
    data = serializers.DateField()
    itens = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(),
        ),
    )

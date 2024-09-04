from rest_framework import serializers


class JogoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField()


class PlataformaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()


class JogoPlataformaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    jogo = JogoSerializer()
    plataforma = PlataformaSerializer()
    preco_diario = serializers.DecimalField(max_digits=10000, decimal_places=2)


class ItemLocacaoSerializer(serializers.Serializer):
    def to_representation(self, instance):

        return super().to_representation(instance)


class LocacaoInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data = serializers.DateField()
    itens = ItemLocacaoSerializer(many=True)


class LocacaoOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data = serializers.DateField()
    itens = ItemLocacaoSerializer(many=True)


ItemLocacaoSerializer._declared_fields["jogo_plataforma"] = JogoPlataformaSerializer()
ItemLocacaoSerializer._declared_fields["dias"] = serializers.IntegerField()
ItemLocacaoSerializer._declared_fields["quantidade"] = serializers.IntegerField()

from datetime import datetime

from rest_framework import serializers


class JogoOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField()


class JosoInputSerializer(serializers.Serializer):
    titulo = serializers.CharField()


class PlataOutputformaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()


class PlataInputformaSerializer(serializers.Serializer):
    nome = serializers.CharField()


class JogoOutputPlataformaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    jogo = JogoOutputSerializer()
    plataforma = PlataOutputformaSerializer()
    preco_diario = serializers.DecimalField(max_digits=10000, decimal_places=2)


class JogoInputPlataformaSerializer(serializers.Serializer):
    jogo = JosoInputSerializer()
    plataforma = PlataInputformaSerializer()
    preco_diario = serializers.DecimalField(max_digits=10000, decimal_places=2)


class ItemLocacaoOutputSerializer(serializers.Serializer):
    def to_representation(self, instance):

        return super().to_representation(instance)


class ItemLocacaoInputSerializer(serializers.Serializer):
    def to_representation(self, instance):

        return super().to_representation(instance)


class ItemLocacaoUpdateSerializer(serializers.Serializer):
    def to_representation(self, instance):

        return super().to_representation(instance)


class CustoTotalOutputSerializer(serializers.Serializer):
    valor = serializers.FloatField()


class LocacaoInputSerializer(serializers.Serializer):
    data = serializers.DateField()
    itens = ItemLocacaoInputSerializer(many=True)


class LocacaoOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data = serializers.DateField()
    itens = ItemLocacaoOutputSerializer(many=True)

    def to_representation(self, instance):
        ##convertenndo datetime para date
        if type(instance.data) is datetime:
            instance.data = datetime.date(instance.data)
        return super().to_representation(instance)


ItemLocacaoOutputSerializer._declared_fields["jogo_plataforma"] = (
    JogoOutputPlataformaSerializer()
)
ItemLocacaoOutputSerializer._declared_fields["dias"] = serializers.IntegerField()
ItemLocacaoOutputSerializer._declared_fields["quantidade"] = serializers.IntegerField()


ItemLocacaoInputSerializer._declared_fields["jogo_plataforma"] = (
    JogoInputPlataformaSerializer()
)
ItemLocacaoInputSerializer._declared_fields["dias"] = serializers.IntegerField()
ItemLocacaoInputSerializer._declared_fields["quantidade"] = serializers.IntegerField()


ItemLocacaoUpdateSerializer._declared_fields["jogo_plataforma"] = (
    JogoOutputPlataformaSerializer()
)
ItemLocacaoUpdateSerializer._declared_fields["dias"] = serializers.IntegerField()
ItemLocacaoUpdateSerializer._declared_fields["quantidade"] = serializers.IntegerField()

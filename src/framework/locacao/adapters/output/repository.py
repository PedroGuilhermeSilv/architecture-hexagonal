from django.db import transaction
from src.core.locacao.ports.output.locacao_repositoy import Locacao, LocacaoRepository
from src.framework.jogo.models import Jogo as JogoModel
from src.framework.jogo.models import JogoPlataforma as JogoPlataformaModel
from src.framework.locacao.models import ItemLocacao as ItemLocacaoModel
from src.framework.locacao.models import Locacao as LocacaoModel
from src.framework.plataforma.models import Plataforma as PlataformaModel


class DjangoORMRepository(LocacaoRepository):
    def __init__(self):
        self.model = LocacaoModel

    def save(self, locacao: Locacao) -> Locacao:
        with transaction.atomic():
            locacao_model = LocacaoModel.objects.create(
                id=locacao.id,
                data=locacao.data,
            )
            for item in locacao.itens:
                jogo, _ = JogoModel.objects.get_or_create(
                    id=item.jogo_plataforma.jogo.id,
                    defaults={"titulo": item.jogo_plataforma.jogo.titulo},
                )
                plataforma, _ = PlataformaModel.objects.get_or_create(
                    id=item.jogo_plataforma.plataforma.id,
                    defaults={"nome": item.jogo_plataforma.plataforma.nome},
                )

                jogo_plataforma, _ = JogoPlataformaModel.objects.get_or_create(
                    id=item.jogo_plataforma.id,
                    defaults={
                        "jogo": jogo,
                        "plataforma": plataforma,
                        "preco_diario": item.jogo_plataforma.preco_diario,
                    },
                )

                ItemLocacaoModel.objects.create(
                    locacao=locacao_model,
                    jogo_plataforma=jogo_plataforma,
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
        return locacao

from django.db import transaction
from src.core.client.domain.entity_client import Cliente
from src.core.locacao.domain.entity_locacao import ItemLocacao
from src.core.locacao.ports.output.locacao_repositoy import Locacao, LocacaoRepository
from src.framework.cliente.models import Cliente as ClienteModel
from src.framework.jogo.models import Jogo as JogoModel
from src.framework.jogo.models import JogoPlataforma as JogoPlataformaModel
from src.framework.locacao.models import ItemLocacao as ItemLocacaoModel
from src.framework.locacao.models import Locacao as LocacaoModel
from src.framework.plataforma.models import Plataforma as PlataformaModel


class DjangoORMLocacaoRepository(LocacaoRepository):
    def save(self, locacao: Locacao) -> Locacao:
        with transaction.atomic():
            cliente = ClienteModel.objects.get(
                email=locacao.cliente.email,
            )
            locacao_model = LocacaoModel.objects.create(
                id=locacao.id,
                data=locacao.data,
                cliente=cliente,
            )
            for item in locacao.itens:
                jogo, _ = JogoModel.objects.get_or_create(
                    titulo=item.jogo_plataforma.jogo.titulo,
                    defaults={"titulo": item.jogo_plataforma.jogo.titulo},
                )
                plataforma, _ = PlataformaModel.objects.get_or_create(
                    nome=item.jogo_plataforma.plataforma.nome,
                    defaults={"nome": item.jogo_plataforma.plataforma.nome},
                )

                jogo_plataforma, _ = JogoPlataformaModel.objects.get_or_create(
                    jogo=jogo,
                    defaults={
                        "jogo": jogo,
                        "plataforma": plataforma,
                        "preco_diario": item.jogo_plataforma.preco_diario,
                    },
                )

                ItemLocacaoModel.objects.get_or_create(
                    locacao=locacao_model,
                    jogo_plataforma=jogo_plataforma,
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
        return self.get_by_id(locacao_model.id)

    def update(self, locacao: Locacao) -> Locacao:
        with transaction.atomic():

            locacao_model = LocacaoModel.objects.get(id=locacao.id)
            locacao_model.data = locacao.data
            ItemLocacaoModel.objects.filter(locacao=locacao_model).delete()
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

                ItemLocacaoModel.objects.get_or_create(
                    locacao=locacao_model,
                    jogo_plataforma=jogo_plataforma,
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
                locacao_model.save()
        return self.get_by_id(locacao.id)

    def get_by_id(self, id: int) -> Locacao:
        locacao_model = LocacaoModel.objects.get(id=id)
        intes = ItemLocacaoModel.objects.filter(locacao=locacao_model)
        cliente = ClienteModel.objects.get(id=locacao_model.cliente.id)
        return Locacao(
            id=locacao_model.id,
            data=locacao_model.data,
            itens=[
                ItemLocacao(
                    jogo_plataforma=JogoPlataformaModel(
                        id=item.jogo_plataforma.id,
                        jogo=JogoModel(
                            id=item.jogo_plataforma.jogo.id,
                            titulo=item.jogo_plataforma.jogo.titulo,
                        ),
                        plataforma=PlataformaModel(
                            id=item.jogo_plataforma.plataforma.id,
                            nome=item.jogo_plataforma.plataforma.nome,
                        ),
                        preco_diario=item.jogo_plataforma.preco_diario,
                    ),
                    dias=item.dias,
                    quantidade=item.quantidade,
                )
                for item in intes
            ],
            cliente=Cliente(
                id=cliente.id,
                nome=cliente.nome,
                email=cliente.email,
                telefone=cliente.telefone,
                senha=cliente.senha,
            ),
        )

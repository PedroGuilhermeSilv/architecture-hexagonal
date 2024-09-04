import pytest
from src.core.jogo.domain.entity_jogo import Jogo
from src.core.jogo.domain.entity_jogo_plataforma import JogoPlataforma
from src.core.locacao.domain.item_locacao.entity_item_locacao import ItemLocacao
from src.core.locacao.domain.locacao.entity_locacao import Locacao
from src.core.plataforma.domain.entity_plataforma import Plataforma
from src.framework.jogo.models import Jogo as JogoModel
from src.framework.jogo.models import JogoPlataforma as JogoPlataformaModel
from src.framework.locacao.adapters.output.repository import DjangoORMRepository
from src.framework.locacao.models import ItemLocacao as ItemLocacaoModel
from src.framework.locacao.models import Locacao as LocacaoModel
from src.framework.plataforma.models import Plataforma as PlataformaModel


@pytest.mark.django_db
def test_save_locacao():
    # Arrange
    jogo = Jogo(id=1, titulo="Jogo Teste")
    plataforma = Plataforma(id=1, nome="Plataforma Teste")
    jogo_plataforma = JogoPlataforma(
        id=1,
        jogo=jogo,
        plataforma=plataforma,
        preco_diario=10.0,
    )
    locacao = Locacao(id=1, data="2023-10-10")
    item_locacao = ItemLocacao(
        jogo_plataforma=jogo_plataforma,
        dias=5,
        quantidade=1,
        locacao=locacao,
    )

    repository = DjangoORMRepository()

    # Act
    repository.save(locacao)

    # Assert
    locacao_model = LocacaoModel.objects.get(id=locacao.id)
    assert locacao_model is not None

    item_locacao_model = ItemLocacaoModel.objects.get(locacao=locacao_model)
    assert item_locacao_model is not None
    assert item_locacao_model.dias == item_locacao.dias
    assert item_locacao_model.quantidade == item_locacao.quantidade

    jogo_model = JogoModel.objects.get(id=jogo.id)
    assert jogo_model is not None
    assert jogo_model.titulo == jogo.titulo

    plataforma_model = PlataformaModel.objects.get(id=plataforma.id)
    assert plataforma_model is not None
    assert plataforma_model.nome == plataforma.nome

    jogo_plataforma_model = JogoPlataformaModel.objects.get(id=jogo_plataforma.id)
    assert jogo_plataforma_model is not None
    assert jogo_plataforma_model.jogo == jogo_model
    assert jogo_plataforma_model.plataforma == plataforma_model

import json

import pytest
from rest_framework.test import APIClient
from src.framework.jogo.models import Jogo as JogoModel
from src.framework.locacao.models import ItemLocacao as ItemLocacaoModel
from src.framework.locacao.models import JogoPlataforma as JogoPlataformaModel
from src.framework.locacao.models import Locacao as LocacaoModel
from src.framework.plataforma.models import Plataforma as PlataformaModel

STATUS_CODE_CREATED = 201
STATUS_CODE_OK = 200


@pytest.mark.django_db
class TestCreateAPI:
    def test_criar_locacao(self):
        # Arrange

        client = APIClient()
        data = {
            "data": "2023-04-01",
            "itens": [
                {
                    "jogo_plataforma": {
                        "jogo": {
                            "titulo": "The Legend of Zelda: Breath of the Wild",
                        },
                        "plataforma": {
                            "nome": "Nintendo Switch",
                        },
                        "preco_diario": "3.99",
                    },
                    "dias": 5,
                    "quantidade": 2,
                },
                {
                    "jogo_plataforma": {
                        "jogo": {
                            "titulo": "Super Mario Odyssey",
                        },
                        "plataforma": {
                            "nome": "Nintendo Switch",
                        },
                        "preco_diario": "2.99",
                    },
                    "dias": 3,
                    "quantidade": 1,
                },
            ],
        }

        # Act
        response = client.post(
            "/api/locacao/",
            data=json.dumps(data),
            content_type="application/json",
        )

        # Assert
        assert response.status_code == STATUS_CODE_CREATED

        locacao_on_db = LocacaoModel.objects.get(id=response.data["id"])
        assert locacao_on_db is not None

        itens_on_db = ItemLocacaoModel.objects.filter(locacao=locacao_on_db)
        assert itens_on_db.count() == len(data["itens"])
        for item_on_db, item in zip(itens_on_db, data["itens"]):
            assert item_on_db.dias == item["dias"]
            assert item_on_db.quantidade == item["quantidade"]
            assert (
                item_on_db.jogo_plataforma.jogo.titulo
                == item["jogo_plataforma"]["jogo"]["titulo"]
            )
            assert (
                item_on_db.jogo_plataforma.plataforma.nome
                == item["jogo_plataforma"]["plataforma"]["nome"]
            )
            assert float(item_on_db.jogo_plataforma.preco_diario) == float(
                item["jogo_plataforma"]["preco_diario"],
            )


@pytest.mark.django_db
class TestUpdateLocacao:
    def test_add_jogo_in_plataforma(self):
        # Arrange
        client = APIClient()

        locacao = LocacaoModel.objects.create(data="2023-04-01")
        item = ItemLocacaoModel.objects.create(
            locacao=locacao,
            dias=5,
            quantidade=2,
            jogo_plataforma=JogoPlataformaModel.objects.create(
                jogo=JogoModel.objects.create(
                    titulo="The Legend of Zelda: Breath of the Wild",
                ),
                plataforma=PlataformaModel.objects.create(nome="Nintendo Switch"),
                preco_diario="3.99",
            ),
        )

        data = {
            "jogo_plataforma": {
                "id": item.jogo_plataforma.id,
                "jogo": {
                    "id": item.jogo_plataforma.jogo.id,
                    "titulo": "Super Mario Odyssey",
                },
                "plataforma": {
                    "id": item.jogo_plataforma.plataforma.id,
                    "nome": "Nintendo Switch",
                },
                "preco_diario": "2.99",
            },
            "dias": 3,
            "quantidade": 1,
        }

        # Act
        response = client.patch(
            f"/api/locacao/{locacao.id}/jogo/",
            data=json.dumps(data),
            content_type="application/json",
        )

        itens = response.json()["itens"]

        # Assert
        assert response.status_code == STATUS_CODE_OK

        itens_on_db = ItemLocacaoModel.objects.filter(locacao=locacao)
        assert itens_on_db.count() == 2
        item_on_db = itens_on_db.last()
        assert item_on_db.dias == itens[1]["dias"]
        assert item_on_db.quantidade == itens[1]["quantidade"]
        assert (
            item_on_db.jogo_plataforma.jogo.titulo
            == itens[1]["jogo_plataforma"]["jogo"]["titulo"]
        )
        assert (
            item_on_db.jogo_plataforma.plataforma.nome
            == itens[1]["jogo_plataforma"]["plataforma"]["nome"]
        )
        assert float(item_on_db.jogo_plataforma.preco_diario) == float(
            itens[1]["jogo_plataforma"]["preco_diario"],
        )


@pytest.mark.django_db
class TestCalcularCustoTotal:
    def test_get_custo_total(self):
        # Arrange
        client = APIClient()

        locacao = LocacaoModel.objects.create(data="2023-04-01")
        item = ItemLocacaoModel.objects.create(
            locacao=locacao,
            dias=5,
            quantidade=2,
            jogo_plataforma=JogoPlataformaModel.objects.create(
                jogo=JogoModel.objects.create(
                    titulo="The Legend of Zelda: Breath of the Wild",
                ),
                plataforma=PlataformaModel.objects.create(nome="Nintendo Switch"),
                preco_diario="3.99",
            ),
        )

        # Act
        response = client.get(f"/api/locacao/{locacao.id}/custo/")

        # Assert
        assert response.status_code == STATUS_CODE_OK
        valor_total = 5 * 2 * 3.99
        assert response.json()["valor"] == round(valor_total, 2)

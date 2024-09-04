import json

import pytest
from rest_framework.test import APIClient

STATUS_CODE_CREATED = 201


@pytest.mark.django_db
class TestCreateAPI:
    def test_criar_locacao(self):
        # Arrange
        client = APIClient()
        data = {
            "id": 1,
            "data": "2023-04-01",
            "itens": [
                {
                    "jogo_plataforma": {
                        "id": 1,
                        "jogo": {
                            "id": 1,
                            "titulo": "The Legend of Zelda: Breath of the Wild",
                        },
                        "plataforma": {
                            "id": 1,
                            "nome": "Nintendo Switch",
                        },
                        "preco_diario": "3.99",
                    },
                    "dias": 5,
                    "quantidade": 2,
                },
                {
                    "jogo_plataforma": {
                        "id": 2,
                        "jogo": {
                            "id": 2,
                            "titulo": "Super Mario Odyssey",
                        },
                        "plataforma": {
                            "id": 1,
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
        assert response.json() == data

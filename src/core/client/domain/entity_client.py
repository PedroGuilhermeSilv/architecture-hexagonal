from dataclasses import dataclass, field


@dataclass
class Cliente:
    id: int
    email: str
    telefone: str
    nome: str
    locacao: list["Locacao"] = field(default_factory=list)  # type: ignore # noqa: F821
    senha: str | None = None

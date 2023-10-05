from typing import List


class Pessoa:
    num_pessoas: int = 0

    def __init__(self, nome: str) -> None:
        self.nome = nome
        Pessoa.num_pessoas += 1


if __name__ == "__main__":
    nomes: List[str] = ["Fabio", "Fernanda", "Daniela", "Valéria"]
    pessoas = [Pessoa(nome) for nome in nomes]
    print(Pessoa.num_pessoas)
    print(pessoas[0].nome)

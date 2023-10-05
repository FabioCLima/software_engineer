class Aluno:
    def __init__(self) -> None:
        self.nome: str = "Zé"
        self.idade: int = 18

    def dobra_idade(self):
        return self.idade * 2


if __name__ == "__main__":
    aluno1 = Aluno()
    aluno1.nome = "Maria"

    aluno2 = Aluno()
    aluno2.idade = 21

    print(aluno1.nome)
    print(aluno2.nome)

    print(aluno1.dobra_idade())
    print(aluno2.dobra_idade())

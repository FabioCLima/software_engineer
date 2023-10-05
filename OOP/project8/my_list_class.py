class ListDeNumeros:
    def __init__(self, numeros) -> None:
        self.numeros = numeros

    def __str__(self) -> str:
        return ",".join([str(n) for n in self.numeros])

    def soma(self):
        return sum(self.numeros)

    def media(self):
        return self.soma() / len(self.numeros)


if __name__ == "__main__":
    minha_lista = ListDeNumeros([1, 3, 5, 7, 9])
    print(f"A soma de {minha_lista} é {minha_lista.soma()}")
    print(f"A média de {minha_lista} é {minha_lista.media()}")

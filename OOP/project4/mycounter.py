class MyCounter:
    """
    A simple counter class.

    Attributes:
        count (int): The current count value.

    >>> mc = MyCounter()
    >>> mc.set_count(5)
    >>> mc.count
    5
    """

    def __init__(self, count: int = 0):
        self.count = count

    def set_count(self, n: int) -> None:
        """
        Set the counter's count to a specific value.

        Args:
            n (int): The value to set the count to.

        >>> mc = MyCounter()
        >>> mc.set_count(7)
        >>> mc.count
        7
        """

        self.count = n


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    mc = MyCounter()  # instanciando o objeto
    print(mc.count)  # printando o valor do atributo do objeto
    mc.set_count(5)  # setando o atributo count com o método count
    mc.count += 1  # somando 1 ao atributo
    print(mc.count)  # verificando novamente o valor do atributo

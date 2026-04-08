from expression import Expression

class Addition(Expression):
    """Expression representant u + v."""
    def __init__(self, u: Expression, v: Expression) -> None:
        self.u = u
        self.v = v

    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) + self.v.evaluer(x)

    def deriver(self) -> "Addition":
        return Addition(self.u.deriver(), self.v.deriver())

    def __str__(self) -> str:
        return f"({self.u} + {self.v})"


class Multiplication(Expression):
    """Expression representant u * v."""

    def __init__(self, u: Expression, v: Expression) -> None:
        self.u = u
        self.v = v

    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) * self.v.evaluer(x)

    def deriver(self) -> "Multiplication":
        return Multiplication(self.u.deriver(), self.v.deriver())

    def __str__(self) -> str:
        return f"({self.u} * {self.v})"
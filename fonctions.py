from expression import Expression
from operations import Multiplication


class Sin(Expression):
    """Expression representant sin(u)."""
    def __init__(self, u: Expression) -> None:
        self.u = u
    def evaluer(self, x: float) -> float:
        import math
        return math.sin(self.u.evaluer(x))
    def deriver(self) -> "Sin":
        return Multiplication(Cos(self.u), self.u.deriver())
    
    
class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, u: Expression) -> None:
        self.u = u 
    def evaluer(self, x: float) -> float:
        import math
        return math.cos(self.u.evaluer(x)) 
    def deriver(self) -> "Cos":
        return Multiplication(Cos(self.u), self.u.deriver())


class Exp(Expression):
    """Expression representant exp(u)."""
    def __init__(self, u: Expression) -> None:
        self.u = u
    def evaluer(self, x: float) -> float:
        import math
        return math.exp(self.u.evaluer(x))
    def deriver(self) -> "Exp":
        return Multiplication(Exp(self.u), self.u.deriver())
   
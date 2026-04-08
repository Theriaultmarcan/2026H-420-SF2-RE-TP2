from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients: list[float]) -> None:
        self.coefficients = coefficients

    def evaluer(self, x: float) -> float:
        return sum(a * (x ** i) for i, a in enumerate(self.coefficients))

    def deriver(self) -> "Polynome":
        if len(self.coefficients) <= 1:
            return Polynome([0])  # La derivee d'une constante est 0
        derivee_coeffs = [i * a for i, a in enumerate(self.coefficients)][1:]
        return Polynome(derivee_coeffs)

    def __str__(self) -> str:
        termes = []
        for i, a in enumerate(self.coefficients):
            if a == 0:
                continue
            abs_a = abs(a)
            if i == 0:
                terme = f"{abs_a}"
            elif i == 1:
                terme = "x" if abs_a == 1 else f"{abs_a}x"
            else:
                terme = f"x^{i}" if abs_a == 1 else f"{abs_a}x^{i}"

            if a < 0:
                terme = f"- {terme}"
            else:
                terme = f"+ {terme}"
            termes.append(terme)
        if not termes:
            return "0"
        termes = list(reversed(termes))

        if termes[0].startswith("+"):
            termes[0] = termes[0][2:] # Enlever le "+ " du premier terme
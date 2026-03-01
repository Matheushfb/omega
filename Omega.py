import sys
import math
import numpy as np 


class Omega:
    def __init__(self,lenstr,dec):
        self.lenstr = lenstr
        self.dec = dec

    def base_montador(self, lenstr: int) -> np.ndarray:
        """Constrói a base fatorial para o sistema de numeração factorádico.

        Args:
            lenstr: Tamanho da string (quantidade de elementos a permutar).

        Returns:
            Array numpy com os pesos posicionais da base fatorial.
        """
        size = lenstr - 1
        self.base = np.empty(size, dtype=int)
        acc = 1
        for idx in range(size - 1, -1, -1):
            self.base[idx] = acc
            acc *= idx + 2
        return self.base

    def gera_montador(self, dec: int, base_montador: np.ndarray) -> np.ndarray:
        """Converte um número decimal para representação em base fatorial (código de Lehmer).

        Args:
            dec: Número decimal a ser convertido (índice da permutação).
            base_montador: Array com os pesos da base fatorial.

        Returns:
            Array numpy com os dígitos na base factorádica.

        Raises:
            ValueError: Se dec ultrapassar o limite para o tamanho da base.
        """
        limite = len(base_montador)
        max_decimal = math.factorial(limite + 1)

        if dec >= max_decimal:
            raise ValueError("Limite do dígito decimal ultrapassado")

        self.montador = np.empty(limite, dtype=int)
        resto = dec

        for i in range(limite):
            self.montador[i], resto = divmod(resto, base_montador[i])

        return self.montador

    def permuta(self, montador: np.ndarray, nome: list) -> list:
        """Aplica o montador (código de Lehmer) para gerar a permutação correspondente.

        Modifica a lista nome in-place de direita para esquerda, realizando
        trocas baseadas nos valores do montador.

        Args:
            montador: Array com os dígitos na base factorádica.
            nome: Lista mutável a ser permutada (ex: list("matheus")).

        Returns:
            A mesma lista nome, agora permutada.
        """
        for i in range(len(nome) - 1, 0, -1):
            pos_destino = i - montador[i - 1]
            nome[i], nome[pos_destino] = nome[pos_destino], nome[i]
        return nome

    def gera_decimal(self, base_montador: np.ndarray, montador: np.ndarray) -> int:
        """Converte o montador (base factorádica) de volta para número decimal.

        Args:
            base_montador: Array com os pesos da base fatorial.
            montador: Array com os dígitos na base factorádica.

        Returns:
            O número decimal correspondente (índice da permutação).
        """
        return sum(
            base_montador[i] * montador[i]
            for i in range(len(base_montador))
        )


def main():
    """Permite chamar via linha de comando: python Omega.py <string> <dec>"""
    if len(sys.argv) != 3:
        print("Uso: python Omega.py <string> <dec>")
        print("  string: texto a ser permutado (ex: matheus)")
        print("  dec: índice da permutação (0 a n!-1)")
        sys.exit(1)

    nome = sys.argv[1]
    dec = int(sys.argv[2])

    o = Omega(len(nome), dec)
    base = o.base_montador(len(nome))
    montador = o.gera_montador(dec, base)
    resultado = o.permuta(montador, list(nome))

    print("".join(resultado))


if __name__ == "__main__":
    main()

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.codice}: {self.nome} {self.cognome}"

    def __eq__(self, other):
        return isinstance(other, Espositore) and self.codice == other.codice
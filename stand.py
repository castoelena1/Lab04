from espositore import Espositore


class Stand:
    def __init__(self, codice, superficie_mq, padiglione, prezzo):
        self.codice = codice
        self.superficie_mq = int(superficie_mq)
        self.padiglione = int(padiglione)
        self._prezzo = float(prezzo)
        self.disponibile = True
        self.espositore = None

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = float(prezzo)

    def assegna(self, espositore):
        if not self.disponibile:
            raise Exception(f"La cabina {self.codice} non è disponibile.")
        self.disponibile = False
        self.espositore = espositore

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.espositore}"
        return f"{self.codice}: Base | {self.superficie_mq} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - {stato}"

    def __repr__(self):
        return f"[{self.__str__()}]"

    def __lt__(self, other):
        return self.prezzo < other.prezzo

class StandPrese(Stand):
    def __init__(self, codice, superficie_mq, padiglione, prezzo, num_prese):
        super().__init__(codice, superficie_mq, padiglione, prezzo)
        self.num_prese = int(num_prese)

    @property
    def prezzo(self):
        return self._prezzo * (1 + 0.07 * self.num_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.espositore}"
        return f"{self.codice}: Prese Extra | {self.superficie_mq} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Prese aggiuntive: {self.num_prese} - {stato}"

class StandPremium(Stand):
    def __init__(self, codice, superficie_mq, padiglione, prezzo, posizione):
        super().__init__(codice, superficie_mq, padiglione, prezzo)
        self.posizione = posizione

    @property
    def prezzo(self):
        return self._prezzo * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.espositore}"
        return f"{self.codice}: Premium | {self.superficie_mq} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Posizione: {self.posizione} - {stato}"

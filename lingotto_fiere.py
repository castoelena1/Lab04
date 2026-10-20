import csv
from stand import *
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        self.stand.clear()
        self.espositori.clear()

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if not row:
                        continue
                    codice = row[0]
                    if codice.startswith("ST"):
                        if len(row) == 4:
                            stand = Stand(*row)
                        elif len(row) == 5:
                            if row[4].isdigit():
                                stand = StandPrese(row[0], row[1], row[2], row[3], row[4])
                            else:
                                stand = StandPremium(row[0], row[1], row[2], row[3], row[4])
                        self.stand.append(stand)
                    elif codice.startswith("ES"):
                        nome, cognome = row[1:]
                        espositore = Espositore(codice, nome, cognome)
                        self.espositori.append(espositore)
        except FileNotFoundError:
            print("File not found")

    def _stand(self, codice):
        return next((s for s in self.stand if s.codice == codice), None)

    def _espositore(self, codice):
        return next((e for e in self.espositori if e.codice == codice), None)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand = self._stand(codice_stand)
        espositore = self._espositore(codice_espositore)

        if not stand:
            raise Exception("Stand non trovato.")
        if not espositore:
            raise Exception("Espositore non trovato.")
        if not stand.disponibile:
            raise Exception("Stand non disponibile.")
        for s in self.stand:
            if espositore == s.espositore:
                raise Exception("Espositore già assegnato ad uno stand.")

        stand.assegna(espositore)

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for e in self.espositori:
            es_assegnato = f"- {e}"
            for s in self.stand:
                if e == s.espositore:
                    es_assegnato = f"{es_assegnato} --> Assegnato allo stand: {s.codice}"
                    break
            print(es_assegnato)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stand)

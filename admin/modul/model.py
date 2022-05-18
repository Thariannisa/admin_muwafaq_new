from datetime import datetime, timezone

modul_KIND = "modul"


class Modul:

    def __init__(self, judul, gambarDefault, PdfUrl, id=None):
        self.id = id
        self.judul = judul
        self.gambarDefault = gambarDefault
        self.PdfUrl = PdfUrl

    def ke_dictionary(self):
        hasil = {}

        if self.id is not None:
            hasil["id"] = self.id
        hasil['judul'] = self.judul
        hasil['gambarDefault'] = self.gambarDefault
        hasil['PdfUrl'] = self.PdfUrl
        return hasil

from enum import Enum


class IslemSonucu(Enum):
    HATA = 0, 'Hata oluştu'
    BASARILI = 200, 'İşlem başarılı'

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]
    
 


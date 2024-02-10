from decimal import Decimal


def getKesirliBolumString(text):
        index = text.find(".")  # Virgülün indeksini bul
        if index != -1:  # Nokta bulunursa
            return text[index + 1:]  # Noktanın bir sonrasından sona kadar olan kısmı döndür
        else:
            return "0"  # Nokta bulunamazsa boş dize döndür

def funcSayininBilimselGosterimde_OlmasiHalinde_BilimselGosterimdenKurtul(number:Decimal):
     strNumber = str(number)
     Index = strNumber.find("E")
     if Index > -1:
        #strNumber =format(number.quantize(Decimal('1')), 'f')
        #number = Decimal(strNumber)
        float_number = float(number) 
        number = Decimal(float_number)
        print("SayininBilimselGosterimde_OlmasiHalinde_Normalize_Et" + str(number))
     else:
        print("SayininBilimselGosterimde_OlmasiHalinde_Normalize_Et: Üstel sayı bulunamadı")
     return number

def SayiyiFormatla(number:Decimal):
        # Fonksiyon parametre olarak aldığı float türündeki sayısı string türünden okunabilir sayıya dönüştürür

        
        number = funcSayininBilimselGosterimde_OlmasiHalinde_BilimselGosterimdenKurtul(number)

        strSayi = str("")
        strNumber = str(number)
        print("SayiyiFormatla - number : " + str(number))
        integer_part = int(number)
        TamSayi = int(number)
        strKesirliSayi = getKesirliBolumString(strNumber)
        strTamSayi = "{:,.0f}".format(TamSayi).replace(",", ".")
        if strKesirliSayi == "0":
            strKesirliSayi =""
        else:
            strKesirliSayi = "," + strKesirliSayi

        # Aşağıdaki satır format fonksiyonu ile sayının tam sayı bölümünü alır ve sonrasına strKesirliSayi değişkeninin içerisindeki kesirli bölümü ekler
        strSayi="{:,.0f}".format(TamSayi).replace(",", ".") + strKesirliSayi

        # print("İşlem böyle sonuçlandı : " + strSayi)
        return strSayi        

def IsNullOrEmpty(s):
    """
    Verilen string'in null (None) veya boş olup olmadığını kontrol eder.

    Args:
        s (str): Kontrol edilecek string.

    Returns:
        bool: True if the string is None or empty, otherwise False.
    """
    return s is None or len(s.strip()) == 0
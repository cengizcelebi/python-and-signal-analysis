import sys
import locale
from PyQt5 import QtWidgets, uic, QtGui, Qt 
from PyQt5.QtWidgets import QMessageBox 

from PyQt5.QtCore import *



# Çelebi yardımcı işlemler bölümü
import Helper_HesapMakinesi as hM
from clsConstants import *
from clsMusterekFonksiyonlar import *

qtcreator_file  = "Tasarimlarim/HesapMakinesi.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

# Hesap makinesinde kullanılan üç ana değer var
# 1: sayıların girildiği ekran (txtScreen): Burada rakamlar formatlanarak string türünden sunulur
# 2: işleme esas olacak sayının float türünden tutulduğu GirilenDeger değişkeni
# 3: aritmetik işlemin matematiksel olarak sunulduğu ekran     


#---- START GLOBAL DEĞİŞKENLER -------------------

# GirilenDeger : Her rakam tıklamasından sonra ekranda oluşacak yeni sayının tutlacağı değişken
GirilenDeger = Decimal(0) 

# strGirilenDegerFormatlanmamis : Bir aritmetik formülünde ardışık olarak girilen işlemlerin ana ekranda 
# okunabilir olarak gösterilmesini sağlamak için kullanılacak ve tüm aritmetik işlemlerin String türünden 
# tutulduğu değişken
strGirilenDegerFormatlanmamis = str('')

# Bellek_YapilanSonIsleminSonucu : Her aritmetik işlemin sonlandırılmasından sonra o sonucun geçici olarak saklanacağı değişken
# Bu değişken M+ ve M- işlevleriye bellekte ilave aritmetik işlemler yapabilmesine imkan vermek için geçici bellek
Bellek_YapilanSonIsleminSonucu = Decimal(0) 

# Bellek : M+ ve M- işlevleriye bellekte ilave aritmetik işlemler yapılırken kullanılacak değişken
Bellek = Decimal(0) 

strMesaj_ParantezliIslem = "Ben henüz parantezlerle işlem ve hesaplama yapabilecek kadar gelişmedim.\n\nLütfen daha sonra tekrar deneyin."
strMesaj_YuzdeliIslem = "Ben henüz yüzdeli (%) hesaplama yapabilecek kadar gelişmedim.\n\nLütfen daha sonra tekrar deneyin."

# SayininIsareti : Yazılmakta olan sayının işaretini tutmak için kullanılır. Seçenekler Pozitif ve Negatif
SayininIsareti ="Pozitif"

#---- END GLOBAL DEĞİŞKENLER -------------------


class app_HesapMakinesi(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #super().__init__()
        Ui_MainWindow.__init__(self) 
        self.setupUi(self)
        
         
        # Veri giriş ekranında sadece sayılar ve matematiksel ifadelerin girişine müsaade edilsin
        regex=QRegExp("[0123456789+%-.,*]+")
        validator = QtGui.QRegExpValidator(regex)
        self.txtScreen.setValidator(validator)
        # --------------------------------------


        self.btn0.clicked.connect(lambda:self.InsertValue_to_Screen(0))
        self.btn1.clicked.connect(lambda:self.InsertValue_to_Screen(1))
        self.btn2.clicked.connect(lambda:self.InsertValue_to_Screen(2))
        self.btn3.clicked.connect(lambda:self.InsertValue_to_Screen(3))
        self.btn4.clicked.connect(lambda:self.InsertValue_to_Screen(4))
        self.btn5.clicked.connect(lambda:self.InsertValue_to_Screen(5))
        self.btn6.clicked.connect(lambda:self.InsertValue_to_Screen(6))
        self.btn7.clicked.connect(lambda:self.InsertValue_to_Screen(7))
        self.btn8.clicked.connect(lambda:self.InsertValue_to_Screen(8))
        self.btn9.clicked.connect(lambda:self.InsertValue_to_Screen(9))
        self.btnVirgul.clicked.connect(lambda:self.InsertValue_to_Screen(','))
        self.btnTemizle.clicked.connect(lambda:self.ClearScreen())
        self.btnToplama.clicked.connect(lambda:self.Set_IslemTuru('+'))
        self.btnCikartma.clicked.connect(lambda:self.Set_IslemTuru('-'))
        self.btnCarpma.clicked.connect(lambda:self.Set_IslemTuru('x'))
        self.btnBolme.clicked.connect(lambda:self.Set_IslemTuru('÷'))
        self.btnEnter.clicked.connect(lambda:self.AritmetikIslemiHesapla_ve_Sonlandir())
        self.btnParantez.clicked.connect(lambda:self.ShowMessage("Uyarı !", strMesaj_ParantezliIslem))
        self.btnYuzde.clicked.connect(lambda:self.ShowMessage("Uyarı !", strMesaj_YuzdeliIslem))
        self.btnMemoryEkleArti.clicked.connect(lambda:self.BellekIslemiYap('+'))
        self.btnMemoryEkleEksi.clicked.connect(lambda:self.BellekIslemiYap('-'))
        self.btnMemoryCagir.clicked.connect(lambda:self.BellekCagir())
        self.btnMemoryTemizle.clicked.connect(lambda:self.BellekTemizle())
        self.btnArtiEksi.clicked.connect(lambda:self.SayininIsaretiniDegistir())
        
        # Klavye ile girişe imkan tanımak için txtScreen'in KeyPress eventine bir Handler ekliyoruz 
        self.txtScreen.keyPressEvent = self.handle_key_press

    def handle_key_press(self, event):
        if event.key() == Qt.Key_0:
            self.InsertValue_to_Screen(0)
        elif event.key() == Qt.Key_1:
            self.InsertValue_to_Screen(1)    
        elif event.key() == Qt.Key_2:
            self.InsertValue_to_Screen(2)    
        elif event.key() == Qt.Key_3:
            self.InsertValue_to_Screen(3)    
        elif event.key() == Qt.Key_4:
            self.InsertValue_to_Screen(4)    
        elif event.key() == Qt.Key_5:
            self.InsertValue_to_Screen(5)    
        elif event.key() == Qt.Key_6:
            self.InsertValue_to_Screen(6)    
        elif event.key() == Qt.Key_7:
            self.InsertValue_to_Screen(7)    
        elif event.key() == Qt.Key_8:
            self.InsertValue_to_Screen(8)    
        elif event.key() == Qt.Key_9:
            self.InsertValue_to_Screen(9)   
        elif event.key() == Qt.Key_Comma or event.key() == Qt.Key_Period:
            self.InsertValue_to_Screen(',')
        elif event.key() == Qt.Key_Plus:
            self.Set_IslemTuru('+')   
        elif event.key() == Qt.Key_Minus:
            self.Set_IslemTuru('-')   
        elif event.key() == Qt.Key_Asterisk:
            self.Set_IslemTuru('x')   
        elif event.key() == Qt.Key_Slash:
            self.Set_IslemTuru('÷')   
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.AritmetikIslemiHesapla_ve_Sonlandir()   
        elif event.key() == Qt.Key_C:
            #self.ClearScreen()
            self.btnTemizle.click() 
    
    def ClearScreen(self):
            global strGirilenDegerFormatlanmamis
            global GirilenDeger
            GirilenDeger = float(0)
            strGirilenDegerFormatlanmamis = str('')
            self.txtScreen.setText("")
            self.txtMainScreen.setText("")
            hM.IslemlerListesi.clear()

    def AritmetikIslemiHesapla_ve_Sonlandir_OLD(self):
        global strGirilenDegerFormatlanmamis
        global GirilenDeger
       
        GirilenDeger = float(0)
        strGirilenDegerFormatlanmamis = str('')
        self.txtScreen.setText("")
        self.txtMainScreen.setText("")
        hM.funcIslemIslemlerListesisiniTemizle()

    def InsertValue_to_Screen(self, val:int): 
        global strGirilenDegerFormatlanmamis
        global GirilenDeger
        global SayininIsareti


        if str(val) == ",":
            # Ekrana herhangi bir sayı girilmeden sadece virgüle tıklanmışsa hata oluşmasını engelle
            if IsNullOrEmpty(strGirilenDegerFormatlanmamis) == True:
                return
            
        # Adım 1: Klavyeden girilendeğeri (sayı ve virgül dahil) global string değişkenine ilave et
        if SayininIsareti == "Negatif":
            strGirilenDegerFormatlanmamis +="-" + str(val)
        else:
            strGirilenDegerFormatlanmamis +=str(val)
        SayininIsareti = "Pozitif" # Sonraki kullanım için resetlemiş oluyoruz


        # print("Adım 1: " + strGirilenDegerFormatlanmamis)

        # Adım 2: Global string değişkeni içerisindeki virgülü nokta ile değiştir
        strTemp = strGirilenDegerFormatlanmamis.replace(',','.')



        # Adım 3: Global string değişkeninden float türüne dönüştürerek sayı üret ve global GirilenDeger değişkenine float sayıyı kaydet
        Sayi = Decimal(strTemp)
        GirilenDeger= Sayi

        # Adım 4: float türündeki sayıyı formatlayarak ekrana yazdır
        strFormatliSayi = SayiyiFormatla(Sayi)
        self.txtScreen.setText(strFormatliSayi)
        # self.txtMainScreen.setText(strFormatliSayi)
        #----------------------------------------------------------------    
    
    def Set_IslemTuru(self, val:str):  
        global strGirilenDegerFormatlanmamis
        global GirilenDeger

        print("Listeye eklenecek değer : " + str(GirilenDeger))
        hM.funcListeyeIslemEkle(GirilenDeger,val)
        self.txtMainScreen.setText(hM.funcGetIslemDokumuString())
        self.txtScreen.setText('')
        GirilenDeger=float(0)  
        strGirilenDegerFormatlanmamis = str("")

    def AritmetikIslemiHesapla_ve_Sonlandir(self):
        """ 
        print("Inside AritmetikIslemiHesapla_ve_Sonlandir") 
        """
        global strGirilenDegerFormatlanmamis
        global GirilenDeger
        global Bellek_YapilanSonIsleminSonucu


        print("En son GirilenDeger : " + str(GirilenDeger))
        hM.funcListeyeIslemEkle(GirilenDeger,"=") 
        #self.txtScreen.setText(SayiyiFormatla(hM.funcGetHesaplamaSonucu))
        self.txtScreen.setText("")
        self.txtMainScreen.setText(hM.funcGetIslemDokumu_ve_Sonucu_String())

        Bellek_YapilanSonIsleminSonucu = hM.funcGetHesaplamaSonucu()
        GirilenDeger = float(0)
        strGirilenDegerFormatlanmamis = ""
        #hM.funcIslemIslemlerListesisiniTemizle()
        print("Bellek_YapilanSonIsleminSonucu : " + str(Bellek_YapilanSonIsleminSonucu))

    def BellekIslemiYap(self, IslemOperatoru:str ):
        global Bellek
        global Bellek_YapilanSonIsleminSonucu
        if Bellek_YapilanSonIsleminSonucu != Decimal(0.0):
            if IslemOperatoru == "+":
              Bellek += Bellek_YapilanSonIsleminSonucu
            elif IslemOperatoru == "-":
              Bellek -= Bellek_YapilanSonIsleminSonucu
        self.lblBellek.setText(str(Bellek))
        
    def BellekCagir(self):

        global strGirilenDegerFormatlanmamis
        global GirilenDeger
        global Bellek
        GirilenDeger = float(0)
        strGirilenDegerFormatlanmamis = str('')
        self.txtScreen.setText("")
        self.txtMainScreen.setText("")

        hM.funcIslemIslemlerListesisiniTemizle()
        self.txtScreen.setText(str(Bellek).replace('.',','))

        strGirilenDegerFormatlanmamis += str(Bellek)
        strTemp = strGirilenDegerFormatlanmamis.replace(',','.')
        Sayi = Decimal(strTemp)
        GirilenDeger= Sayi

    def BellekTemizle(self):
        global Bellek
        global Bellek_YapilanSonIsleminSonucu
        Bellek = Decimal(0)
        Bellek_YapilanSonIsleminSonucu = Decimal(0)
    
    def SayininIsaretiniDegistir(self):
        global SayininIsareti

        CurrentInput = self.txtScreen.text()
        if IsNullOrEmpty(CurrentInput)==True:
            self.txtScreen.setText("-")
            SayininIsareti ="Negatif"
        else:    
            if CurrentInput[0] == '-':
               CurrentInput = CurrentInput.replace("-", "") 
               self.txtScreen.setText(CurrentInput)
               SayininIsareti ="Pozitif"
            else:
                self.txtScreen.setText("-" + CurrentInput)
                SayininIsareti ="Negatif"

    def ShowMessage(self, strTitle:str, strMessage:str):
        #hM.funcShowMessage("deneme")
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(strMessage)
        msg_box.setWindowTitle(strTitle)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        # Font boyutunu ayarla
        font = QtGui.QFont()
        font.setPointSize(11)  # 16 punto font boyutu
        msg_box.setFont(font)

        # msg_box.show() 
        msg_box.exec_() 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = app_HesapMakinesi()
    window.show()
    sys.exit(app.exec_())
    
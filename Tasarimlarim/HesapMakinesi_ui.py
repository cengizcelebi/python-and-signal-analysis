# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CENGİZ\Desktop\PhytonCalismalarim\Tasarimlarim\HesapMakinesi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(372, 654)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(372, 592))
        Form.setMaximumSize(QtCore.QSize(372, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\CENGİZ\\Desktop\\PhytonCalismalarim\\Tasarimlarim\\../images/icon Hesap Makinesi.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: red;\n"
"}\n"
"\n"
" QToolButton{\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    font-size: 20px;\n"
"    padding: 10px;\n"
"    width: 20px;\n"
"    height:20px;\n"
"    background: gray;\n"
"    color:white;\n"
"}\n"
"\n"
"QToolButton:hover{    \n"
"     background: white;\n"
"    color:black;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background: #f2f2f2;\n"
"}\n"
"\n"
"QToolButton#btnParantez,\n"
"QToolButton#btnYuzde\n"
"{\n"
"     background: lightgray;\n"
"    border: 2px solid lightgray;\n"
"}\n"
"\n"
"QToolButton#btnMemoryTemizle,\n"
"QToolButton#btnMemoryEkleArti,\n"
"QToolButton#btnMemoryEkleEksi,\n"
"QToolButton#btnMemoryCagir\n"
"{\n"
"    background: #64a2ff;\n"
"    border-color: #64a2ff;\n"
"    font-size: 16px;\n"
"}")
        self.txtScreen = QtWidgets.QLineEdit(Form)
        self.txtScreen.setGeometry(QtCore.QRect(20, 100, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.txtScreen.setFont(font)
        self.txtScreen.setAcceptDrops(False)
        self.txtScreen.setAutoFillBackground(False)
        self.txtScreen.setText("")
        self.txtScreen.setFrame(False)
        self.txtScreen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtScreen.setPlaceholderText("")
        self.txtScreen.setObjectName("txtScreen")
        self.btnTemizle = QtWidgets.QToolButton(Form)
        self.btnTemizle.setGeometry(QtCore.QRect(290, 520, 61, 51))
        self.btnTemizle.setStyleSheet("background-color:#f40352;\n"
"border: 2px solid #f40352;")
        self.btnTemizle.setCheckable(False)
        self.btnTemizle.setObjectName("btnTemizle")
        self.btnParantez = QtWidgets.QToolButton(Form)
        self.btnParantez.setGeometry(QtCore.QRect(20, 520, 61, 51))
        self.btnParantez.setObjectName("btnParantez")
        self.btnYuzde = QtWidgets.QToolButton(Form)
        self.btnYuzde.setGeometry(QtCore.QRect(110, 520, 61, 51))
        self.btnYuzde.setObjectName("btnYuzde")
        self.btnBolme = QtWidgets.QToolButton(Form)
        self.btnBolme.setGeometry(QtCore.QRect(290, 240, 61, 51))
        self.btnBolme.setObjectName("btnBolme")
        self.btnCarpma = QtWidgets.QToolButton(Form)
        self.btnCarpma.setGeometry(QtCore.QRect(290, 310, 61, 51))
        self.btnCarpma.setObjectName("btnCarpma")
        self.btn7 = QtWidgets.QToolButton(Form)
        self.btn7.setGeometry(QtCore.QRect(20, 240, 61, 51))
        self.btn7.setObjectName("btn7")
        self.btn9 = QtWidgets.QToolButton(Form)
        self.btn9.setGeometry(QtCore.QRect(200, 240, 61, 51))
        self.btn9.setObjectName("btn9")
        self.btn8 = QtWidgets.QToolButton(Form)
        self.btn8.setGeometry(QtCore.QRect(110, 240, 61, 51))
        self.btn8.setObjectName("btn8")
        self.btnCikartma = QtWidgets.QToolButton(Form)
        self.btnCikartma.setGeometry(QtCore.QRect(290, 380, 61, 51))
        self.btnCikartma.setObjectName("btnCikartma")
        self.btn4 = QtWidgets.QToolButton(Form)
        self.btn4.setGeometry(QtCore.QRect(20, 310, 61, 51))
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QToolButton(Form)
        self.btn6.setGeometry(QtCore.QRect(200, 310, 61, 51))
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QToolButton(Form)
        self.btn5.setGeometry(QtCore.QRect(110, 310, 61, 51))
        self.btn5.setObjectName("btn5")
        self.btnToplama = QtWidgets.QToolButton(Form)
        self.btnToplama.setGeometry(QtCore.QRect(290, 450, 61, 51))
        self.btnToplama.setObjectName("btnToplama")
        self.btn1 = QtWidgets.QToolButton(Form)
        self.btn1.setGeometry(QtCore.QRect(20, 380, 61, 51))
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QToolButton(Form)
        self.btn3.setGeometry(QtCore.QRect(200, 380, 61, 51))
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QToolButton(Form)
        self.btn2.setGeometry(QtCore.QRect(110, 380, 61, 51))
        self.btn2.setObjectName("btn2")
        self.btnEnter = QtWidgets.QToolButton(Form)
        self.btnEnter.setGeometry(QtCore.QRect(200, 450, 61, 51))
        self.btnEnter.setStyleSheet("color:#f40352;\n"
"background-color:white;\n"
"padding-top:5px;")
        self.btnEnter.setObjectName("btnEnter")
        self.btnVirgul = QtWidgets.QToolButton(Form)
        self.btnVirgul.setGeometry(QtCore.QRect(110, 450, 61, 51))
        self.btnVirgul.setStyleSheet("font-size:18px;\n"
"font-weight:bold;\n"
"line-height: 12px;\n"
"padding-top:0px;\n"
"vertical-align:top")
        self.btnVirgul.setObjectName("btnVirgul")
        self.btn0 = QtWidgets.QToolButton(Form)
        self.btn0.setGeometry(QtCore.QRect(20, 450, 61, 51))
        self.btn0.setObjectName("btn0")
        self.txtMainScreen = QtWidgets.QTextEdit(Form)
        self.txtMainScreen.setGeometry(QtCore.QRect(20, 20, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtMainScreen.setFont(font)
        self.txtMainScreen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtMainScreen.setObjectName("txtMainScreen")
        self.btnMemoryCagir = QtWidgets.QToolButton(Form)
        self.btnMemoryCagir.setGeometry(QtCore.QRect(110, 170, 61, 51))
        self.btnMemoryCagir.setObjectName("btnMemoryCagir")
        self.btnMemoryEkleEksi = QtWidgets.QToolButton(Form)
        self.btnMemoryEkleEksi.setGeometry(QtCore.QRect(200, 170, 61, 51))
        self.btnMemoryEkleEksi.setObjectName("btnMemoryEkleEksi")
        self.btnMemoryTemizle = QtWidgets.QToolButton(Form)
        self.btnMemoryTemizle.setGeometry(QtCore.QRect(20, 170, 61, 51))
        self.btnMemoryTemizle.setObjectName("btnMemoryTemizle")
        self.btnMemoryEkleArti = QtWidgets.QToolButton(Form)
        self.btnMemoryEkleArti.setGeometry(QtCore.QRect(290, 170, 61, 51))
        self.btnMemoryEkleArti.setObjectName("btnMemoryEkleArti")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 590, 331, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lblBellek = QtWidgets.QLabel(self.groupBox)
        self.lblBellek.setGeometry(QtCore.QRect(40, 10, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblBellek.setFont(font)
        self.lblBellek.setText("")
        self.lblBellek.setObjectName("lblBellek")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnArtiEksi = QtWidgets.QToolButton(Form)
        self.btnArtiEksi.setGeometry(QtCore.QRect(200, 520, 61, 51))
        self.btnArtiEksi.setObjectName("btnArtiEksi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hesap Makinesi"))
        self.btnTemizle.setText(_translate("Form", "C"))
        self.btnParantez.setText(_translate("Form", "()"))
        self.btnYuzde.setText(_translate("Form", "%"))
        self.btnBolme.setText(_translate("Form", "÷"))
        self.btnCarpma.setText(_translate("Form", "×"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn8.setText(_translate("Form", "8"))
        self.btnCikartma.setText(_translate("Form", "-"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn5.setText(_translate("Form", "5"))
        self.btnToplama.setText(_translate("Form", "+"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn2.setText(_translate("Form", "2"))
        self.btnEnter.setText(_translate("Form", "="))
        self.btnVirgul.setText(_translate("Form", "."))
        self.btn0.setText(_translate("Form", "0"))
        self.btnMemoryCagir.setText(_translate("Form", "MR"))
        self.btnMemoryEkleEksi.setText(_translate("Form", "M -"))
        self.btnMemoryTemizle.setText(_translate("Form", "MC"))
        self.btnMemoryEkleArti.setText(_translate("Form", "M +"))
        self.label.setText(_translate("Form", "M : "))
        self.btnArtiEksi.setText(_translate("Form", "+/-"))

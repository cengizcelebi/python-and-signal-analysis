# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CENGİZ\Desktop\PhytonCalismalarim\Tasarimlarim\frm_Dicom_Processor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 785)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("QTextEdit{\n"
"    border:solid 4px black;\n"
"    background:#ffffff;\n"
"    font-size:11px;\n"
"}\n"
"\n"
"QPushButton,\n"
"QToolButton{\n"
"    background-color:gray;\n"
"    color:white;\n"
"    font-size:13px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover{\n"
"    background:white; \n"
"    color:gray; \n"
"}\n"
"\n"
"QPushButton#btnOpenFile{\n"
"    background-color:#f40352;\n"
"    border: 2px solid #f40352;\n"
"}\n"
"\n"
"QPushButton#btnOpenFile:hover{\n"
"    background:white;  \n"
"    color:#f40352;\n"
"}\n"
"\n"
".clsDeneme{\n"
"color:red\n"
"}")
        self.btnOpenFile = QtWidgets.QPushButton(Form)
        self.btnOpenFile.setGeometry(QtCore.QRect(30, 20, 149, 41))
        self.btnOpenFile.setStyleSheet("")
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.txtHeader = QtWidgets.QTextEdit(Form)
        self.txtHeader.setGeometry(QtCore.QRect(60, 150, 831, 581))
        self.txtHeader.setObjectName("txtHeader")
        self.btnOpenFolder = QtWidgets.QPushButton(Form)
        self.btnOpenFolder.setGeometry(QtCore.QRect(230, 20, 149, 41))
        self.btnOpenFolder.setStyleSheet("")
        self.btnOpenFolder.setObjectName("btnOpenFolder")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dicom Processor"))
        self.btnOpenFile.setText(_translate("Form", "Dicom Dosyası Seç"))
        self.btnOpenFolder.setText(_translate("Form", "Dicom Data Klasörü Seç"))
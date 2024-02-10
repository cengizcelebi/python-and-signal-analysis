# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CENGİZ\Desktop\PhytonCalismalarim\Tasarimlarim\frm_matplotlib_2DResimIslemleri.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1084, 842)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\CENGİZ\\Desktop\\PhytonCalismalarim\\Tasarimlarim\\../images/icon-matplotlib.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QPlainTextEdit{\n"
"    border:solid 4px black;\n"
"    background:#ffffff;\n"
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
"}\n"
" ")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 991, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnOpenFile = QtWidgets.QPushButton(Form)
        self.btnOpenFile.setGeometry(QtCore.QRect(10, 100, 141, 41))
        self.btnOpenFile.setStyleSheet("")
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 611, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lblPath = QtWidgets.QLabel(self.groupBox)
        self.lblPath.setGeometry(QtCore.QRect(20, 30, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblPath.setFont(font)
        self.lblPath.setObjectName("lblPath")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(640, 160, 401, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblProperties = QtWidgets.QLabel(self.groupBox_2)
        self.lblProperties.setGeometry(QtCore.QRect(20, 30, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblProperties.setFont(font)
        self.lblProperties.setObjectName("lblProperties")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 260, 1061, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtEdit1 = QtWidgets.QPlainTextEdit(self.tab)
        self.txtEdit1.setGeometry(QtCore.QRect(10, 90, 1021, 421))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txtEdit1.setFont(font)
        self.txtEdit1.setWhatsThis("")
        self.txtEdit1.setStyleSheet("")
        self.txtEdit1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtEdit1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txtEdit1.setLineWidth(1)
        self.txtEdit1.setMidLineWidth(0)
        self.txtEdit1.setDocumentTitle("")
        self.txtEdit1.setPlainText("")
        self.txtEdit1.setPlaceholderText("")
        self.txtEdit1.setObjectName("txtEdit1")
        self.btn1 = QtWidgets.QPushButton(self.tab)
        self.btn1.setGeometry(QtCore.QRect(20, 30, 131, 41))
        self.btn1.setAutoDefault(False)
        self.btn1.setDefault(False)
        self.btn1.setFlat(False)
        self.btn1.setObjectName("btn1")
        self.chcGrid_Plot = QtWidgets.QCheckBox(self.tab)
        self.chcGrid_Plot.setGeometry(QtCore.QRect(190, 30, 211, 31))
        self.chcGrid_Plot.setObjectName("chcGrid_Plot")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtEdit2 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.txtEdit2.setGeometry(QtCore.QRect(20, 90, 1011, 421))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txtEdit2.setFont(font)
        self.txtEdit2.setFrameShape(QtWidgets.QFrame.Box)
        self.txtEdit2.setPlainText("")
        self.txtEdit2.setPlaceholderText("")
        self.txtEdit2.setObjectName("txtEdit2")
        self.btn2 = QtWidgets.QPushButton(self.tab_3)
        self.btn2.setGeometry(QtCore.QRect(20, 30, 131, 41))
        self.btn2.setObjectName("btn2")
        self.ddlCmapOptions = QtWidgets.QComboBox(self.tab_3)
        self.ddlCmapOptions.setGeometry(QtCore.QRect(170, 30, 331, 41))
        self.ddlCmapOptions.setObjectName("ddlCmapOptions")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 331, 16))
        self.label_2.setObjectName("label_2")
        self.chcGrid_Pseudocolor = QtWidgets.QCheckBox(self.tab_3)
        self.chcGrid_Pseudocolor.setGeometry(QtCore.QRect(520, 30, 211, 31))
        self.chcGrid_Pseudocolor.setObjectName("chcGrid_Pseudocolor")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.btn3 = QtWidgets.QPushButton(self.tab_4)
        self.btn3.setGeometry(QtCore.QRect(20, 30, 131, 41))
        self.btn3.setObjectName("btn3")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn4 = QtWidgets.QPushButton(self.tab_2)
        self.btn4.setGeometry(QtCore.QRect(20, 30, 131, 41))
        self.btn4.setObjectName("btn4")
        self.chcGrid_GrayScale = QtWidgets.QCheckBox(self.tab_2)
        self.chcGrid_GrayScale.setGeometry(QtCore.QRect(190, 30, 211, 31))
        self.chcGrid_GrayScale.setObjectName("chcGrid_GrayScale")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.btn5 = QtWidgets.QPushButton(self.tab_5)
        self.btn5.setGeometry(QtCore.QRect(20, 30, 131, 41))
        self.btn5.setObjectName("btn5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.txtHtmlContentHolder = QtWidgets.QTextEdit(self.tab_6)
        self.txtHtmlContentHolder.setGeometry(QtCore.QRect(110, 90, 761, 341))
        self.txtHtmlContentHolder.setObjectName("txtHtmlContentHolder")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.btnOpen3DdataFile = QtWidgets.QPushButton(self.tab_7)
        self.btnOpen3DdataFile.setGeometry(QtCore.QRect(20, 20, 141, 41))
        self.btnOpen3DdataFile.setStyleSheet("")
        self.btnOpen3DdataFile.setObjectName("btnOpen3DdataFile")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 80, 671, 241))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lbl3D_W = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_W.setGeometry(QtCore.QRect(130, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_W.setFont(font)
        self.lbl3D_W.setObjectName("lbl3D_W")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.label_5.setObjectName("label_5")
        self.lbl3D_H = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_H.setGeometry(QtCore.QRect(130, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_H.setFont(font)
        self.lbl3D_H.setObjectName("lbl3D_H")
        self.lbl3D_Z = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_Z.setGeometry(QtCore.QRect(130, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_Z.setFont(font)
        self.lbl3D_Z.setObjectName("lbl3D_Z")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(340, 70, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_Number_of_Slices = QtWidgets.QLabel(self.groupBox_3)
        self.label_Number_of_Slices.setGeometry(QtCore.QRect(340, 100, 101, 16))
        self.label_Number_of_Slices.setObjectName("label_Number_of_Slices")
        self.lbl3D_voxel_Width = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_voxel_Width.setGeometry(QtCore.QRect(440, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_voxel_Width.setFont(font)
        self.lbl3D_voxel_Width.setObjectName("lbl3D_voxel_Width")
        self.lbl3D_Number_of_Slices = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_Number_of_Slices.setGeometry(QtCore.QRect(440, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_Number_of_Slices.setFont(font)
        self.lbl3D_Number_of_Slices.setObjectName("lbl3D_Number_of_Slices")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(340, 40, 91, 16))
        self.label_8.setObjectName("label_8")
        self.lbl3D_voxel_Height = QtWidgets.QLabel(self.groupBox_3)
        self.lbl3D_voxel_Height.setGeometry(QtCore.QRect(440, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl3D_voxel_Height.setFont(font)
        self.lbl3D_voxel_Height.setObjectName("lbl3D_voxel_Height")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "2D Grafik İşlemleri"))
        self.label.setText(_translate("Form", "\"matplotlib\" Kütüphanesi ile 2D Grafik/Resim İşlemleri"))
        self.btnOpenFile.setText(_translate("Form", "Resim Dosyası Seç"))
        self.groupBox.setTitle(_translate("Form", "Dosya Adresi"))
        self.lblPath.setText(_translate("Form", "_"))
        self.groupBox_2.setTitle(_translate("Form", "Resim Boyutu"))
        self.lblProperties.setText(_translate("Form", "_"))
        self.lblProperties.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.tabWidget.setWhatsThis(_translate("Form", "<html><head/><body><p>Sana ne</p></body></html>"))
        self.txtEdit1.setProperty("class", _translate("Form", "clsTxtEditor"))
        self.btn1.setText(_translate("Form", "Komutu Çalıştır"))
        self.chcGrid_Plot.setText(_translate("Form", "Grid çizgilerini göster"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Image Plotting"))
        self.btn2.setText(_translate("Form", "Komutu Çalıştır"))
        self.label_2.setText(_translate("Form", "Uygulanacak Renk Paleti"))
        self.chcGrid_Pseudocolor.setText(_translate("Form", "Grid çizgilerini göster"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Applying Pseudocolor"))
        self.btn3.setText(_translate("Form", "Komutu Çalıştır"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Histogram"))
        self.btn4.setText(_translate("Form", "Komutu Çalıştır"))
        self.chcGrid_GrayScale.setText(_translate("Form", "Grid çizgilerini göster"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Gray Scale"))
        self.btn5.setText(_translate("Form", "Komutu Çalıştır"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Split RGB Channels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Page"))
        self.btnOpen3DdataFile.setText(_translate("Form", "3D Veri Dosyası Seç"))
        self.groupBox_3.setTitle(_translate("Form", "Data Boyutu"))
        self.lbl3D_W.setText(_translate("Form", "_"))
        self.lbl3D_W.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.label_3.setText(_translate("Form", "Width : "))
        self.label_4.setText(_translate("Form", "Height : "))
        self.label_5.setText(_translate("Form", "Number of Images : "))
        self.lbl3D_H.setText(_translate("Form", "_"))
        self.lbl3D_H.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.lbl3D_Z.setText(_translate("Form", "_"))
        self.lbl3D_Z.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.label_6.setText(_translate("Form", "Voxel Height : "))
        self.label_Number_of_Slices.setText(_translate("Form", "Number of Slices : "))
        self.lbl3D_voxel_Width.setText(_translate("Form", "_"))
        self.lbl3D_voxel_Width.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.lbl3D_Number_of_Slices.setText(_translate("Form", "_"))
        self.lbl3D_Number_of_Slices.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.label_8.setText(_translate("Form", "Voxel Width : "))
        self.lbl3D_voxel_Height.setText(_translate("Form", "_"))
        self.lbl3D_voxel_Height.setProperty("class", _translate("Form", "clsDeneme clsDeneme234"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "3D Data Processing"))

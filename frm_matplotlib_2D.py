import sys
 
from PyQt5 import QtWidgets, uic, QtGui, Qt 
from PyQt5.QtWidgets import (QMessageBox, QAction, QApplication, QFileDialog, QMainWindow,
                            QMdiArea, QMessageBox, QTextEdit, QWidget)

from PyQt5.QtCore import *


from PIL import Image
import matplotlib.image as mpimg # Bu kütüphane resmin boyutlarını okumak için gerekli

import matplotlib.pyplot as plt
import numpy as np


qtcreator_file  = "Tasarimlarim/frm_matplotlib_2DResimIslemleri.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

fileName = str("")

class app_MatPlotLib2D(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #super().__init__()
        Ui_MainWindow.__init__(self) 
        self.setupUi(self)
        
        self.btnOpenFile.clicked.connect(lambda:self.SelectImageFile())
        self.btn1.clicked.connect(lambda:self.func1_PlotImage())
        self.btn2.clicked.connect(lambda:self.func2_PseudocolorImage())
        self.btn3.clicked.connect(lambda:self.func3_HistogramImage())
        self.btn4.clicked.connect(lambda:self.func4_GrayScaleImage())
        self.btn5.clicked.connect(lambda:self.func5_SplitIntoRGBchannelsImage())

        self.btnOpen3DdataFile.clicked.connect(lambda:self.temp_Select3DDataFile())
        
        
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)

        strTextEdit1_Content = (
                    "Bu bölümdeki örnekler için aşağıdaki bağlantıyı ziyaret edin:\n"
                    "https://matplotlib.org/stable/tutorials/index.html\n\n"
                    "We use Pillow to open an image (with PIL.Image.open), and "
                    "immediately convert the \nPIL.Image.Image object into an 8-bit (dtype=uint8) numpy array.\n\n"
                    "   img = np.asarray(Image.open('" + fileName + "')\n"
                    "   print(repr(img))\n"
                    "   imgplot = plt.imshow(img)\nplt.show()\n\n\n"
                    "Each inner list represents a pixel. Here, with an RGB image, there are 3 values. Since it's a black and white image, R, G, and B are all similar.\n"
                    "An RGBA (where A is alpha, or transparency) has 4 values per inner list, and a simple luminance image just has one value (and is thus only a 2-D array, not a 3-D array). For RGB and RGBA images, Matplotlib supports float32 and uint8 data types. For grayscale, Matplotlib supports only float32. If your array data does not meet one of these descriptions, you need to rescale it.\n\n"
                    "So, you have your data in a numpy array (either by importing it, or by generating it). Let's render it. In Matplotlib, this is performed using the imshow() function. Here we'll grab the plot object. This object gives you an easy way to manipulate the plot from the prompt.\n\n"
                    "   imgplot = plt.imshow(img)"
                    )
        strTextEdit2_Content = (
                    "Applying pseudocolor schemes to image plots\n\n"
                    "Pseudocolor can be a useful tool for enhancing contrast and visualizing your data more easily. This is especially useful when making presentat.ions of your data using projectors - their contrast is typically quite poor.\n\n"
                    "Pseudocolor is only relevant to single-channel, grayscale, luminosity images. We currently have an RGB image. Since R, G, and B are all similar (see for yourself above or in your data), we can just pick one channel of our data using array slicing.\n\n"
                    "\n"
                    "\n     lum_img = img[:, :, 0]"
                    "\n     plt.imshow(lum_img)"
                    "\n"
                    )
        self.txtEdit1.setPlainText(strTextEdit1_Content)
        self.txtEdit2.setPlainText(strTextEdit2_Content)
        
        options = ["gray", "nipy_spectral", "jet", "hsv", "gnuplot", "terrain", "ocean", "cubehelix", "tab10", "tab20", "tab20b", "tab20c", "flag", "prism", "gist_earth", "gist_stern", "brg", "CMRmap", "viridis", "plasma", "inferno", "magma", "cividis", "spring", "summer", "autumn", "winter", "cool", "Wistia", "hot", "coolwarm", "bwr", "RdPu", "PuRd", "OrRd", "YlOrRd", "YlOrBr", "Reds", "Oranges", "Greens", "Blues", "Purples", "Greys", "seismic", "BuPu", "GnBu", "PuBu", "YlGnBu", "PuBuGn", "BuGn", "YlGn"]
        self.ddlCmapOptions.addItems(options)

        with open("index.htm", "r", encoding="utf-8") as file:
            html_content = file.read()
        self.txtHtmlContentHolder.setHtml(html_content)

        # btnOpen3DdataFile
    def Select3DDataFile(self): 
       global fileName
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       filter = "3D Veri Dosyaları (*.df1 *.hd1 *.raw)"
       fileName, _ = QFileDialog.getOpenFileName(self, "3D Veri Dosyası Seç", "", filter, options=options)
       if fileName:
            # Resmin boyutlarını al
            # 8-bit raw dosyasını okuyun
            data = np.fromfile(fileName, dtype=np.uint16)
            print(data)

             
            self.lbl3DProperties.setText(str(181) + " x " + str(217) + " x " + str(181))        
    
    
    dataWidth =int(0)
    dataHeight =int(0)
    dataNumOfImages =int(0)
    voxelWidth =float(0)
    voxelHeight =float(0)
    voxelNumOfSlices =float(0)
    
    
    def temp_Select3DDataFile(self): 

        import struct

        global fileName
        global dataWidth  
        global dataHeight  
        global dataNumOfImages  
        global voxelWidth  
        global voxelHeight  
        global voxelNumOfSlices  

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filter = "3D Veri Dosyaları (*.df1 *.hd1 *.raw)"
        fileName, _ = QFileDialog.getOpenFileName(self, "3D Veri Dosyası Seç", "", filter, options=options)

        HeaderfileName=fileName.replace("df1","hd1")

        if HeaderfileName:
            # Header dosyasını açın ve içeriğini okuyun
            with open(HeaderfileName, "rb") as file:
                header_content = file.read()

            # İlk 8 baytı 4 integer parametreye çözümleyin
            integer_params = struct.unpack("4h", header_content[:8])

            # Sonraki 24 baytı 3 floating point parametreye çözümleyin
            float_params = struct.unpack("3d", header_content[8:32])

            # Elde edilen değerleri yazdırın
            dataWidth =integer_params[0]
            dataHeight =integer_params[1]
            dataNumOfImages =integer_params[2]
            voxelWidth =float_params[0]
            voxelHeight =float_params[1]
            voxelNumOfSlices =float_params[2]

            print("Integer Parametreler:", integer_params)
            print("Floating Point Parametreler:", float_params)
            self.lbl3D_W.setText(str(integer_params[0])) 
            self.lbl3D_H.setText(str(integer_params[1])) 
            self.lbl3D_Z.setText(str(integer_params[2])) 
            self.lbl3D_voxel_Width.setText(str(float_params[0])) 
            self.lbl3D_voxel_Height.setText(str(float_params[1])) 
            self.lbl3D_Number_of_Slices.setText(str(float_params[2])) 


            # 8-bit raw dosyasını okuyun
            data = np.fromfile(fileName, dtype=np.uint8)

            # Veriyi yeniden şekillendirin (3D veri olduğunu varsayalım)
             
            data = data.reshape((dataWidth, dataHeight, dataNumOfImages))

            # Veriyi 2D kesitler halinde görselleştirin
            fig, axs = plt.subplots(3, 3, figsize=(50, 50))
            for i in range(3):
                for j in range(3):
                    axs[i, j].imshow(data[:, :, i * 3 + j], cmap='gray')  # Her bir kesiti görselleştirin
                    axs[i, j].axis('off')  # Eksenleri kapatın
            plt.show()

             

    def SelectImageFile(self): 
       global fileName

       
       
       options = QFileDialog.Options()
       options |= QFileDialog.DontUseNativeDialog
       filter = "Resim Dosyaları (*.png *.jpg *.jpeg *.jpe *.bmp *.gif *.tiff)"
       fileName, _ = QFileDialog.getOpenFileName(self, "Dosya Seç", "", filter, options=options)
       if fileName:
            self.lblPath.setText(fileName)
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)
            self.btn4.setEnabled(True)
            self.btn5.setEnabled(True)

            # Resmin boyutlarını al
            img = mpimg.imread(fileName)
            height, width, _ = img.shape
            self.lblProperties.setText(str(width) + " px x " + str(height) + " px")

            

    def func1_PlotImage(self):
       global fileName
       plt.figure()
       img2 = np.asarray(Image.open(fileName))
       print(repr(img2))
       imgplot = plt.imshow(img2)
       plt.title("Image Plot")
       plt.xlabel('X')
       plt.ylabel('Y')

       if self.chcGrid_Plot.isChecked():
           plt.grid(True)
       plt.show()

    
    def func2_PseudocolorImage(self):
       global fileName
       plt.figure()
       img = np.asarray(Image.open(fileName))
       print(repr(img))
       lum_img = img[:, :, 0]
       #plt.imshow(lum_img)
       plt.imshow(lum_img, cmap=self.ddlCmapOptions.currentText())
       #plt.contour(lum_img, levels=5)  # 10 seviyede konturlar
       plt.colorbar()
       plt.xlabel('X')
       plt.ylabel('Y')
       if self.chcGrid_Pseudocolor.isChecked():
           plt.grid(True)
       plt.title("Image Plot with Pseudocolor Applied: \n" + self.ddlCmapOptions.currentText())
       plt.show()

    def func3_HistogramImage(self):
       global fileName
       plt.figure()
       img = np.asarray(Image.open(fileName))
       print(repr(img))
       lum_img = img[:, :, 0]
       plt.hist(img.ravel(), bins=range(256), fc='k', ec='k')
       plt.grid(True)
       plt.xlabel('X - Ekseni: RGB değerlerinin 0-255 aralığında normalleştirilmiş karşılıkları')
       plt.ylabel('Y - Ekseni: Normalleştirilmiş piksel değerlerinin görülme sıklığı')
       plt.title("Image Histogram Plot")
       plt.show()

    def func4_GrayScaleImage(self):
       global fileName
       plt.figure()
       img = np.asarray(Image.open(fileName))
       print(repr(img))

       # Resmi gray scale'e dönüştür
       gray_img = img.mean(axis=2) 
       """
       img.mean(axis=2) ifadesindeki axis=2 parametresi, ortalama işleminin hangi eksen boyunca gerçekleştirileceğini belirtir. 
       Bu parametre, resmin boyutlandırma şeklini dikkate alarak belirlenir.

       Renkli bir görüntü, tipik olarak üç boyutlu bir dizi olarak temsil edilir: Yükseklik (height), Genişlik (width) ve Renk Kanalları (RGB). 
       Bu durumda, axis=2 parametresi, işlemin üçüncü boyutta gerçekleştirilmesi gerektiğini belirtir.

       axis=2, numpy dizisindeki üçüncü boyutu temsil eder. Renkli bir görüntüde bu boyut, renk kanallarını (kırmızı, yeşil, mavi) içerir. 
       Bu nedenle, img.mean(axis=2) ifadesi, her pikselin üç renk kanalının ortalamasını alarak gri tonlamalı bir görüntü oluşturur.
       
       """
       # Gray scale resmi göster
       plt.imshow(gray_img, cmap='gray')

       if self.chcGrid_GrayScale.isChecked():
           print("chcGrid_GrayScale.isChecked()")
           plt.grid(True)
       
       plt.colorbar()
       plt.xlabel('X - Ekseni: Genişlik')
       plt.ylabel('Y - Ekseni: Yükseklik')
       plt.title("Image Plot with Gray Scale Applied")
       #plt.axis('off')  # Eksenleri kapat
       plt.show()
        
    def func5_SplitIntoRGBchannelsImage_OLD(self):
       global fileName   
       img = plt.imread(fileName)

       # R, G, B bileşenlerine ayır
       R = img[:, :, 0]
       G = img[:, :, 1]
       B = img[:, :, 2]

       # R, G, B bileşenlerini görüntüle
       plt.figure(figsize=(20, 10))

       plt.subplot(2, 3, 1)
       plt.imshow(G, cmap='gray')
       plt.title('Kırmızı (R)')
       plt.axis('off')

       plt.subplot(2, 3, 2)
       plt.imshow(G, cmap='gray')
       plt.title('Yeşil (G)')
       plt.axis('off')

       plt.subplot(2, 3, 3)
       plt.imshow(G)
       plt.title('Mavi (B)')
       #plt.axis('off')

       

       plt.show()

    def func5_SplitIntoRGBchannelsImage(self):
       global fileName   
        
       # RGB bir resmi yükle
        
       img = Image.open(fileName)

       # R, G, B bileşenlerine ayır
       R, G, B = img.split()

       plt.figure(figsize=(10, 5))

       plt.subplot(2, 3, 1)
       plt.imshow(R, cmap='grey')
       plt.title('Kırmızı (R)')
        
       plt.subplot(2, 3, 2)
       plt.imshow(G, cmap='grey')
       plt.title('Yeşil (G)')

       plt.subplot(2, 3, 3)
       plt.imshow(B, cmap='grey')
       plt.title('Mavi (B)')

       # Her bir kanalın histogramını hesaplayın
       r_histogram = R.histogram()
       g_histogram = G.histogram()
       b_histogram = B.histogram()

       plt.subplot(2, 3, 4)
       plt.bar(range(256), r_histogram, color='red', alpha=0.7)
       plt.title("Red Histogram")
       plt.grid(True)

       plt.subplot(2, 3, 5)
       plt.bar(range(256), g_histogram, color='green', alpha=0.7)
       plt.title("Green Histogram")
       plt.grid(True)

       plt.subplot(2, 3, 6)
       plt.bar(range(256), b_histogram, color='blue', alpha=0.7)
       plt.title("Blue Histogram")
       plt.grid(True)

       plt.show()
 

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
    window = app_MatPlotLib2D()
    window.show()
    sys.exit(app.exec_())
import sys
 
from PyQt5 import QtWidgets, uic, QtGui, Qt 
 
from PyQt5.QtWidgets import (QMessageBox, QAction, QApplication, QFileDialog, QMainWindow,
                            QMdiArea, QMessageBox, QTextEdit, QWidget)

from PyQt5.QtCore import *

from PIL import Image
import matplotlib.image as mpimg # Bu kütüphane resmin boyutlarını okumak için gerekli

import imageio as iio
import scipy.ndimage as ndi
 

import matplotlib.pyplot as plt
import numpy as np


 


qtcreator_file  = "Tasarimlarim/frm_Dicom_Processor.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

fileName = str("")
dataWidth =int(0)
dataHeight =int(0)
dataNumOfImages =int(0)
voxelWidth =float(0)
voxelHeight =float(0)
voxelNumOfSlices =float(0)


class app_DicomProcessor(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #super().__init__()
        Ui_MainWindow.__init__(self) 
        self.setupUi(self)

        icn=QtGui.QIcon("images/dicom.ico")
        self.setWindowIcon(icn)
        
        self.btnOpenFile.clicked.connect(lambda:self.Select3DDataFile())
        self.btnOpenFolder.clicked.connect(lambda:self.Select3D_DataFolder())
         

    
    def Select3DDataFile(self): 
        global fileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filter = "Dicom Veri Dosyaları (*.dcm)"
        fileName, _ = QFileDialog.getOpenFileName(self, "Dicom Dosyası Seç", "", filter, options=options)
        if fileName:
            brain_slice = iio.v2.imread(fileName, 'DICOM')
            type(brain_slice)
            
            self.txtHeader.setText(str(brain_slice.meta).replace(",", ",\n"))
            
            fig, ax = plt.subplots(1, 1, figsize=(10, 10))
            plt.imshow(brain_slice, cmap='gray')
            plt.axis('off')
            plt.show()

            # ax.set_xticks(np.arange(0, 255, 10))
            # ax.set_yticks(np.arange(0, 255, 10))
            # ax.set_xticks(np.arange(0, 255, 2), minor=True)
            # ax.set_yticks(np.arange(0, 255, 2), minor=True)
            # ax.grid(which='major', color='grey', linestyle='-', linewidth=1)
            # ax.grid(which='minor', color='grey', linestyle='-', linewidth=1)

            print(brain_slice.shape)
            print(brain_slice.meta['Rows'])
            print(brain_slice.meta['Columns'])
            #print(brain_slice.meta)
             
    def Select3D_DataFolder(self):
        # Klasör seçme iletişim kutusunu aç0
        folder_path = QFileDialog.getExistingDirectory(self, "Klasör Seç" )
        print("Seçilen Klasör:", folder_path)
        if folder_path:
            brain_vol = iio.volread(folder_path, 'DICOM')
            print(brain_vol.shape)
            plt.imshow(brain_vol[96], cmap='bone')
            plt.axis('on')
            plt.show()

            plt.imshow(brain_vol[:, 128], cmap='bone')
            plt.axis('on')
            plt.show()

            plt.imshow(ndi.rotate(brain_vol[:, :, 128], 270), cmap='grey')
            plt.axis('off')
            plt.show()


            fig_rows = 4
            fig_cols = 4
            n_subplots = fig_rows * fig_cols
            n_slice = brain_vol.shape[0]
            step_size = n_slice // n_subplots
            plot_range = n_subplots * step_size
            start_stop = int((n_slice - plot_range) / 2)

            fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

            for idx, img in enumerate(range(start_stop, plot_range, step_size)):
                axs.flat[idx].imshow(brain_vol[img, :, :], cmap='gray')
                axs.flat[idx].axis('off')
                    
            plt.tight_layout()
            plt.show()


            plt.plot(ndi.histogram(brain_vol, min=0, max=np.max(brain_vol), bins=50))
            plt.show()

             
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = app_DicomProcessor()
    window.show()
    sys.exit(app.exec_())                    
    
    
    
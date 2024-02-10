
from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QSettings, QSignalMapper,
        QSize, QTextStream, Qt, QProcess)
from PyQt5.QtGui import QIcon, QKeySequence, QFont
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget)


from PyQt5.QtWidgets import QMdiSubWindow
from frm_HesapMakinesi import app_HesapMakinesi
from frm_matplotlib_2D import app_MatPlotLib2D
from pyqt_first import app_VergiHesapMakinesi
 
class MdiChild(QTextEdit):
    sequenceNumber = 1

    def __init__(self):
        super(MdiChild, self).__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled = True
        icn=QIcon("images/text-file.ico")
        self.setWindowIcon(icn)

    def newFile(self):
        self.isUntitled = True
        self.curFile = "document%d.txt" % MdiChild.sequenceNumber
        MdiChild.sequenceNumber += 1
        self.setWindowTitle(self.curFile + '[*]')

        self.document().contentsChanged.connect(self.documentWasModified)

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "MDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return False

        instr = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.setPlainText(instr.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)

        self.document().contentsChanged.connect(self.documentWasModified)

        return True

    def save(self):
        if self.isUntitled:
            return self.saveAs()
        else:
            return self.saveFile(self.curFile)

    def saveAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", self.curFile)
        if not fileName:
            return False

        return self.saveFile(fileName)

    def saveFile(self, fileName):
        file = QFile(fileName)

        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "MDI",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outstr = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outstr << self.toPlainText()
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        return True

    def userFriendlyCurrentFile(self):
        return self.strippedName(self.curFile)

    def currentFile(self):
        return self.curFile

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def documentWasModified(self):
        self.setWindowModified(self.document().isModified())

    def maybeSave(self):
        if self.document().isModified():
            ret = QMessageBox.warning(self, "MDI",
                    "'%s' has been modified.\nDo you want to save your "
                    "changes?" % self.userFriendlyCurrentFile(),
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def setCurrentFile(self, fileName):
        self.curFile = QFileInfo(fileName).canonicalFilePath()
        self.isUntitled = False
        self.document().setModified(False)
        self.setWindowModified(False)
        self.setWindowTitle(self.userFriendlyCurrentFile() + "[*]")

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()



class MDIParent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çelebi MDI Parent Uygulaması")
        icn=QIcon("images/text-file.ico")
        self.setWindowIcon(icn)

        self.mdiArea = QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.updateMenus()
        self.readSettings()
        self.setWindowTitle("MDI")
        #self.hesap_makinesini_goster()

    
    def hesap_makinesini_goster_OLD(self):
        hesap_makinesi = app_HesapMakinesi()
        hesap_makinesi.setFixedSize(382, 674)
        subwindow = QMdiSubWindow()

        subwindow.setWidget(hesap_makinesi)
        # Boyutlandırılabilirliği devre dışı bırak
        subwindow.setFixedSize(subwindow.sizeHint())
        
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()
    
    def hesap_makinesini_goster(self):

        # Alt uygulamayı başlat
        


        hesap_makinesi = app_HesapMakinesi()
        hesap_makinesi.setFixedSize(382, 674)
        subwindow = QMdiSubWindow()

        subwindow.setWidget(hesap_makinesi)
        # Boyutlandırılabilirliği devre dışı bırak
        subwindow.setFixedSize(subwindow.sizeHint())
        
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()

         

    def vergi_HesapMakinesini_goster(self):
        vergi_hesap_makinesi = app_VergiHesapMakinesi()
        vergi_hesap_makinesi.setFixedSize(382, 674)
        subwindow = QMdiSubWindow()

        subwindow.setWidget(vergi_hesap_makinesi)
        # Boyutlandırılabilirliği devre dışı bırak
        subwindow.setFixedSize(subwindow.sizeHint())
        
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()

    def matPlotLib_2D_Islemleri_Formunu_goster(self):
        matPlotLib_2D = app_MatPlotLib2D()
        matPlotLib_2D.setFixedSize(1084, 842)
        subwindow = QMdiSubWindow()

        subwindow.setWidget(matPlotLib_2D)
        # Boyutlandırılabilirliği devre dışı bırak
        subwindow.setFixedSize(subwindow.sizeHint())
        
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()

    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            self.writeSettings()
            event.accept()
         

    def newFile(self):
        child = self.createMdiChild()
        child.newFile()
        child.show()

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if fileName:
            existing = self.findMdiChild(fileName)
            if existing:
                self.mdiArea.setActiveSubWindow(existing)
                return

            child = self.createMdiChild()
            if child.loadFile(fileName):
                self.statusBar().showMessage("File loaded", 2000)
                child.show()
            else:
                child.close()

    def save(self):
        if self.activeMdiChild() and self.activeMdiChild().save():
            self.statusBar().showMessage("File saved", 2000)

    def saveAs(self):
        if self.activeMdiChild() and self.activeMdiChild().saveAs():
            self.statusBar().showMessage("File saved", 2000)

    def cut(self):
        if self.activeMdiChild():
            self.activeMdiChild().cut()

    def copy(self):
        if self.activeMdiChild():
            self.activeMdiChild().copy()

    def paste(self):
        if self.activeMdiChild():
            self.activeMdiChild().paste()

    def about(self):
        QMessageBox.about(self, "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    def updateMenus(self):
        hasMdiChild = (self.activeMdiChild() is not None)
        self.saveAct.setEnabled(hasMdiChild)
        self.saveAsAct.setEnabled(hasMdiChild)
        self.pasteAct.setEnabled(hasMdiChild)
        self.closeAct.setEnabled(hasMdiChild)
        self.closeAllAct.setEnabled(hasMdiChild)
        self.tileAct.setEnabled(hasMdiChild)
        self.cascadeAct.setEnabled(hasMdiChild)
        self.nextAct.setEnabled(hasMdiChild)
        self.previousAct.setEnabled(hasMdiChild)
        self.separatorAct.setVisible(hasMdiChild)

        hasSelection = (self.activeMdiChild() is not None and
                        self.activeMdiChild().textCursor().hasSelection())
        self.cutAct.setEnabled(hasSelection)
        self.copyAct.setEnabled(hasSelection)

    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows = self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) != 0)

        for i, window in enumerate(windows):
            child = window.widget()

            text = "%d %s" % (i + 1, child.userFriendlyCurrentFile())
            if i < 9:
                text = '&' + text

            action = self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.activeMdiChild())
            action.triggered.connect(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    def createMdiChild(self):
        child = MdiChild()
        self.mdiArea.addSubWindow(child)

        child.copyAvailable.connect(self.cutAct.setEnabled)
        child.copyAvailable.connect(self.copyAct.setEnabled)

        return child

    def createActions(self):
        self.newAct = QAction(QIcon('images/new-file.ico'), "&Yeni", self,
                shortcut=QKeySequence.New, statusTip="Create a new file",
                triggered=self.newFile)
        
        self.hesapMakinesiAct = QAction(QIcon('images/icon Hesap Makinesi.ico'), "Hesap Makinesi", self,
                shortcut=QKeySequence.New, statusTip="Hesap makinesini aç",
                triggered=self.hesap_makinesini_goster)
        
        self.vergiHesapMakinesiAct = QAction(QIcon('images/icon Hesap Makinesi.ico'), "Vergi Hesap Makinesi", self,
                shortcut=QKeySequence.New, statusTip="Hesap makinesini aç",
                triggered=self.vergi_HesapMakinesini_goster)
        
        self.matPlotLibAct = QAction(QIcon('images/icon-matplotlib.ico'), "Mat Plot Lib 2D Image İşlemleri", self,
                shortcut=QKeySequence.New, statusTip="Mat Plot Lib 2D Image İşlemleri",
                triggered=self.matPlotLib_2D_Islemleri_Formunu_goster)

        self.openAct = QAction(QIcon('images/open-file.ico'), "&Aç...", self,
                shortcut=QKeySequence.Open, statusTip="Open an existing file",
                triggered=self.open)

        self.saveAct = QAction(QIcon('images/save-file.ico'), "&Kaydet", self,
                shortcut=QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)

        self.saveAsAct = QAction("&Farklı Kaydet...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Save the document under a new name",
                triggered=self.saveAs)

        self.exitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit,
                statusTip="Exit the application",
                triggered=QApplication.instance().closeAllWindows)

        self.cutAct = QAction(QIcon('images/cut.png'), "Cu&t", self,
                shortcut=QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut)

        self.copyAct = QAction(QIcon('images/copy.png'), "&Copy", self,
                shortcut=QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy)

        self.pasteAct = QAction(QIcon('images/paste.png'), "&Paste", self,
                shortcut=QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste)

        self.closeAct = QAction("Cl&ose", self,
                statusTip="Close the active window",
                triggered=self.mdiArea.closeActiveSubWindow)

        self.closeAllAct = QAction("Close &All", self,
                statusTip="Close all the windows",
                triggered=self.mdiArea.closeAllSubWindows)

        self.tileAct = QAction("&Tile", self, statusTip="Tile the windows",
                triggered=self.mdiArea.tileSubWindows)

        self.cascadeAct = QAction("&Cascade", self,
                statusTip="Cascade the windows",
                triggered=self.mdiArea.cascadeSubWindows)

        self.nextAct = QAction("Ne&xt", self, shortcut=QKeySequence.NextChild,
                statusTip="Move the focus to the next window",
                triggered=self.mdiArea.activateNextSubWindow)

        self.previousAct = QAction("Pre&vious", self,
                shortcut=QKeySequence.PreviousChild,
                statusTip="Move the focus to the previous window",
                triggered=self.mdiArea.activatePreviousSubWindow)

        self.separatorAct = QAction(self)
        self.separatorAct.setSeparator(True)

        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Dosya")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        action = self.fileMenu.addAction("Switch layout direction")
        action.triggered.connect(self.switchLayoutDirection)
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Düzenle")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.editMenu = self.menuBar().addMenu("Araçlar")
        self.editMenu.addAction(self.hesapMakinesiAct)
        self.editMenu.addAction(self.vergiHesapMakinesiAct)
        self.editMenu.addAction(self.matPlotLibAct)

        self.windowMenu = self.menuBar().addMenu("&WPencere")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Yardım")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        size=QSize(20,20) 
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.setIconSize(size)
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.setIconSize(size)
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        settings = QSettings('Trolltech', 'MDI Example')
        pos = settings.value('pos', QPoint(200, 200))
        size = settings.value('size', QSize(400, 400))
        self.move(pos)
        self.resize(size)

    def writeSettings(self):
        settings = QSettings('Trolltech', 'MDI Example')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def findMdiChild(self, fileName):
        canonicalFilePath = QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList():
            if window.widget().currentFile() == canonicalFilePath:
                return window
        return None

    def switchLayoutDirection(self):
        if self.layoutDirection() == Qt.LeftToRight:
            QApplication.setLayoutDirection(Qt.RightToLeft)
        else:
            QApplication.setLayoutDirection(Qt.LeftToRight)

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    
    # MDI form için genel fontu belirleyelim
    new_font = app.font()
    new_font.setPointSize(10)
    new_font.setFamilies(["Segoe UI"])
    app.setFont(new_font)

    window = MDIParent()
    window.show()
    sys.exit(app.exec_())
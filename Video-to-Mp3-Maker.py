from PyQt5 import QtCore, QtGui, QtWidgets
import moviepy.editor as mp 
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 364)
        MainWindow.setMaximumSize(QtCore.QSize(418, 364))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(170, 40, 71, 41))
        self.openBtn.setObjectName("openBtn")
        self.openBtn.clicked.connect(self.openFile)


        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(160, 170, 91, 41))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.saveFileName)


        self.videoFile = QtWidgets.QLineEdit(self.centralwidget)
        self.videoFile.setGeometry(QtCore.QRect(20, 110, 381, 31))
        self.videoFile.setObjectName("videoFile")
        self.videoFile.setReadOnly(True)


        self.audioFilename = QtWidgets.QLineEdit(self.centralwidget)
        self.audioFilename.setGeometry(QtCore.QRect(20, 230, 381, 31))
        self.audioFilename.setObjectName("audioFilename")
        self.audioFilename.setReadOnly(True)
        

        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(170, 290, 81, 41))
        self.convert.setObjectName("convert")
        self.convert.clicked.connect(self.convertVideo)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video-to-Mp3 Maker"))
        self.openBtn.setText(_translate("MainWindow", "Open File"))
        self.saveBtn.setText(_translate("MainWindow", "Save File As"))
        self.convert.setText(_translate("MainWindow", "Convert"))

    def openFile(self):
        global videofilename
        file = QtWidgets.QFileDialog.getOpenFileName(None,'Open File','c:\\','Video Files (*.mp4 *.webm *.avi *.mkv)')
        videofilename = file[0]
        print('Opened:',videofilename)
        self.videoFile.setText(os.path.basename(videofilename))
    
    def saveFileName(self):
        global audiofilename
        file = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File As', 'c:\\', 'Audio File (*.mp3)')
        audiofilename = file[0]
        print('Saving File As: ', audiofilename)
        self.audioFilename.setText(os.path.basename(audiofilename))        

    def convertVideo(self):
        try:
            video = mp.VideoFileClip(videofilename)
            video.audio.write_audiofile(audiofilename)
            print("Converted") 
            msgDone = QtWidgets.QMessageBox()
            msgDone.setIcon(QtWidgets.QMessageBox.Information)
            msgDone.setWindowTitle("Done")
            msgDone.setText("Conversion Completed")
            msgDone.exec_()       
            os.startfile(os.path.dirname(audiofilename))
            self.videoFile.clear()
            self.audioFilename.clear()
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Error!!")
            msgError.exec_()            
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

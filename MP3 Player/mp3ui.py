# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#Song names put in a list
song_list = []
with open("song_names.txt") as songNames:
    for line in songNames:
        song_list.append(line)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(238, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.PLAY = QtWidgets.QPushButton(self.centralwidget)
        self.PLAY.setGeometry(QtCore.QRect(70, 160, 111, 41))
        self.PLAY.setObjectName("PLAY")
        
        self.Unpause = QtWidgets.QPushButton(self.centralwidget)
        self.Unpause.setGeometry(QtCore.QRect(120, 200, 111, 41))
        self.Unpause.setObjectName("Unpause")

        self.PREVIOUS = QtWidgets.QPushButton(self.centralwidget)
        self.PREVIOUS.setGeometry(QtCore.QRect(120, 240, 111, 41))
        self.PREVIOUS.setObjectName("PREVIOUS")

        self.NEXT = QtWidgets.QPushButton(self.centralwidget)
        self.NEXT.setGeometry(QtCore.QRect(10, 240, 111, 41))
        self.NEXT.setObjectName("NEXT")

           
        self.PAUSE = QtWidgets.QPushButton(self.centralwidget)
        self.PAUSE.setGeometry(QtCore.QRect(10, 200, 111, 41))
        self.PAUSE.setObjectName("PAUSE")

        self.ShowSong = QtWidgets.QLabel(self.centralwidget)
        self.ShowSong.setGeometry(QtCore.QRect(30, 70, 191, 81))
        self.ShowSong.setAlignment(QtCore.Qt.AlignCenter)
        self.ShowSong.setObjectName("ShowSong")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 238, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.current_song = 0

        #interacion buttons with other stuff
        self.PLAY.clicked.connect(lambda: self.Play(song_list[self.current_song]))
        self.PAUSE.clicked.connect(self.Pause)
        self.Unpause.clicked.connect(self.Unnpause)
        self.NEXT.clicked.connect(lambda: self.Next("No Time to Die"))
        self.PREVIOUS.clicked.connect(lambda: self.Previous("No Time to Die"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PLAY.setText(_translate("MainWindow", "PLAY"))
        self.Unpause.setText(_translate("MainWindow", "Unpause"))
        self.PREVIOUS.setText(_translate("MainWindow", "Previous"))
        self.NEXT.setText(_translate("MainWindow", "Next"))
        self.ShowSong.setText(_translate("MainWindow", "Song Name"))
        self.PAUSE.setText(_translate("MainWindow", "Pause"))
    
    #Play the song
    def Play(self,song_name):
        song_path="Songs/{}".format(song_name).strip()+".mp3"
    
        self.ShowSong.setText(song_name)
        mixer.music.load(song_path)
        mixer.music.play()
    #Pause song
    def Pause(self):
        mixer.music.pause()
    #Unpause song
    def Unnpause(self):
        mixer.music.unpause()
    #Next song
    def Next(self,song_name):
        if self.current_song  <= 2:
            self.current_song +=1
            print(self.current_song)
            self.Play(song_list[self.current_song ])
    #Previous Song
    def Previous(self,song_name):
        if self.current_song  >0:
            self.current_song -=1
            print(self.current_song)
            self.Play(song_list[self.current_song ])
            


if __name__ == "__main__":
    import sys
    import os
    from pygame import mixer
    mixer.init()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_statistics_graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 525)
        self.by_artist = QtWidgets.QPushButton(Dialog)
        self.by_artist.setGeometry(QtCore.QRect(40, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.by_artist.setFont(font)
        self.by_artist.setObjectName("by_artist")
        self.main_title = QtWidgets.QLabel(Dialog)
        self.main_title.setGeometry(QtCore.QRect(120, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.by_label = QtWidgets.QPushButton(Dialog)
        self.by_label.setGeometry(QtCore.QRect(200, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.by_label.setFont(font)
        self.by_label.setObjectName("by_label")
        self.by_goat = QtWidgets.QPushButton(Dialog)
        self.by_goat.setGeometry(QtCore.QRect(371, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.by_goat.setFont(font)
        self.by_goat.setObjectName("by_goat")
        self.graph = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.graph.setGeometry(QtCore.QRect(40, 140, 461, 361))
        self.graph.setObjectName("graph")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Estatistica por grafico"))
        self.by_artist.setText(_translate("Dialog", "Por artista"))
        self.main_title.setText(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">Grafico de quantidades:</span></p></body></html>',
            )
        )
        self.by_label.setText(_translate("Dialog", "Por gravadora"))
        self.by_goat.setText(_translate("Dialog", "Por GOAT"))


from PyQt5 import QtWebEngineWidgets

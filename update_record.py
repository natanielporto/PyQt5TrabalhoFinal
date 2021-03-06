# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateRecord.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 525)
        self.update_btn = QtWidgets.QPushButton(Dialog)
        self.update_btn.setGeometry(QtCore.QRect(60, 100, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.remove_record = QtWidgets.QLabel(Dialog)
        self.remove_record.setGeometry(QtCore.QRect(60, 60, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_record.setFont(font)
        self.remove_record.setObjectName("remove_record")
        self.update_input = QtWidgets.QLineEdit(Dialog)
        self.update_input.setGeometry(QtCore.QRect(120, 60, 381, 21))
        self.update_input.setObjectName("update_input")
        self.remove_title = QtWidgets.QLabel(Dialog)
        self.remove_title.setGeometry(QtCore.QRect(110, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.remove_title.setFont(font)
        self.remove_title.setObjectName("remove_title")
        self.record_label = QtWidgets.QLabel(Dialog)
        self.record_label.setGeometry(QtCore.QRect(60, 340, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.record_label.setFont(font)
        self.record_label.setObjectName("record_label")
        self.goat_box = QtWidgets.QCheckBox(Dialog)
        self.goat_box.setGeometry(QtCore.QRect(60, 420, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.goat_box.setFont(font)
        self.goat_box.setObjectName("goat_box")
        self.artist_input = QtWidgets.QLineEdit(Dialog)
        self.artist_input.setGeometry(QtCore.QRect(130, 300, 371, 21))
        self.artist_input.setObjectName("artist_input")
        self.score_input = QtWidgets.QLineEdit(Dialog)
        self.score_input.setGeometry(QtCore.QRect(440, 380, 61, 21))
        self.score_input.setObjectName("score_input")
        self.duration_input = QtWidgets.QLineEdit(Dialog)
        self.duration_input.setGeometry(QtCore.QRect(140, 380, 61, 21))
        self.duration_input.setObjectName("duration_input")
        self.artist = QtWidgets.QLabel(Dialog)
        self.artist.setGeometry(QtCore.QRect(60, 300, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.artist.setFont(font)
        self.artist.setObjectName("artist")
        self.track_input = QtWidgets.QLineEdit(Dialog)
        self.track_input.setGeometry(QtCore.QRect(320, 380, 61, 21))
        self.track_input.setObjectName("track_input")
        self.record_input = QtWidgets.QLineEdit(Dialog)
        self.record_input.setGeometry(QtCore.QRect(120, 260, 381, 21))
        self.record_input.setObjectName("record_input")
        self.tracks = QtWidgets.QLabel(Dialog)
        self.tracks.setGeometry(QtCore.QRect(210, 380, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tracks.setFont(font)
        self.tracks.setObjectName("tracks")
        self.duration = QtWidgets.QLabel(Dialog)
        self.duration.setGeometry(QtCore.QRect(60, 380, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.duration.setFont(font)
        self.duration.setObjectName("duration")
        self.add_title = QtWidgets.QLabel(Dialog)
        self.add_title.setGeometry(QtCore.QRect(50, 160, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_title.setFont(font)
        self.add_title.setObjectName("add_title")
        self.update_data_btn = QtWidgets.QPushButton(Dialog)
        self.update_data_btn.setGeometry(QtCore.QRect(60, 450, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_data_btn.setFont(font)
        self.update_data_btn.setObjectName("update_data_btn")
        self.add_record = QtWidgets.QLabel(Dialog)
        self.add_record.setGeometry(QtCore.QRect(60, 260, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_record.setFont(font)
        self.add_record.setObjectName("add_record")
        self.grade = QtWidgets.QLabel(Dialog)
        self.grade.setGeometry(QtCore.QRect(390, 380, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grade.setFont(font)
        self.grade.setObjectName("grade")
        self.record_label_input = QtWidgets.QLineEdit(Dialog)
        self.record_label_input.setGeometry(QtCore.QRect(160, 340, 341, 21))
        self.record_label_input.setObjectName("record_label_input")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editar Disco"))
        self.update_btn.setText(_translate("Dialog", "Alterar"))
        self.remove_record.setText(_translate("Dialog", "Disco:"))
        self.remove_title.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center"><span style=" font-size:18pt;">Qual disco deseja alterar?</span></p></body></html>',
            )
        )
        self.record_label.setText(_translate("Dialog", "Gravadora:"))
        self.goat_box.setText(
            _translate("Dialog", "Melhor Disco / Banda / Artista de todos os tempos.")
        )
        self.artist.setText(_translate("Dialog", "Artista:"))
        self.tracks.setText(_translate("Dialog", "Nº de faixas:"))
        self.duration.setText(_translate("Dialog", "Duracao:"))
        self.add_title.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center"><span style=" font-size:18pt;">Preencha todos os campos </span></p><p align="center"><span style=" font-size:18pt;">abaixo para alterar o disco.</span></p></body></html>',
            )
        )
        self.update_data_btn.setText(_translate("Dialog", "Substituir dados"))
        self.add_record.setText(_translate("Dialog", "Disco:"))
        self.grade.setText(_translate("Dialog", "Nota:"))

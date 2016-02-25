# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sebastian\PycharmProjects\can-ethernet-monitor\ui\disenos\designer\dialog_puerto_com.ui'
#
# Created: Thu Feb 25 12:57:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SerialDialog(object):
    def setupUi(self, SerialDialog):
        SerialDialog.setObjectName("SerialDialog")
        SerialDialog.resize(256, 154)
        SerialDialog.setMinimumSize(QtCore.QSize(256, 154))
        SerialDialog.setMaximumSize(QtCore.QSize(256, 154))
        self.verticalLayoutWidget_2 = QtGui.QWidget(SerialDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 251, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelar = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout.addWidget(self.cancelar)
        self.aceptar = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.aceptar.setObjectName("aceptar")
        self.horizontalLayout.addWidget(self.aceptar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SerialDialog)
        QtCore.QMetaObject.connectSlotsByName(SerialDialog)

    def retranslateUi(self, SerialDialog):
        SerialDialog.setWindowTitle(QtGui.QApplication.translate("SerialDialog", "PUERTO COM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SerialDialog", "Seleccione el puerto", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("SerialDialog", "cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("SerialDialog", "aceptar", None, QtGui.QApplication.UnicodeUTF8))


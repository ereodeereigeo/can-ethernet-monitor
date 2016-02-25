# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/seba/PycharmProjects/can-ethernet-monitor/ui/disenos/designer/dialog_can_bridge.ui'
#
# Created: Thu Feb 25 12:27:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CanBridgeDialog(object):
    def setupUi(self, CanBridgeDialog):
        CanBridgeDialog.setObjectName("CanBridgeDialog")
        CanBridgeDialog.resize(296, 151)
        CanBridgeDialog.setMinimumSize(QtCore.QSize(296, 151))
        CanBridgeDialog.setMaximumSize(QtCore.QSize(296, 151))
        self.verticalLayoutWidget = QtGui.QWidget(CanBridgeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox_3 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.spinBox_4 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_4.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_4.setMaximum(255)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout.addWidget(self.spinBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_5 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_5.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMaximum(65535)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_2.addWidget(self.spinBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(CanBridgeDialog)
        QtCore.QMetaObject.connectSlotsByName(CanBridgeDialog)

    def retranslateUi(self, CanBridgeDialog):
        CanBridgeDialog.setWindowTitle(QtGui.QApplication.translate("CanBridgeDialog", "PUERTO CAN BRIDGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CanBridgeDialog", "Selecciona IP y puerto ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CanBridgeDialog", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CanBridgeDialog", "Puerto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CanBridgeDialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("CanBridgeDialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))


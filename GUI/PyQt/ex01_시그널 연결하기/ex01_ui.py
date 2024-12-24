# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex01.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 290)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(80, 80, 76, 20))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 40, 75, 24))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(80, 100, 76, 20))
        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(80, 140, 76, 20))
        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(80, 120, 76, 20))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(200, 60, 120, 141))
        self.groupBox.setMinimumSize(QSize(0, 141))
        self.groupBox.setMaximumSize(QSize(120, 16777215))
        self.checkBox_8 = QCheckBox(self.groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(20, 70, 76, 20))
        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(20, 90, 76, 20))
        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(20, 30, 76, 20))
        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 50, 76, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex04.ui'
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
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(409, 315)
        self.cb1 = QCheckBox(Dialog)
        self.cb1.setObjectName(u"cb1")
        self.cb1.setGeometry(QRect(100, 110, 76, 20))
        self.cb2 = QCheckBox(Dialog)
        self.cb2.setObjectName(u"cb2")
        self.cb2.setGeometry(QRect(100, 130, 76, 20))
        self.cb3 = QCheckBox(Dialog)
        self.cb3.setObjectName(u"cb3")
        self.cb3.setGeometry(QRect(100, 150, 76, 20))
        self.cb4 = QCheckBox(Dialog)
        self.cb4.setObjectName(u"cb4")
        self.cb4.setGeometry(QRect(100, 170, 76, 20))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(210, 60, 120, 151))
        self.gcb2 = QCheckBox(self.groupBox)
        self.gcb2.setObjectName(u"gcb2")
        self.gcb2.setGeometry(QRect(20, 70, 76, 20))
        self.gcb4 = QCheckBox(self.groupBox)
        self.gcb4.setObjectName(u"gcb4")
        self.gcb4.setGeometry(QRect(20, 110, 76, 20))
        self.gcb3 = QCheckBox(self.groupBox)
        self.gcb3.setObjectName(u"gcb3")
        self.gcb3.setGeometry(QRect(20, 90, 76, 20))
        self.gcb1 = QCheckBox(self.groupBox)
        self.gcb1.setObjectName(u"gcb1")
        self.gcb1.setGeometry(QRect(20, 50, 76, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cb1.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.cb2.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.cb3.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.cb4.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        self.gcb2.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.gcb4.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.gcb3.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.gcb1.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
    # retranslateUi


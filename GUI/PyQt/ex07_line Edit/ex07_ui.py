# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex07.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 110, 131, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 111, 16))
        self.btn = QPushButton(Dialog)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(210, 110, 121, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"This is Line Edit", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"This is Line Edit", None))
        self.btn.setText(QCoreApplication.translate("Dialog", u"Change Label Text", None))
    # retranslateUi


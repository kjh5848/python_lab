# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex05.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 141, 21))
        self.c_btn = QPushButton(Dialog)
        self.c_btn.setObjectName(u"c_btn")
        self.c_btn.setGeometry(QRect(70, 140, 75, 24))
        self.p_btn = QPushButton(Dialog)
        self.p_btn.setObjectName(u"p_btn")
        self.p_btn.setGeometry(QRect(240, 140, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Change Text", None))
        self.c_btn.setText(QCoreApplication.translate("Dialog", u"change Text", None))
        self.p_btn.setText(QCoreApplication.translate("Dialog", u"Print Text", None))
    # retranslateUi


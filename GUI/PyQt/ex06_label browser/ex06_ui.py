# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex06.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(487, 361)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 60, 256, 192))
        self.print = QPushButton(Dialog)
        self.print.setObjectName(u"print")
        self.print.setGeometry(QRect(340, 80, 75, 24))
        self.setText = QPushButton(Dialog)
        self.setText.setObjectName(u"setText")
        self.setText.setGeometry(QRect(340, 120, 75, 24))
        self.appendText = QPushButton(Dialog)
        self.appendText.setObjectName(u"appendText")
        self.appendText.setGeometry(QRect(340, 160, 75, 24))
        self.clear = QPushButton(Dialog)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(340, 200, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc624\ub298 \ud558\ub8e8 \ud408\uc774\ud305</p></body></html>", None))
        self.print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.setText.setText(QCoreApplication.translate("Dialog", u"SetText", None))
        self.appendText.setText(QCoreApplication.translate("Dialog", u"AppendText", None))
        self.clear.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi


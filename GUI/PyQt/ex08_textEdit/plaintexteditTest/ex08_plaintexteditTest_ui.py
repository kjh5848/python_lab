# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex08_plaintexteditTest.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(634, 251)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 91, 16))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 90, 221, 100))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_printPlainTextEdit = QPushButton(self.layoutWidget)
        self.btn_printPlainTextEdit.setObjectName(u"btn_printPlainTextEdit")

        self.verticalLayout_2.addWidget(self.btn_printPlainTextEdit)

        self.btn_clearPlainTextEdit = QPushButton(self.layoutWidget)
        self.btn_clearPlainTextEdit.setObjectName(u"btn_clearPlainTextEdit")

        self.verticalLayout_2.addWidget(self.btn_clearPlainTextEdit)

        self.btn_appendPlainText = QPushButton(self.layoutWidget)
        self.btn_appendPlainText.setObjectName(u"btn_appendPlainText")

        self.verticalLayout_2.addWidget(self.btn_appendPlainText)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 40, 371, 194))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plaintextedit_Test = QPlainTextEdit(self.layoutWidget1)
        self.plaintextedit_Test.setObjectName(u"plaintextedit_Test")

        self.horizontalLayout.addWidget(self.plaintextedit_Test)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Plain Text Edit", None))
        self.btn_printPlainTextEdit.setText(QCoreApplication.translate("Dialog", u"Print Plain Text Edit", None))
        self.btn_clearPlainTextEdit.setText(QCoreApplication.translate("Dialog", u"Clear Plain Text Edit", None))
        self.btn_appendPlainText.setText(QCoreApplication.translate("Dialog", u"Append Plain Text", None))
        self.plaintextedit_Test.setPlainText(QCoreApplication.translate("Dialog", u"This is Plain Text Edit\n"
"This widget support PlainText", None))
    # retranslateUi


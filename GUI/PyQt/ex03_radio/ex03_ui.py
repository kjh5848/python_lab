# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex03.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(130, 60, 120, 141))
        self.GroupBox_rad3 = QRadioButton(self.groupBox)
        self.GroupBox_rad3.setObjectName(u"GroupBox_rad3")
        self.GroupBox_rad3.setGeometry(QRect(10, 100, 89, 20))
        self.GroupBox_rad1 = QRadioButton(self.groupBox)
        self.GroupBox_rad1.setObjectName(u"GroupBox_rad1")
        self.GroupBox_rad1.setGeometry(QRect(10, 40, 89, 20))
        self.GroupBox_rad2 = QRadioButton(self.groupBox)
        self.GroupBox_rad2.setObjectName(u"GroupBox_rad2")
        self.GroupBox_rad2.setGeometry(QRect(10, 70, 89, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        self.GroupBox_rad3.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.GroupBox_rad1.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.GroupBox_rad2.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '프로그램단계.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 50, 186, 52))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.cmb_Test_6 = QComboBox(self.layoutWidget)
        self.cmb_Test_6.addItem("")
        self.cmb_Test_6.addItem("")
        self.cmb_Test_6.addItem("")
        self.cmb_Test_6.addItem("")
        self.cmb_Test_6.setObjectName(u"cmb_Test_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.cmb_Test_6)

        self.cmb_Test_7 = QComboBox(self.layoutWidget)
        self.cmb_Test_7.addItem("")
        self.cmb_Test_7.addItem("")
        self.cmb_Test_7.addItem("")
        self.cmb_Test_7.setObjectName(u"cmb_Test_7")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.cmb_Test_7)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\ud504\ub85c\uadf8\ub7a8 \ub2e8\uacc4", None))
        self.cmb_Test_6.setItemText(0, QCoreApplication.translate("Dialog", u"\ud504\ub85c\uadf8\ub7a8 \ub4f1\ub85d", None))
        self.cmb_Test_6.setItemText(1, QCoreApplication.translate("Dialog", u"\uc0ac\uc804\uc9c1\ubb34\uc6b4\uc601", None))
        self.cmb_Test_6.setItemText(2, QCoreApplication.translate("Dialog", u"\uc77c\uacbd\ud5d8 \uc6b4\uc601", None))
        self.cmb_Test_6.setItemText(3, QCoreApplication.translate("Dialog", u"\uc77c\uacbd\ud5d8 \uc885\ub8cc", None))

        self.cmb_Test_7.setItemText(0, QCoreApplication.translate("Dialog", u"1st Item", None))
        self.cmb_Test_7.setItemText(1, QCoreApplication.translate("Dialog", u"2nd Item", None))
        self.cmb_Test_7.setItemText(2, QCoreApplication.translate("Dialog", u"3rd Item", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"\ub2e8\uc704", None))
    # retranslateUi


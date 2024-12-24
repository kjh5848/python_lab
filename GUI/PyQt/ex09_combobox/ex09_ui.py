# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex09.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(697, 633)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 24, 371, 265))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_display = QLabel(self.layoutWidget)
        self.lbl_display.setObjectName(u"lbl_display")

        self.verticalLayout.addWidget(self.lbl_display)

        self.cmb_Test = QComboBox(self.layoutWidget)
        self.cmb_Test.addItem("")
        self.cmb_Test.addItem("")
        self.cmb_Test.addItem("")
        self.cmb_Test.setObjectName(u"cmb_Test")

        self.verticalLayout.addWidget(self.cmb_Test)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_printItem = QPushButton(self.layoutWidget)
        self.btn_printItem.setObjectName(u"btn_printItem")

        self.horizontalLayout_2.addWidget(self.btn_printItem)

        self.btn_clearItem = QPushButton(self.layoutWidget)
        self.btn_clearItem.setObjectName(u"btn_clearItem")

        self.horizontalLayout_2.addWidget(self.btn_clearItem)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineedit_addItem = QLineEdit(self.layoutWidget)
        self.lineedit_addItem.setObjectName(u"lineedit_addItem")

        self.horizontalLayout.addWidget(self.lineedit_addItem)

        self.btn_addItem = QPushButton(self.layoutWidget)
        self.btn_addItem.setObjectName(u"btn_addItem")

        self.horizontalLayout.addWidget(self.btn_addItem)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cmb_second = QComboBox(self.layoutWidget)
        self.cmb_second.setObjectName(u"cmb_second")

        self.horizontalLayout_3.addWidget(self.cmb_second)

        self.btn_deleteItem = QPushButton(self.layoutWidget)
        self.btn_deleteItem.setObjectName(u"btn_deleteItem")

        self.horizontalLayout_3.addWidget(self.btn_deleteItem)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_display.setText(QCoreApplication.translate("Dialog", u"Display ComboBox Text", None))
        self.cmb_Test.setItemText(0, QCoreApplication.translate("Dialog", u"1st Item", None))
        self.cmb_Test.setItemText(1, QCoreApplication.translate("Dialog", u"2nd Item", None))
        self.cmb_Test.setItemText(2, QCoreApplication.translate("Dialog", u"3rd Item", None))

        self.btn_printItem.setText(QCoreApplication.translate("Dialog", u"PrintItem", None))
        self.btn_clearItem.setText(QCoreApplication.translate("Dialog", u"ClearItem", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Add Item to ComboBox", None))
        self.btn_addItem.setText(QCoreApplication.translate("Dialog", u"AddItem", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Delete ComboBox Item", None))
        self.btn_deleteItem.setText(QCoreApplication.translate("Dialog", u"DeleteItem", None))
    # retranslateUi


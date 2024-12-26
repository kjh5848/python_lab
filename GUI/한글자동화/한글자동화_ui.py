# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '한글자동화.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 611, 216))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.program_label = QLabel(self.verticalLayoutWidget)
        self.program_label.setObjectName(u"program_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.program_label)

        self.program_cmb1 = QComboBox(self.verticalLayoutWidget)
        self.program_cmb1.addItem("")
        self.program_cmb1.addItem("")
        self.program_cmb1.addItem("")
        self.program_cmb1.addItem("")
        self.program_cmb1.setObjectName(u"program_cmb1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.program_cmb1)

        self.program_cmb2 = QComboBox(self.verticalLayoutWidget)
        self.program_cmb2.addItem("")
        self.program_cmb2.addItem("")
        self.program_cmb2.addItem("")
        self.program_cmb2.setObjectName(u"program_cmb2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.program_cmb2)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_7)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_5 = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(526, 29))

        self.horizontalLayout_5.addWidget(self.textEdit_5)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(75, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(153, 153, 153);")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_4 = QTextEdit(self.verticalLayoutWidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(526, 29))
        self.textEdit_4.setMaximumSize(QSize(526, 29))

        self.horizontalLayout_4.addWidget(self.textEdit_4)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 0))
        self.pushButton_4.setMaximumSize(QSize(75, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(153, 153, 153);")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 756, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.program_label.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \ub2e8\uacc4", None))
        self.program_cmb1.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \ub4f1\ub85d", None))
        self.program_cmb1.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc0ac\uc804\uc9c1\ubb34\uc6b4\uc601", None))
        self.program_cmb1.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc77c\uacbd\ud5d8 \uc6b4\uc601", None))
        self.program_cmb1.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc77c\uacbd\ud5d8 \uc885\ub8cc", None))

        self.program_cmb2.setItemText(0, QCoreApplication.translate("MainWindow", u"1st Item", None))
        self.program_cmb2.setItemText(1, QCoreApplication.translate("MainWindow", u"2nd Item", None))
        self.program_cmb2.setItemText(2, QCoreApplication.translate("MainWindow", u"3rd Item", None))

        self.label_7.setText("")
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140\uacbd\ub85c", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud55c\uae00\uacbd\ub85c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
    # retranslateUi


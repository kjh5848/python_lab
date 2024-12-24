# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex02.ui'
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
    QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(610, 482)
        self.btn_1 = QPushButton(dialog)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(110, 80, 131, 81))
        self.btn_2 = QPushButton(dialog)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(380, 80, 131, 81))

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Dialog", None))
#if QT_CONFIG(whatsthis)
        self.btn_1.setWhatsThis(QCoreApplication.translate("dialog", u"<html><head/><body><p>asd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_1.setText(QCoreApplication.translate("dialog", u"btn_1", None))
#if QT_CONFIG(whatsthis)
        self.btn_2.setWhatsThis(QCoreApplication.translate("dialog", u"<html><head/><body><p>asd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_2.setText(QCoreApplication.translate("dialog", u"btn_2", None))
    # retranslateUi


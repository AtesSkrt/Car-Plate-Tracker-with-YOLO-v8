# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import login_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 401, 101))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 361, 61))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:200;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/login_/icons8-car-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 60))
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 100, 401, 201))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 30, 201, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);\n"
"\n"
"\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 90, 201, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);\n"
"\n"
"\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 131, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 131, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 140, 121, 51))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setItalic(False)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);\n"
"height:45px;\n"
"width:200;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"\n"
"border-top-right-radius:15px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:  rgb(0, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_2.setIconSize(QSize(60, 60))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"  PLATE TRACKER", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi


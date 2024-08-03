# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_deneme.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.take_image_button = QPushButton(self.centralwidget)
        self.take_image_button.setObjectName(u"take_image_button")
        self.take_image_button.setGeometry(QRect(340, 470, 141, 41))
        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(120, 520, 581, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet(u"\n"
"\n"
"border-radius:15px;\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.screen_label = QLabel(self.centralwidget)
        self.screen_label.setObjectName(u"label")
        self.screen_label.setGeometry(QRect(100, 10, 600, 450))
        self.screen_label.setFrameShape(QFrame.Box)
        self.screen_label.setFrameShadow(QFrame.Raised)
        self.screen_label.setLineWidth(5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.take_image_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.info_label.setText("")
        self.screen_label.setText("")
    # retranslateUi


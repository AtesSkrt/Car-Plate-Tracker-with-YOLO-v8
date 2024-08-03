# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_son_main_yildiz.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(981, 757)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"text-align:left;\n"
"height:60px;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, -1, -1, -1)
        self.avatar_sidebar_opened = QLabel(self.widget_2)
        self.avatar_sidebar_opened.setObjectName(u"avatar_sidebar_opened")
        self.avatar_sidebar_opened.setStyleSheet(u"")
        self.avatar_sidebar_opened.setPixmap(QPixmap(u":/Button_Icons/icons8-male-user-64.png"))
        self.avatar_sidebar_opened.setScaledContents(True)
        self.avatar_sidebar_opened.setMargin(5)

        self.horizontalLayout_2.addWidget(self.avatar_sidebar_opened)

        self.horizontalSpacer_3 = QSpacerItem(18, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.current_user = QLabel(self.widget_2)
        self.current_user.setObjectName(u"current_user")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.current_user.setFont(font)
        self.current_user.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.current_user)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, 0, -1)
        self.watc_screen_sidebar_opened = QPushButton(self.widget_2)
        self.watc_screen_sidebar_opened.setObjectName(u"watc_screen_sidebar_opened")
        font1 = QFont()
        font1.setBold(False)
        self.watc_screen_sidebar_opened.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/Button_Icons/icons/camera white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Button_Icons/icons/camera icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.watc_screen_sidebar_opened.setIcon(icon)
        self.watc_screen_sidebar_opened.setIconSize(QSize(32, 32))
        self.watc_screen_sidebar_opened.setCheckable(True)
        self.watc_screen_sidebar_opened.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.watc_screen_sidebar_opened)

        self.add_penalty_sidebar_closed_2 = QPushButton(self.widget_2)
        self.add_penalty_sidebar_closed_2.setObjectName(u"add_penalty_sidebar_closed_2")
        self.add_penalty_sidebar_closed_2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/Button_Icons/icons/no! white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Button_Icons/icons/no! icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.add_penalty_sidebar_closed_2.setIcon(icon1)
        self.add_penalty_sidebar_closed_2.setIconSize(QSize(28, 28))
        self.add_penalty_sidebar_closed_2.setCheckable(True)
        self.add_penalty_sidebar_closed_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_penalty_sidebar_closed_2)

        self.inspect_database_sidebar_closed_2 = QPushButton(self.widget_2)
        self.inspect_database_sidebar_closed_2.setObjectName(u"inspect_database_sidebar_closed_2")
        self.inspect_database_sidebar_closed_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/Button_Icons/icons/database white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Button_Icons/icons/adatabase icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.inspect_database_sidebar_closed_2.setIcon(icon2)
        self.inspect_database_sidebar_closed_2.setIconSize(QSize(35, 35))
        self.inspect_database_sidebar_closed_2.setCheckable(True)
        self.inspect_database_sidebar_closed_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.inspect_database_sidebar_closed_2)

        self.staff_operations_sidebar_opened = QPushButton(self.widget_2)
        self.staff_operations_sidebar_opened.setObjectName(u"staff_operations_sidebar_opened")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setBold(False)
        self.staff_operations_sidebar_opened.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/Button_Icons/icons/add user white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Button_Icons/icons/add user icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.staff_operations_sidebar_opened.setIcon(icon3)
        self.staff_operations_sidebar_opened.setIconSize(QSize(38, 38))
        self.staff_operations_sidebar_opened.setCheckable(True)
        self.staff_operations_sidebar_opened.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.staff_operations_sidebar_opened)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 331, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout_sidebar_opened = QPushButton(self.widget_2)
        self.logout_sidebar_opened.setObjectName(u"logout_sidebar_opened")
        font3 = QFont()
        font3.setBold(True)
        self.logout_sidebar_opened.setFont(font3)
        self.logout_sidebar_opened.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../PycharmProjects/Project_plates/Lib/source/icons/log out white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_sidebar_opened.setIcon(icon4)
        self.logout_sidebar_opened.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.logout_sidebar_opened)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.Main_window = QWidget(self.centralwidget)
        self.Main_window.setObjectName(u"Main_window")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.Main_window.setFont(font4)
        self.Main_window.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.Main_window)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sidebar_button = QPushButton(self.Main_window)
        self.sidebar_button.setObjectName(u"sidebar_button")
        self.sidebar_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:70;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Button_Icons/icons/menubar white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sidebar_button.setIcon(icon5)
        self.sidebar_button.setIconSize(QSize(60, 60))
        self.sidebar_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.sidebar_button)

        self.horizontalSpacer_4 = QSpacerItem(658, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.Main_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font3)
        self.Inspect_Database = QWidget()
        self.Inspect_Database.setObjectName(u"Inspect_Database")
        self.layoutWidget = QWidget(self.Inspect_Database)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 661, 621))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(198, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.label_2.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_8 = QSpacerItem(248, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.database_search_button = QPushButton(self.layoutWidget)
        self.database_search_button.setObjectName(u"database_search_button")
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(False)
        self.database_search_button.setFont(font6)
        self.database_search_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:130;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/Button_Icons/icons8-search-128 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/Button_Icons/icons8-search-128.png", QSize(), QIcon.Normal, QIcon.On)
        self.database_search_button.setIcon(icon6)
        self.database_search_button.setIconSize(QSize(25, 25))
        self.database_search_button.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.database_search_button)

        self.database_search_bar = QLineEdit(self.layoutWidget)
        self.database_search_bar.setObjectName(u"database_search_bar")

        self.horizontalLayout_5.addWidget(self.database_search_bar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.database_table = QTableWidget(self.layoutWidget)
        if (self.database_table.columnCount() < 4):
            self.database_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.database_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.database_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.database_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.database_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.database_table.rowCount() < 1):
            self.database_table.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.database_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        self.database_table.setObjectName(u"database_table")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.database_table.setFont(font7)
        self.database_table.setFrameShape(QFrame.StyledPanel)
        self.database_table.setLineWidth(1)
        self.database_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.database_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.database_table.setAutoScrollMargin(16)
        self.database_table.setGridStyle(Qt.SolidLine)
        self.database_table.setCornerButtonEnabled(True)
        self.database_table.horizontalHeader().setCascadingSectionResizes(False)
        self.database_table.horizontalHeader().setMinimumSectionSize(150)
        self.database_table.horizontalHeader().setDefaultSectionSize(150)
        self.database_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.database_table)

        self.pushButton = QPushButton(self.Inspect_Database)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 640, 171, 41))
        font8 = QFont()
        font8.setPointSize(18)
        font8.setBold(True)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:130;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Button_Icons/icons8-delete-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(35, 35))
        self.pushButton_2 = QPushButton(self.Inspect_Database)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(550, 640, 111, 41))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(False)
        self.pushButton_2.setFont(font9)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:130;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.pushButton_2.setIconSize(QSize(35, 35))
        self.add_penalty_button_2 = QPushButton(self.Inspect_Database)
        self.add_penalty_button_2.setObjectName(u"add_penalty_button_2")
        self.add_penalty_button_2.setGeometry(QRect(20, 640, 191, 41))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        self.add_penalty_button_2.setFont(font10)
        self.add_penalty_button_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:150;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Button_Icons/icons8-add-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_penalty_button_2.setIcon(icon8)
        self.add_penalty_button_2.setIconSize(QSize(30, 30))
        self.stackedWidget.addWidget(self.Inspect_Database)
        self.Add_Penalty = QWidget()
        self.Add_Penalty.setObjectName(u"Add_Penalty")
        self.layoutWidget1 = QWidget(self.Add_Penalty)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 659, 73))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(198, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        font11 = QFont()
        font11.setPointSize(20)
        font11.setBold(False)
        self.label_5.setFont(font11)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_10 = QSpacerItem(248, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.line = QFrame(self.Add_Penalty)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 100, 671, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.Add_Penalty)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 510, 671, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.add_penalty_info = QLabel(self.Add_Penalty)
        self.add_penalty_info.setObjectName(u"add_penalty_info")
        self.add_penalty_info.setGeometry(QRect(160, 530, 381, 31))
        self.add_penalty_info.setFont(font9)
        self.add_penalty_info.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.layoutWidget2 = QWidget(self.Add_Penalty)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 120, 681, 391))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.layoutWidget2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:70;\n"
"border:none;\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"\n"
"	border-top-right-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.penalty_plate_input = QLineEdit(self.widget_3)
        self.penalty_plate_input.setObjectName(u"penalty_plate_input")
        font12 = QFont()
        font12.setStyleStrategy(QFont.PreferDefault)
        self.penalty_plate_input.setFont(font12)
        self.penalty_plate_input.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"height: 25px;")

        self.gridLayout_2.addWidget(self.penalty_plate_input, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.penalty_amount_input = QLineEdit(self.widget_3)
        self.penalty_amount_input.setObjectName(u"penalty_amount_input")
        self.penalty_amount_input.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"height: 25px;")

        self.gridLayout_2.addWidget(self.penalty_amount_input, 1, 1, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"height: 25px;\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.add_penalty_button = QPushButton(self.layoutWidget2)
        self.add_penalty_button.setObjectName(u"add_penalty_button")
        self.add_penalty_button.setFont(font4)
        self.add_penalty_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:150;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.add_penalty_button.setIcon(icon8)
        self.add_penalty_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.add_penalty_button)

        self.horizontalSpacer_14 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.Add_Penalty)
        self.Watch_Screen = QWidget()
        self.Watch_Screen.setObjectName(u"Watch_Screen")
        self.label_6 = QLabel(self.Watch_Screen)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 0, 161, 51))
        self.label_6.setFont(font11)
        self.widget_5 = QWidget(self.Watch_Screen)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 50, 661, 601))
        self.widget_5.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"border-radius:30px;")
        self.watch_screen_screen = QLabel(self.widget_5)
        self.watch_screen_screen.setObjectName(u"watch_screen_screen")
        self.watch_screen_screen.setGeometry(QRect(10, 10, 641, 401))
        self.watch_screen_screen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.watch_screen_info_label = QLabel(self.widget_5)
        self.watch_screen_info_label.setObjectName(u"watch_screen_info_label")
        self.watch_screen_info_label.setGeometry(QRect(90, 500, 501, 41))
        font13 = QFont()
        font13.setPointSize(12)
        self.watch_screen_info_label.setFont(font13)
        self.watch_screen_info_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.layoutWidget3 = QWidget(self.widget_5)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 420, 631, 51))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(28, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)

        self.start_camera_button = QPushButton(self.layoutWidget3)
        self.start_camera_button.setObjectName(u"start_camera_button")
        self.start_camera_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:110;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Button_Icons/icons/log out white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_camera_button.setIcon(icon9)
        self.start_camera_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_16.addWidget(self.start_camera_button)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)

        self.read_plate_button = QPushButton(self.layoutWidget3)
        self.read_plate_button.setObjectName(u"read_plate_button")
        self.read_plate_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:200;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Button_Icons/icons8-capture-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.read_plate_button.setIcon(icon10)
        self.read_plate_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_16.addWidget(self.read_plate_button)

        self.horizontalSpacer_17 = QSpacerItem(188, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_17)

        self.graphicsView = QGraphicsView(self.widget_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 110, 256, 192))
        self.graphicsView.setFrameShape(QFrame.StyledPanel)
        self.graphicsView_2 = QGraphicsView(self.widget_5)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(380, 110, 256, 192))
        self.stackedWidget.addWidget(self.Watch_Screen)
        self.widget_5.raise_()
        self.label_6.raise_()
        self.Staff_Actions = QWidget()
        self.Staff_Actions.setObjectName(u"Staff_Actions")
        self.label_7 = QLabel(self.Staff_Actions)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, -20, 221, 61))
        self.label_7.setFont(font5)
        self.line_3 = QFrame(self.Staff_Actions)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 30, 641, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.staff_table = QTableWidget(self.Staff_Actions)
        if (self.staff_table.columnCount() < 4):
            self.staff_table.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.staff_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.staff_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.staff_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.staff_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        if (self.staff_table.rowCount() < 1):
            self.staff_table.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.staff_table.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.staff_table.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.staff_table.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.staff_table.setItem(0, 2, __qtablewidgetitem12)
        self.staff_table.setObjectName(u"staff_table")
        self.staff_table.setGeometry(QRect(20, 260, 641, 231))
        self.staff_table.horizontalHeader().setDefaultSectionSize(155)
        self.widget_4 = QWidget(self.Staff_Actions)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 50, 681, 581))
        self.widget_4.setStyleSheet(u"\n"
"border-radius:30px;\n"
"background-color: rgb(220, 220, 220);")
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 60, 261, 20))
        self.label_9.setFont(font7)
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 100, 251, 16))
        self.label_10.setFont(font7)
        self.staff_name_input = QLineEdit(self.widget_4)
        self.staff_name_input.setObjectName(u"staff_name_input")
        self.staff_name_input.setGeometry(QRect(420, 60, 211, 21))
        self.staff_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.staff_password_input = QLineEdit(self.widget_4)
        self.staff_password_input.setObjectName(u"staff_password_input")
        self.staff_password_input.setGeometry(QRect(420, 100, 211, 21))
        self.staff_password_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        self.layoutWidget4 = QWidget(self.widget_4)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(40, 470, 601, 51))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(378, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)

        self.delete_staff_button = QPushButton(self.layoutWidget4)
        self.delete_staff_button.setObjectName(u"delete_staff_button")
        self.delete_staff_button.setFont(font13)
        self.delete_staff_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:70;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"width:190px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Button_Icons/icons8-delete-user-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_staff_button.setIcon(icon11)
        self.delete_staff_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.delete_staff_button)

        self.layoutWidget5 = QWidget(self.widget_4)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(40, 140, 591, 51))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(368, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.add_staff_button = QPushButton(self.layoutWidget5)
        self.add_staff_button.setObjectName(u"add_staff_button")
        font14 = QFont()
        font14.setPointSize(13)
        font14.setBold(False)
        self.add_staff_button.setFont(font14)
        self.add_staff_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"height:45px;\n"
"width:180;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Button_Icons/icons/add user white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_staff_button.setIcon(icon12)
        self.add_staff_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_15.addWidget(self.add_staff_button)

        self.stackedWidget.addWidget(self.Staff_Actions)
        self.widget_4.raise_()
        self.label_7.raise_()
        self.line_3.raise_()
        self.staff_table.raise_()

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.Main_window, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"height:60px;\n"
"border:none;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.avatar_sidebar_closed = QLabel(self.widget)
        self.avatar_sidebar_closed.setObjectName(u"avatar_sidebar_closed")
        self.avatar_sidebar_closed.setPixmap(QPixmap(u":/Button_Icons/icons8-male-user-64.png"))
        self.avatar_sidebar_closed.setScaledContents(True)
        self.avatar_sidebar_closed.setMargin(5)

        self.horizontalLayout.addWidget(self.avatar_sidebar_closed)

        self.horizontalSpacer_2 = QSpacerItem(13, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(35)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.watc_screen_sidebar_closed = QPushButton(self.widget)
        self.watc_screen_sidebar_closed.setObjectName(u"watc_screen_sidebar_closed")
        self.watc_screen_sidebar_closed.setIcon(icon)
        self.watc_screen_sidebar_closed.setIconSize(QSize(32, 32))
        self.watc_screen_sidebar_closed.setCheckable(True)
        self.watc_screen_sidebar_closed.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.watc_screen_sidebar_closed)

        self.add_penalty_sidebar_closed = QPushButton(self.widget)
        self.add_penalty_sidebar_closed.setObjectName(u"add_penalty_sidebar_closed")
        self.add_penalty_sidebar_closed.setIcon(icon1)
        self.add_penalty_sidebar_closed.setIconSize(QSize(28, 28))
        self.add_penalty_sidebar_closed.setCheckable(True)
        self.add_penalty_sidebar_closed.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_penalty_sidebar_closed)

        self.inspect_database_sidebar_closed = QPushButton(self.widget)
        self.inspect_database_sidebar_closed.setObjectName(u"inspect_database_sidebar_closed")
        self.inspect_database_sidebar_closed.setIcon(icon2)
        self.inspect_database_sidebar_closed.setIconSize(QSize(35, 35))
        self.inspect_database_sidebar_closed.setCheckable(True)
        self.inspect_database_sidebar_closed.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.inspect_database_sidebar_closed)

        self.staff_operations_sidebar_closed = QPushButton(self.widget)
        self.staff_operations_sidebar_closed.setObjectName(u"staff_operations_sidebar_closed")
        self.staff_operations_sidebar_closed.setIcon(icon3)
        self.staff_operations_sidebar_closed.setIconSize(QSize(38, 38))
        self.staff_operations_sidebar_closed.setCheckable(True)
        self.staff_operations_sidebar_closed.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.staff_operations_sidebar_closed)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 220, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.logout_sidebar_closed = QPushButton(self.widget)
        self.logout_sidebar_closed.setObjectName(u"logout_sidebar_closed")
        self.logout_sidebar_closed.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 170, 255);\n"
"	font-weight:bold;\n"
"}")
        self.logout_sidebar_closed.setIcon(icon9)
        self.logout_sidebar_closed.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.logout_sidebar_closed)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sidebar_button.toggled.connect(self.widget.setHidden)
        self.sidebar_button.toggled.connect(self.widget_2.setVisible)
        self.staff_operations_sidebar_closed.toggled.connect(self.staff_operations_sidebar_opened.setChecked)
        self.inspect_database_sidebar_closed.toggled.connect(self.inspect_database_sidebar_closed_2.setChecked)
        self.add_penalty_sidebar_closed.toggled.connect(self.add_penalty_sidebar_closed_2.setChecked)
        self.watc_screen_sidebar_closed.toggled.connect(self.watc_screen_sidebar_opened.setChecked)
        self.watc_screen_sidebar_opened.toggled.connect(self.watc_screen_sidebar_closed.setChecked)
        self.add_penalty_sidebar_closed_2.toggled.connect(self.add_penalty_sidebar_closed.setChecked)
        self.inspect_database_sidebar_closed_2.toggled.connect(self.inspect_database_sidebar_closed.setChecked)
        self.staff_operations_sidebar_opened.toggled.connect(self.staff_operations_sidebar_closed.setChecked)
        self.logout_sidebar_opened.clicked.connect(MainWindow.close)
        self.logout_sidebar_closed.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.avatar_sidebar_opened.setText("")
        self.current_user.setText(QCoreApplication.translate("MainWindow", u"Ate\u015f \u00d6zt\u00fcrk", None))
        self.watc_screen_sidebar_opened.setText(QCoreApplication.translate("MainWindow", u"Watch Screen        ", None))
        self.add_penalty_sidebar_closed_2.setText(QCoreApplication.translate("MainWindow", u"Add Penalty           ", None))
        self.inspect_database_sidebar_closed_2.setText(QCoreApplication.translate("MainWindow", u"Inspect Databse   ", None))
        self.staff_operations_sidebar_opened.setText(QCoreApplication.translate("MainWindow", u"Staff Actions          ", None))
        self.logout_sidebar_opened.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.sidebar_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inspect Database", None))
        self.database_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.database_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Plate Number", None));
        ___qtablewidgetitem1 = self.database_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Penalty", None));
        ___qtablewidgetitem2 = self.database_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Entered Date", None));
        ___qtablewidgetitem3 = self.database_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.database_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"no", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Refresh Table", None))
        self.add_penalty_button_2.setText(QCoreApplication.translate("MainWindow", u"Add Penalty", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Add Penalty", None))
        self.add_penalty_info.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.penalty_plate_input.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Write Penalty Amount:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Write Plate Number to Add Penalty Points:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Write Penalty Reason:", None))
        self.add_penalty_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Watch Screen", None))
        self.watch_screen_screen.setText("")
        self.watch_screen_info_label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.start_camera_button.setText(QCoreApplication.translate("MainWindow", u"Start Camera", None))
        self.read_plate_button.setText(QCoreApplication.translate("MainWindow", u"Read Plate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"STAFF ACTIONS", None))
        ___qtablewidgetitem5 = self.staff_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Staff ID", None));
        ___qtablewidgetitem6 = self.staff_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Name-Surname", None));
        ___qtablewidgetitem7 = self.staff_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem8 = self.staff_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem9 = self.staff_table.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"no", None));

        __sortingEnabled = self.staff_table.isSortingEnabled()
        self.staff_table.setSortingEnabled(False)
        self.staff_table.setSortingEnabled(__sortingEnabled)

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enter Staff Name and Surname:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Enter Staff Password:", None))
        self.delete_staff_button.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Staff", None))
        self.add_staff_button.setText(QCoreApplication.translate("MainWindow", u"Add Staff", None))
        self.avatar_sidebar_closed.setText("")
        self.watc_screen_sidebar_closed.setText("")
        self.add_penalty_sidebar_closed.setText("")
        self.inspect_database_sidebar_closed.setText("")
        self.staff_operations_sidebar_closed.setText("")
        self.logout_sidebar_closed.setText("")
    # retranslateUi


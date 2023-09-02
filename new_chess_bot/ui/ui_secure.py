# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_SecureWindow(object):
    def setupUi(self, SecureWindow):
        if not SecureWindow.objectName():
            SecureWindow.setObjectName(u"SecureWindow")
        SecureWindow.setEnabled(True)
        SecureWindow.resize(618, 141)
        SecureWindow.setStyleSheet(u"background-color: transparent;")
        SecureWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(SecureWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setBaseSize(QSize(1, 50))
        self.splitter.setStyleSheet(u"")
        self.splitter.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        sizePolicy.setHeightForWidth(self.verticalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget.setBaseSize(QSize(1, 50))
        self.Layout = QVBoxLayout(self.verticalLayoutWidget)
        self.Layout.setObjectName(u"Layout")
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.CodeInput = QLineEdit(self.verticalLayoutWidget)
        self.CodeInput.setObjectName(u"CodeInput")
        self.CodeInput.setEnabled(True)
        self.CodeInput.setStyleSheet(u"background-color: #fff;\n"
"    color: #000;\n"
"    border-radius: 7px;\n"
"    font-size: 35px;\n"
"	height: 50px;\n"
"	padding: 3px 15px;")

        self.Layout.addWidget(self.CodeInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.NextButton = QPushButton(self.verticalLayoutWidget)
        self.NextButton.setObjectName(u"NextButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy1)
        self.NextButton.setBaseSize(QSize(1, 50))
        self.NextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextButton.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e74c3c, stop: 0.5 #c0392b, stop: 1.0 #922b21);\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"    font-size: 2em;\n"
"    height: 50px;\n"
"    width: 250px;\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #fff;\n"
"    color: #000;\n"
"	cursor: pointer;\n"
"}")

        self.horizontalLayout.addWidget(self.NextButton)


        self.Layout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout.addWidget(self.splitter)

        SecureWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecureWindow)

        QMetaObject.connectSlotsByName(SecureWindow)
    # setupUi

    def retranslateUi(self, SecureWindow):
        SecureWindow.setWindowTitle(QCoreApplication.translate("SecureWindow", u"Enter a code", None))
        self.CodeInput.setText("")
        self.NextButton.setText(QCoreApplication.translate("SecureWindow", u"NEXT", None))
    # retranslateUi


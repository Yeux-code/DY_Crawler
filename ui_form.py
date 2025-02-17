# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1050, 600)
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 60, 91, 23))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 220, 111, 23))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 300, 141, 23))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 420, 75, 23))
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 260, 75, 23))
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(180, 0, 831, 541))
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 370, 75, 23))
        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 460, 75, 23))
        self.pushButton_8 = QPushButton(self.tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(30, 140, 75, 23))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 170, 101, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u6253\u5f00Chrome", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u91c7\u96c6\u5355\u9875", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u83b7\u53d6\u8fbe\u4eba\u6296\u97f3\u4e3b\u9875\u4fe1\u606f", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"\u6296\u97f3\u767b\u5f55", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"\u751f\u6210\u8868\u683c", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"\u5bfc\u51fa\u8868\u683c", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"\u81ea\u52a8\u91c7\u96c6", None))
        self.label.setText(QCoreApplication.translate("Widget", u"(\u8981\u5148\u767b\u5f55\u6296\u97f3)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Tab 2", None))
    # retranslateUi


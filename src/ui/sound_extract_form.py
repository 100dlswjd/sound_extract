# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sound_extract_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(239, 100)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_save_path = QLabel(Form)
        self.label_save_path.setObjectName(u"label_save_path")

        self.horizontalLayout.addWidget(self.label_save_path)

        self.lineEdit_save_path = QLineEdit(Form)
        self.lineEdit_save_path.setObjectName(u"lineEdit_save_path")
        self.lineEdit_save_path.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_save_path)

        self.pushButton_save_path_select = QPushButton(Form)
        self.pushButton_save_path_select.setObjectName(u"pushButton_save_path_select")

        self.horizontalLayout.addWidget(self.pushButton_save_path_select)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_save_path.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5\uc704\uce58", None))
        self.pushButton_save_path_select.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5\uc704\uce58 \uc120\ud0dd", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\ucd94\ucd9c\ud558\uae30", None))
    # retranslateUi


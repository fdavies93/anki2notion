# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_ui/upload.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_upload(object):
    def setupUi(self, upload):
        upload.setObjectName("upload")
        upload.resize(640, 646)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        upload.setFont(font)
        self.scrollArea = QtWidgets.QScrollArea(upload)
        self.scrollArea.setGeometry(QtCore.QRect(20, 120, 601, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 55))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mapping_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mapping_grid.setContentsMargins(0, 0, 0, 0)
        self.mapping_grid.setObjectName("mapping_grid")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.mapping_grid.addWidget(self.label_2, 0, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.mapping_grid.addWidget(self.comboBox_2, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.mapping_grid.addWidget(self.comboBox, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.mapping_grid.addWidget(self.label_3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.mapping_grid.addWidget(self.label, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.mapping_grid.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.mapping_grid.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.mapping_grid.addWidget(self.label_6, 1, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(upload)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 584, 601, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.upload_button.setObjectName("upload_button")
        self.horizontalLayout.addWidget(self.upload_button)
        self.cancel_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.progress_bar = QtWidgets.QProgressBar(upload)
        self.progress_bar.setGeometry(QtCore.QRect(20, 514, 601, 31))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_label = QtWidgets.QLabel(upload)
        self.progress_label.setGeometry(QtCore.QRect(20, 554, 601, 20))
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(upload)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 460, 601, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.sync_mode = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.sync_mode.setObjectName("sync_mode")
        self.sync_mode.addItem("")
        self.sync_mode.addItem("")
        self.sync_mode.addItem("")
        self.horizontalLayout_5.addWidget(self.sync_mode)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.primary_key = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.primary_key.setObjectName("primary_key")
        self.horizontalLayout_5.addWidget(self.primary_key)
        self.formLayoutWidget_2 = QtWidgets.QWidget(upload)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 601, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.anki_deck_select = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.anki_deck_select.setObjectName("anki_deck_select")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.anki_deck_select)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.notion_database_select = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.notion_database_select.setObjectName("notion_database_select")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.notion_database_select)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.anki_card_type_select = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.anki_card_type_select.setObjectName("anki_card_type_select")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.anki_card_type_select)

        self.retranslateUi(upload)
        self.sync_mode.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(upload)

    def retranslateUi(self, upload):
        _translate = QtCore.QCoreApplication.translate
        upload.setWindowTitle(_translate("upload", "Download"))
        self.label_2.setText(_translate("upload", "Notion Column"))
        self.comboBox_2.setItemText(0, _translate("upload", "Text"))
        self.comboBox_2.setItemText(1, _translate("upload", "Select"))
        self.comboBox_2.setItemText(2, _translate("upload", "Multi-Select"))
        self.comboBox.setItemText(0, _translate("upload", "<None>"))
        self.label_3.setText(_translate("upload", "Anki Field"))
        self.label.setText(_translate("upload", "Notion Type"))
        self.label_4.setText(_translate("upload", "Placeholder"))
        self.label_5.setText(_translate("upload", "Anki Type"))
        self.label_6.setText(_translate("upload", "TextLabel"))
        self.upload_button.setText(_translate("upload", "Upload"))
        self.cancel_button.setText(_translate("upload", "Cancel"))
        self.progress_label.setText(_translate("upload", "0/0 Uploaded"))
        self.label_8.setText(_translate("upload", "Sync Mode"))
        self.sync_mode.setItemText(0, _translate("upload", "Append"))
        self.sync_mode.setItemText(1, _translate("upload", "Soft Merge"))
        self.sync_mode.setItemText(2, _translate("upload", "Hard Merge"))
        self.label_9.setText(_translate("upload", "Primary Key"))
        self.label_10.setText(_translate("upload", "Anki Deck"))
        self.label_7.setText(_translate("upload", "Notion Database"))
        self.label_11.setText(_translate("upload", "Anki Card Type"))

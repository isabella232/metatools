# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_apply_templates.ui'
#
# Created: Tue Mar 29 19:25:24 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ApplyTemplatesDialog(object):
    def setupUi(self, ApplyTemplatesDialog):
        ApplyTemplatesDialog.setObjectName(_fromUtf8("ApplyTemplatesDialog"))
        ApplyTemplatesDialog.resize(465, 263)
        self.gridLayout = QtGui.QGridLayout(ApplyTemplatesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.externalFilesCheckBox = QtGui.QCheckBox(ApplyTemplatesDialog)
        self.externalFilesCheckBox.setObjectName(_fromUtf8("externalFilesCheckBox"))
        self.horizontalLayout.addWidget(self.externalFilesCheckBox)
        self.btnSelectDataFiles = QtGui.QPushButton(ApplyTemplatesDialog)
        self.btnSelectDataFiles.setEnabled(False)
        self.btnSelectDataFiles.setObjectName(_fromUtf8("btnSelectDataFiles"))
        self.horizontalLayout.addWidget(self.btnSelectDataFiles)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(ApplyTemplatesDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.organizationComboBox = QtGui.QComboBox(self.groupBox)
        self.organizationComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.organizationComboBox.setObjectName(_fromUtf8("organizationComboBox"))
        self.gridLayout_2.addWidget(self.organizationComboBox, 0, 1, 1, 1)
        self.licenseComboBox = QtGui.QComboBox(self.groupBox)
        self.licenseComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.licenseComboBox.setObjectName(_fromUtf8("licenseComboBox"))
        self.gridLayout_2.addWidget(self.licenseComboBox, 1, 1, 1, 1)
        self.workflowComboBox = QtGui.QComboBox(self.groupBox)
        self.workflowComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.workflowComboBox.setObjectName(_fromUtf8("workflowComboBox"))
        self.gridLayout_2.addWidget(self.workflowComboBox, 2, 1, 1, 1)
        self.organizationManageButton = QtGui.QPushButton(self.groupBox)
        self.organizationManageButton.setObjectName(_fromUtf8("organizationManageButton"))
        self.gridLayout_2.addWidget(self.organizationManageButton, 0, 2, 1, 1)
        self.licenseManageButton = QtGui.QPushButton(self.groupBox)
        self.licenseManageButton.setObjectName(_fromUtf8("licenseManageButton"))
        self.gridLayout_2.addWidget(self.licenseManageButton, 1, 2, 1, 1)
        self.workflowManageButton = QtGui.QPushButton(self.groupBox)
        self.workflowManageButton.setObjectName(_fromUtf8("workflowManageButton"))
        self.gridLayout_2.addWidget(self.workflowManageButton, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.logFileLineEdit = QtGui.QLineEdit(self.groupBox)
        self.logFileLineEdit.setReadOnly(True)
        self.logFileLineEdit.setObjectName(_fromUtf8("logFileLineEdit"))
        self.gridLayout_2.addWidget(self.logFileLineEdit, 3, 1, 1, 1)
        self.selectLogFileButton = QtGui.QPushButton(self.groupBox)
        self.selectLogFileButton.setObjectName(_fromUtf8("selectLogFileButton"))
        self.gridLayout_2.addWidget(self.selectLogFileButton, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.mainButtonBox = QtGui.QDialogButtonBox(ApplyTemplatesDialog)
        self.mainButtonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.mainButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
        self.mainButtonBox.setObjectName(_fromUtf8("mainButtonBox"))
        self.gridLayout.addWidget(self.mainButtonBox, 2, 1, 1, 1)
        self.layerListView = QtGui.QListWidget(ApplyTemplatesDialog)
        self.layerListView.setObjectName(_fromUtf8("layerListView"))
        self.gridLayout.addWidget(self.layerListView, 1, 0, 1, 1)

        self.retranslateUi(ApplyTemplatesDialog)
        QtCore.QMetaObject.connectSlotsByName(ApplyTemplatesDialog)

    def retranslateUi(self, ApplyTemplatesDialog):
        ApplyTemplatesDialog.setWindowTitle(QtGui.QApplication.translate("ApplyTemplatesDialog", "Apply templates", None, QtGui.QApplication.UnicodeUTF8))
        self.externalFilesCheckBox.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Select files from disk", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectDataFiles.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Select files...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ApplyTemplatesDialog", "Templates", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Institution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Workflow", None, QtGui.QApplication.UnicodeUTF8))
        self.organizationManageButton.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Manage", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseManageButton.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Manage", None, QtGui.QApplication.UnicodeUTF8))
        self.workflowManageButton.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Manage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Log file", None, QtGui.QApplication.UnicodeUTF8))
        self.selectLogFileButton.setText(QtGui.QApplication.translate("ApplyTemplatesDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_viewer.ui'
#
# Created: Tue Feb 22 16:04:42 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MetatoolsViewer(object):
    def setupUi(self, MetatoolsViewer):
        MetatoolsViewer.setObjectName(_fromUtf8("MetatoolsViewer"))
        MetatoolsViewer.resize(413, 305)
        self.verticalLayout = QtGui.QVBoxLayout(MetatoolsViewer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(MetatoolsViewer)
        self.webView.setMinimumSize(QtCore.QSize(250, 150))
        self.webView.setStyleSheet(_fromUtf8(""))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.buttonBox = QtGui.QDialogButtonBox(MetatoolsViewer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MetatoolsViewer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MetatoolsViewer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MetatoolsViewer.reject)
        QtCore.QMetaObject.connectSlotsByName(MetatoolsViewer)

    def retranslateUi(self, MetatoolsViewer):
        MetatoolsViewer.setWindowTitle(QtGui.QApplication.translate("MetatoolsViewer", "Metadata viewer", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit

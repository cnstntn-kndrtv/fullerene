# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullerenegui.ui'
#
# Created: Fri May 15 22:17:08 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FullereneGUI(object):
    def setupUi(self, FullereneGUI):
        FullereneGUI.setObjectName(_fromUtf8("FullereneGUI"))
        FullereneGUI.resize(1006, 699)
        self.centralWidget = QtGui.QWidget(FullereneGUI)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tab_main = QtGui.QTabWidget(self.centralWidget)
        self.tab_main.setGeometry(QtCore.QRect(0, 10, 997, 641))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tab_main.sizePolicy().hasHeightForWidth())
        self.tab_main.setSizePolicy(sizePolicy)
        self.tab_main.setAutoFillBackground(True)
        self.tab_main.setObjectName(_fromUtf8("tab_main"))
        self.tab_select_fullerenes = QtGui.QWidget()
        self.tab_select_fullerenes.setObjectName(_fromUtf8("tab_select_fullerenes"))
        self.table_select = QtGui.QTableWidget(self.tab_select_fullerenes)
        self.table_select.setGeometry(QtCore.QRect(9, 75, 981, 451))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_select.sizePolicy().hasHeightForWidth())
        self.table_select.setSizePolicy(sizePolicy)
        self.table_select.setMinimumSize(QtCore.QSize(0, 0))
        self.table_select.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_select.setDragEnabled(False)
        self.table_select.setAlternatingRowColors(True)
        self.table_select.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_select.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_select.setObjectName(_fromUtf8("table_select"))
        self.table_select.setColumnCount(6)
        self.table_select.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_select.setHorizontalHeaderItem(5, item)
        self.button_build = QtGui.QPushButton(self.tab_select_fullerenes)
        self.button_build.setGeometry(QtCore.QRect(870, 560, 85, 27))
        self.button_build.setObjectName(_fromUtf8("button_build"))
        self.button_preview = QtGui.QPushButton(self.tab_select_fullerenes)
        self.button_preview.setGeometry(QtCore.QRect(780, 560, 85, 27))
        self.button_preview.setObjectName(_fromUtf8("button_preview"))
        self.layoutWidget = QtGui.QWidget(self.tab_select_fullerenes)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 710, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_N = QtGui.QLabel(self.layoutWidget)
        self.label_N.setObjectName(_fromUtf8("label_N"))
        self.horizontalLayout.addWidget(self.label_N)
        self.spinbox_N = QtGui.QSpinBox(self.layoutWidget)
        self.spinbox_N.setMinimum(20)
        self.spinbox_N.setMaximum(200)
        self.spinbox_N.setSingleStep(2)
        self.spinbox_N.setObjectName(_fromUtf8("spinbox_N"))
        self.horizontalLayout.addWidget(self.spinbox_N)
        self.checkbox_IPR = QtGui.QCheckBox(self.layoutWidget)
        self.checkbox_IPR.setObjectName(_fromUtf8("checkbox_IPR"))
        self.horizontalLayout.addWidget(self.checkbox_IPR)
        spacerItem = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_iso_from = QtGui.QLabel(self.layoutWidget)
        self.label_iso_from.setObjectName(_fromUtf8("label_iso_from"))
        self.horizontalLayout.addWidget(self.label_iso_from)
        self.spinbox_iso_from = QtGui.QSpinBox(self.layoutWidget)
        self.spinbox_iso_from.setMaximum(999999)
        self.spinbox_iso_from.setObjectName(_fromUtf8("spinbox_iso_from"))
        self.horizontalLayout.addWidget(self.spinbox_iso_from)
        self.label_iso_to = QtGui.QLabel(self.layoutWidget)
        self.label_iso_to.setObjectName(_fromUtf8("label_iso_to"))
        self.horizontalLayout.addWidget(self.label_iso_to)
        self.spinbox_iso_to = QtGui.QSpinBox(self.layoutWidget)
        self.spinbox_iso_to.setMaximum(999999999)
        self.spinbox_iso_to.setProperty("value", 1)
        self.spinbox_iso_to.setObjectName(_fromUtf8("spinbox_iso_to"))
        self.horizontalLayout.addWidget(self.spinbox_iso_to)
        spacerItem1 = QtGui.QSpacerItem(77, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_symmetry = QtGui.QLabel(self.layoutWidget)
        self.label_symmetry.setObjectName(_fromUtf8("label_symmetry"))
        self.horizontalLayout.addWidget(self.label_symmetry)
        self.combobox_symmetry = QtGui.QComboBox(self.layoutWidget)
        self.combobox_symmetry.setObjectName(_fromUtf8("combobox_symmetry"))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.combobox_symmetry.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.combobox_symmetry)
        self.layoutWidget1 = QtGui.QWidget(self.tab_select_fullerenes)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 40, 707, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_Nisomers = QtGui.QLabel(self.layoutWidget1)
        self.label_Nisomers.setScaledContents(True)
        self.label_Nisomers.setObjectName(_fromUtf8("label_Nisomers"))
        self.horizontalLayout_2.addWidget(self.label_Nisomers)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_max_results = QtGui.QLabel(self.layoutWidget1)
        self.label_max_results.setObjectName(_fromUtf8("label_max_results"))
        self.horizontalLayout_2.addWidget(self.label_max_results)
        self.spinBox_max_results = QtGui.QSpinBox(self.layoutWidget1)
        self.spinBox_max_results.setMinimum(1)
        self.spinBox_max_results.setMaximum(99999999)
        self.spinBox_max_results.setProperty("value", 1000)
        self.spinBox_max_results.setObjectName(_fromUtf8("spinBox_max_results"))
        self.horizontalLayout_2.addWidget(self.spinBox_max_results)
        self.button_show = QtGui.QPushButton(self.layoutWidget1)
        self.button_show.setObjectName(_fromUtf8("button_show"))
        self.horizontalLayout_2.addWidget(self.button_show)
        self.formLayoutWidget = QtGui.QWidget(self.tab_select_fullerenes)
        self.formLayoutWidget.setGeometry(QtCore.QRect(530, 540, 251, 51))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinbox_GC_k = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinbox_GC_k.setObjectName(_fromUtf8("spinbox_GC_k"))
        self.horizontalLayout_3.addWidget(self.spinbox_GC_k)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinbox_GC_l = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinbox_GC_l.setObjectName(_fromUtf8("spinbox_GC_l"))
        self.horizontalLayout_3.addWidget(self.spinbox_GC_l)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_GC_CN = QtGui.QLabel(self.formLayoutWidget)
        self.label_GC_CN.setText(_fromUtf8(""))
        self.label_GC_CN.setObjectName(_fromUtf8("label_GC_CN"))
        self.horizontalLayout_3.addWidget(self.label_GC_CN)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.tab_main.addTab(self.tab_select_fullerenes, _fromUtf8(""))
        self.tab_transform_fullerene = QtGui.QWidget()
        self.tab_transform_fullerene.setObjectName(_fromUtf8("tab_transform_fullerene"))
        self.tab_main.addTab(self.tab_transform_fullerene, _fromUtf8(""))
        self.tab_layout2d = QtGui.QWidget()
        self.tab_layout2d.setObjectName(_fromUtf8("tab_layout2d"))
        self.tab_main.addTab(self.tab_layout2d, _fromUtf8(""))
        self.tab_geometry = QtGui.QWidget()
        self.tab_geometry.setObjectName(_fromUtf8("tab_geometry"))
        self.tab_main.addTab(self.tab_geometry, _fromUtf8(""))
        self.tab_analysis = QtGui.QWidget()
        self.tab_analysis.setObjectName(_fromUtf8("tab_analysis"))
        self.tab_main.addTab(self.tab_analysis, _fromUtf8(""))
        self.tab_output = QtGui.QWidget()
        self.tab_output.setObjectName(_fromUtf8("tab_output"))
        self.tab_main.addTab(self.tab_output, _fromUtf8(""))
        FullereneGUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(FullereneGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1006, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        FullereneGUI.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(FullereneGUI)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        FullereneGUI.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(FullereneGUI)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        FullereneGUI.setStatusBar(self.statusBar)

        self.retranslateUi(FullereneGUI)
        self.tab_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FullereneGUI)

    def retranslateUi(self, FullereneGUI):
        FullereneGUI.setWindowTitle(_translate("FullereneGUI", "FullereneGUI", None))
        self.table_select.setSortingEnabled(True)
        item = self.table_select.horizontalHeaderItem(0)
        item.setText(_translate("FullereneGUI", "Isomer", None))
        item = self.table_select.horizontalHeaderItem(1)
        item.setText(_translate("FullereneGUI", "Symmetry", None))
        item = self.table_select.horizontalHeaderItem(2)
        item.setText(_translate("FullereneGUI", "HOMO electrons", None))
        item = self.table_select.horizontalHeaderItem(3)
        item.setText(_translate("FullereneGUI", "HOMO-LUMO Gap", None))
        item = self.table_select.horizontalHeaderItem(4)
        item.setText(_translate("FullereneGUI", "NMR Pattern", None))
        item = self.table_select.horizontalHeaderItem(5)
        item.setText(_translate("FullereneGUI", "Spiral", None))
        self.button_build.setText(_translate("FullereneGUI", "Build", None))
        self.button_preview.setText(_translate("FullereneGUI", "Preview", None))
        self.label_N.setText(_translate("FullereneGUI", "N:", None))
        self.checkbox_IPR.setText(_translate("FullereneGUI", "IPR", None))
        self.label_iso_from.setText(_translate("FullereneGUI", "Isomers from:", None))
        self.label_iso_to.setText(_translate("FullereneGUI", "to:", None))
        self.label_symmetry.setText(_translate("FullereneGUI", "Symmetry:", None))
        self.combobox_symmetry.setItemText(0, _translate("FullereneGUI", "Any", None))
        self.combobox_symmetry.setItemText(1, _translate("FullereneGUI", " C1", None))
        self.combobox_symmetry.setItemText(2, _translate("FullereneGUI", " Cs", None))
        self.combobox_symmetry.setItemText(3, _translate("FullereneGUI", " Ci", None))
        self.combobox_symmetry.setItemText(4, _translate("FullereneGUI", " C2", None))
        self.combobox_symmetry.setItemText(5, _translate("FullereneGUI", "C3", None))
        self.combobox_symmetry.setItemText(6, _translate("FullereneGUI", "C3v", None))
        self.combobox_symmetry.setItemText(7, _translate("FullereneGUI", "C3h", None))
        self.combobox_symmetry.setItemText(8, _translate("FullereneGUI", " D2", None))
        self.combobox_symmetry.setItemText(9, _translate("FullereneGUI", "D2d", None))
        self.combobox_symmetry.setItemText(10, _translate("FullereneGUI", "D2h", None))
        self.combobox_symmetry.setItemText(11, _translate("FullereneGUI", " D3", None))
        self.combobox_symmetry.setItemText(12, _translate("FullereneGUI", "D3d", None))
        self.combobox_symmetry.setItemText(13, _translate("FullereneGUI", "D3h", None))
        self.combobox_symmetry.setItemText(14, _translate("FullereneGUI", " D5", None))
        self.combobox_symmetry.setItemText(15, _translate("FullereneGUI", "D5d", None))
        self.combobox_symmetry.setItemText(16, _translate("FullereneGUI", "D5h", None))
        self.combobox_symmetry.setItemText(17, _translate("FullereneGUI", " D6", None))
        self.combobox_symmetry.setItemText(18, _translate("FullereneGUI", "D6d", None))
        self.combobox_symmetry.setItemText(19, _translate("FullereneGUI", "D6h", None))
        self.combobox_symmetry.setItemText(20, _translate("FullereneGUI", " S4", None))
        self.combobox_symmetry.setItemText(21, _translate("FullereneGUI", " S6", None))
        self.combobox_symmetry.setItemText(22, _translate("FullereneGUI", "  T", None))
        self.combobox_symmetry.setItemText(23, _translate("FullereneGUI", " Td", None))
        self.combobox_symmetry.setItemText(24, _translate("FullereneGUI", " Th", None))
        self.combobox_symmetry.setItemText(25, _translate("FullereneGUI", "  I", None))
        self.combobox_symmetry.setItemText(26, _translate("FullereneGUI", " Ih", None))
        self.label_Nisomers.setText(_translate("FullereneGUI", "1 C20 isomers in total, 1 matching filter .", None))
        self.label_max_results.setText(_translate("FullereneGUI", "Maximum number of results:", None))
        self.button_show.setText(_translate("FullereneGUI", "Show", None))
        self.label.setText(_translate("FullereneGUI", "Goldberg-Coxeter transform", None))
        self.label_2.setText(_translate("FullereneGUI", "k:", None))
        self.label_3.setText(_translate("FullereneGUI", "l:", None))
        self.label_4.setText(_translate("FullereneGUI", "Result:", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_select_fullerenes), _translate("FullereneGUI", "Select Fullerene", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_transform_fullerene), _translate("FullereneGUI", "Transformation", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_layout2d), _translate("FullereneGUI", "Graph Layout", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_geometry), _translate("FullereneGUI", "3D Geometry", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_analysis), _translate("FullereneGUI", "Analysis", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_output), _translate("FullereneGUI", "Export", None))


class FullereneGUI(QtGui.QMainWindow, Ui_FullereneGUI):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

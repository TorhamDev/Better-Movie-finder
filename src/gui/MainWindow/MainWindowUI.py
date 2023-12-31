from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(600, 450)
        Form.setMinimumSize(QtCore.QSize(600, 450))
        Form.setWindowIcon(QtGui.QIcon('./gui/images/search.png'))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Type your movie here :')
        self.horizontalLayout.addWidget(self.lineEdit)
        self.search_btn = QtWidgets.QPushButton(parent=Form)
        self.search_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./gui/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.list_widget = QtWidgets.QListWidget(parent=Form)
        self.list_widget.setObjectName("list_widget")
        self.verticalLayout.addWidget(self.list_widget)
        self.clear_btn = QtWidgets.QPushButton(parent=Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./gui/images/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clear_btn.setIcon(icon1)
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout.addWidget(self.clear_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.output = QtWidgets.QTextEdit(parent=Form)
        self.output.setObjectName("output")
        self.output.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Movie Finder"))
        self.lineEdit.setAccessibleDescription(_translate("Form", "type here"))
        self.clear_btn.setText(_translate("Form", "Clear"))


import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1459, 1028)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.a_topFrame = QtWidgets.QFrame(self.centralwidget)
        self.a_topFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.a_topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.a_topFrame.setObjectName("a_topFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.a_topFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtWidgets.QLabel(self.a_topFrame)
        self.titleLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel, 0, QtCore.Qt.AlignTop)
        self.processFrame = QtWidgets.QFrame(self.a_topFrame)
        self.processFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.processFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.processFrame.setObjectName("processFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.processFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 21, -1, -1)
        self.horizontalLayout_3.setSpacing(21)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.processLabel = QtWidgets.QLabel(self.processFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.processLabel.sizePolicy().hasHeightForWidth())
        self.processLabel.setSizePolicy(sizePolicy)
        self.processLabel.setObjectName("processLabel")
        self.horizontalLayout_3.addWidget(self.processLabel)
        self.processSpinBox = QtWidgets.QSpinBox(self.processFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.processSpinBox.sizePolicy().hasHeightForWidth())
        self.processSpinBox.setSizePolicy(sizePolicy)
        self.processSpinBox.setObjectName("processSpinBox")
        self.horizontalLayout_3.addWidget(self.processSpinBox)
        self.resourcesLabel_2 = QtWidgets.QLabel(self.processFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.resourcesLabel_2.sizePolicy().hasHeightForWidth())
        self.resourcesLabel_2.setSizePolicy(sizePolicy)
        self.resourcesLabel_2.setObjectName("resourcesLabel_2")
        self.horizontalLayout_3.addWidget(self.resourcesLabel_2)
        self.resourcesSpinBox = QtWidgets.QSpinBox(self.processFrame)
        self.resourcesSpinBox.setObjectName("resourcesSpinBox")
        self.horizontalLayout_3.addWidget(self.resourcesSpinBox)
        self.btnGenerate = QtWidgets.QPushButton(self.processFrame)
        self.btnGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerate.setObjectName("btnGenerate")
        self.horizontalLayout_3.addWidget(self.btnGenerate)
        self.buttonsFrame = QtWidgets.QFrame(self.processFrame)
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.buttonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_6.setContentsMargins(-1, 21, -1, 21)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnLoadExample = QtWidgets.QPushButton(self.buttonsFrame)
        self.btnLoadExample.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLoadExample.setAutoFillBackground(False)
        self.btnLoadExample.setObjectName("btnLoadExample")
        self.horizontalLayout_6.addWidget(self.btnLoadExample)
        self.horizontalLayout_3.addWidget(self.buttonsFrame)
        self.verticalLayout_2.addWidget(
            self.processFrame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.a_topFrame)
        self.b_middleFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.b_middleFrame.sizePolicy().hasHeightForWidth())
        self.b_middleFrame.setSizePolicy(sizePolicy)
        self.b_middleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.b_middleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.b_middleFrame.setObjectName("b_middleFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.b_middleFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resourcesFrame = QtWidgets.QFrame(self.b_middleFrame)
        self.resourcesFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.resourcesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resourcesFrame.setObjectName("resourcesFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.resourcesFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resourcesLabel = QtWidgets.QLabel(self.resourcesFrame)
        self.resourcesLabel.setObjectName("resourcesLabel")
        self.verticalLayout_3.addWidget(
            self.resourcesLabel, 0, QtCore.Qt.AlignTop)
        self.resTableWidget = QtWidgets.QTableWidget(self.resourcesFrame)
        self.resTableWidget.setMinimumSize(QtCore.QSize(440, 309))
        self.resTableWidget.setMaximumSize(QtCore.QSize(593, 320))
        self.resTableWidget.setAutoFillBackground(False)
        self.resTableWidget.setStyleSheet("QTableWidget {\n"
                                          "    background-color: #F5F5F5;\n"
                                          "    border: 1px solid #CCCCCC;\n"
                                          "    border-radius: 5px;\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item {\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:selected {\n"
                                          "    background-color: #AED6F1;\n"
                                          "    color: black;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:hover {\n"
                                          "    background-color: #D6EAF8;\n"
                                          "    color: black;\n"
                                          "}")
        self.resTableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resTableWidget.setObjectName("resTableWidget")
        self.resTableWidget.setColumnCount(0)
        self.resTableWidget.setRowCount(0)
        self.resTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.resTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.resTableWidget)
        self.horizontalLayout.addWidget(self.resourcesFrame)
        self.allocationFrame = QtWidgets.QFrame(self.b_middleFrame)
        self.allocationFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.allocationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allocationFrame.setObjectName("allocationFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.allocationFrame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.allocationLabel = QtWidgets.QLabel(self.allocationFrame)
        self.allocationLabel.setObjectName("allocationLabel")
        self.verticalLayout_8.addWidget(
            self.allocationLabel, 0, QtCore.Qt.AlignTop)
        self.alocTableWidget = QtWidgets.QTableWidget(self.allocationFrame)
        self.alocTableWidget.setMinimumSize(QtCore.QSize(439, 309))
        self.alocTableWidget.setMaximumSize(QtCore.QSize(594, 320))
        self.alocTableWidget.setStyleSheet("QTableWidget {\n"
                                           "    background-color: #F5F5F5;\n"
                                           "    border: 1px solid #CCCCCC;\n"
                                           "    border-radius: 5px;\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item {\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item:selected {\n"
                                           "    background-color: #AED6F1;\n"
                                           "    color: black;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item:hover {\n"
                                           "    background-color: #D6EAF8;\n"
                                           "    color: black;\n"
                                           "}")
        self.alocTableWidget.setObjectName("alocTableWidget")
        self.alocTableWidget.setColumnCount(0)
        self.alocTableWidget.setRowCount(0)
        self.verticalLayout_8.addWidget(self.alocTableWidget)
        self.horizontalLayout.addWidget(self.allocationFrame)
        self.maxFrame = QtWidgets.QFrame(self.b_middleFrame)
        self.maxFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.maxFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.maxFrame.setObjectName("maxFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.maxFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.maxLabel = QtWidgets.QLabel(self.maxFrame)
        self.maxLabel.setObjectName("maxLabel")
        self.verticalLayout_4.addWidget(self.maxLabel, 0, QtCore.Qt.AlignTop)
        self.maxTableWidget = QtWidgets.QTableWidget(self.maxFrame)
        self.maxTableWidget.setMinimumSize(QtCore.QSize(440, 309))
        self.maxTableWidget.setMaximumSize(QtCore.QSize(594, 320))
        self.maxTableWidget.setStyleSheet("QTableWidget {\n"
                                          "    background-color: #F5F5F5;\n"
                                          "    border: 1px solid #CCCCCC;\n"
                                          "    border-radius: 5px;\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item {\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:selected {\n"
                                          "    background-color: #AED6F1;\n"
                                          "    color: black;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:hover {\n"
                                          "    background-color: #D6EAF8;\n"
                                          "    color: black;\n"
                                          "}")
        self.maxTableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.maxTableWidget.setObjectName("maxTableWidget")
        self.maxTableWidget.setColumnCount(0)
        self.maxTableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.maxTableWidget)
        self.horizontalLayout.addWidget(self.maxFrame)
        self.verticalLayout.addWidget(self.b_middleFrame)
        self.c_bottomFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.c_bottomFrame.sizePolicy().hasHeightForWidth())
        self.c_bottomFrame.setSizePolicy(sizePolicy)
        self.c_bottomFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_bottomFrame.setObjectName("c_bottomFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.c_bottomFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.avaiableFrame = QtWidgets.QFrame(self.c_bottomFrame)
        self.avaiableFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.avaiableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avaiableFrame.setObjectName("avaiableFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.avaiableFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.avaiableLabel = QtWidgets.QLabel(self.avaiableFrame)
        self.avaiableLabel.setObjectName("avaiableLabel")
        self.verticalLayout_7.addWidget(
            self.avaiableLabel, 0, QtCore.Qt.AlignTop)
        self.availTableWidget = QtWidgets.QTableWidget(self.avaiableFrame)
        self.availTableWidget.setMinimumSize(QtCore.QSize(440, 273))
        self.availTableWidget.setMaximumSize(QtCore.QSize(593, 285))
        self.availTableWidget.setStyleSheet("QTableWidget {\n"
                                            "    background-color: #F5F5F5;\n"
                                            "    border: 1px solid #CCCCCC;\n"
                                            "    border-radius: 5px;\n"
                                            "    padding: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QTableWidget::item {\n"
                                            "    padding: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QTableWidget::item:selected {\n"
                                            "    background-color: #AED6F1;\n"
                                            "    color: black;\n"
                                            "}\n"
                                            "\n"
                                            "QTableWidget::item:hover {\n"
                                            "    background-color: #D6EAF8;\n"
                                            "    color: black;\n"
                                            "}")
        self.availTableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.availTableWidget.setObjectName("availTableWidget")
        self.availTableWidget.setColumnCount(0)
        self.availTableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.availTableWidget)
        self.btnCalcAvailable = QtWidgets.QPushButton(self.avaiableFrame)
        self.btnCalcAvailable.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalcAvailable.setObjectName("btnCalcAvailable")
        self.verticalLayout_7.addWidget(
            self.btnCalcAvailable, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.avaiableFrame)
        self.neededFrame = QtWidgets.QFrame(self.c_bottomFrame)
        self.neededFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.neededFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.neededFrame.setObjectName("neededFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.neededFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.neededLabel = QtWidgets.QLabel(self.neededFrame)
        self.neededLabel.setObjectName("neededLabel")
        self.verticalLayout_9.addWidget(
            self.neededLabel, 0, QtCore.Qt.AlignTop)
        self.needTableWidget = QtWidgets.QTableWidget(self.neededFrame)
        self.needTableWidget.setMinimumSize(QtCore.QSize(430, 273))
        self.needTableWidget.setMaximumSize(QtCore.QSize(594, 285))
        self.needTableWidget.setStyleSheet("QTableWidget {\n"
                                           "    background-color: #F5F5F5;\n"
                                           "    border: 1px solid #CCCCCC;\n"
                                           "    border-radius: 5px;\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item {\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item:selected {\n"
                                           "    background-color: #AED6F1;\n"
                                           "    color: black;\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item:hover {\n"
                                           "    background-color: #D6EAF8;\n"
                                           "    color: black;\n"
                                           "}")
        self.needTableWidget.setObjectName("needTableWidget")
        self.needTableWidget.setColumnCount(0)
        self.needTableWidget.setRowCount(0)
        self.verticalLayout_9.addWidget(self.needTableWidget)
        self.btnCalcNeed = QtWidgets.QPushButton(self.neededFrame)
        self.btnCalcNeed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalcNeed.setObjectName("btnCalcNeed")
        self.verticalLayout_9.addWidget(
            self.btnCalcNeed, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.neededFrame)
        self.reqFrame = QtWidgets.QFrame(self.c_bottomFrame)
        self.reqFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.reqFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reqFrame.setObjectName("reqFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.reqFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.reqLabel = QtWidgets.QLabel(self.reqFrame)
        self.reqLabel.setObjectName("reqLabel")
        self.verticalLayout_5.addWidget(self.reqLabel, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.reqFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reqLabel_2 = QtWidgets.QLabel(self.frame)
        self.reqLabel_2.setObjectName("reqLabel_2")
        self.horizontalLayout_4.addWidget(self.reqLabel_2)
        self.reqSpinBox = QtWidgets.QSpinBox(self.frame)
        self.reqSpinBox.setEnabled(False)
        self.reqSpinBox.setObjectName("reqSpinBox")
        self.horizontalLayout_4.addWidget(self.reqSpinBox)
        self.verticalLayout_5.addWidget(self.frame)
        self.reqTableWidget = QtWidgets.QTableWidget(self.reqFrame)
        self.reqTableWidget.setMinimumSize(QtCore.QSize(439, 210))
        self.reqTableWidget.setMaximumSize(QtCore.QSize(593, 285))
        self.reqTableWidget.setAutoFillBackground(False)
        self.reqTableWidget.setStyleSheet("QTableWidget {\n"
                                          "    background-color: #F5F5F5;\n"
                                          "    border: 1px solid #CCCCCC;\n"
                                          "    border-radius: 5px;\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item {\n"
                                          "    padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:selected {\n"
                                          "    background-color: #AED6F1;\n"
                                          "    color: black;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item:hover {\n"
                                          "    background-color: #D6EAF8;\n"
                                          "    color: black;\n"
                                          "}")
        self.reqTableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.reqTableWidget.setObjectName("reqTableWidget")
        self.reqTableWidget.setColumnCount(0)
        self.reqTableWidget.setRowCount(0)
        self.reqTableWidget.verticalHeader().setMinimumSectionSize(30)
        self.reqTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.reqTableWidget)
        self.btnRequest = QtWidgets.QPushButton(self.reqFrame)
        self.btnRequest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRequest.setObjectName("btnRequest")
        self.verticalLayout_5.addWidget(
            self.btnRequest, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.reqFrame)
        self.verticalLayout.addWidget(self.c_bottomFrame)

        # available and need table cannot be edited
        self.needTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.availTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # disable request button and calculate need button and calculate available button
        self.btnRequest.setEnabled(False)
        self.btnCalcNeed.setEnabled(False)
        self.btnCalcAvailable.setEnabled(False)

        # button connections
        self.btnGenerate.clicked.connect(self.generateInputFields)
        self.btnCalcAvailable.clicked.connect(self.calculateAvailable)
        self.btnCalcNeed.clicked.connect(self.calculateNeed)
        self.btnRequest.clicked.connect(self.openNewWindow)
        self.btnLoadExample.clicked.connect(self.loadExample)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # function to generate input fields

    def generateInputFields(self):

        # make sure that the input fields are not 0
        if int(self.processSpinBox.text()) == 0 or int(self.resourcesSpinBox.text()) == 0:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Please enter a number greater than 0")
            return

        try:

            self.processes = int(self.processSpinBox.text())
            self.resources = int(self.resourcesSpinBox.text())

            # generate resources table with default values of 0
            self.resTableWidget.setColumnCount(self.resources)
            self.resTableWidget.setRowCount(1)
            self.resTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.resTableWidget.setVerticalHeaderLabels(
                ["Resources"])
            for i in range(self.resources):
                self.resTableWidget.setItem(
                    0, i, QtWidgets.QTableWidgetItem("0"))

            # generate available table
            self.availTableWidget.setColumnCount(self.resources)
            self.availTableWidget.setRowCount(1)
            self.availTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.availTableWidget.setVerticalHeaderLabels(
                ["Available"])

            # generate max table with default values of 0
            self.maxTableWidget.setColumnCount(self.resources)
            self.maxTableWidget.setRowCount(self.processes)
            self.maxTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.maxTableWidget.setVerticalHeaderLabels(
                [f"P{i+1}" for i in range(self.processes)])
            for i in range(self.processes):
                for j in range(self.resources):
                    self.maxTableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem("0"))

            # generate allocation table with default values of 0
            self.alocTableWidget.setColumnCount(self.resources)
            self.alocTableWidget.setRowCount(self.processes)
            self.alocTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.alocTableWidget.setVerticalHeaderLabels(
                [f"P{i+1}" for i in range(self.processes)])
            for i in range(self.processes):
                for j in range(self.resources):
                    self.alocTableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem("0"))

            # generate need table
            self.needTableWidget.setColumnCount(self.resources)
            self.needTableWidget.setRowCount(self.processes)
            self.needTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.needTableWidget.setVerticalHeaderLabels(
                [f"P{i+1}" for i in range(self.processes)])

            # generate request table
            self.reqTableWidget.setColumnCount(self.resources)
            self.reqTableWidget.setRowCount(1)
            self.reqTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.reqTableWidget.setVerticalHeaderLabels(
                ["Request"])

            # enable request spinbox
            self.reqSpinBox.setEnabled(True)

            # set spinbox max value to the number of processes
            self.reqSpinBox.setMaximum(self.processes)

            # enable calculate available button
            self.btnCalcAvailable.setEnabled(True)

        except Exception as e:
            print(f"Error: {e}")

    # function to calculate available

    def calculateAvailable(self):

        try:
            # check if all values are positive numbers only in the resources table, max table and allocation table
            for i in range(self.resources):
                if not self.resTableWidget.item(0, i).text().isnumeric():
                    QtWidgets.QMessageBox.warning(
                        self.centralwidget, "Error", "Resources table values must be POSITIVE numbers only")
                    return

            for i in range(self.processes):
                for j in range(self.resources):
                    if not self.maxTableWidget.item(i, j).text().isnumeric():
                        QtWidgets.QMessageBox.warning(
                            self.centralwidget, "Error", "Max table values must be POSITIVE numbers only")
                        return
                    if not self.alocTableWidget.item(i, j).text().isnumeric():
                        QtWidgets.QMessageBox.warning(
                            self.centralwidget, "Error", "Allocation table values must be POSITIVE numbers only")
                        return

            # get resources table values
            resources = []
            for i in range(self.resources):
                resources.append(
                    int(self.resTableWidget.item(0, i).text()))

            # get allocation table values
            allocation = []
            for i in range(self.processes):
                allocation.append([])
                for j in range(self.resources):
                    allocation[i].append(
                        int(self.alocTableWidget.item(i, j).text()))

            # calculate available
            available = []
            for i in range(self.resources):
                available.append(resources[i] - sum(allocation[j][i]
                                                    for j in range(self.processes)))

            # display available
            for i in range(self.resources):
                self.availTableWidget.setItem(
                    0, i, QtWidgets.QTableWidgetItem(str(available[i])))
            self.btnCalcNeed.setEnabled(True)

        except Exception as e:
            print(f"Error: {e}")

    # function to open a new window when button is clicked

    def openNewWindow(self):

        try:
            # check if spinbox value is not 0
            if self.reqSpinBox.value() == 0:
                QtWidgets.QMessageBox.warning(
                    self.centralwidget, "Error", "Select a process to request resources from")
                return

            # check if request table values are positive numbers only
            for i in range(self.resources):
                if not self.reqTableWidget.item(0, i).text().isnumeric():
                    QtWidgets.QMessageBox.warning(
                        self.centralwidget, "Error", "Request table values must be POSITIVE numbers only")
                    return

            # open new window
            self.newWindow = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.newWindow)
            self.newWindow.show()

            # calculate new allocation table in new window by adding request to old allocation for the selected process only
            self.ui.newAlocTableWidget.setColumnCount(self.resources)
            self.ui.newAlocTableWidget.setRowCount(self.processes)
            self.ui.newAlocTableWidget.setHorizontalHeaderLabels(
                [f"R{i+1}" for i in range(self.resources)])
            self.ui.newAlocTableWidget.setVerticalHeaderLabels(
                [f"P{i+1}" for i in range(self.processes)])
            for i in range(self.processes):
                for j in range(self.resources):
                    if i == self.reqSpinBox.value() - 1:
                        self.ui.newAlocTableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(int(self.alocTableWidget.item(i, j).text()) + int(self.reqTableWidget.item(0, j).text()))))
                    else:
                        self.ui.newAlocTableWidget.setItem(
                            i, j, QtWidgets.QTableWidgetItem(str(int(self.alocTableWidget.item(i, j).text()))))

            # calculate new need table in new window by subtracting maxmimum from new allocation
            self.ui.newNeedTableWidget.setColumnCount(self.resources)
            self.ui.newNeedTableWidget.setRowCount(self.processes)
            self.ui.newNeedTableWidget.setHorizontalHeaderLabels(
                [f"R{i + 1}" for i in range(self.resources)])
            self.ui.newNeedTableWidget.setVerticalHeaderLabels(
                [f"P{i + 1}" for i in range(self.processes)])
            for i in range(self.processes):
                for j in range(self.resources):
                    self.ui.newNeedTableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(int(self.maxTableWidget.item(i, j).text()) - int(self.ui.newAlocTableWidget.item(i, j).text()))))

            # calculate new available table in new window by subtracting request from available
            self.ui.newAvailTableWidget.setColumnCount(self.resources)
            self.ui.newAvailTableWidget.setRowCount(1)
            self.ui.newAvailTableWidget.setHorizontalHeaderLabels(
                [f"R{i + 1}" for i in range(self.resources)])
            self.ui.newAvailTableWidget.setVerticalHeaderLabels(
                ["Available"])
            for i in range(self.resources):
                self.ui.newAvailTableWidget.setItem(
                    0, i, QtWidgets.QTableWidgetItem(str(int(self.availTableWidget.item(0, i).text()) - int(self.reqTableWidget.item(0, i).text()))))

            # calculate new safe sequence in new window by running the banker's algorithm on the new tables and displaying the safe sequence if it exists in the output text edit
            # when the button in new window is clicked
            self.ui.btnCheckReq.clicked.connect(self.calcSafeSeq)

        except Exception as e:
            print(f"Error: {e}")

    # function to calculate safe sequence

    def calcSafeSeq(self):

        try:

            # set new available table values
            for i in range(self.resources):
                self.ui.newAvailTableWidget.setItem(
                    0, i, QtWidgets.QTableWidgetItem(str(int(self.availTableWidget.item(0, i).text()) - int(self.reqTableWidget.item(0, i).text()))))

            # get new need table values
            need = []
            for i in range(self.processes):
                need.append([])
                for j in range(self.resources):
                    need[i].append(
                        int(self.ui.newNeedTableWidget.item(i, j).text()))

            # get new allocation table values
            allocation = []
            for i in range(self.processes):
                allocation.append([])
                for j in range(self.resources):
                    allocation[i].append(
                        int(self.ui.newAlocTableWidget.item(i, j).text()))

            # get new available table values
            available = []
            for i in range(self.resources):
                available.append(
                    int(self.ui.newAvailTableWidget.item(0, i).text()))

            # calculate safe sequence and output the available table after each iteration
            # show error message if safe sequence does not exist
            self.ui.outputTextEdit.clear()
            # self.ui.outputTextEdit.append("Safe Sequence: ")
            self.ui.outputTextEdit.append(
                self.bankersAlgorithm(self.ui.newNeedTableWidget, self.ui.newAlocTableWidget, self.ui.newAvailTableWidget))

        except Exception as e:
            print(f"Error: {e}")

    # function to run the banker's algorithm

    def bankersAlgorithm(self, needTableWidget, alocTableWidget, availTableWidget):

        try:

            # get need table values
            need = []
            for i in range(self.processes):
                need.append([])
                for j in range(self.resources):
                    need[i].append(
                        int(needTableWidget.item(i, j).text()))

            # get allocation table values
            allocation = []
            for i in range(self.processes):
                allocation.append([])
                for j in range(self.resources):
                    allocation[i].append(
                        int(alocTableWidget.item(i, j).text()))

            # get available table values
            available = []
            for i in range(self.resources):
                available.append(
                    int(availTableWidget.item(0, i).text()))

            # calculate safe sequence and output the available table after each iteration

            # Check if the request can be fulfilled by comparing it with the Need resources:
            if any(self.reqTableWidget.item(0, i).text() > needTableWidget.item(0, i).text() for i in range(self.resources)):
                QtWidgets.QMessageBox.warning(
                    self.centralwidget, "Result", "Request Denied, since it exceeds the Need resources")
                self.ui.outputTextEdit.append(
                    "Request Denied, Deadlock Occurs")
                return

            # Check if the need table in the new window contains any negative values:
            if any(int(needTableWidget.item(i, j).text()) < 0 for i in range(self.processes) for j in range(self.resources)):
                QtWidgets.QMessageBox.warning(
                    self.centralwidget, "Result", "Request Denied, since it exceeds the Need resources")
                self.ui.outputTextEdit.append(
                    "Request Denied, Deadlock Occurs")
                return

            safeSeq = []
            work = available.copy()
            finish = [False] * self.processes
            while False in finish:
                for i in range(self.processes):
                    if finish[i] == False:
                        for j in range(self.resources):
                            if need[i][j] > work[j]:
                                break
                        else:
                            for j in range(self.resources):
                                work[j] += allocation[i][j]
                            finish[i] = True
                            safeSeq.append(i + 1)
                            self.ui.outputTextEdit.append(
                                f"Available after P{i + 1} is executed: {work}")

                            # put the work list in the available table
                            for j in range(self.resources):
                                availTableWidget.setItem(
                                    0, j, QtWidgets.QTableWidgetItem(str(work[j])))
                            QtWidgets.QApplication.processEvents()
                            time.sleep(1)

            if len(safeSeq) == self.processes:
                # show message box with the safe sequence and output the safe sequence
                QtWidgets.QMessageBox.information(
                    self.ui.centralwidget, "Result", "Request Granted. " + "Safe Sequence:  " + " -> ".join("P" + str(i) for i in safeSeq))
                # return the safe sequence as a string with the process numbers and the word P before each number and a -> after each process number
                return "Safe Sequence: " + " -> ".join("P" + str(i) for i in safeSeq)
            else:
                return "Deadlock Occurs"

        except Exception as e:
            print(f"Error: {e}")

    # function to calculate need

    def calculateNeed(self):

        try:

            # fill request table with 0s
            for i in range(self.resources):
                self.reqTableWidget.setItem(
                    0, i, QtWidgets.QTableWidgetItem("0"))

            # get max table values
            max = []
            for i in range(self.processes):
                max.append([])
                for j in range(self.resources):
                    max[i].append(
                        int(self.maxTableWidget.item(i, j).text()))

            # get allocation table values
            allocation = []
            for i in range(self.processes):
                allocation.append([])
                for j in range(self.resources):
                    allocation[i].append(
                        int(self.alocTableWidget.item(i, j).text()))

            # calculate need
            need = []
            for i in range(self.processes):
                need.append([])
                for j in range(self.resources):
                    need[i].append(max[i][j] - allocation[i][j])

            # display need
            for i in range(self.processes):
                for j in range(self.resources):
                    self.needTableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(need[i][j])))

            # enable request button
            self.btnRequest.setEnabled(True)

        except Exception as e:
            print(f"Error: {e}")

    # function to load the input fields and tables with values i have already set

    def loadExample(self):

        try:

            # enable calculate available button
            self.btnCalcAvailable.setEnabled(True)

            # set spinboxes values
            self.processSpinBox.setValue(5)
            self.resourcesSpinBox.setValue(3)

            # call generate input fields function
            self.generateInputFields()

            # set total resources values
            self.resTableWidget.setRowCount(1)
            self.resTableWidget.setColumnCount(3)
            self.resTableWidget.setItem(
                0, 0, QtWidgets.QTableWidgetItem("10"))
            self.resTableWidget.setItem(
                0, 1, QtWidgets.QTableWidgetItem("5"))
            self.resTableWidget.setItem(
                0, 2, QtWidgets.QTableWidgetItem("7"))

            # set allocation table values
            self.alocTableWidget.setRowCount(5)
            self.alocTableWidget.setColumnCount(3)
            self.alocTableWidget.setItem(
                0, 0, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                0, 1, QtWidgets.QTableWidgetItem("1"))
            self.alocTableWidget.setItem(
                0, 2, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                1, 0, QtWidgets.QTableWidgetItem("2"))
            self.alocTableWidget.setItem(
                1, 1, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                1, 2, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                2, 0, QtWidgets.QTableWidgetItem("3"))
            self.alocTableWidget.setItem(
                2, 1, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                2, 2, QtWidgets.QTableWidgetItem("2"))
            self.alocTableWidget.setItem(
                3, 0, QtWidgets.QTableWidgetItem("2"))
            self.alocTableWidget.setItem(
                3, 1, QtWidgets.QTableWidgetItem("1"))
            self.alocTableWidget.setItem(
                3, 2, QtWidgets.QTableWidgetItem("1"))
            self.alocTableWidget.setItem(
                4, 0, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                4, 1, QtWidgets.QTableWidgetItem("0"))
            self.alocTableWidget.setItem(
                4, 2, QtWidgets.QTableWidgetItem("2"))

            # set max table values
            self.maxTableWidget.setRowCount(5)
            self.maxTableWidget.setColumnCount(3)
            self.maxTableWidget.setItem(
                0, 0, QtWidgets.QTableWidgetItem("7"))
            self.maxTableWidget.setItem(
                0, 1, QtWidgets.QTableWidgetItem("5"))
            self.maxTableWidget.setItem(
                0, 2, QtWidgets.QTableWidgetItem("3"))
            self.maxTableWidget.setItem(
                1, 0, QtWidgets.QTableWidgetItem("3"))
            self.maxTableWidget.setItem(
                1, 1, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                1, 2, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                2, 0, QtWidgets.QTableWidgetItem("9"))
            self.maxTableWidget.setItem(
                2, 1, QtWidgets.QTableWidgetItem("0"))
            self.maxTableWidget.setItem(
                2, 2, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                3, 0, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                3, 1, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                3, 2, QtWidgets.QTableWidgetItem("2"))
            self.maxTableWidget.setItem(
                4, 0, QtWidgets.QTableWidgetItem("4"))
            self.maxTableWidget.setItem(
                4, 1, QtWidgets.QTableWidgetItem("3"))
            self.maxTableWidget.setItem(
                4, 2, QtWidgets.QTableWidgetItem("3"))

        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Banker's Algorithm GUI"))
        self.titleLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Banker\'s Algorithm</span></p></body></html>"))
        self.processLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Number of Processes:</span></p></body></html>"))
        self.resourcesLabel_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Number of Resources:</span></p></body></html>"))
        self.btnGenerate.setText(_translate(
            "MainWindow", "Generate Input Fields"))
        self.btnLoadExample.setText(_translate("MainWindow", "Load Example"))
        self.resourcesLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Total Resources:</span></p></body></html>"))
        self.allocationLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Current Allocation:</span></p></body></html>"))
        self.maxLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Maximum Need:</span></p></body></html>"))
        self.avaiableLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Available Resources :</span></p></body></html>"))
        self.btnCalcAvailable.setText(_translate(
            "MainWindow", "Calculate Available"))
        self.neededLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Remaining Need:</span></p></body></html>"))
        self.btnCalcNeed.setText(_translate("MainWindow", "Calculate Need"))
        self.reqLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Requested Resources:</span></p></body></html>"))
        self.reqLabel_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Process Requesting Resources:</span></p></body></html>"))
        self.btnRequest.setText(_translate(
            "MainWindow", "Request Resources for Process"))


class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Results")
        MainWindow.resize(1019, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newAllocationFrame = QtWidgets.QFrame(self.mainFrame)
        self.newAllocationFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.newAllocationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newAllocationFrame.setObjectName("newAllocationFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.newAllocationFrame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.newAllocationLabel_2 = QtWidgets.QLabel(self.newAllocationFrame)
        self.newAllocationLabel_2.setObjectName("newAllocationLabel_2")
        self.verticalLayout_8.addWidget(
            self.newAllocationLabel_2, 0, QtCore.Qt.AlignTop)
        self.newAlocTableWidget = QtWidgets.QTableWidget(
            self.newAllocationFrame)
        self.newAlocTableWidget.setMinimumSize(QtCore.QSize(293, 278))
        self.newAlocTableWidget.setMaximumSize(QtCore.QSize(594, 320))
        self.newAlocTableWidget.setStyleSheet("QTableWidget {\n"
                                              "    background-color: #F5F5F5;\n"
                                              "    border: 1px solid #CCCCCC;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 5px;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item {\n"
                                              "    padding: 5px;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item:selected {\n"
                                              "    background-color: #AED6F1;\n"
                                              "    color: black;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item:hover {\n"
                                              "    background-color: #D6EAF8;\n"
                                              "    color: black;\n"
                                              "}")
        self.newAlocTableWidget.setObjectName("newAlocTableWidget")
        self.newAlocTableWidget.setColumnCount(0)
        self.newAlocTableWidget.setRowCount(0)
        self.verticalLayout_8.addWidget(self.newAlocTableWidget)
        self.horizontalLayout_2.addWidget(self.newAllocationFrame)
        self.newNeededFrame = QtWidgets.QFrame(self.mainFrame)
        self.newNeededFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.newNeededFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newNeededFrame.setObjectName("newNeededFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.newNeededFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.newNeededLabel = QtWidgets.QLabel(self.newNeededFrame)
        self.newNeededLabel.setObjectName("newNeededLabel")
        self.verticalLayout_9.addWidget(
            self.newNeededLabel, 0, QtCore.Qt.AlignTop)
        self.newNeedTableWidget = QtWidgets.QTableWidget(self.newNeededFrame)
        self.newNeedTableWidget.setMinimumSize(QtCore.QSize(294, 278))
        self.newNeedTableWidget.setMaximumSize(QtCore.QSize(594, 285))
        self.newNeedTableWidget.setStyleSheet("QTableWidget {\n"
                                              "    background-color: #F5F5F5;\n"
                                              "    border: 1px solid #CCCCCC;\n"
                                              "    border-radius: 5px;\n"
                                              "    padding: 5px;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item {\n"
                                              "    padding: 5px;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item:selected {\n"
                                              "    background-color: #AED6F1;\n"
                                              "    color: black;\n"
                                              "}\n"
                                              "\n"
                                              "QTableWidget::item:hover {\n"
                                              "    background-color: #D6EAF8;\n"
                                              "    color: black;\n"
                                              "}")
        self.newNeedTableWidget.setObjectName("newNeedTableWidget")
        self.newNeedTableWidget.setColumnCount(0)
        self.newNeedTableWidget.setRowCount(0)
        self.verticalLayout_9.addWidget(self.newNeedTableWidget)
        self.horizontalLayout_2.addWidget(self.newNeededFrame)
        self.newAvaiableFrame = QtWidgets.QFrame(self.mainFrame)
        self.newAvaiableFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.newAvaiableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newAvaiableFrame.setObjectName("newAvaiableFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.newAvaiableFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.newAvaiableLabel = QtWidgets.QLabel(self.newAvaiableFrame)
        self.newAvaiableLabel.setObjectName("newAvaiableLabel")
        self.verticalLayout_7.addWidget(
            self.newAvaiableLabel, 0, QtCore.Qt.AlignTop)
        self.newAvailTableWidget = QtWidgets.QTableWidget(
            self.newAvaiableFrame)
        self.newAvailTableWidget.setMinimumSize(QtCore.QSize(294, 278))
        self.newAvailTableWidget.setMaximumSize(QtCore.QSize(593, 285))
        self.newAvailTableWidget.setStyleSheet("QTableWidget {\n"
                                               "    background-color: #F5F5F5;\n"
                                               "    border: 1px solid #CCCCCC;\n"
                                               "    border-radius: 5px;\n"
                                               "    padding: 5px;\n"
                                               "}\n"
                                               "\n"
                                               "QTableWidget::item {\n"
                                               "    padding: 5px;\n"
                                               "}\n"
                                               "\n"
                                               "QTableWidget::item:selected {\n"
                                               "    background-color: #AED6F1;\n"
                                               "    color: black;\n"
                                               "}\n"
                                               "\n"
                                               "QTableWidget::item:hover {\n"
                                               "    background-color: #D6EAF8;\n"
                                               "    color: black;\n"
                                               "}")
        self.newAvailTableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.newAvailTableWidget.setObjectName("newAvailTableWidget")
        self.newAvailTableWidget.setColumnCount(0)
        self.newAvailTableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.newAvailTableWidget)
        self.horizontalLayout_2.addWidget(self.newAvaiableFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        self.outputFrame = QtWidgets.QFrame(self.centralwidget)
        self.outputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputFrame.setObjectName("outputFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.outputFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnCheckReq = QtWidgets.QPushButton(self.outputFrame)
        self.btnCheckReq.setObjectName("btnCheckReq")
        self.verticalLayout_2.addWidget(
            self.btnCheckReq, 0, QtCore.Qt.AlignHCenter)
        self.outputTextEdit = QtWidgets.QTextEdit(self.outputFrame)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.verticalLayout_2.addWidget(self.outputTextEdit)
        self.verticalLayout.addWidget(self.outputFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        # disable the user from entering data into the tables
        self.newAvailTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.newAlocTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.newNeedTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # disable the user from entering data into the text edit
        self.outputTextEdit.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Results"))
        self.newAllocationLabel_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">New Current Allocation:</span></p></body></html>"))
        self.newNeededLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Remaining Need:</span></p></body></html>"))
        self.newAvaiableLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Available Resources :</span></p></body></html>"))
        self.btnCheckReq.setText(_translate("MainWindow", "Check Request"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

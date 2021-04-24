import sys

from PySide2 import QtWidgets, QtCore
from ui import MainWindow


class MainTestWindow(QtWidgets.QMainWindow):
    """
    Класс главного окна
    """
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.initUI()
    #
    #     self.ui = MainWindow.Ui_MainWindow()
    #     self.ui.setupUi(self)
    #
    #     # Подключаем к кнопке "Открыть" функционал: метод OnPushButtonOpenClicked
    #     self.ui.pushButtonOpen.clicked.connect(self.OnPushButtonOpenClicked)
    #     # Подключаем к кнопке "Применить" функционал: метод OnPushButtonAcceptClicked
    #     self.ui.pushButtonAccept.clicked.connect(self.OnPushButtonAcceptClicked)
    #
    # def OnPushButtonOpenClicked(self):
    #     file_path, ok = QtWidgets.QFileDialog.getOpenFileNames(self, "Выбор файла")
    #     if not ok:
    #         return

    #     print(file_path)
    #     print("Нажата кнопка 'Открыть'")
    #
    # def OnPushButtonAcceptClicked(self):
    #     print(self.ui.lineEdit.text())
    #     print(self.ui.lineEdit_2.text())
    #     print(self.ui.lineEdit_3.text())
    #     print(self.ui.lineEdit_4.text())

    def initUI(self):
        #centralWidget = QtWidgets.QWidget()

        layoutV = QtWidgets.QVBoxLayout()

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.textEdit_1 = QtWidgets.QTextEdit()
        self.textEdit_1.append('textEdit_1')

        textEdit_2 = QtWidgets.QTextEdit()
        textEdit_2.append('textEdit_2')

        textEdit_3 = QtWidgets.QTextEdit()
        textEdit_3.append('textEdit_3')

        splitter.addWidget(self.textEdit_1)
        splitter.addWidget(textEdit_2)
        splitter.addWidget(textEdit_3)
        #layoutV.addWidget(splitter)

        #centralWidget.setLayout(splitter)
        self.setCentralWidget(splitter)

        self.textEdit_1.installEventFilter(self)

    def eventFilter(self, watched:QtCore.QObject, event:QtCore.QEvent) -> bool:
        if watched == self.textEdit_1 and event.type() == QtCore.QEvent.Resize:
            print(self.textEdit_1.size().height())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = MainTestWindow()
    windows.show()
    app.exec_()

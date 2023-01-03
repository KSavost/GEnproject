from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import random

import sys


a = []
e = []
o = []
u = []
s = []
dict = {'e': '','s': '','i': ''','a':''','o': ''}



class Ui_Generator(object):
    def setupUi(self, Generator):
        Generator.setObjectName("Generator")
        Generator.resize(400, 325)
        Generator.setStyleSheet("background-color: rgb(255, 152, 84);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Generator)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 120, 100, 25))
        self.radioButton.setStyleSheet("\n"
"background-color: rgb(255, 152, 84);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("but1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 150, 100, 25))
        self.radioButton_2.setStyleSheet("background-color: rgb(255, 152, 84);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("but2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 180, 100, 25))
        self.radioButton_3.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 152, 84);")
        self.radioButton_3.setObjectName("but3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 50))
        self.label.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 152, 84);")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 391, 40))
        self.label_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 152, 84);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 280, 200, 25))
        self.pushButton.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("genbut")
        Generator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Generator)
        self.statusbar.setObjectName("statusbar")
        Generator.setStatusBar(self.statusbar)
        self.genbut.clicked.connect(generating())
        self.retranslateUi(Generator)
        QtCore.QMetaObject.connectSlotsByName(Generator)

    def generating(self):
        global a
        global e
        global u
        global o
        test = [2, 3, 4]
        r9 = random.choice(test)
        n9 = []
        n10 = []
        n11 = []
        n12 = []

    def r9(r9, big_arr, n9):
        arr = []
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        global bad_arr
        for i in range(r9):
            ind = random.choice(a)
            arr.append(ind)
            a.remove(ind)
            ind1 = random.randint(1, len(b))
            b.remove(ind1)
            w1 = random.randint(1, len(big_arr[ind1]))
            big_arr[ind1].remove(w1)
            w2 = random.randint(1, len(big_arr[ind1]))
            big_arr[ind1].remove(w2)
            w3 = random.randint(1, len(big_arr[ind1]))
            big_arr[ind1].remove(w3)
            n9[ind - 1] = [w1, w2, w3, sep = '\n']
            f = [i for i in range(5) if i not in arr]
            for i in a:
                ind = random.choice(a)
                arr.append(ind)
                a.remove(ind)
                ind1 = random.randint(1, len(b))
                b.remove(ind1)
                w1 = random.randint(1, len(big_arr[ind1]))
                big_arr[ind1].remove(w1)
                w2 = random.randint(1, len(big_arr[ind1]))
                big_arr[ind1].remove(w2)
                w3 = random.randint(1, len(big_arr[ind1]))
                big_arr[ind1].remove(w3)
                n9[i - 1] = [w1, w2, w3]
            return n9, big_arr

    def add_label(self):
        self.new_text.setText('Пожалуйста, подождите...')
        self.new_text.move(175, 350)
        self.new_text.adjustSize()

    def func(self):
        self.but1.clicked.connect(lambda: self.get_vars(self.but1.text()))
        self.but2.clicked.connect(lambda: self.get_vars(self.but2.text()))
        self.but3.clicked.connect(lambda: self.get_vars(self.but3.text()))
        self.genbut.clicked.connect(lambda: self.get_vars(self.genbut.text()))
        self.genbut.clicked.connect(self.generating())

    def get_vars(self, n):
        print(n)



    def retranslateUi(self, Generator):
        _translate = QtCore.QCoreApplication.translate
        Generator.setWindowTitle(_translate("Generator", "MainWindow"))
        self.radioButton.setText(_translate("Generator", "2 варианта"))
        self.radioButton_2.setText(_translate("Generator", "3 варианта"))
        self.radioButton_3.setText(_translate("Generator", "4 варианта"))
        self.label.setText(_translate("Generator", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Вас приветствует генератор задач ЕГЭ!</span></p></body></html>"))
        self.label_2.setText(_translate("Generator", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Выберите нужное количество вариантов:</span></p></body></html>"))
        self.pushButton.setText(_translate("Generator", "Сгенерировать варианты:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Generator = QtWidgets.QMainWindow()
    ui = Ui_Generator()
    ui.setupUi(Generator)
    Generator.show()
    sys.exit(app.exec_())





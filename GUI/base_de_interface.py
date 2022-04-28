import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QGridLayout
# Imports do modulo sys, da janela, da aplicação, do botão, do widget e do
# grid


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        
        self.btn = QPushButton('Texto do botão')
        # Texto do botão
        self.btn.setStyleSheet('font-size: 20px;')
        # Tamanho da fonte do botão
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        
        self.btn.clicked.connect(self.acao)
        # Ação que o botão irá executar
        
        self.setCentralWidget(self.cw)
    

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
    
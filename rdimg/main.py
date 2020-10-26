import sys
from design import *

from PyQt5.QtWidgets import QMainWindow,QApplication, QFileDialog
from PyQt5.QtGui import  QPixmap

class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.openimg)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def openimg(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'/home/calhe/Imagens',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.AbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.lblImage.setPixmap(self.original_img)
        self.inpLargura.setText(str(self.original_img.width()))
        self.inpAltura.setText(str(self.original_img.height()))



    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'/home/calhe/Imagens',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')
    def redimensionar(self):
        largura = int(self.inpLargura.text())
        self.nova_imagem = self.original_img.scaledTowidth(largura)
        self.lblImage.setPixmap(self.nova_imagem)
        self.inpLargura.setText(str(self.nova_img.width()))
        self.inpAltura.setText(str(self.nova_img.height()))






if __name__ == '__main__':
    qt = QApplication(sys.argv)
    img = Redimensionar()
    img.show()
    qt.exec_()


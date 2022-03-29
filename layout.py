#Passsos para importar o PyQt
#01. entrar na pasta Scrips no local de instalação do python
# Para fazer isso:
#02. buscar no windows por python
#03. Mouse, tecla direita abrir local do arquivo
#04. Novamente, abrir local do arquivo
#05. Abrir pasta Scrips
#06. Copiar o caminho mostrado
#07. Prompt de comando
#08. . CD . < colar o caminho >
#09. pip install pyqt5

#layout.py
#exemplos de interfaces usando py



from PyQt5.QtWidgets import*

def botao_clicado():
    alerta = QMessageBox()
    alerta.setText('Você clicou!')
    alerta.exec_()




#criar uma aplivação
app = QApplication([])

btAcima = QPushButton('Acima')
btAbaixo = QPushButton('Abaixo')

btAcima.clicked.connect(botao_clicado)
btAbaixo.clicked.connect(botao_clicado)

#define layout vertical
layout = QHBoxLayout()
layout.addWidget(btAcima)
layout.addWidget(btAbaixo)

#define uma janela gráfica
window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()

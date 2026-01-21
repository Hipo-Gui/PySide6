import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Button text')
button.setStyleSheet('font-size: 40px;')
button.show() 

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 80px;')
button2.show() 


button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 80px;')
button3.show()

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1 )
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 2, 1, 1, 2)

central_widget.show() # Central widget entre na hierarquia e mostra sua janela
app.exec() # O loop da aplicação 
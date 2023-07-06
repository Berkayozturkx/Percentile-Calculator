#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class PercentileCalculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Yüzdelik Dilim Hesaplayıcı")
        self.window_width = 400
        self.window_height = 400
        self.setGeometry(100,100,self.window_width,self.window_height)
        self.show()
    def init_ui(self):
        
        #başlık
        head = QLabel("Yüzdelik Dilim Hesaplayıcı",self)
        head.setGeometry(0, 10, 400, 60)
        
        font = QFont('Times',14)
        font.setBold(True)
        font.setItalic(True)
        
        color = QGraphicsColorizeEffect()
        color.setColor(Qt.darkBlue)
        
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        head.setGraphicsEffect(color)
        
        #genel sıralama etiketi
        firstLabel = QLabel("Genel Sıralama",self)
        firstLabel.setAlignment(Qt.AlignCenter)
        firstLabel.setGeometry(20, 100, 170, 40)
        firstLabel.setStyleSheet("QLabel"
                                     "{"
                                     "border : 2px solid black;"
                                     "background : rgba(70, 70, 70, 35);"
                                     "}")
        firstLabel.setFont(QFont('Times',9))
        
        #Genel sıralama etiketinin QLineEditi
        self.total = QLineEdit(self)
        onlyInt = QIntValidator()
        self.total.setValidator(onlyInt)
        self.total.setGeometry(200, 100, 180, 40)
        self.total.setAlignment(Qt.AlignCenter)
        self.total.setFont(QFont('Times',9))
        
        #Sıralamanız etiketi
        secondLabel = QLabel("Sıralamanız",self)
        secondLabel.setAlignment(Qt.AlignCenter)
        secondLabel.setStyleSheet("QLabel"
                                   "{"
                                   "border : 2px solid black;"
                                   "background : rgba(70, 70, 70, 35);"
                                   "}")
        secondLabel.setFont(QFont('Times',9))
        secondLabel.setGeometry(20, 150, 170, 40)
        
        #Sıralamanız etkiketinin QLineEditi
        self.rank = QLineEdit(self)
        self.rank.setValidator(onlyInt)
        self.rank.setAlignment(Qt.AlignCenter)
        self.rank.setFont(QFont('Times',9))
        self.rank.setGeometry(200, 150, 180, 40)
        
        #Hesapla butonu
        calculate = QPushButton("Hesapla",self)
        calculate.clicked.connect(self.calculator)
        calculate.setGeometry(125, 220, 150, 40)
        
        #Sonuç etiketi
        self.result = QLabel("",self)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setFont(QFont('Arial',11))
        self.result.setGeometry(50, 300, 300, 60)
        
    def calculator(self):
        total_participation = self.total.text()
        rank = self.rank.text()
        conclusion = 0
        
        if len(total_participation) == 0 or len(rank) == 0:
            return
        
        total_participation = int(total_participation)
        rank = int(rank)
        
        if total_participation == 0 or rank == 0:
            return
        else:
        
            conclusion = round(((rank*100)/total_participation),3)
        
            self.result.setStyleSheet("QLabel"
                            "{"
                            "border : 3px solid black;"
                            "background : white;"
                            "}")
            self.result.setText("Yüzdelik Dilim: " + str(conclusion))
        
app = QApplication(sys.argv)
window = PercentileCalculator()
sys.exit(app.exec_())


# In[ ]:





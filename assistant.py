from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import wikipedia
import wolframalpha
import sys
import os
import speech_recognition as sr

app=QApplication(sys.argv)
win=QMainWindow()
win.setFixedSize(700,600)
win.setWindowTitle("Professor")

###############################################

def saysomething():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio=r.listen(source)
    try:
        print("You said :"+r.recognize_google(audio))
    except:
        print("Say again.I can't get that")
        
def myaction():
    x=myline.text()
    try:
        myappid=wolframalpha.Client("3E24XL-XKWT4UPEGA")
        res=myappid.query(x)
        ans=next(res.results).text
        l1.setText(ans)
        os.system('espeak "{}"'.format(ans))
    except:
        l1.setText(wikipedia.summary(x))
        y=wikipedia.summary(x)
        os.system('espeak "{}"'.format(y))
        
###############################################

myline=QtWidgets.QLineEdit(win)
myline.setPlaceholderText('Ask Me Anything....')
myline.resize(600,25)
myline.move(30,20)

b1=QtWidgets.QPushButton(win)
b1.setText("Search")
b1.clicked.connect(saysomething)
b1.setFixedSize(60,25)
b1.move(640,20)

l1=QtWidgets.QTextEdit(win)
l1.move(30,50)
l1.setFixedSize(600,400)
os.system('espeak "HELLO SHIWAANS How Are You?"')
win.show()
sys.exit(app.exec_())

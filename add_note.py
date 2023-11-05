import io
import sys


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>add_window</class>
 <widget class="QWidget" name="add_window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>600</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>600</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Добавить</string>
  </property>
  <widget class="QPushButton" name="add_btn">
   <property name="geometry">
    <rect>
     <x>450</x>
     <y>450</y>
     <width>141</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Добавить</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="title_input">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>80</y>
     <width>300</width>
     <height>40</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
  </widget>
  <widget class="QTextEdit" name="text_input">
   <property name="geometry">
    <rect>
     <x>125</x>
     <y>180</y>
     <width>350</width>
     <height>200</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>40</y>
     <width>301</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>15</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Заголовок:</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>150</y>
     <width>341</width>
     <height>20</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>15</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Основной текст:</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="error_label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>415</y>
     <width>401</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Add(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.add_btn.clicked.connect(self.add)

    def add(self):
        error_message = ""
        if not self.title_input.text():
            error_message += "Введите заголовок!! "
        if not self.text_input.toPlainText():
            error_message += "Введите основной текст!! "
        self.error_label.setText(error_message)
        if not error_message:
            file = open('/home/linechangerr/projects/Keeps/clipboard.txt', 'w')
            file.write(f"{self.title_input.text()}\n{self.text_input.toPlainText()}")
            file.close()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Add()
    ex.show()
    sys.exit(app.exec_())
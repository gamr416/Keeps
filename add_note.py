import io
import sys
import os
import sqlite3

from PyQt5.QtCore import QDateTime
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
     <y>50</y>
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
     <x>130</x>
     <y>140</y>
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
     <y>10</y>
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
     <y>100</y>
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
     <y>435</y>
     <width>401</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QDateTimeEdit" name="date_input">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>390</y>
     <width>351</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>356</y>
     <width>341</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Дата(UTC)</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
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
        date = QDateTime(2030, 1, 1, 1, 1)
        self.date_input.setDateTime(date)
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path)
        lines = file.read().split('\n')
        self.id = lines[0]
        self.name = lines[1]
        self.email = lines[2]
        self.password = lines[3]
        self.code = 403

    def add(self):
        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()
        error_message = ""
        if not self.title_input.text():
            error_message += "Введите заголовок!! "
        if not self.text_input.toPlainText():
            error_message += "Введите основной текст!! "
        self.error_label.setText(error_message)
        if not error_message:
            time = [int(num) for num in str(self.date_input.dateTime())[23:-1].split(', ')]
            text = self.title_input.text() + '\n' + self.text_input.toPlainText()
            print(1)
            command = self.cur.execute(
                    f"""INSERT INTO {'s' + str(self.id)}(note, date, picture)
                        VALUES('{text}', '{time}', '{''}')"""
                )
            
            self.con.commit()
            self.con.close()
            self.close()
            print(2)
            


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Add()
    ex.show()
    sys.exit(app.exec_())

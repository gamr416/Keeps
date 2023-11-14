import io
import sys
import os
import sqlite3


from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsPixmapItem, QGraphicsScene

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>profile_window</class>
 <widget class="QWidget" name="profile_window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>700</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1000</width>
    <height>700</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000</width>
    <height>700</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Ваш профиль</string>
  </property>
  <widget class="QGraphicsView" name="profile_picture">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>20</y>
     <width>191</width>
     <height>171</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="commit_btn">
   <property name="geometry">
    <rect>
     <x>790</x>
     <y>610</y>
     <width>211</width>
     <height>61</height>
    </rect>
   </property>
   <property name="text">
    <string>PushButton</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_label">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>20</y>
     <width>241</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QLabel" name="email_label">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>70</y>
     <width>241</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>250</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 1</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_2">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>250</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 2</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_3">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>250</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 3</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_4">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>290</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 4</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_5">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>290</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 5</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_6">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>290</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 6</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_7">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>330</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 7</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_8">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>330</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 8</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="checkBox_9">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>330</y>
     <width>92</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Панель 9</string>
   </property>
  </widget>
  <widget class="QPushButton" name="change_picture">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>140</y>
     <width>151</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Поменять картинку</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Profile(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.change_picture.clicked.connect(self.change_pic)
        count = 0
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path)
        lines = file.read().split('\n')
        self.id = lines[0]
        self.name = lines[1]
        self.email = lines[2]
        self.password = lines[3]
        self.name_label.setText(self.name)
        self.email_label.setText(self.email)
        self.checkboxes = [
            self.checkBox,
            self.checkBox_2,
            self.checkBox_3,
            self.checkBox_4,
            self.checkBox_5,
            self.checkBox_6,
            self.checkBox_7,
            self.checkBox_8,
            self.checkBox_9,
        ]
        for elem in self.checkboxes:
            if not elem.isChecked():
                elem.setChecked(False)
                count += 1

    def change_pic(self):
        file_name = QFileDialog.getOpenFileName(
        self, 'Выбрать картинку', '',
        'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        print(file_name)
        if not file_name:
            return
        self.image_qt = QImage(file_name)

        pix = QPixmap(file_name)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        print(scene)
        self.profile_picture.setScene(scene)

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
            self.storage.add_note(time, text)
            command = self.cur.execute(
                    f"""INSERT INTO {'s' + str(self.id)}(note, date)
                        VALUES('{text}', '{time}')"""
                )
            
            self.con.commit()
            self.con.close()
            self.close()
            print(2)
            


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Profile()
    ex.show()
    sys.exit(app.exec_())

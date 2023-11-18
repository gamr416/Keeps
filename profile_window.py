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
  <widget class="QLabel" name="name_label">
   <property name="geometry">
    <rect>
     <x>430</x>
     <y>240</y>
     <width>521</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QLabel" name="email_label">
   <property name="geometry">
    <rect>
     <x>430</x>
     <y>180</y>
     <width>561</width>
     <height>61</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QPushButton" name="change_picture">
   <property name="geometry">
    <rect>
     <x>430</x>
     <y>310</y>
     <width>151</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Поменять картинку</string>
   </property>
  </widget>
  <widget class="QLabel" name="profile_picture">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>391</width>
     <height>381</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>120</pointsize>
    </font>
   </property>
   <property name="text">
    <string>👤</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="exit_btn">
   <property name="geometry">
    <rect>
     <x>760</x>
     <y>20</y>
     <width>211</width>
     <height>101</height>
    </rect>
   </property>
   <property name="text">
    <string>Выйти из аккаунта</string>
   </property>
  </widget>
  <widget class="QPushButton" name="delete_btn">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>580</y>
     <width>201</width>
     <height>111</height>
    </rect>
   </property>
   <property name="text">
    <string>Удалить аккаунт</string>
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
        self.exit_btn.clicked.connect(self.quit)
        self.delete_btn.clicked.connect(self.delete_account)
        file.close()

    def delete_account(self):
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path, 'w')
        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()

        command = self.cur.execute(f"""DROP TABLE {'s' + str(self.id)}""")
        command = self.cur.execute(f"""DELETE FROM users WHERE id = '{self.id}'""")

        self.con.commit()
        self.con.close()
        self.close()
        file.write('')
        file.close()
        exit()

    def change_pic(self):
        file_name = QFileDialog.getOpenFileName(
        self, 'Выбрать картинку', '',
        'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        if not file_name:
            return
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path, 'w')
        file.write(f'{self.id}\n{self.name}\n{self.email}\n{self.password}\n{file_name}\n')
        file.close()

        self.pixmap = QPixmap(file_name)
        self.image = self.profile_picture
        self.image.setPixmap(self.pixmap)
        print(1)
        self.pixmap = QPixmap(file_name)
        self.profile_picture.hide()
        self.image.setPixmap(self.pixmap)
        print(2)

        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()
        

    
    def quit(self):
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path, 'w')
        file.write('')
        file.close()
        exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Profile()
    ex.show()
    sys.exit(app.exec_())

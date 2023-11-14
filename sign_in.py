import io
import sys
import sqlite3
import os

from registration import Registration
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>sign_in_window</class>
 <widget class="QWidget" name="sign_in_window">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>776</width>
    <height>648</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>776</width>
    <height>648</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>776</width>
    <height>648</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Вход в Заметки</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="sign_in_btn">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>340</y>
      <width>211</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QPushButton" name="register_btn">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>430</y>
      <width>211</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Регистрация</string>
    </property>
   </widget>
   <widget class="QLabel" name="sign_in_label">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>20</y>
      <width>421</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Вы не вошли в аккаунт</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="textInteractionFlags">
     <set>Qt::TextSelectableByMouse</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="email_input">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>190</y>
      <width>221</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="password_label">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>230</y>
      <width>221</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Пароль:</string>
    </property>
   </widget>
   <widget class="QLabel" name="email_label">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>160</y>
      <width>221</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Электронная почта:</string>
    </property>
   </widget>
   <widget class="QLabel" name="error_label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>580</y>
      <width>771</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="password_input">
    <property name="geometry">
     <rect>
      <x>282</x>
      <y>274</y>
      <width>221</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class SignIn(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.sign_in_btn.clicked.connect(self.check)
        self.register_btn.clicked.connect(self.open_register_window)
        
        
        

    def check(self):
        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()
        error_message = ''
        if not self.email_input.text():
            error_message += 'Введите email!! '
        elif '@gmail.com' not in self.email_input.text():
            error_message += 'Неверный email!! '
        if not self.password_input.text():
            error_message += 'Введите пароль!! '
        #Нету в таблице
        if not error_message:
            user_data = self.cur.execute("""SELECT email FROM users""").fetchall()
            right_email = False
            if (self.email_input.text(), ) in user_data:
                    right_email = True
            if right_email:
                user_password = self.cur.execute(f"""SELECT password FROM users 
                                                    WHERE email='{self.email_input.text()}'""").fetchall()
                if self.password_input.text() == user_password[0][0]:
                    pass
                    #Открытие основного приложения
                else:
                    error_message += 'Пароль неверный!!'
            else:
                error_message += 'Аккаунта не существует!!'
        command = self.cur.execute(f"""SELECT "id" FROM "users" WHERE email="{self.email_input.text()}" """).fetchall()
        command1 = self.cur.execute(f"""SELECT "name" FROM "users" WHERE email="{self.email_input.text()}" """).fetchall()
        absolute_path = os.path.dirname(__file__)
        relative_path = 'current_user.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path, 'w')
        file.write(f'{command[0][0]}\n{command1[0][0]}\n{self.email_input.text()}\n{self.password_input.text()}')
        self.error_label.setText(error_message)
        self.con.close()
        self.close()
        file.close()
        
    def open_register_window(self):
        self.register_window = Registration()
        self.register_window.show()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignIn()
    ex.show()
    sys.exit(app.exec_())

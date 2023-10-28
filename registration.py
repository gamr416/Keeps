import io
import sys
import sqlite3


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>registration_window</class>
 <widget class="QWidget" name="registration_window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>400</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>400</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="name_label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>70</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Имя:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="name_input">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>100</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="email_label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>140</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Электронная почта:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="email_input">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>170</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="password_label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>210</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Пароль:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="password_input">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>240</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="confirm_password_label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>280</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Подтвердите пароль:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="confirm_password_input">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>310</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="register_btn">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>370</y>
     <width>180</width>
     <height>60</height>
    </rect>
   </property>
   <property name="maximumSize">
    <size>
     <width>400</width>
     <height>500</height>
    </size>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Зарегистрироваться!</string>
   </property>
  </widget>
  <widget class="QLabel" name="error_label">
   <property name="geometry">
    <rect>
     <x>6</x>
     <y>436</y>
     <width>391</width>
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
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.register_btn.clicked.connect(self.check)
        #Написан адрес для моего линукса, на винде поменять!!
        self.con = sqlite3.connect("/home/linechangerr/projects/Keeps/databases/users_db")
        self.cur = self.con.cursor()

    def check(self):
        error_message = ""
        if not self.name_input.text():
            error_message += "Введите имя!!\n"
        if not self.email_input.text():
            error_message += "Введите email!! "
        elif self.email_input.text()[-10:] != '@gmail.com':
            error_message += "Неверный email!! "
        if not self.password_input.text():
            error_message += "Введите пароль!! "
        elif self.password_input.text() and self.password_input.text() != self.confirm_password_input.text():
            error_message += "Пароли не совпадают!!"
        print(error_message)
        self.error_label.setText(error_message)
        if not error_message:
            command = self.cur.execute(
                f"""INSERT INTO users(name, email, password)
                    VALUES('{self.name_input.text()}',
                           '{self.email_input.text()}',
                           '{self.password_input.text()}')"""
            )
        self.con.commit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Registration()
    ex.show()
    sys.exit(app.exec_())

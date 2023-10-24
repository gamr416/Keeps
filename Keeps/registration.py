import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>registration_window</class>
 <widget class="QMainWindow" name="registration_window">
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
   <string>Регистрация</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="register_btn">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>360</y>
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
   <widget class="QLineEdit" name="password_input">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>239</y>
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
   <widget class="QLineEdit" name="email_input">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>169</y>
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
   <widget class="QLabel" name="name_label">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>75</y>
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
   <widget class="QLabel" name="error_label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>430</y>
      <width>391</width>
      <height>71</height>
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
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.register_btn.clicked.connect(self.check)

    def check(self):
        error_message = ''
        if not self.name_input.text():
            error_message += 'Введите имя!!\n'
        if not self.email_input.text():
            error_message += 'Введите email!! '
        elif '@gmail.com' not in self.email_input.text():
            error_message += 'Неверный email!! '
        if not self.password_input.text():
            error_message += 'Введите пароль!! '
        elif self.password_input.text() and self.password_input.text() != self.confirm_password_input.text():
            error_message += 'Пароли не совпадают!!'
        print(error_message)
        self.error_label.setText(error_message)
        if not error_message:
            pass
            #Отправка на поцту + закрытие окна




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())

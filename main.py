import io
import sys
import sqlite3
import os

from sign_in import SignIn
from add_note import Add
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1200</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1200</width>
    <height>800</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1201</width>
    <height>801</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Заметки</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="settings_btn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>30</pointsize>
     </font>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Настройки&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="text">
     <string>⚙</string>
    </property>
    <property name="flat">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>80</y>
      <width>1121</width>
      <height>641</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="2">
      <widget class="QTextBrowser" name="textBrowser_3">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(196, 177, 2);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
       <property name="html">
        <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QTextBrowser" name="textBrowser">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(160, 20, 20);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
       <property name="html">
        <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QTextBrowser" name="textBrowser_8">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(84, 18, 128);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
      </widget>
     </item>
     <item row="4" column="2">
      <widget class="QTextBrowser" name="textBrowser_9">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(128, 18, 86);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QTextBrowser" name="textBrowser_5">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(0, 145, 90);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QTextBrowser" name="textBrowser_4">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(53, 117, 16);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
       <property name="html">
        <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="2">
      <widget class="QTextBrowser" name="textBrowser_6">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(0, 102, 145);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QTextBrowser" name="textBrowser_7">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(48, 31, 143);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QTextBrowser" name="textBrowser_2">
       <property name="font">
        <font>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">QTextBrowser{background-color: rgb(200, 120, 0);
								  color: rgb(255, 255, 255)}</string>
       </property>
       <property name="markdown">
        <string/>
       </property>
       <property name="html">
        <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="profile_btn">
    <property name="geometry">
     <rect>
      <x>1130</x>
      <y>20</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>30</pointsize>
     </font>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Ваш профиль&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="text">
     <string>👤</string>
    </property>
    <property name="flat">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="email_label">
    <property name="geometry">
     <rect>
      <x>790</x>
      <y>20</y>
      <width>331</width>
      <height>20</height>
     </rect>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Ваш email&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="name_label">
    <property name="geometry">
     <rect>
      <x>830</x>
      <y>50</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Ваше имя&lt;/p&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="add_btn">
    <property name="geometry">
     <rect>
      <x>1010</x>
      <y>740</y>
      <width>181</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QLabel" name="none_label">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>400</y>
      <width>751</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>10</y>
      <width>731</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>17</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Надеюсь у вас хороший денёк!</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        absolute_path = os.path.dirname(__file__)
        relative_path = 'databases/users_db'
        full_path = os.path.join(absolute_path, relative_path)
        self.con = sqlite3.connect(full_path)
        self.cur = self.con.cursor()
        self.add_btn.clicked.connect(self.add)
        count = 0
        self.notes = [
            self.textBrowser,
            self.textBrowser_2,
            self.textBrowser_3,
            self.textBrowser_4,
            self.textBrowser_5,
            self.textBrowser_6,
            self.textBrowser_7,
            self.textBrowser_8,
            self.textBrowser_9,
        ]
        for elem in self.notes:
            if not elem.toPlainText():
                elem.hide()
                count += 1
        if count >= 9:
            self.none_label.setText('У вас пока нет заметок')

    def add(self):
        self.add_window = Add()
        self.add_window.show()
        absolute_path = os.path.dirname(__file__)
        relative_path = 'clipboard.txt'
        full_path = os.path.join(absolute_path, relative_path)
        file = open(full_path)
        lines = file.read().split('\n')
        command = self.cur.execute("""INSERT INTO 
                                   
""")
        file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    absolute_path = os.path.dirname(__file__)
    relative_path = 'current_user.txt'
    full_path = os.path.join(absolute_path, relative_path)
    file = open("/home/linechangerr/projects/Keeps/current_user.txt")
    if file.read():
        ex = Main()
    else:
        ex = SignIn()
    ex.show()
    sys.exit(app.exec_())

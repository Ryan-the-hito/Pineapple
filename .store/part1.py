#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSystemTrayIcon, QMenu, QComboBox, QDialog,
                             QDialogButtonBox, QMenuBar, QFrame, QFileDialog, QPlainTextEdit, QTabWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap, QTextCursor
import PyQt6.QtGui
import sys
import webbrowser
import os
from pathlib import Path
import re

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("pineapple.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🛡️ Add a shield!")
menu.addAction(action3)

'''action4 = QAction("⚙️ Preferences")
menu.addAction(action4)'''

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
button_action = QAction("&Let's collect!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(button_action)
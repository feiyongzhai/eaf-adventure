#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Andy Stewart
#
# Author:     Andy Stewart <lazycat.manatee@gmail.com>
# Maintainer: Andy Stewart <lazycat.manatee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QMessageBox
from core.buffer import Buffer
from core.utils import eval_in_emacs, PostGui, get_emacs_vars, interactive, message_to_emacs, get_emacs_func_result, get_emacs_config_dir, touch, get_emacs_var

class AppBuffer(Buffer):
    def __init__(self, buffer_id, url, arguments):
        Buffer.__init__(self, buffer_id, url, arguments, True)

        vwidgets = QWidget()
        vlayout = QVBoxLayout()
        b1 = QPushButton("tt")
        vlayout.addWidget(b1)
        vlayout.addWidget(QPushButton("some"))
        vwidgets.setLayout(vlayout)

        # def on_button_clicked():
        #     alert = QMessageBox()
        #     alert.setText('You clicked the button!')
        #     alert.exec_()

        def on_button_clicked():
            eval_in_emacs('browse-url', ['https://feiyongzhai.github.io/'])

        b1.clicked.connect(on_button_clicked)
        # self.add_widget(QPushButton("emacs"))
        self.add_widget(vwidgets)
        self.buffer_widget.setStyleSheet(
            "background: {}; color: {}; font-size: 100px;".format(
                self.theme_background_color,
                self.theme_foreground_color
            )
        )

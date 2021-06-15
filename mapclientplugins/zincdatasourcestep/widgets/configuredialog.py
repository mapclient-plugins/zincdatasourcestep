'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os

from PySide2.QtWidgets import QDialog, QFileDialog, QDialogButtonBox

from mapclientplugins.zincdatasourcestep.widgets.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.zincdatasourcestep.zincdatadata import ZincDataData

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, state, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        self.setState(state)
        self.validate()
        self._makeConnections()

    def _makeConnections(self):
        self._ui.dataButton.clicked.connect(self._dataButtonClicked)
        self._ui.dataLineEdit.textChanged.connect(self.validate)
        self._ui.identifierLineEdit.textChanged.connect(self.validate)

    def setState(self, state):
        self._ui.identifierLineEdit.setText(state._identifier)
        self._ui.dataLineEdit.setText(state._dataLocation)

    def getState(self):
        state = ZincDataData()
        state._identifier = self._ui.identifierLineEdit.text()
        state._dataLocation = self._ui.dataLineEdit.text()

        return state

    def validate(self):
        identifier_valid = len(self._ui.identifierLineEdit.text()) > 0
        if identifier_valid:
            self._ui.identifierLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.identifierLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        data_valid = len(self._ui.dataLineEdit.text()) > 0
        if data_valid:
            self._ui.dataLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.dataLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        valid = identifier_valid and data_valid
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

        return valid

    def _dataButtonClicked(self):
        (fileName, _) = QFileDialog.getOpenFileName(self, 'Select Zinc File', self._ui.previousLocationLabel.text())

        if fileName:
            location = os.path.basename(fileName)
            self._ui.previousLocationLabel.setText(location)
            self._ui.dataLineEdit.setText(fileName)

        self.validate()

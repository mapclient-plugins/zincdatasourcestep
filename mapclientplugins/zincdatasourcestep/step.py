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
from PySide6 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.zincdatasourcestep.widgets.configuredialog import ConfigureDialog
from mapclientplugins.zincdatasourcestep.zincdatadata import ZincDataData


class ZincDataSourceStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be used as a starting point
    for new steps.
    '''

    def __init__(self, location):
        super(ZincDataSourceStep, self).__init__('Zinc Data Source', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._icon = QtGui.QImage(':/zincdatasource/images/zinc_data_icon.png')
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#zincdata'))
        self._state = ZincDataData()

    def configure(self):
        d = ConfigureDialog(self._state, self._main_window)
        d.setModal(True)
        if d.exec_():
            self._state = d.getState()

        self._configured = d.validate()
        if self._configured and self._configuredObserver:
            self._configuredObserver()

    def getIdentifier(self):
        return self._state.identifier()

    def setIdentifier(self, identifier):
        self._state.set_identifier(identifier)

    def serialize(self):
        return self._state.serialize()

    def deserialize(self, string):
        self._state.deserialize(string)
        d = ConfigureDialog(self._state)
        self._configured = d.validate()

    def portOutput(self):
        return self._state


def getConfigFilename(identifier):
    return identifier + '.conf'

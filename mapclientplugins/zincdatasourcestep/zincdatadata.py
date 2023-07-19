"""
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
"""
import json


class ZincDataData(object):
    def __init__(self):
        self._identifier = ''
        self._dataLocation = ''

    def identifier(self):
        return self._identifier

    def set_identifier(self, identifier):
        self._identifier = identifier

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        self.__dict__.update(json.loads(string))

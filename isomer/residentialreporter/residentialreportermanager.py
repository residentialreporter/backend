#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ResidentialReporter
# ================
# Copyright (C) 2020 ResidentialReporter Community <info@residentialreporter.de> and
# others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


Module: residentialreporterManager
======================


"""

from isomer.component import ConfigurableComponent, handler
from isomer.events.system import authorized_event
from isomer.events.client import send


class residentialreporterevent(authorized_event):
    pass


class residentialreporterManager(ConfigurableComponent):
    """
    """

    configprops = {
        'some_bool_field': {
            'type': 'boolean',
            'title': 'Some bool field',
            'description': 'Sample Field for boolean configuration values',
            'default': True
        }
    }

    channel = 'isomer-web'

    def __init__(self, *args, **kwargs):
        """
        Initialize the residentialreporter Manager component.

        :param args:
        """

        super(residentialreporterManager, self).__init__(
            "ResidentialReporterMANAGER",
            *args, **kwargs
        )

        self.log("Started")

    @handler(residentialreporterevent)
    def residentialreporterevent(self, event):
        """Handler for sample event"""

        packet = {
            'component': 'isomer.residentialreporter.residentialreportermanager',
            'action': 'residentialreporterevent',
            'data': {
                'text': 'Hello World!'
            }
        }

        self.fireEvent(send(event.client.uuid, packet))

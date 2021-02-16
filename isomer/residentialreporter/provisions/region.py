#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ResidentialReporter
# =======
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

from isomer.logger import isolog as log

from isomer.misc.std import std_now, std_uuid

regions = []


def provision_regions(items, database_name, overwrite=False,
                        clear=False, skip_user_check=False):

    from isomer.provisions.base import provisionList
    from isomer.database import objectmodels

    provisionList(regions, 'region',
                  overwrite, clear, skip_user_check)

    log('Provisioning: regions: Done.', emitter='PROVISIONS')


provision = {
    'data': regions,
    'method': provision_regions
}

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

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""
Schema: region
==============

Contains
--------

region: combines groups of moderators with region-local locations and other meta data


"""

from isomer.schemata.base import base_object, uuid_object, geo_coordinate

regionSchema = base_object(
    "region",
    no_additional=False,
    no_color=True,
    roles_write=["region-admin, admin"],
    roles_create=["admin"],
    roles_read=["public"],
    roles_list=["public"]
)

regionSchema["properties"].update(
    {
        "title": {"type": "string", "roles": {"write": "admin"}},
        "description": {"type": "string"},
        "zoom": {"type": "integer", "max": 16, "min": 5},
        "coordinate": geo_coordinate(),
        "moderators": {
            "type": "array",
            "items": uuid_object("user"),
            "roles": {"read": ["region-admin", "admin"]}
        },
        "active": {"type": "boolean", "roles": {"write": "admin"}},
        "hide": {"type": "boolean", "roles": {"write": "admin"}},
        "hide_message": {"type": "string", "roles": {"write": "admin"}},
        "slug": {"type": "string", "roles": {"write": "admin"}},
        "slug_aliases": {"type": "string", "roles": {"write": "admin"}},
        "created": {
            "type": "string",
            "roles": {"write": "admin"}
        },
        "updated": {"type": "string"},
    }
)

regionSchema["history"] = True

regionForm = [
    {
        "key": "title"
    },
    {
        "type": "flex", "flex-flow": "row wrap",
        "items": [
            {"key": "created", "type": "date", "readonly": True},
            {"key": "updated", "type": "date", "readonly": True},
        ]
    },
    {
        "type": "section",
        "title": "Notes",
        "expandable": True,
        "expanded": True,
        "items": [{"key": "description", "type": "textarea", "notitle": True}]
    }
]

region = {"schema": regionSchema, "form": regionForm}

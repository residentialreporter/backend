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
Schema: location
================

Contains
--------

location: basic data structure to capture vacancies.


"""

from isomer.schemata.base import base_object, uuid_object, geo_coordinate

locationSchema = base_object(
    "location",
    no_additional=False,
    no_color=True,
    roles_create=["user"],
    roles_write=["owner", "region-admin", "admin", "moderator"],
)

locationSchema["properties"].update(
    {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "degree": {"type": "string"},
        "since": {"type": "string"},
        "buildingType": {"type": "string"},
        "reporter": {"type": "string", "roles": "moderator"},
        "address": {
            "type": "object",
            "properties": {
                "street_1": {"type": "string"},
                "street_2": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "zip_code": {"type": "string"}
            }
        },
        "coordinate": geo_coordinate(),
        "region": uuid_object("region"),
        "type": {
            "type": "string",
            "enum": ["repossession", "vacant", "defect", "other"]
        },
        "active": {"type": "boolean", "roles": {"write": "moderator"}, "default": False},
        "demolished": {"type": "boolean", "default": False},
        "demolish_rumor": {"type": "boolean", "default": False},
        "slug": {"type": "string", "roles": {"write": "moderator"}, "default": ""},
        "slug_aliases": {"type": "string", "roles": {"write": "moderator"}, "default": ""},
        "created": {
            "type": "string",
            "roles": {"write": "moderator"},
        },
        "updated": {"type": "string"},
    }
)
locationSchema["history"] = True

locationForm = [
    {"type": "flex", "flex-flow": "row wrap", "items": ["title", "type"]},
    {"key": "address.street_1", "title": "Address", "placeholder": "Street"},
    {"key": "address.street_2", "notitle": True},
    {
        "type": "div",
        "display": "flex",
        "flex-direction": "row",
        "items": [
            {
                "key": "address.city", "flex": "3 3 150px",
                "notitle": True, "placeholder": "City"
            },
            {
                "key": "address.state", "flex": "1 1 50px",
                "notitle": True, "placeholder": "State"
            },
            {
                "key": "address.zip_code", "flex": "2 2 100px",
                "notitle": True, "placeholder": "Zip Code"
            }
        ]
    },
    {
        "type": "flex", "flex-flow": "row wrap",
        "items": [
            {"key": "emptySince", "type": "date"},
            {"key": "created", "type": "date", "readonly": True},
            {"key": "updated", "type": "date", "readonly": True}
        ]
    },
    {
        "type": "section",
        "title": "Description",
        "expandable": True,
        "expanded": True,
        "items": [{"key": "description", "type": "textarea", "notitle": True}]
    }
]

locationSpecials = {"moderated": ["admin", "region-admin", "moderator", "owner"]}

location = {
    "schema": locationSchema,
    "form": locationForm,
    "specials": locationSpecials,
}

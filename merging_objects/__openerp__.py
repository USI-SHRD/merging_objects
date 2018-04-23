# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Merging Objects",
    "version": "1.0",
    "category": "Tools",
    "description": """
Merge objects:
==============

This Module will give you the possibility to merge 2 or more objects together:
------------------------------------------------------------------------------

Example:
--------

    * IF you want to merge 2 or more products, select the Product to merge, and select which one to keep.
    * All SO, PO, Pickings, etc. of selected records will be add to the one that you keep.

Version 1.0:
------------

    * Merge the linked attatchments, mails, etc.
    * Migrate to 10.0
""",
    "author": "Judy Zhang, Jeff Wang",
    "website": "http://www.gooderp.org/",
    "contributors": "Judy Zhang <judy@osbzr.com>, Jeff Wang <jeff@osbzr.com>, Mathieu Vatel <mathieu@julius.fr>",
    "depends": [
                "base",
                ],
    "data": [
             "wizard/merging_objects_view.xml",
             "views/res_config_view.xml",
             ],
    "demo": [],
    "installable": True,
    "active": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

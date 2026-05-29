# -*- coding: utf-8 -*-
###############################################################################
#
#    Pixelwave Software
#
#    Copyright (C) 2026-TODAY Pixelwave Infotech(<https://www.pixelwaveinfotech.com>)
#    Author: Milan Hirani(pixelwaveinfotech@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
###############################################################################
{
    'name': 'Custom Changes',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': '',
    'description': """
    """,
    "author": "Pixelwave Infotech",
    "website": "https://pixelwaveinfotech.com",
    'depends': ['base', 'base_vat', 'contacts'],
    'data': [
        "security/security.xml",
        "data/res_partner_data.xml",
        "views/res_partner_views.xml",
        "views/project_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'currency': 'USD',
}

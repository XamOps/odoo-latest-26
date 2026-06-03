# -*- coding: utf-8 -*-
###############################################################################
#
#    Pixelwave Infotech
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
    'name': 'Currency Format (K/M/B)',
    'version': '19.0.1.0.0',
    'category': 'CRM',
    'summary': 'Format large currency numbers as K, M, B across all views',
    'description': 'Displays currency amounts in abbreviated format: 4,000 → $4K, 1,200,000 → $1.2M, 1,000,000,000 → $1B',
    "author": "Pixelwave Infotech",
    "website": "https://pixelwaveinfotech.com",
    'depends': ['crm', 'web'],
    'assets': {
        'web.assets_backend': [
            'pixel_currency_format/static/src/js/currency_format.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

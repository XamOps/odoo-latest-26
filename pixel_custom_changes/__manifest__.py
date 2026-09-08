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
    'name': 'Custom Changes',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': '',
    'description': """ Custom Changes
    """,
    "author": "Pixelwave Infotech",
    "website": "https://pixelwaveinfotech.com",
    'depends': ['base', 'base_vat', 'contacts', 'crm', 'hr_payroll', 'l10n_in_hr_payroll'],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/res_partner_data.xml",
        "views/res_partner_views.xml",
        "views/project_views.xml",
        # "views/crm_lead_views.xml",
        "views/res_config_settings_views.xml",
        'views/hr_employee_views.xml',
        'views/hr_version_view.xml',
        'views/hr_leave_view.xml',
        'views/hr_payslip_view.xml',
        'report/custom_payslip_report.xml',
        'report/custom_payslip_action.xml',
        "wizard/give_access_wizard_view.xml",
    ],
    'assets': {
        'web.assets_backend': [
            # 'pixel_custom_changes/static/src/**/*',
            'pixel_custom_changes/static/src/js/hr_payslip_list_controller.js',
            'pixel_custom_changes/static/src/js/payslip_batch.js',
            'pixel_custom_changes/static/src/xml/hr_payslip_list_controller.xml',
            'pixel_custom_changes/static/src/xml/payslip_batch.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'currency': 'USD',
}

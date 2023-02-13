# Copyright 2023 Therp (http://therp.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ip_whitelist = fields.Char(
        string="IP Whitelist", config_parameter="auth_pass_ip_restriction.ip_whitelist", default="127.0.0.1"
    )

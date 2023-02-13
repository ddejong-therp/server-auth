from odoo import models
from odoo.exceptions import AccessDenied
from odoo.http import request


class ResUsers(models.Model):
    _inherit = "res.users"

    def _check_credentials(self, password, env):
        ip = request.httprequest.environ["REMOTE_ADDR"]
        ip_whitelist = self.env["ir.config_parameter"].get_param(
            "auth_restriction.ip_whitelist"
        )
        if not ip in ip_whitelist:
            raise AccessDenied("IP %s not allowed to authenticate with a password" % ip)
        return super()._check_credentials(password, env)

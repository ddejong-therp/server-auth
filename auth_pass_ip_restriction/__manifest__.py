# Copyright 2023 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Password Authentication IP Restriction",
    "version": "14.0.1.0.0",
    "summary": "Restricts authentication by password to a whitelist of IPs",
    "author": "Sunflower IT",
    "website": "http://sunflowerweb.nl/",
    "category": "Uncategorized",
    "sequence": 0,
    "depends": [
        "auth_signup",
        "web",
    ],
    "data": [
        "views/settings.xml",
        "views/webclient_templates.xml",
    ],
    "application": False,
    "installable": True,
}

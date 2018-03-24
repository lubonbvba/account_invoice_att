# -*- coding: utf-8 -*-

from openerp import models, fields, api
import pdb


class res_company(models.Model):
    _inherit = 'res.company'
    default_attachments=fields.Many2many('ir.attachment')
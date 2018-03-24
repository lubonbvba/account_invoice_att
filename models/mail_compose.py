# -*- coding: utf-8 -*-

from openerp import models, fields, api
import pdb



class mail_compose_message(models.Model):
    _inherit = 'mail.compose.message'

    @api.model
    def get_mail_values(self, wizard, res_ids):
        context = self._context
        #pdb.set_trace()
        if context.get('active_model') == 'account.invoice':
            company=self.env['account.invoice'].browse(context['active_id']).company_id
            for att in company.default_attachments:
                wizard.attachment_ids=[(4,att.id)]
            #pdb.set_trace()
        return super(mail_compose_message, self).get_mail_values(wizard,res_ids)    



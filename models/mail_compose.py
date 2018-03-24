# -*- coding: utf-8 -*-

from openerp import models, fields, api
import pdb



class mail_compose_message(models.Model):
    _inherit = 'mail.compose.message'

    @api.multi
    def zzzsend_mail(self):
        context = self._context
        if context.get('default_model') == 'account.invoice' and \
                context.get('default_res_id') and context.get('mark_invoice_as_sent'):
 #           invoice = self.env['account.invoice'].browse(context['default_res_id'])
 #           invoice = invoice.with_context(mail_post_autofollow=True)
 #           invoice.write({'sent': True})
 #           invoice.message_post(body=_("Invoice sent"))
            company=self.env['account.invoice'].browse(context['default_res_id']).company_id
            for att in company.default_attachments:
                self.attachment_ids=[(4,att.id)]
        return super(mail_compose_message, self).send_mail()	

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



from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    name = fields.Char('Order Reference', required=True, index=True, copy=False, default='Nuevo')

from odoo import api, exceptions, fields, models, _
from odoo.tools.float_utils import float_round, float_is_zero

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    material = fields.Many2one('material.product', string='Material')
    designer = fields.Many2one('designer.product', string='Diseñador')
    measures = fields.Char('Medidas (cm)')
    
class MaterialProduct(models.Model):
    _name = 'material.product'
    
    name = fields.Char(string='Nombre')

class DesignerProduct(models.Model):
    _name = 'designer.product'
    
    name = fields.Char(string='Nombre')
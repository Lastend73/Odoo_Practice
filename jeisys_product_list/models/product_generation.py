from odoo import api, fields, models, _
import json

from odoo.exceptions import ValidationError

class product_generation(models.Model):
    _name = 'product.generation'
    _description = "Product D"
    _rec_name = 'Product_Generation' #소제목 변경
    _parent_store = True
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Many2one("product.line", string="Product Line", required="True") 
    Product_Model= fields.Many2one("product.model", string="Product Model", required="True") 
    Product_Generation= fields.Char(string="Product Generation", required="True")
    parent_path = fields.Char(index=True)
    parent_id = fields.Many2one('product.generation', string='Parent class')
    # child_ids = fields.One2many('product.Generation', 'parent_id', string='Child lines')

    Product_Model_id = fields.Many2one("product.model", string='Model Product_Line')

    @api.onchange('Product_Generation')
    def option_check(self):
        type_check =self.search_count([('Product_Class','=',self.Product_Class.id),('Product_Line','=',self.Product_Line.id),('Product_Model','=',self.Product_Model.id),('Product_Generation','=',self.Product_Generation)])
        if bool(type_check) == True:
            self.Product_Generation=""
            raise ValidationError(_("type must be unique"))
    
   

   


from odoo import api, fields, models, _
import json

from odoo.exceptions import ValidationError

class product_line(models.Model):
    _name = 'product.line'
    _description = "Product Line"
    _rec_name = 'Product_Line' #소제목 변경
    _parent_store = True
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Char(string="Product Line", required="True")

    parent_id = fields.Many2one('product.line', string='Parent class')
    child_ids = fields.One2many('product.model', 'Product_Line_id', string='Child lines')
    parent_path = fields.Char(index=True)
    Product_Class_id = fields.Many2one("product.class", string='Model product.class')
     
    @api.onchange('Product_Line')
    def option_check(self):
        type_check =self.search_count([('Product_Class','=',self.Product_Class.id),('Product_Line','=',self.Product_Line)])
        if bool(type_check) == True:
            self.Product_Line=""
            raise ValidationError(_("type must be unique"))
    
   
   

   


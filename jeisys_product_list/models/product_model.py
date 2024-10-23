from odoo import api, fields, models, _
import json
from odoo.exceptions import ValidationError

class product_model(models.Model):
    _name = 'product.model'
    _description = "Product Model"
    _rec_name = 'Product_Model' #소제목 변경
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Many2one("product.line", string="Product Line", required="True") 
    Product_Model= fields.Char(string="Product Model", required="True")
    
    @api.onchange('Product_Model')
    def option_check(self):
        type_check =self.search_count([('Product_Class','=',self.Product_Class.id),('Product_Line','=',self.Product_Line.id),('Product_Model','=',self.Product_Model)])
        if bool(type_check) == True:
            self.Product_Model=""
            raise ValidationError(_("type must be unique"))
    
   

   


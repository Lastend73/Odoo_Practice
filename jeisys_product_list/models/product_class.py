from odoo import api, fields, models, _
import json

from odoo.exceptions import ValidationError

class product_class(models.Model):
    _name = 'product.class'
    _description = "Product Class"
    _rec_name = 'Product_Class' #소제목 변경
    
    Product_Class = fields.Char(string="Product Class", required="True") 

    @api.onchange('Product_Class')
    def option_check(self):
        type_check =self.search_count([('Product_Class','=',self.Product_Class)])
        if bool(type_check) == True:
            self.Product_Class=""
            raise ValidationError(_("type must be unique"))
    
   




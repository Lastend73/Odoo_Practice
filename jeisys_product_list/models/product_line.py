from odoo import api, fields, models, _
import json

from odoo import http
from odoo.http import request

class product_line(models.Model):
    _name = 'product.line'
    _description = "Product Line"
    _rec_name = 'Product_Line' #소제목 변경
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Char(string="Product Line", required="True")
     
    
   

   


from odoo import api, fields, models, _
import json

from odoo import http
from odoo.http import request

class product_generation(models.Model):
    _name = 'product.generation'
    _description = "Product D"
    _rec_name = 'Product_Generation' #소제목 변경
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Many2one("product.line", string="Product Line", required="True") 
    Product_Model= fields.Many2one("product.model", string="Product Model", required="True") 
    Product_Generation= fields.Char(string="Product Generation", required="True")
    
   

   


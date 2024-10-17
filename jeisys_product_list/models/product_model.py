from odoo import api, fields, models, _
import json

from odoo import http
from odoo.http import request

class product_model(models.Model):
    _name = 'product.model'
    _description = "Product Model"
    _rec_name = 'Product_Model' #소제목 변경
    
    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Many2one("product.line", string="Product Line", required="True") 
    Product_Model= fields.Char(string="Product Model", required="True")
    
   

   


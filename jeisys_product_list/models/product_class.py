from odoo import api, fields, models, _
import json

from odoo import http
from odoo.http import request

class product_class(models.Model):
    _name = 'product.class'
    _description = "Product Class"
    _rec_name = 'Product_Class' #소제목 변경
    
    Product_Class = fields.Char(string="Product Class", required="True") 
     
    
   

   


from odoo import api, fields, models, _

from odoo.exceptions import ValidationError

class product_line(models.Model):
    _name = 'product.import'
    _description = "Product Line"

    
    Product_Title = fields.Char( string="Title", required="True") 
    Product_File_Name = fields.Char("Name")
    Product_File = fields.Binary(string="File", required="True")
    
    
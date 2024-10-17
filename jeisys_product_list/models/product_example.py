from odoo import api, fields, models, _

class product_example(models.Model):
    _name = 'product.example'
    _description = "Product example"
    #_rec_name = 'Product_Class' #소제목 변경
    
    Product_Type = fields.Selection([('Class','Product Class'),('Line','Product Line'),('Model','Product Model'),('Generation','Product Generation'),('Components','Product Components')], group_expand='_expand_groups', string="Product Type", required="True") 
    Product_Type_Title = fields.Char(string="Title", required="True")
     
    @api.model
    def _expand_groups(self, states, domain, order):
        return ['Class','Line','Model','Generation','Components']
   

   


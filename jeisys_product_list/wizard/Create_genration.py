from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Create_Generation(models.TransientModel ):
    _name = 'create.product.generation'
    _description = "Create Product Generation"

    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Many2one("product.line", string="Product Line", domain="[('Product_Class','=',Product_Class)]", required="True") 
    Product_Model= fields.Many2one("product.model", string="Product Model", required="True") 
    Product_Generation= fields.Char(string="Product Generation", required="True")

    def Create_generation_option(self):

        self.env["product.generation"].create({'Product_Class':self.Product_Class.id,'Product_Line':self.Product_Line.id,'Product_Model':self.Product_Model.id,'Product_Generation':self.Product_Generation})

        add_data_id = self.env["product.generation"].search([("Product_Line", "=", self.Product_Line.id),("Product_Class","=",self.Product_Class.id),("Product_Model","=",self.Product_Model.id),("Product_Generation","=",self.Product_Generation)]).id
        
        context= self.env.context

        user_data_id = context.get('user_data_id')
        record = self.env['product.main'].browse(user_data_id)
        
        record.Product_Class = self.Product_Class.id
        record.Product_Line = self.Product_Line.id
        record.Product_Model = self.Product_Model.id
        record.Product_Generation = add_data_id

        self.search([]).unlink()
    
    # #중복체크(duplicate check)
    # @api.onchange('equipment_option')
    # def option_check(self):
    #     type_check =self.env["qr.option"].search_count([('equipment_type','=',self.equipment_type),('equipment_option','=',self.equipment_option)])
    #     if bool(type_check) == True:
    #          raise ValidationError(_("type must be unique"))
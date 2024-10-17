from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Create_Line(models.TransientModel ):
    _name = 'create.product.line'
    _description = "Create Product line"

    Product_Class = fields.Many2one("product.class", string="Product Class", required="True") 
    Product_Line = fields.Char(string="Product Line", required="True")

    def Create_line_option(self):

        self.env["product.line"].create({'Product_Class':self.Product_Class.id,'Product_Line':self.Product_Line})

        add_data_id = self.env["product.line"].search([("Product_Line", "=", self.Product_Line),("Product_Class","=",self.Product_Class.id)]).id
        
        context= self.env.context

        user_data_id = context.get('user_data_id')
        record = self.env['product.main'].browse(user_data_id)
        
        record.Product_Class = self.Product_Class.id
        record.Product_Line = add_data_id

        self.search([]).unlink()

        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload'
        # }
    
    # #중복체크(duplicate check)
    # @api.onchange('equipment_option')
    # def option_check(self):
    #     type_check =self.env["qr.option"].search_count([('equipment_type','=',self.equipment_type),('equipment_option','=',self.equipment_option)])
    #     if bool(type_check) == True:
    #          raise ValidationError(_("type must be unique"))
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Create_class(models.TransientModel ):
    _name = 'create.product.class'
    _description = "Create Product Class"

    Product_Class = fields.Char(string="Product Class", required="True") 

    def Create_class_option(self):
        self.env["product.class"].create({'Product_Class':self.Product_Class})

        context= self.env.context
        user_data_id = context.get('user_data_id')
        record = self.env['product.main'].browse(user_data_id)
        record.Product_Class = self.Product_Class

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
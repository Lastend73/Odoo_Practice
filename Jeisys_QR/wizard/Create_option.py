from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CreateQrOption(models.TransientModel ):
    _name = 'create.qr.option'
    _description = "Create QR Code Option"

    equipment_type = fields.Selection([('DENSITY','DENSITY'),('POTENZA','POTENZA'),('LinearZ','LinearZ'),],required=True) # 장비 목록
    equipment_option = fields.Char(String="Options") # 장비 옵션    

    def Create_Equipment_option(self):
        self.env["qr.option"].create({'equipment_type':self.equipment_type,'equipment_option':self.equipment_option})
        self.search([]).unlink()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }
    
    #중복체크(duplicate check)
    @api.onchange('equipment_option')
    def option_check(self):
        type_check =self.env["qr.option"].search_count([('equipment_type','=',self.equipment_type),('equipment_option','=',self.equipment_option)])
        if bool(type_check) == True:
             raise ValidationError(_("type must be unique"))
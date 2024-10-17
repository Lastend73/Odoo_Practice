from odoo import api, fields, models,_

from odoo.exceptions import ValidationError

class QrOption(models.Model):
    _name = 'qr.option'
    _description = "QR Code Option"
    _rec_name = 'equipment_option' #소제목 변경

    equipment_type = fields.Selection([('DENSITY','DENSITY'),('POTENZA','POTENZA'),('LinearZ','LinearZ'),],required=True, default="DENSITY") # 장비 목록
    equipment_option = fields.Char(String="Options",required=True) # 장비 옵션    
    

    #중복체크(duplicate check)
    @api.onchange('equipment_option','equipment_type')
    def option_check(self):
        type_check =self.search_count([('equipment_type','=',self.equipment_type),('equipment_option','=',self.equipment_option)])
        print("type_check",type_check)
        print(bool(type_check ))
        if bool(type_check) == True:
            self.equipment_option=""
            raise ValidationError(_("type must be unique"))
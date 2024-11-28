from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class inventory_manage(models.Model):
    _name = 'inventory.management'
    _description = "List of inventory data"
    
    team_name = fields.Char(string = "Team", required="True") # 장비명
    equipment_name = fields.Char(string = "Equipment", required="True") # 장비명
    model_name = fields.Char(string = "Model Name", required="True") # 모델명
    buy_date = fields.Date(string = "Buy date") # 구매일자
    control_manager = fields.Many2one('res.users',string = "Manager") # 관리자
    check_date = fields.Date(string='Check Date') # 확인 일자


    

    

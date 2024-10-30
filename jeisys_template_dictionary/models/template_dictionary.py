from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class template_dic(models.Model):
    _name = 'template.dictionary'
    _description = "List of template to import data"
    _rec_name = 'Action_id' #소제목 변경
    

    title = fields.Char(string = "Title", required="True") # 영상 제목

    Action_id = fields.Many2one("ir.actions.actions", string = "Action Id")
    file_template = fields.Many2many('ir.attachment', string='test')

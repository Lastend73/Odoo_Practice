from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class template_dic(models.Model):
    _name = 'template.dictionary'
    _description = "List of template to import data"
    
    title = fields.Char(string = "Title", required="True") # 영상 제목

    file_template_title = fields.Char(string="binary_file_name", attachment=True)    
    file_template = fields.Binary(string='File')

    

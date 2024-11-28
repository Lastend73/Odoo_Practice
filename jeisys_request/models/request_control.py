from odoo import api, fields, models

from odoo.addons.web_editor.tools import get_video_embed_code

class Request_control(models.Model): #db
    _name = 'request.control' # 테이블 이름
    _description = 'Jeisys Request Control' # 설명
    
    request_code = fields.Char(string='Request Code',required=True, readonly=True, copy=False,)
    name = fields.Char(string = 'name')
    
    @api.model
    def create(self, vals):
        vals['request_code'] = self.env['ir.sequence'].next_by_code('jeisys.request')
        return super(Request_control, self).create(vals)  

   
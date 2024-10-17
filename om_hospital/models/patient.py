from odoo import api, fields, models

from odoo.addons.web_editor.tools import get_video_embed_code

class HostpitalPatient(models.Model): #db
    _name = 'hostpital.patient' # 테이블 이름
    _description = 'Test fiiiidfdf' # 설명
    _inherit = 'mail.thread'

    name = fields.Char(string='Test name', required = True, tracking=True)
    age = fields.Integer(string = "Test age", tracking=True)
    is_child = fields.Boolean(string="is child ?", tracking=True)
    notes = fields.Text(string="noote")
    gender = fields.Selection([('Male','male'),('Female','female'),('others','Others'),], tracking=True)

    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')
    embed_code = fields.Html(compute="_compute_embed_code", sanitize=False)

    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url) or False
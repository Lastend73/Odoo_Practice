from odoo import api, fields, models, _
from odoo.addons.web_editor.tools import get_video_embed_code
import json

from io import BytesIO
import qrcode
import base64

from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

from odoo.exceptions import ValidationError

class QRLIST(models.Model):
    _name = 'qr.list'
    _description = "QR Code list"
    _rec_name = 'Title' #소제목 변경

    Title = fields.Char(string="Title", required="True") # 영상 제목
    Qr_type = fields.Selection([('Odoo','Odoo'),('Naver','Naver'),], default="Odoo") #QR타입[네이버,자체]
    Equipment_type = fields.Selection([('DENSITY','DENSITY'),('POTENZA','POTENZA'),('LinearZ','LinearZ'),], default="DENSITY") # 장비 종류
    Useage_id = fields.Many2one("qr.option","Equipment Option", domain="[('equipment_type','=',Equipment_type)]") #사용 부위
    video_link = fields.Char(string= 'Video URL')
    embed_code = fields.Html(string = 'Video', compute="_compute_embed_code", sanitize=False) # 화면 출력용
    country = fields.Selection([('Korea','한국'),('USA','USA'),('Japen','日本')] , default="Korea")

    Naver_Qr_Link = fields.Char(string = 'Naver QR Link') #네이버 QR링크
    Naver_QR_img = fields.Image(string = "Naver QR Img")   #네이버 QR이미지 

    Odoo_Qr_key = fields.Char(string="Unique Key") #Key
    Odoo_Qr_img_binary = fields.Binary('Odoo QR Code', compute='_compute_qr_code')
    Odoo_Qr_Link = fields.Char(string = 'Odoo Qr Link', readonly=True) #Odoo QR링크

    # _sql_constraints = [
    #     ('unique_Odoo_Qr_key', 'unique (Odoo_Qr_key)', 'Key must be unique')
    # ]

    @api.onchange('Odoo_Qr_key')
    def key_check(self):
        key_check =self.search_count([('Odoo_Qr_key','=',self.Odoo_Qr_key)])
        print("key_check :",key_check)
        if key_check > 0:
             raise ValidationError(_("key must be unique"))
        
    # 비디오 출력용
    @api.onchange('video_link')
    def _compute_embed_code(self):
        for rec in self:
            print("test")
            rec.embed_code = get_video_embed_code(rec.video_link) or ""

    @api.onchange('Equipment_type')
    def onchange_Equipment(self):
            self.Useage_id =""

    @api.onchange('Odoo_Qr_key')
    def _compute_qr_code(self):
        #domain_name=self.env['ir.config_parameter'].sudo().get_param('web.base.url') 도메인 가져오기
        domain_name = request.httprequest.headers.get('Host')
        for record in self:
            if record.Odoo_Qr_key:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                link_data = domain_name+"/qr?key="+record.Odoo_Qr_key
                qr.add_data(link_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # 이미지를 바이너리 데이터로 변환하여 저장
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                record.Odoo_Qr_Link = link_data
                record.Odoo_Qr_img_binary = qr_image
            else:
                record.Odoo_Qr_img_binary = False

    def open_qr_option(self):
         return {
                "name":"Create Equpimnet option",
                "type" : "ir.actions.act_window",
                "res_model" : "create.qr.option",
                "view_mode" : "form",
                "target" : "new", #popup 하려면 필요한 옵션(?)
                "context" : {'default_equipment_type':self.Equipment_type}
         }
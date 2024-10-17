from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class QRCode_link(http.Controller):
    @http.route('/qr', type='http', auth='public', website=True)
    def qr_link(self, **kw):
        print("접속했어여")
        test = request.httprequest.headers.get('Host')
        print("test :",test)
        key = kw.get('key')
        print(key)

        # env 속성 추가
        self.env = request.env

        my_model = self.env['qr.list'].sudo()
        records = my_model.search([('Odoo_Qr_key', '=', key)])

        # 첫 번째 레코드의 value 값 출력
        if records:
            value = records[0].video_link
            print("url:", value)
            return redirect(value)
        else:
            print("레코드를 찾을 수 없습니다.")
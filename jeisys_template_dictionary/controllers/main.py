import base64
import io

from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

import json

class template_download(http.Controller):
    @http.route('/tmsdownload/binary', type='http', auth='public', methods=['POST'], website=True)
    def template_download(self, **kw):
        # print(templatename)
        print("aaaaa")
        name = kw.get('filename', False)
        email = kw.get('decoded_data', False)

        print(name)
        print(email)
        return "a"
        # self.env = request.env
        # print("a")
        # print(request.env.context)
        # file_name = kw.get('file_name')
        # binary_data = kw.get('decoded_data')
        
        # decoded_data = base64.b64decode(binary_data)

        # byte_stream = io.BytesIO(decoded_data)

        # # 5. 파일 이름 설정 (필요에 따라 변경)
        # return http.send_file(byte_stream, filename=file_name, as_attachment=True)
        

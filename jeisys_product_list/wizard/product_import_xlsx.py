from odoo import api, fields, models, _

import tempfile
import binascii
import xlrd
from odoo.exceptions import ValidationError

from odoo.http import request
from odoo import http
import base64
import io
import pprint

import requests
import json

class Create_class(models.TransientModel):
    _name = 'product.import.wiz'
    _description = "import product xlsx"

    file_directfield = fields.Many2one('template.dictionary') 
    file_template = fields.Binary( string="Template File", related='file_directfield.file_template') 
    file_title = fields.Char(string='File Title', related ='file_directfield.file_template_title')

    import_file = fields.Binary("Import File")
    file_name = fields.Char("File name")


    @api.model
    def default_get(self, fields):
        res = super(Create_class, self).default_get(fields)
        try :
            compare_action_id = self.env['template.dictionary'].sudo().search(["|",('title', '=', "제품 체계도"),('title', 'ilike', "Jeisys Product List")]).id
            print(compare_action_id)
            res['file_directfield'] = compare_action_id
            return res
        except : 
            raise ValidationError(_("오류 발생"))
                
    # Excel Download
    def download_template(self):
        filename = self.file_title
        decoded_data = base64.b64decode(self.file_template)

        encoded_data = base64.b64encode(decoded_data).decode('utf-8') 

        url = 'http://localhost:8072/tmsdownload/binary'
        headers = {'Content-Type': 'application/json'}
        data = {
            "params": {
                "filename": filename,
                "decoded_data": "제품 체계도" 
            }
        }
        data_json = json.dumps(data)
        print(data_json)
        try:
            r = requests.post(url=url, data=data_json, headers=headers)
            r.raise_for_status()  # HTTP 에러 발생 시 예외 발생

            print("요청 URL:", r.url)
            print("요청 헤더:", r.request.headers)
            print("요청 본문:", r.request.body)
            print("응답 상태 코드:", r.status_code)
            print("응답 헤더:", r.headers)
            print("응답 본문:", r.text)

        except requests.exceptions.RequestException as e:
            print("요청 에러:", e)
        # return {
        # 'type': 'ir.actions.act_url',
        # 'url': f'tmsdownload/binary?file_name={filename}&decoded_data={self.file_template}',  # 이동하려는 URL
        # 'target': 'new',  # 새 창에서 열기
        # }   
            
    #Excel Import
    def product_input_excel(self):
        try :
            if not '.xls' in self.file_name[-5:]:
                raise ValidationError("엑셀 파일을 올려주세요")
            fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xls")
            fp.write(binascii.a2b_base64(self.import_file))
            fp.seek(0)

            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)

            if sheet.ncols == 0:
                return
            
            #sheet.cell_value(row, col)
            first_row = [sheet.cell_value(3, col) for col in range(1,7)]

            import_lines = []
            print(sheet.nrows)
            for row in range(4, sheet.nrows):
                line = {}
                for col in range(1,7):
                    line[first_row[col-1]] = sheet.cell_value(row, col)
                
                if (line["제품 용도"] == "") or (line["제품군"] == "") or (line["제품 모델"] == "")  :
                    raise ValidationError("양식을 확인해주세요")
                            
                import_lines.append(line)

                product_class_id = self.env["product.class"].search([('Product_Class', '=', line.get("제품 용도"))], limit=1).id
                product_line_id = self.env["product.line"].search([('Product_Class', '=', product_class_id), ('Product_Line', '=', line.get("제품군"))], limit=1).id
                product_model_id = self.env["product.model"].search([('Product_Class', '=', product_class_id), ('Product_Line', '=', product_line_id), ('Product_Model', '=', line.get("제품 모델"))], limit=1).id
                product_generation_id = self.env["product.generation"].search([('Product_Class', '=', product_class_id), ('Product_Line', '=', product_line_id), ('Product_Model', '=', product_model_id), ('Product_Generation', '=', line.get("제품 세대"))], limit=1).id  
                Product_Nation = line.get("국가명")
                Note = line.get("비고")
                print(Note)

                product_main_check_id = self.env["product.main"].search([('Product_Class', '=', product_class_id), ('Product_Line', '=', product_line_id), ('Product_Model', '=', product_model_id), ('Product_Generation', '=',product_generation_id ),('Product_Generation', '=',product_generation_id ),('Product_Nation', '=',Product_Nation ),('Note', '=',Note )], limit=1).id  
                
                pprint.pprint(line)
                if not product_class_id:
                    print("aa")
                    product_class_id = self.env["product.class"].create({'Product_Class': line.get("제품 용도")}).id
                    product_line_id = self.env["product.line"].create({'Product_Class': product_class_id, 'Product_Line': line.get("제품군")}).id
                    product_model_id = self.env["product.model"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': line.get("제품 모델")}).id
                    product_generation_id = self.env["product.generation"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': product_model_id, 'Product_Generation': line.get("제품 세대")}).id
                elif not product_line_id:
                    print("BB")
                    product_line_id = self.env["product.line"].create({'Product_Class': product_class_id, 'Product_Line': line.get("제품군")}).id
                    product_model_id = self.env["product.model"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': line.get("제품 모델")}).id
                    product_generation_id = self.env["product.generation"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': product_model_id, 'Product_Generation': line.get("제품 세대")}).id
                elif not product_model_id:
                    print("CC")
                    product_model_id = self.env["product.model"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': line.get("제품 모델")}).id
                    product_generation_id = self.env["product.generation"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': product_model_id, 'Product_Generation': line.get("제품 세대")}).id
                elif not product_generation_id:  # product_generation_id 조건 추가
                    print("DD")
                    product_generation_id = self.env["product.generation"].create({'Product_Class': product_class_id, 'Product_Line': product_line_id, 'Product_Model': product_model_id, 'Product_Generation': line.get("제품 세대")}).id
                
                if product_main_check_id : 
                    print("TTTTTTT")
                    continue 
                else :
                    print("aaaaaaaa")
                    self.env["product.main"].create({
                        'Product_Class': product_class_id,
                        'Product_Line': product_line_id,
                        'Product_Model': product_model_id,
                        'Product_Generation':product_generation_id,
                        'Product_Nation': Product_Nation,
                        'Note': Note
                        })
            
            #f5
            return {
                'type': 'ir.actions.client',
                'tag': 'reload'
            }
        except :
           raise ValidationError(_("업로드에 문제가 발생 하였습니다."))

            

        

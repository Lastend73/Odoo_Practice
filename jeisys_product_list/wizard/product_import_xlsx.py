from odoo import api, fields, models, _

import tempfile
import binascii
import xlrd
from odoo.exceptions import ValidationError

import pprint

class Create_class(models.TransientModel):
    _name = 'product.import.wiz'
    _description = "import product xlsx"

    check_template_file = fields.Many2one('template.dictionary',string='check model')
    file_template = fields.Many2many(related='check_template_file.file_template', string="Template File")

    import_file = fields.Binary("Import File")
    file_name = fields.Char("File name")


    @api.model
    def default_get(self, fields):
        try :
            res = super(Create_class, self).default_get(fields)
            compare_action_id = self.env['template.dictionary'].sudo().search(["|",('title', '=', "제품 체계도"),('title', '=', "Jeisys Product List")]).id
            res['check_template_file'] = compare_action_id
            return res
        except : 
            raise ValidationError(_("오류 발생"))
            
        
        # attachment_id = self.env['ir.attachment'].sudo().search([('name', 'ilike', '제품 체계도')], limit=1)
        # print("fsdfasdfasd",attachment_id.id)
        # if attachment_id:
        #     res['check_template_file'] = 'True'
        #     res['template_file'] = [(6, 0, [attachment_id.id])]
        # return res

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
                Permission_name = line.get("실 사용 명칭")

                product_main_check_id = self.env["product.main"].search([('Product_Class', '=', product_class_id), ('Product_Line', '=', product_line_id), ('Product_Model', '=', product_model_id), ('Product_Generation', '=',product_generation_id ),('Product_Generation', '=',product_generation_id ),('Product_Nation', '=',Product_Nation ),('Permission_name', '=',Permission_name )], limit=1).id  
                
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
                        'Permission_name': Permission_name
                        })
            
            #f5
            return {
                'type': 'ir.actions.client',
                'tag': 'reload'
            }
        except :
           raise ValidationError(_("업로드에 문제가 발생 하였습니다."))

            

        
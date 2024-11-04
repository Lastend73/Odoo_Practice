from odoo import models, fields, api, _


class template_dic(models.Model):
    _name = "owl.todo.list"
    _description = "OWl Todo List App"

    name = fields.Char(string="Task Name")
    completed = fields.Boolean()
    color = fields.Char()

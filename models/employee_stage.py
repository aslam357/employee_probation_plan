from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    stage_id = fields.Many2one('hr.stage', string="Stage")
    status = fields.Selection([
        ('probation', 'Probation'),
        ('employment', 'Employment'),
        ('noticeperiod', 'Notice Period'),
        ('resigned', 'Resigned'),
        ('terminated', 'Terminated')
    ], string="Status", default="employment")

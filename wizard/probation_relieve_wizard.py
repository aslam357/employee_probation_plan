from odoo import models, fields

class EmployeeProbationRelieveWizard(models.TransientModel):
    _name = 'hr.employee.probation.relieve.wizard'
    _description = 'Probation Relieve Wizard'
    
    employee_id = fields.Many2one('hr.employee', string='Employee')
    parent_id = fields.Many2one('hr.employee', string='Manager')
    job_id = fields.Many2one('hr.job', string='Job Position')
    department_id = fields.Many2one('hr.department', string='Department')
    coach_id = fields.Many2one('hr.employee', string='Coach')
    probation_start_date = fields.Date(string='Start Date')
    probation_end_date = fields.Date(string='End Date')
    progress_rating = fields.Selection([
        ('poor', 'Poor'),
        ('average', 'Average'),
        ('good', 'Good'),
        ('excellent', 'Excellent')
    ], string='Progress Rating')
    review_comments = fields.Char(string='Review Comments')
    extra_info = fields.Char(string='Extra Information')

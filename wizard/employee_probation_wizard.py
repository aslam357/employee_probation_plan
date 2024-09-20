from odoo import models, fields
from odoo.exceptions import UserError

class HrEmployeeProbationWizard(models.TransientModel):
    _name = 'hr.employee.probation.wizard'
    _description = 'Employee Probation Wizard'

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    parent_id = fields.Many2one('hr.employee', string="Head of Function")
    job_id = fields.Many2one('hr.job', string="Job Position")
    department_id = fields.Many2one('hr.department', string="Department")
    coach_id = fields.Many2one('hr.employee', string="Line Manager")
    probation_start_date = fields.Date(string="Join Date", required=True)
    probation_end_date = fields.Date(string="Probation Complete Date", required=True)
    progress_rating = fields.Selection([
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★')],
    string="Progress Rating"
)
    plan = fields.Text(string="Plan")
    review_comments = fields.Text(string="Review Comments")
    extra_info = fields.Char(string="Extra Information")

class HrEmployeeProbationSetPlanWizard(HrEmployeeProbationWizard):
    _name = 'hr.employee.probation.set.plan.wizard'
    _description = 'Set Probation Plan Wizard'

    def action_set_probation_plan(self):
        self._update_probation({
            'plan': self.plan,
            'state': 'in_progress'
        })

class HrEmployeeProbationSendReviewWizard(HrEmployeeProbationWizard):
    _name = 'hr.employee.probation.send.review.wizard'
    _description = 'Send Review Wizard'

    def action_send_review(self):
        if not self.review_comments:
            raise UserError("Please provide review comments.")
        self._update_probation({
            'review_comments': self.review_comments,
            'state': 'draft'
        })

    def action_refuse(self):
        self._update_probation({
            'state': 'draft'
        })
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class HrEmployeeProbation(models.Model):
    _name = 'hr.employee.probation'
    _description = 'Employee Probation'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    parent_id = fields.Many2one('hr.employee', string="Head Of Function")
    job_id = fields.Many2one('hr.job', string="Job Position")
    department_id = fields.Many2one('hr.department', string="Department")
    coach_id = fields.Many2one('hr.employee', string="Line Manager")
    probation_start_date = fields.Date(string="Join Date")
    probation_end_date = fields.Date(string="Probation Complete Date")
    progress_rating = fields.Selection([
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★')],
    string="Progress Rating"
)
    probation_status = fields.Selection([
        ('active', 'Active'),
        ('completed', 'Probation End')],
        string="Employment Status",
        compute='_compute_probation_status',
        store=True
    )
    plan = fields.Text(string="Probation Plan")
    review_comments = fields.Text("Review Comments")
    extra_info = fields.Text(string="Extra Information")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'Waiting Approval'),
        ('completed', 'Done')],
        default='draft', string="State"
    )

    def _send_email(self, template_xml_id):
        template = self.env.ref(template_xml_id, raise_if_not_found=False)
        if not template:
            raise UserError(f"Email template with ID '{template_xml_id}' not found.")
        mail_id = template.send_mail(self.id, force_send=True)
        if not mail_id:
            raise UserError("Failed to send the email.")

    @api.depends('probation_end_date')
    def _compute_probation_status(self):
        today = fields.Date.today()
        for record in self:
            if record.probation_end_date:
                if record.probation_end_date < today:
                    if record.state != 'in_progress':  
                        record.probation_status = 'active'
                        record.state = 'in_progress'
                        template = self.env.ref('probation_plan.email_template_probation_extension')
                        if template:
                            template.send_mail(record.id, force_send=True)
                        else:
                            raise UserError("Email template for probation end not found.")
                elif record.probation_end_date > today:
                    if record.state != 'completed':  
                        record.probation_status = 'completed'
                        record.state = 'completed'
                        template = self.env.ref('probation_plan.email_template_probation_end')
                        if template:
                            template.send_mail(record.id, force_send=True)
                        else:
                            raise UserError("Email template for probation end not found.")
            
            else:
                record.probation_status = 'active'
                record.state = 'draft'

    def action_set_probation_plan(self):
        pass

    def action_send_review(self):
        if not self.review_comments:
            raise UserError("Please provide review comments.")
        self.write({'state': 'in_progress'})
        template = self.env.ref('probation_plan.email_template_probation_relieve')
        template.send_mail(self.id, force_send=True)

    def action_refuse(self):
        self.state = 'draft'





from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    express_shipping = fields.Boolean(default=False, string="Express Shipping")

    def _action_launch_stock_rule(self, *args, **kwargs):
        """ if procurement_group_id exists than it will be extended
        so we clean up it for create new one for the non express delivery  """

        exp_line = self.filtered(lambda rec: rec.express_shipping)
        super(SaleOrderLine, exp_line)._action_launch_stock_rule(*args, **kwargs)

        self.order_id.procurement_group_id = False
        super(SaleOrderLine, self - exp_line)._action_launch_stock_rule(*args, **kwargs)

        return True

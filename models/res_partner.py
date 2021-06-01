from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    primary_address = fields.Boolean(string="Primary address")

    @api.model
    def create(self, vals):
        """ We need to make only first created delivery address as primary.
        """

        current_obj = super(ResPartner, self).create(vals)
        delivery_address_list = current_obj.parent_id.child_ids.filtered(
            lambda obj: obj.type == 'delivery' and obj.id != current_obj.id)
        if len(delivery_address_list) == 0:
            current_obj.primary_address = True

        if current_obj.primary_address:
            for rec in delivery_address_list:
                rec.write({'primary_address': False})
        return current_obj

    def write(self, vals):
        """ When user set new address as primary, other addresses should be reset.
        """

        if "primary_address" in vals and vals["primary_address"]:
            delivery_address_list = self.parent_id.child_ids.filtered(
                lambda obj: obj.type == 'delivery' and obj.id != self.id)
            for rec in delivery_address_list:
                rec.write({'primary_address': False})

        return super(ResPartner, self).write(vals)

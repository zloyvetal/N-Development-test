# N-Development-test
test task
# Odoo addons version 14.0

This Odoo addon extends the default functionality of the Sale module.
We can set the express_shipping checkbox when creating a quotation line, therefore new delivery will be prepared.

| File | Description |
|--------|-------------|
|:res_partner_inh.py: | Added primary_address field to the res.partner module. The field is being set to True during the first creation of the address with type "delivery". The field can be changed by the user manually. Only 1 address with the type "delivery" can have primary_address == True.  |
|:sale_order_line_inh.py : Extends the _action_launch_stock_rule function in the sale.order.line module. Adds possibility for multiple deliveries in one order.
|

Some solutions were made by my understanding of the business logic. Usually, such solutions should be made by the business.

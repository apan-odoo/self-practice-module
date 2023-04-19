from odoo import models,fields, Command


class ReservationMain(models.Model):
    _inherit = "reservation.main"

    def check_out_action(self):
        # print("hii")
        self.env["account.move"].create(
            {
                # 'partner_id': self.name,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create(
                        {
                            'name': self.hotel_id.name,
                            'quantity': 1,
                            'price_unit': 0.06*self.net_amount,
                        }
                    ),
                    Command.create(
                        {
                            'name': 'administrative fees',
                            'quantity': 1,
                            'price_unit': 100.00,
                        }
                    )
                ]
            }
        )
        return super(ReservationMain, self).check_out_action()

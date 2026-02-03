def pre_init_hook(cr):
    cr.execute(
        """
        ALTER TABLE sale_order
            ADD COLUMN IF NOT EXISTS commission_total NUMERIC;
        """
    )
    cr.execute(
        "ALTER TABLE sale_order_line "
        "ADD COLUMN IF NOT EXISTS commission_free BOOLEAN"
    )

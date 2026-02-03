def pre_init_hook(cr):
    cr.execute(
        "ALTER TABLE account_move " "ADD COLUMN IF NOT EXISTS commission_total NUMERIC"
    )
    cr.execute(
        "ALTER TABLE account_move_line "
        "ADD COLUMN IF NOT EXISTS commission_free BOOLEAN"
    )

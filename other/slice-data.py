invoice = """
0.....6.................................40........52...55........
1583  The Hitchhiker's Guide to Python      $12.79    5    $63,95
1263  High Performance Python               $35.96    3   $107.88
1932  Python for Data Analysis              $35.92    2    $71.84
"""

PRODUCT_ID = slice(0, 6)
PRODUCT_NAME = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

invoice_lines = invoice.split('\n')[2:]

for item in invoice_lines:
    print(item[UNIT_PRICE], item[PRODUCT_NAME])
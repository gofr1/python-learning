import string
import re

columns = [
    '\tFiscal  year',
    'Sales Channel',
    'Customer Hierarchy',
    'Net proceeds of sales (for NNS) [300]',
    '[-] Bad goods and SG Goods sales allowances [325]',
    'Allowances damaged goods not returned [267]',
    'Salvage and 2nd grade goods sales allows [263]',
    'Net proceeds of sales [306]'
]

for column in columns:
    # save original column name with quotes
    old_column = '\'' + column + '\''
    
    # remove punctuation
    for char in string.punctuation:
        column = column.replace(char, ' ')
    
    # remove different tabulation and new lines etc.
    for char in string.whitespace:
        column = column.replace(char, ' ')
    
    # replace spaces with underscopes and add quotes
    new_column = '\'' + re.sub('\s+', '_', column.lower().strip()) + '\''
    
    # print cleaned column names
    print('({: <55} ,{: <55})'.format(old_column, new_column))

# Output:
#* ('      Fiscal  year'                                         ,'fiscal_year'                                          )
#* ('Sales Channel'                                         ,'sales_channel'                                        )
#* ('Customer Hierarchy'                                    ,'customer_hierarchy'                                   )
#* ('Net proceeds of sales (for NNS) [300]'                 ,'net_proceeds_of_sales_for_nns_300'                    )
#* ('[-] Bad goods and SG Goods sales allowances [325]'     ,'bad_goods_and_sg_goods_sales_allowances_325'          )
#* ('Allowances damaged goods not returned [267]'           ,'allowances_damaged_goods_not_returned_267'            )
#* ('Salvage and 2nd grade goods sales allows [263]'        ,'salvage_and_2nd_grade_goods_sales_allows_263'         )
#* ('Net proceeds of sales [306]'                           ,'net_proceeds_of_sales_306'                            )
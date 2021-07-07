"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Joseph Aiyeoribe.
Date: 2nd September, 2020.
"""

import currency

src_value = str(input("3-letter code for original currency: "))

dst_value = str(input("3-letter code for the new currency: "))

amt_value = float(input("Amount of the original currency: "))

result = currency.exchange(src_value, dst_value, amt_value)

#dst_value = round(dst_value,3)

print('You can exchange '+str(amt_value)+' '+str(src_value)+' for '+str(round(currency.exchange(src_value, dst_value, amt_value),3))+' '+str(dst_value)+'.')

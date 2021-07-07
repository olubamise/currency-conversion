"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Joseph Aiyeoribe.
Date: 2nd September, 2020.
"""

import introcs

APIKEY = 'ZNXDUOkKKzPptpsvWyWk2U3EdmMK4ykjUKcE9DLj1iMe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string'

    assert len(s) != 0, repr(s)+' cannot be empty'

    assert introcs.rfind_str(s,' ') >= 0, repr(s)+' string provided does not have space'

    #check1 = introcs.find_str(s,'.')
    #check for leading space in the string
    #s = introcs.lstrip(s)

    first_space=introcs.index_str(s,' ')


    #print(s[:first_space])
    return s[:first_space]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string'

    assert introcs.rfind_str(s,' ') >= 0, repr(s)+' string provided does not have space'

    first_space=introcs.find_str(s,' ')

    return s[first_space+1:]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str, repr(s)+' is not a string'



    start_quote_pos = introcs.find_str(s,'"')
    #print(start_quote_pos)
    end_quote_pos = introcs.find_str(s,'"',start_quote_pos+1)

    message = (' string provided ' +
               'does not have quotes')
    assert start_quote_pos > -1 and end_quote_pos > -1, repr(s)+message
    result = s[start_quote_pos+1:end_quote_pos]
    return(result)


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    #'{"success": true, "src":"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    start_quote_pos = introcs.find_str(json,'"',23)

    end_quote_pos = introcs.find_str(json,'"',start_quote_pos+1)

    result = introcs.lstrip(json[start_quote_pos+1:end_quote_pos],' :')
    #print(start_quote_pos)
    return(result)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
#{"success": true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error": ""}'


    start_quote_pos = introcs.find_str(json,'"dst":')
    #print(start_quote_pos)
    end_quote_pos = introcs.find_str(json,'",',start_quote_pos+1)

    result = introcs.lstrip(json[start_quote_pos+6:end_quote_pos],' "')
    #print(result)
    return(result)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, repr(json)+' is not a string'
    start_quote_pos = introcs.find_str(json,'"error":')

    end_quote_pos = introcs.find_str(json,'"}',start_quote_pos+1)

    result = introcs.lstrip(json[start_quote_pos+8:end_quote_pos],' "')
    #print(len(result) > 0)
    return len(result) > 0


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    message = (' should be a nonempty' +
               ' string with only letters')
    assert type(src) == str and introcs.isalpha(src) == True, repr(src)

    message1 = (' should be a nonempty ' +
                'string with only letters')

    assert type(dst) == str and introcs.isalpha(dst) == True, repr(dst)

    message2 = (' should be a float ' +
                'or integer value')

    assert type(amt) == int or type(amt) == float, repr(amt)+message2

    # api-endpoint
    URL = "http://ecpyfac.ecornell.com/python/currency/fixed?"

    params = 'src='+src+'&dst='+dst+'&amt='+str(amt)+'&key='+APIKEY
    #print(params)

    URL = URL + params

    result = introcs.urlread(URL)

    return result


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    #print(currency)
    is_cur_valid = service_response(currency, 'EUR', 1.0)
    #print(is_cur_valid)

    start_quote_pos = introcs.find_str(is_cur_valid,'"error":')

    end_quote_pos = introcs.find_str(is_cur_valid,'"}',start_quote_pos+1)
    #{"success": true, "src": "1.0 Euro", "dst": "1.0 Euro", "error": ""}

    result = introcs.lstrip(is_cur_valid[start_quote_pos+9:end_quote_pos],' "')
    #print (result)

    return len(result) == 0


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src) == str, repr(src)+' is not a string'
    assert type(dst) == str, repr(dst)+' is not a string'
    assert type(amt) == float or type(amt) == int
    test_dst_value = iscurrency(dst)
    assert test_dst_value == True
    test_src_value = iscurrency(src)
    assert test_src_value == True

    exchange_amt_temp = get_dst(service_response(src, dst, amt))
    #print(exchange_amt_temp)
    ex_amt_pos = introcs.find_str(exchange_amt_temp,' ')
    exchange_amt = exchange_amt_temp[:ex_amt_pos]
    #print(exchange_amt)
    result = float(exchange_amt)

    return result










    

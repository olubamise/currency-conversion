"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Joseph Aiyeoribe.
Date: 2nd September, 2020.
"""


import introcs
import currency


def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')


    result = currency.before_space('0.863569 Euros')
    introcs.assert_equals('0.863569', result)


    result = currency.before_space('0.863569  Euros')
    introcs.assert_equals('0.863569', result)


    result = currency.before_space(' 0.863569 Euros')
    introcs.assert_equals('', result)


    result = currency.before_space(' 0.863569Euros')
    introcs.assert_equals('', result)


def test_after_space():
    """
    Test procedure for after_space
    """
    print('Testing after_space')


    result = currency.after_space('0.863569 Euros')
    introcs.assert_equals('Euros', result)


    result = currency.after_space('0.863569  Euros')
    introcs.assert_equals(' Euros', result)


    result = currency.after_space('0.863569 Euros ')
    introcs.assert_equals('Euros ', result)


    result = currency.after_space('0.863569Euros ')
    introcs.assert_equals('', result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "" C D')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes('"A  C D"')
    introcs.assert_equals('A  C D', result)


def test_get_src():
    """
    Test procedure for get_src
    """
    print('Testing get_src')

    message = ('{"success": true, "src":"2 United States Dollars"' +
    ', "dst": "1.772814 Euros", "error": ""}')
    result = currency.get_src(message)
    introcs.assert_equals('2 United States Dollars', result)

    message1 = ('{"success": true, "src": "2 United States Dollars", "dst"' +
                ': "1.772814 Euros", "error": ""}')
    result = currency.get_src(message1)
    introcs.assert_equals('2 United States Dollars', result)

    message2 = ('{"success":false,"src":"","dst":"","error"' +
                ':"Source currency code is invalid."}')
    result = currency.get_src(message2)
    introcs.assert_equals('', result)

    message3 = ('{"success":false,"src": "","dst":"","error":"Source ' +
                'currency code is invalid."}')
    result = currency.get_src(message3)
    introcs.assert_equals('', result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')

    message1 = ('{"success": true, "src": "2 United States ' +
                'Dollars", "dst": "1.772814 Euros", "error": ""}')
    result = currency.get_dst(message1)
    introcs.assert_equals('1.772814 Euros', result)


    message2 = ('{"success":false,"src":"","dst":"","error":"Source' +
                ' currency code is invalid."}')
    result = currency.get_dst(message2)
    introcs.assert_equals('', result)

    message = ('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 ' +
               'Euros", "error":""}')
    result = currency.get_dst(message)
    introcs.assert_equals('1.772814 Euros', result)


    message3 = ('{"success":false,"src":"","dst": "","error":"Source ' +
                'currency code is invalid."}')
    result = currency.get_dst(message3)
    introcs.assert_equals('', result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')

    message = ('{"success":false,"src":"","dst":"","error":"Source ' +
               'currency code is invalid."}')
    result = currency.has_error(message)
    introcs.assert_equals(True,result)


    message1 = ('{"success": true, "src": "2 United States Dollars", "dst": ' +
                '"1.772814 Euros", "error": ""}')
    result = currency.has_error(message1)
    introcs.assert_equals(False,result)

    message4 = ('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 ' +
                'Euros", "error":""}')
    result = currency.has_error(message4)
    introcs.assert_equals(False,result)


    message3 = ('{"success":false,"src":"","dst":"","error": "Source ' +
                'currency code is invalid."}')
    result = currency.has_error(message3)
    introcs.assert_equals(True,result)


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')


    message = ('{"success": true, "src": "2.5 United States ' +
               'Dollars", "dst": "2.2160175 Euros", "error": ""}')
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals(message,result)

    message1 = ('{"success": true, "src": "-1.0 United States ' +
                'Dollar", "dst": "-0.377029 ' +
                'Bahraini Dinar", "error": ""}')
    result = currency.service_response('USD','BHD',-1.0)
    introcs.assert_equals(message1,result)

    message2 = ('{"success": false, "src": "", "dst": "", "error": "The rate for ' +
                'currency DOL is not present."}')
    result = currency.service_response('USD','DOL',1.0)
    introcs.assert_equals(message2,result)

    message3 = ('{"success": false, "src": "", "dst": "", "error": "The rate ' +
                'for currency DOL is not present."}')
    result = currency.service_response('DOL','EUR',1.0)
    introcs.assert_equals(message3,result)


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print('Testing iscurrency')


    result = currency.iscurrency('EUR')
    introcs.assert_equals(True,result)

    result = currency.iscurrency('WWW')
    introcs.assert_equals(False,result)


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')
    #currency.exchange('USD','EUR',2.5)

    result = currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175,result)

    result = currency.exchange('USD','EUR',-2.0)
    introcs.assert_floats_equal(-1.772814,result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()


print("All tests completed successfully.")

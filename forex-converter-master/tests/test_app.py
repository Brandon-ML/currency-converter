import unittest
from app import app, get_exchange_rate
from flask import session

class CurrencyConverterTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the application for testing. This method is called before each test.
        - app.testing: Configures the application for testing (affects error handling and other settings).
        - self.client: A test client for the application. Used to simulate requests to the application.
        """
        app.testing = True
        self.client = app.test_client()

    def test_index_page(self):
        """
        Test that the index page can be accessed.
        - Checks if the index page is returning a 200 status code.
        - Verifies that a specific part of the page content ('Convert USD to') is present, indicating a successful load.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Convert USD to', response.data.decode())

    def test_conversion_endpoint(self):
        """
        Test the conversion functionality.
        - Uses POST to simulate a user submitting the form with specific currencies and amount.
        - 'EUR,JPY' and '100' are used as test data representing a common use case.
        - Checks for a 200 status code and the presence of 'Exchange Rates' in the response to confirm functionality.
        """
        response = self.client.post('/convert', data={
            'toCurrency': 'EUR,JPY',
            'amount': '100'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Exchange Rates', response.data.decode())

    def test_invalid_currency_code(self):
        """
        Test handling of invalid currency codes.
        - Simulates a form submission with an invalid currency code ('XXX').
        - Uses follow_redirects=True to follow the redirect to the index page after submission.
        - Checks for the presence of the 'Invalid Currency Code' flash message in the session.
        """
        with self.client as c:
            response = c.post('/convert', data={
                'toCurrency': 'XXX',
                'amount': '100'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            # Assuming your flash messages are categorized, you could check like this:
            self.assertTrue('Invalid Currency Code' in session['_flashes'][0][1])

    def test_invalid_amount(self):
        """
        Test handling of invalid amounts.
        - Simulates a form submission with an invalid amount ('invalid').
        - Uses follow_redirects=True to ensure the response follows any redirects.
        - Checks for the presence of the 'Invalid amount' flash message in the session.
        """
        with self.client as c:
            response = c.post('/convert', data={
                'toCurrency': 'EUR',
                'amount': 'invalid'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue('Invalid amount' in session['_flashes'][0][1])

    def test_api_call(self):
        """
        Test the API call function directly.
        - Checks the functionality of the get_exchange_rate function with a set of currencies ('EUR', 'JPY').
        - Verifies that the response is not None and is of type dict, indicating a successful API call and response format.
        """
        symbols = ['EUR', 'JPY']
        rates = get_exchange_rate(symbols)
        self.assertIsNotNone(rates)
        self.assertIsInstance(rates, dict)
        

if __name__ == '__main__':
    unittest.main()


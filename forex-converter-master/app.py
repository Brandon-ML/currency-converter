from flask import Flask, redirect, request, render_template, flash, url_for
import requests, traceback

app = Flask(__name__)
app.secret_key = '12345'

API_KEY = 'c2c8ac54d7204aea43a74f67827e94d2'

# A dictionary mapping currency codes to their symbols
money_system = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "CAD": "C$",
    "AUD": "A$",
    "CHF": "Fr",
    "CNY": "¥",
    "HKD": "HK$",
    "NZD": "NZ$"
}

def get_exchange_rate(symbols):
   """
    Fetches the exchange rates for the given list of currency symbols.
    
    Args:
        symbols (list): A list of currency codes to get the exchange rates for.
    
    Returns:
        dict: A dictionary of currency codes to their exchange rates if successful, None otherwise.
    """
   #Construct the API URL with the provided symbols
   url = f"http://api.exchangerate.host/live?access_key={API_KEY}&currencies={','.join(symbols)}"

   #Make an HTTP get request to the API
   response = requests.get(url)
   print(response.json()) #Debug: print the JSON response

   #check if the API request was successful
   if response.status_code == 200:
      data = response.json()
      #Check if 'quotes' is present in the response
      if 'quotes' in data:
         return data['quotes'] #return the exchange rates
      else:
         #if 'quotes' is not present flash an error and return None
         flash("Invalid Currency Code")
         return None

   else:
      #flash an error if the API request failed
      flash(f"Error: The API request failed with status code {response.status_code}")
      return None
       

@app.route('/')
def index():
    """
    Renders the index page where the user can input currencies and amounts to be converted.
    """
    return render_template('index.html')  

@app.route('/convert', methods=['POST'])
def convert():
    """
    Handles the currency conversion by fetching the exchange rates and calculating the converted amounts.
    
    The function reads the input from the form, fetches the current exchange rates,
    calculates the converted amounts, and then renders the result page with the calculated values.
    
    Returns:
        A redirection to the index page if an error occurs, or the result page with conversion results.
    """
    #Extract currency and amount from the form data
    symbols = request.form.get('toCurrency').upper().split(',')
    amount_str = request.form.get('amount')

    try:
       #Convert the amount to a float, handle invalid input
       amount= float(amount_str)
    except ValueError:
       flash("Invalid amount")
       return redirect(url_for('index'))
    
    
    try:
        #Fetch exchange rates for the given symbols
        quotes = get_exchange_rate(symbols)
        if quotes is None:
            #if no rates were fetched, redirect to index
            return redirect(url_for('index'))

        #Calculate converted amounts for each currency
        converted_amounts = {f"{currency}": round(quote * amount, 2) for currency, quote in quotes.items()}
        #Render and return the result page with conversion results
        return render_template('result.html', quotes=converted_amounts, amount=amount, money_system=money_system)

    except Exception as e:
       #Handle any unexpected exceptions
       print(f"An unexpected error occurred: {e}")
       traceback.print_exc()  #Print the traceback for debugging

        # Flash a more detailed error message to the user for debugging
       flash(f"An unexpected error occurred: {str(e)}", 'error') #Flash a detailed error message
       return redirect(url_for('index')) #Redirect to index on error

   

if __name__ == '__main__':
    app.run(debug=True)

# //suggestions and improvements
# //1. Consider keeping the Secret Key and API Key more secure by using an environment variable.
# //2. The print(response.json()) statement within the get_exchange_rate function is useful for debugging and development, remove it in the production code.
# //3. For error handling, instead of printing the entire traceback to the console, consider logging it to a file or another logging system for better management

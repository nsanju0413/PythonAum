from flask import Flask, render_template, request
import requests

app = Flask(__name__)

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://open.er-api.com/v6/latest'
        self.exchange_rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        params = {'apikey': self.api_key}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['rates']
        else:
            raise Exception(f"Error fetching exchange rates: {response.status_code}")

    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount  # No conversion needed for the same currency

        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency code")

        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]
        converted_amount = amount * (to_rate / from_rate)
        return round(converted_amount, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    api_key = '8ffc54e515d24260b607099a9973ec99'
    converter = CurrencyConverter(api_key)

    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()

        result = converter.convert_currency(amount, from_currency, to_currency)
        return render_template('result.html', amount=amount, from_currency=from_currency,
                               to_currency=to_currency, result=result)

    except ValueError as e:
        return render_template('error.html', error=f"Error: {e}")
    except Exception as e:
        return render_template('error.html', error=f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)

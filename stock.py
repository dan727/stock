from flask import Flask, render_template, request
from alpha_vantage.timeseries import TimeSeries
import requests, pprint


app = Flask(__name__)

@app.route('/stocks', methods=['POST'])
def stocks():
    stock_symbol = request.form['ssymbol']
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+stock_symbol+'&interval=5min&apikey=7KY3WGUYTHYBYFK6') 
    json_object = r.text
    #j_obj = json_object['Time Series (5min)']['2019-08-05 16:00:00']['1. open']
    #return render_template('stocks.html',stock=j_obj)
    return json_object

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def aboutpage():
    return render_template('about.html')

# api 7KY3WGUYTHYBYFK6
# ts = TimeSeries(key='7KY3WGUYTHYBYFK6')
# data = ts.get_intraday('GOOGL')

# pp = pprint.PrettyPrinter(indent=1)


# pp.pprint(data)

if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask, jsonify, request


app = Flask(__name__)

portfolios = [
    {
        'portfolio_name': "My portfolio",
        'stocks':[
            {
                'name': "AMZN",
                'price': 3202.78,
                'sigma': 0.16
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only 

# GET /portfolios
@app.route('/portfolios') 
def get_portfolios(): 
    return jsonify({"portfolios": portfolios}) 

# GET /portfolio/<string:portfolio_name>
@app.route('/portfolio/<string:portfolio_name>') #Flask syntax
def get_portfolio(portfolio_name): #name has to be the same
    for portfolio in portfolios:
        if portfolio['portfolio_name'] == portfolio_name:
            return jsonify(portfolio)
        return jsonify({'message': 'portfolio not found'})

# GET /portfolio/<string:portfolio_name>/stocks
@app.route('/portfolio/<string:portfolio_name>/stocks')
def get_stocks_in_portfolio(portfolio_name):
    for portfolio in portfolios:
        if portfolio['portfolio_name'] == portfolio_name:
            return jsonify({'stocks': portfolio['stocks']})
        return jsonify({'message': 'portfolio not found'})

# GET /portfolio/<string:portfolio_name>/<string:name>
@app.route('/portfolio/<string:portfolio_name>/<string:name>')
def get_stock_in_portfolio(portfolio_name, name):
    for portfolio in portfolios:
        for stock in portfolio['stocks']:
            if portfolio['portfolio_name'] == portfolio_name and stock['name'] == name:
                return jsonify({'stocks': stock})
    return jsonify({'message': 'stock not found'})

# POST 
@app.route('/portfolio', methods=['POST'])
def create_portfolio():
    request_data = request.get_json()
    new_portfolio = {
        'portfolio_name': request_data['portfolio_name'],
        'stocks': []
    }
    portfolios.append(new_portfolio)
    return jsonify(new_portfolio)

# POST /portfolio/<string:portfolio_name>/stock {name:, price:, sigma:}
@app.route('/portfolio/<string:portfolio_name>/stock', methods=['POST'])
def create_stock_in_portfolio(portfolio_name):
    request_data = request.get_json()
    for portfolio in portfolios:
        if portfolio ['portfolio_name'] == portfolio_name:
            new_stock = {
                'name': request_data['name'],
                'price': request_data['price'],
                'sigma': request_data['sigma']
            }
            portfolio['stocks'].append(new_stock)
            return jsonify(new_stock)
    return jsonify({'message': 'portfolio not found'})
        
app.run(port=5000)
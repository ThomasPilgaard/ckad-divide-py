import flask
import json
import math

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/divide', methods=['GET'])
def divide():
    dividend = int(flask.request.args.get('dividend'))
    divisor = int(flask.request.args.get('divisor'))
    result = divide(dividend, divisor)
    timeconsumingCalculations(dividend, divisor)
    return createResponse(result)

def divide(dividend, divisor):
    quotient = dividend / divisor
    return quotient

def createResponse(quotient):
    response = {}
    response['result'] = quotient
    return response

def timeconsumingCalculations(numb1, numb2):
    var1 = math.factorial(numb1)
    var2 = math.factorial(numb2)
    var3 = math.gcd(numb1, numb2)
    var4 = var1 * var2 * var3

app.run(debug=True, host='0.0.0.0')

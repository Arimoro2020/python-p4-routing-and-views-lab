#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    count = '0\n'
    for i in range(1, parameter):
        count +=f'{i}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
   
    if operation == '+':
        sum =  num1 + num2
        return str(sum)
    
    elif operation == '-':
        subtract = num1 - num2
        return str(subtract)
      
    
    elif operation == '*':
        multiply = num1 * num2
        return str(multiply)
      
    
    elif operation == 'div':
        division = num1 / num2
        return str(division)
      
    else:
        modulus = num1 % num2
        return str(modulus)
      






if __name__ == '__main__':
    app.run(port=5555, debug=True)

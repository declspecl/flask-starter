#!/usr/bin/env python

from flask import Flask, jsonify

app = Flask(__name__)

def gcd(a, b): #Greatest Common Divisor
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b): #Lowest Common Multiple
    return (a * b) // gcd(a, b)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/lcm/<int:num1>/<int:num2>')
def get_lcm(num1, num2):
    result = lcm(num1, num2)
    return jsonify({'lcm': result})

@app.route('/gcd/<int:num1>/<int:num2>')
def get_gcd(num1, num2):
    result = gcd(num1, num2)
    return jsonify({'gcd': result})

if __name__ == "__main__":
    app.run(debug=True)

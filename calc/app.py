from operations import *

from flask import Flask, request

app = Flask(__name__)

math_ops = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div  
    }

@app.route('/math/<op>')
def show_math(op):
    """Do math on a and b"""    
    func = math_ops[op]
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = func(a, b)
    return f'{result}'
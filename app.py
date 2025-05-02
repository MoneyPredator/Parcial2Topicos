from flask import Flask, Response
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>') # http://127.0.0.1:5000/ 
def getFactorial(num):
    try:
        res = math.factorial(num) #res = Resultado
        msj = f"El factorial de {num} es {res}" #msj = Mensaje
    except ValueError:
        msj = "Error: Numero no valido"
    
    return Response(msj, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
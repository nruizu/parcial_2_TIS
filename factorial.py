from flask import Flask

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def calcular_factorial(num):
    resultado = 1
    for i in range(num):
        resultado *= i + 1
    return f'El factorial de {num} es {resultado}'

if __name__ == '__main__':
    app.run(debug=True)

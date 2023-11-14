from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def converter_moeda():
    if request.method == 'POST':
        valor = float(request.form['valor'])
        moeda_origem = request.form['moeda_origem']
        moeda_destino = request.form['moeda_destino']

        api_key = '7bc22b558be5927b88c70435'
        url = f'https://open.er-api.com/v6/latest/{moeda_origem}?apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        taxa_cambio = data['rates'][moeda_destino]

        valor_convertido = valor * taxa_cambio

        return render_template('resultado.html', valor_convertido=valor_convertido, moeda_origem=moeda_origem, moeda_destino=moeda_destino, valor=valor)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

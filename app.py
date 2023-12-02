from flask import Flask, request, jsonify
from flask_cors import CORS 
import numpy as np
import joblib

# Inicializar o aplicativo Flask
app = Flask(__name__)
CORS(app) 

# Carregar o modelo de árvore de decisão
modelo_arvore_decisao = joblib.load('modelo_arvore_decisao.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    # Obter os dados da requisição
    dados = request.get_json()

    # Certificar-se de que os dados são uma lista e convertê-los para uma matriz NumPy
    dados_array = np.array(list(dados.values())).reshape(1, -1)

    # Fazer a previsão usando o modelo de árvore de decisão
    resultado_arvore_decisao = modelo_arvore_decisao.predict(dados_array)

    # Converter o resultado para um formato adequado para resposta
    resultado_dict = {'resultado': int(resultado_arvore_decisao[0])}

    return jsonify(resultado_dict)

# Rodar o aplicativo
if __name__ == '__main__':
    app.run()

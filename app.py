from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS
import json

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": ["*"]}})  # Habilitar CORS para toda la aplicación - todos permitidos para fines de desarrollo
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Habilitar CORS para una ruta específica

@app.route('/users', methods=['GET'])
def get_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
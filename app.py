# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para la Prueba 1: Funcional (Registro de producto)
@app.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.get_json() or {}
    nombre = data.get('nombre')
    precio = data.get('precio')

    # Validamos que el nombre no esté vacío y el precio sea válido
    if not nombre or precio is None or precio <= 0:
        return jsonify({"status": "error", "message": "Datos de producto inválidos"}), 400

    return jsonify({"status": "success", "message": "Producto registrado"}), 201


# Endpoint para la Prueba 2: Seguridad (Login)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username', '')
    password = data.get('password', '')

    # Simulación de sanitización: si detecta sintaxis SQL maliciosa, bloquea el acceso
    caracteres_maliciosos = ["'", "OR", "--", "="]
    if any(char in username.upper() for char in ["'", "OR"]):
        return jsonify({"status": "error", "message": "Intento de inyección SQL detectado y bloqueado"}), 401

    if username == "estudiante@cun.edu.co" and password == "Password123*":
        return jsonify({"status": "success", "message": "Inicio de sesión exitoso"}), 200

    return jsonify({"status": "error", "message": "Credenciales incorrectas"}), 401


if __name__ == '__main__':
    app.run(port=5000)
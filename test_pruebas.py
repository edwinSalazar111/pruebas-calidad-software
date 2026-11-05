# test_pruebas.py
import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestPruebasSoftware(unittest.TestCase):

    # PRUEBA 1: FUNCIONAL
    def test_01_validacion_datos_producto(self):
        print("\n--- EJECUTANDO PRUEBA 1: FUNCIONAL ---")
        payload = {"nombre": "", "precio": -10}  # Datos inválidos
        response = requests.post(f"{BASE_URL}/productos", json=payload)
        
        print(f"Código HTTP recibido: {response.status_code}")
        print(f"Respuesta del Servidor: {response.json()}")
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["status"], "error")

    # PRUEBA 2: SEGURIDAD
    def test_02_bloqueo_inyeccion_sql(self):
        print("\n--- EJECUTANDO PRUEBA 2: SEGURIDAD ---")
        payload = {"username": "' OR '1'='1", "password": "' OR '1'='1"}  # Ataque SQLi
        response = requests.post(f"{BASE_URL}/login", json=payload)
        
        print(f"Código HTTP recibido: {response.status_code}")
        print(f"Respuesta del Servidor: {response.json()}")
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["status"], "error")


if __name__ == '__main__':
    unittest.main()
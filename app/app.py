from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Contador de requisições HTTP')

@app.route('/')
def index():
    return "Aplicação Flask rodando!", 200

@app.route('/health')
def health():
    REQUEST_COUNT.inc()
    return "OK", 200

if __name__ == "__main__":
    start_http_server(8001)  # Porta que exporta métricas (http://localhost:8001/)
    app.run(host="0.0.0.0", port=5000)  # Porta da aplicação


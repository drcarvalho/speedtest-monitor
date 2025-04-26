import time
import threading
import subprocess
import json
from flask import Flask, Response

app = Flask(__name__)

# Variável para armazenar o último resultado
latest_metrics = "# No data collected yet\n"

# Função para rodar o speedtest periodicamente
def run_speedtest_periodically():
    global latest_metrics
    while True:
        try:
            result = subprocess.run(
                ['speedtest', '--accept-license', '--accept-gdpr', '--format=json'],
                capture_output=True, text=True, timeout=300
            )
            data = json.loads(result.stdout)

            download = data['download']['bandwidth'] * 8 / 1e6  # Convertendo para Mbps
            upload = data['upload']['bandwidth'] * 8 / 1e6      # Convertendo para Mbps
            ping = data['ping']['latency']

            latest_metrics = (
                f'# HELP internet_download_speed_mbps Download speed in Mbps\n'
                f'# TYPE internet_download_speed_mbps gauge\n'
                f'internet_download_speed_mbps {download:.2f}\n'
                f'# HELP internet_upload_speed_mbps Upload speed in Mbps\n'
                f'# TYPE internet_upload_speed_mbps gauge\n'
                f'internet_upload_speed_mbps {upload:.2f}\n'
                f'# HELP internet_ping_latency_ms Ping latency in ms\n'
                f'# TYPE internet_ping_latency_ms gauge\n'
                f'internet_ping_latency_ms {ping:.2f}\n'
            )
            print(f"[{time.ctime()}] Speedtest completed successfully.")
        except Exception as e:
            latest_metrics = f"# Error: {str(e)}\n"
            print(f"[{time.ctime()}] Error running speedtest: {e}")

        # Aguarda 5 minutos (300 segundos)
        time.sleep(300)

# Endpoint para o Prometheus coletar
@app.route('/metrics')
def metrics():
    return Response(latest_metrics, mimetype='text/plain')

if __name__ == '__main__':
    # Inicia a thread para rodar o speedtest periodicamente
    thread = threading.Thread(target=run_speedtest_periodically)
    thread.daemon = True
    thread.start()

    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=9516)

FROM python:3.11-slim

RUN apt update && apt install -y curl gnupg ca-certificates unzip

RUN pip install flask

# Baixa o binário diretamente do site oficial
RUN curl -L -o /tmp/speedtest-cli.tgz https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-x86_64.tgz && \
    tar -xvzf /tmp/speedtest-cli.tgz -C /usr/local/bin && \
    chmod +x /usr/local/bin/speedtest && \
    rm /tmp/speedtest-cli.tgz

COPY speedtest_exporter.py /app/
WORKDIR /app

CMD ["python", "speedtest_exporter.py"]

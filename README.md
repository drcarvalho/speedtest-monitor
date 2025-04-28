# Monitore sua internet com SpeedTest, Prometheus e Grafana

Este repositório contém a configuração para um sistema de monitoramento de velocidade de internet utilizando o **Speedtest Exporter**, **Prometheus** e **Grafana**. O Speedtest Exporter coleta as métricas de download, upload e latência de ping da sua conexão de internet e as expõe para o Prometheus. O Grafana é usado para visualizar essas métricas.

## Tecnologias

- **Docker**: Utilizado para orquestrar os containers do Speedtest Exporter, Prometheus e Grafana.
- **Speedtest CLI**: Usado para realizar os testes de velocidade de internet.
- **Prometheus**: Coleta e armazena as métricas expostas pelo Speedtest Exporter.
- **Grafana**: Visualiza as métricas armazenadas no Prometheus. user: admin pwd: admin

## Estrutura do Repositório

```plaintext
/
├── docker-compose.yml          # Arquivo de configuração do Docker Compose
├── grafana/                    # Configurações do Grafana (Dashboards, Datasources)
│   ├── dashboards/             # Dashboards do Grafana
│   ├── dashboards.yml          # Configuração para provisionamento dos Dashboards
│   └── datasources/            # Configuração de datasources do Grafana
├── prometheus/                 # Configurações do Prometheus
│   └── prometheus.yml          # Arquivo de configuração do Prometheus
└── speedtest-exporter/         # Código-fonte do Speedtest Exporter
    ├── Dockerfile              # Dockerfile do Speedtest Exporter
    └── speedtest_exporter.py   # Script Python que expõe as métricas do Speedtest

"""
Sistema de Envio Automático de Relatórios - Versão Profissional
Autor: Seu Nome
Data: 2025-01-07

Funcionalidades:
- Geração de múltiplos tipos de gráficos
- Templates HTML profissionais para email
- Configuração segura via variáveis de ambiente
- Agendamento automático de envios
- Logging detalhado e tratamento de erros
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yagmail
import os
from datetime import datetime, timedelta
import logging
import json
from pathlib import Path
from dotenv import load_dotenv
import schedule
import time
import sys

class EmailReportSender:
    def __init__(self):
        """Inicializa o sistema de envio de relatórios."""
        self.setup_logging()
        load_dotenv()  # Carrega variáveis do arquivo .env
        self.validate_environment()
        
    def setup_logging(self):
        """Configura sistema de logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('email_reports.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def validate_environment(self):
        """Valida se todas as variáveis de ambiente necessárias estão configuradas."""
        required_vars = ['EMAIL_SENDER', 'EMAIL_PASSWORD', 'EMAIL_RECIPIENTS']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            self.logger.error(f"Variáveis de ambiente ausentes: {missing_vars}")
            self.logger.info("Crie um arquivo .env com as seguintes variáveis:")
            self.logger.info("EMAIL_SENDER=seu_email@gmail.com")
            self.logger.info("EMAIL_PASSWORD=sua_senha_de_app")
            self.logger.info("EMAIL_RECIPIENTS=destinatario1@email.com,destinatario2@email.com")
            raise ValueError("Configuração de email incompleta")
            
    def load_sales_data(self, file_path="vendas.csv"):
        """Carrega e valida dados de vendas."""
        try:
            if not Path(file_path).exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
                
            df = pd.read_csv(file_path)
            
            # Validações básicas
            if df.empty:
                raise ValueError("Arquivo de vendas está vazio")
                
            required_columns = ['Cliente', 'Vendas']
            missing_cols = set(required_columns) - set(df.columns)
            if missing_cols:
                raise ValueError(f"Colunas ausentes: {missing_cols}")
                
            self.logger.info(f"Dados carregados: {len(df)} registros")
            return df
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar dados: {e}")
            raise
            
    def generate_charts(self, df):
        """Gera múltiplos gráficos profissionais."""
        charts_generated = []
        
        # Configuração do estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        try:
            # 1. Gráfico de barras - Vendas por Cliente
            fig, ax = plt.subplots(figsize=(12, 6))
            bars = ax.bar(df['Cliente'], df['Vendas'], color=sns.color_palette("viridis", len(df)))
            ax.set_title('Vendas por Cliente', fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('Cliente', fontsize=12)
            ax.set_ylabel('Vendas (R$)', fontsize=12)
            
            # Adiciona valores nas barras
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                       f'R$ {height:,.0f}', ha='center', va='bottom', fontweight='bold')
            
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            chart1 = 'grafico_vendas_barras.png'
            plt.savefig(chart1, dpi=300, bbox_inches='tight')
            plt.close()
            charts_generated.append(chart1)
            
            # 2. Gráfico de pizza - Distribuição de vendas
            fig, ax = plt.subplots(figsize=(10, 8))
            colors = sns.color_palette("Set3", len(df))
            wedges, texts, autotexts = ax.pie(df['Vendas'], labels=df['Cliente'], 
                                            autopct='%1.1f%%', colors=colors, startangle=90)
            
            # Melhora a formatação
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                autotext.set_fontsize(10)
                
            ax.set_title('Distribuição de Vendas por Cliente', fontsize=16, fontweight='bold', pad=20)
            chart2 = 'grafico_vendas_pizza.png'
            plt.savefig(chart2, dpi=300, bbox_inches='tight')
            plt.close()
            charts_generated.append(chart2)
            
            # 3. Gráfico de linha com tendência (simulado)
            fig, ax = plt.subplots(figsize=(12, 6))
            # Simula dados temporais para demonstração
            dates = pd.date_range(start='2024-01-01', periods=len(df), freq='M')
            ax.plot(dates, df['Vendas'].values, marker='o', linewidth=3, markersize=8)
            ax.set_title('Evolução das Vendas ao Longo do Tempo', fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('Período', fontsize=12)
            ax.set_ylabel('Vendas (R$)', fontsize=12)
            ax.grid(True, alpha=0.3)
            
            # Formatação do eixo Y
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
            plt.xticks(rotation=45)
            plt.tight_layout()
            chart3 = 'grafico_vendas_linha.png'
            plt.savefig(chart3, dpi=300, bbox_inches='tight')
            plt.close()
            charts_generated.append(chart3)
            
            self.logger.info(f"Gráficos gerados: {len(charts_generated)}")
            return charts_generated
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar gráficos: {e}")
            raise
            
    def calculate_statistics(self, df):
        """Calcula estatísticas detalhadas dos dados."""
        stats = {
            'total_vendas': float(df['Vendas'].sum()),
            'media_vendas': float(df['Vendas'].mean()),
            'maior_venda': float(df['Vendas'].max()),
            'menor_venda': float(df['Vendas'].min()),
            'cliente_top': df.loc[df['Vendas'].idxmax(), 'Cliente'],
            'total_clientes': len(df),
            'data_relatorio': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'vendas_acima_media': len(df[df['Vendas'] > df['Vendas'].mean()]),
            'percentual_top_cliente': float((df['Vendas'].max() / df['Vendas'].sum()) * 100)
        }
        return stats
        
    def create_html_template(self, stats):
        """Cria template HTML profissional para o email."""
        html_template = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Vendas</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f8f9fa;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .stats-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }}
                .stat-card {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    text-align: center;
                    border-left: 4px solid #667eea;
                }}
                .stat-value {{
                    font-size: 2em;
                    font-weight: bold;
                    color: #667eea;
                    margin: 10px 0;
                }}
                .stat-label {{
                    color: #666;
                    font-size: 0.9em;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                .charts-section {{
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    margin: 30px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding: 20px;
                    background: #667eea;
                    color: white;
                    border-radius: 10px;
                }}
                .highlight {{
                    background: #e3f2fd;
                    padding: 15px;
                    border-radius: 5px;
                    border-left: 4px solid #2196f3;
                    margin: 20px 0;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📊 Relatório de Vendas</h1>
                <p>Gerado automaticamente em {stats['data_relatorio']}</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">R$ {stats['total_vendas']:,.2f}</div>
                    <div class="stat-label">Total de Vendas</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">R$ {stats['media_vendas']:,.2f}</div>
                    <div class="stat-label">Média por Cliente</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{stats['total_clientes']}</div>
                    <div class="stat-label">Total de Clientes</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{stats['percentual_top_cliente']:.1f}%</div>
                    <div class="stat-label">Share do Top Cliente</div>
                </div>
            </div>
            
            <div class="highlight">
                <h3>🏆 Destaque do Período</h3>
                <p><strong>{stats['cliente_top']}</strong> foi o cliente com maior volume de vendas: 
                <strong>R$ {stats['maior_venda']:,.2f}</strong></p>
                <p>{stats['vendas_acima_media']} de {stats['total_clientes']} clientes ficaram acima da média.</p>
            </div>
            
            <div class="charts-section">
                <h3>📈 Análises Visuais</h3>
                <p>Os gráficos detalhados estão em anexo para análise mais aprofundada.</p>
            </div>
            
            <div class="footer">
                <p>Relatório gerado automaticamente pelo Sistema de Análise de Vendas</p>
                <p>Para dúvidas ou sugestões, entre em contato conosco.</p>
            </div>
        </body>
        </html>
        """
        return html_template
        
    def send_email(self, charts, stats):
        """Envia email com relatório e gráficos."""
        try:
            # Configurações do email
            sender_email = os.getenv('EMAIL_SENDER')
            sender_password = os.getenv('EMAIL_PASSWORD')
            recipients = os.getenv('EMAIL_RECIPIENTS').split(',')
            
            # Cria conteúdo HTML
            html_content = self.create_html_template(stats)
            
            # Configura cliente de email
            yag = yagmail.SMTP(sender_email, sender_password)
            
            # Prepara anexos
            attachments = charts.copy()
            
            # Envia email
            subject = f"📊 Relatório de Vendas - {stats['data_relatorio']}"
            
            yag.send(
                to=recipients,
                subject=subject,
                contents=html_content,
                attachments=attachments
            )
            
            self.logger.info(f"Email enviado com sucesso para {len(recipients)} destinatário(s)")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao enviar email: {e}")
            return False
            
    def generate_and_send_report(self):
        """Processo completo de geração e envio do relatório."""
        try:
            self.logger.info("Iniciando geração de relatório automatizado")
            
            # Carrega dados
            df = self.load_sales_data()
            
            # Gera gráficos
            charts = self.generate_charts(df)
            
            # Calcula estatísticas
            stats = self.calculate_statistics(df)
            
            # Envia email
            success = self.send_email(charts, stats)
            
            if success:
                self.logger.info("Relatório enviado com sucesso!")
                return True
            else:
                self.logger.error("Falha no envio do relatório")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro no processo de relatório: {e}")
            return False
            
    def schedule_reports(self):
        """Agenda envios automáticos de relatórios."""
        # Agenda para toda segunda-feira às 9h
        schedule.every().monday.at("09:00").do(self.generate_and_send_report)
        
        # Agenda para todo dia 1º do mês às 8h
        schedule.every().day.at("08:00").do(self._check_monthly_report)
        
        self.logger.info("Agendamentos configurados:")
        self.logger.info("- Relatório semanal: Segunda-feira às 9h")
        self.logger.info("- Relatório mensal: Todo dia 1º às 8h")
        
        print("Sistema de relatórios automáticos iniciado...")
        print("Pressione Ctrl+C para parar")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Verifica a cada minuto
        except KeyboardInterrupt:
            self.logger.info("Sistema de agendamento interrompido pelo usuário")
            
    def _check_monthly_report(self):
        """Verifica se é o primeiro dia do mês para envio mensal."""
        if datetime.now().day == 1:
            self.logger.info("Enviando relatório mensal")
            self.generate_and_send_report()

if __name__ == "__main__":
    # Cria instância do sistema
    email_system = EmailReportSender()
    
    # Verifica argumentos da linha de comando
    if len(sys.argv) > 1 and sys.argv[1] == "--schedule":
        # Modo agendamento
        email_system.schedule_reports()
    else:
        # Envio único
        success = email_system.generate_and_send_report()
        if not success:
            sys.exit(1)

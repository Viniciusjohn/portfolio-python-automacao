"""
Relatório Automatizado de Vendas - Versão Profissional
Autor: Seu Nome
Data: 2025-01-07

Funcionalidades:
- Leitura e validação de dados CSV
- Filtragem configurável de vendas
- Geração de relatórios detalhados
- Logging completo de operações
- Tratamento robusto de erros
"""

import pandas as pd
import json
import logging
from datetime import datetime
from pathlib import Path
import sys

class RelatorioVendas:
    def __init__(self, config_file="config.json"):
        """Inicializa o gerador de relatórios com configurações."""
        self.setup_logging()
        self.config = self.load_config(config_file)
        
    def setup_logging(self):
        """Configura sistema de logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('relatorio_vendas.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def load_config(self, config_file):
        """Carrega configurações do arquivo JSON."""
        try:
            if Path(config_file).exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                self.logger.info(f"Configurações carregadas de {config_file}")
                return config
            else:
                # Configurações padrão
                default_config = {
                    "arquivo_entrada": "vendas.csv",
                    "arquivo_saida": "vendas_filtradas.csv",
                    "valor_minimo": 1000,
                    "colunas_obrigatorias": ["Cliente", "Vendas"],
                    "formato_data": "%Y-%m-%d %H:%M:%S"
                }
                self.save_config(default_config, config_file)
                self.logger.info(f"Arquivo de configuração criado: {config_file}")
                return default_config
        except Exception as e:
            self.logger.error(f"Erro ao carregar configurações: {e}")
            raise
            
    def save_config(self, config, config_file):
        """Salva configurações no arquivo JSON."""
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
            
    def validate_data(self, df):
        """Valida estrutura e qualidade dos dados."""
        errors = []
        
        # Verifica colunas obrigatórias
        missing_cols = set(self.config["colunas_obrigatorias"]) - set(df.columns)
        if missing_cols:
            errors.append(f"Colunas ausentes: {missing_cols}")
            
        # Verifica dados vazios
        if df.empty:
            errors.append("Dataset está vazio")
            
        # Verifica valores negativos em Vendas
        if 'Vendas' in df.columns and (df['Vendas'] < 0).any():
            errors.append("Encontrados valores negativos na coluna Vendas")
            
        # Verifica duplicatas
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            self.logger.warning(f"Encontradas {duplicates} linhas duplicadas")
            
        if errors:
            raise ValueError(f"Erros de validação: {'; '.join(errors)}")
            
        self.logger.info("Validação de dados concluída com sucesso")
        return True
        
    def load_data(self):
        """Carrega dados do arquivo CSV com validação."""
        try:
            arquivo = self.config["arquivo_entrada"]
            if not Path(arquivo).exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")
                
            df = pd.read_csv(arquivo)
            self.logger.info(f"Dados carregados: {len(df)} registros de {arquivo}")
            
            self.validate_data(df)
            return df
            
        except Exception as e:
            self.logger.error(f"Erro ao carregar dados: {e}")
            raise
            
    def filter_sales(self, df):
        """Filtra vendas baseado no valor mínimo configurado."""
        valor_minimo = self.config["valor_minimo"]
        
        df_original_count = len(df)
        df_filtrado = df[df["Vendas"] > valor_minimo].copy()
        df_filtrado_count = len(df_filtrado)
        
        self.logger.info(f"Filtro aplicado: vendas > {valor_minimo}")
        self.logger.info(f"Registros filtrados: {df_filtrado_count}/{df_original_count}")
        
        return df_filtrado
        
    def generate_statistics(self, df_original, df_filtrado):
        """Gera estatísticas detalhadas dos dados."""
        stats = {
            "timestamp": datetime.now().strftime(self.config["formato_data"]),
            "total_registros_original": len(df_original),
            "total_registros_filtrados": len(df_filtrado),
            "valor_minimo_filtro": self.config["valor_minimo"],
            "vendas_originais": {
                "total": float(df_original["Vendas"].sum()),
                "media": float(df_original["Vendas"].mean()),
                "maximo": float(df_original["Vendas"].max()),
                "minimo": float(df_original["Vendas"].min())
            },
            "vendas_filtradas": {
                "total": float(df_filtrado["Vendas"].sum()) if not df_filtrado.empty else 0,
                "media": float(df_filtrado["Vendas"].mean()) if not df_filtrado.empty else 0,
                "maximo": float(df_filtrado["Vendas"].max()) if not df_filtrado.empty else 0,
                "minimo": float(df_filtrado["Vendas"].min()) if not df_filtrado.empty else 0
            }
        }
        
        return stats
        
    def save_results(self, df_filtrado, stats):
        """Salva resultados filtrados e estatísticas."""
        # Salva CSV filtrado
        arquivo_saida = self.config["arquivo_saida"]
        df_filtrado.to_csv(arquivo_saida, index=False)
        self.logger.info(f"Dados filtrados salvos em: {arquivo_saida}")
        
        # Salva estatísticas
        stats_file = "relatorio_estatisticas.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=4, ensure_ascii=False)
        self.logger.info(f"Estatísticas salvas em: {stats_file}")
        
        return arquivo_saida, stats_file
        
    def print_summary(self, stats):
        """Imprime resumo formatado dos resultados."""
        print("\n" + "="*60)
        print("RELATORIO DE VENDAS - RESUMO EXECUTIVO")
        print("="*60)
        print(f"Processado em: {stats['timestamp']}")
        print(f"Registros processados: {stats['total_registros_original']}")
        print(f"Registros qualificados: {stats['total_registros_filtrados']}")
        print(f"Filtro aplicado: vendas > R$ {stats['valor_minimo_filtro']:,.2f}")
        
        print(f"\nVENDAS TOTAIS:")
        print(f"   Total Geral: R$ {stats['vendas_originais']['total']:,.2f}")
        print(f"   Media Geral: R$ {stats['vendas_originais']['media']:,.2f}")
        
        if stats['total_registros_filtrados'] > 0:
            print(f"\nVENDAS QUALIFICADAS:")
            print(f"   Total Qualificado: R$ {stats['vendas_filtradas']['total']:,.2f}")
            print(f"   Media Qualificada: R$ {stats['vendas_filtradas']['media']:,.2f}")
            print(f"   Maior Venda: R$ {stats['vendas_filtradas']['maximo']:,.2f}")
        else:
            print(f"\nNenhuma venda atende ao criterio minimo de R$ {stats['valor_minimo_filtro']:,.2f}")
            
        print("="*60)
        
    def run(self):
        """Executa o processo completo de geração de relatório."""
        try:
            self.logger.info("Iniciando geração de relatório de vendas")
            
            # Carrega dados
            df_original = self.load_data()
            
            # Aplica filtros
            df_filtrado = self.filter_sales(df_original)
            
            # Gera estatísticas
            stats = self.generate_statistics(df_original, df_filtrado)
            
            # Salva resultados
            arquivo_csv, arquivo_stats = self.save_results(df_filtrado, stats)
            
            # Exibe resumo
            self.print_summary(stats)
            
            self.logger.info("Relatório gerado com sucesso!")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro na geração do relatório: {e}")
            return False

if __name__ == "__main__":
    # Executa o relatório
    relatorio = RelatorioVendas()
    success = relatorio.run()
    
    if not success:
        sys.exit(1)

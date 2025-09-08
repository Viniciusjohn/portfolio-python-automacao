"""
Dashboard Interativo de Vendas - Versão Profissional
Autor: Seu Nome
Data: 2025-01-07

Funcionalidades:
- Interface web moderna com Streamlit
- Múltiplas visualizações interativas
- Filtros dinâmicos
- Exportação de relatórios
- Métricas em tempo real
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import json
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

class SalesDashboard:
    def __init__(self):
        """Inicializa o dashboard de vendas."""
        self.load_custom_css()
        
    def load_custom_css(self):
        """Carrega CSS customizado para melhorar a aparência."""
        st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
        }
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        }
        </style>
        """, unsafe_allow_html=True)
        
    def load_data(self, file_path="vendas.csv"):
        """Carrega dados de vendas com cache."""
        try:
            df = pd.read_csv(file_path)
            
            # Adiciona dados simulados para demonstração mais rica
            if len(df) < 10:
                # Expande dataset para demonstração
                additional_data = {
                    'Cliente': ['Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia'],
                    'Vendas': [2200, 890, 1650, 3100, 750, 1980]
                }
                df_additional = pd.DataFrame(additional_data)
                df = pd.concat([df, df_additional], ignore_index=True)
            
            # Adiciona colunas simuladas para análise mais rica
            np.random.seed(42)
            df['Regiao'] = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], len(df))
            df['Categoria'] = np.random.choice(['Premium', 'Standard', 'Basic'], len(df))
            df['Data_Venda'] = pd.date_range(start='2024-01-01', periods=len(df), freq='W')
            df['Meta'] = df['Vendas'] * np.random.uniform(0.8, 1.2, len(df))
            
            return df
            
        except FileNotFoundError:
            st.error("Arquivo vendas.csv não encontrado!")
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()
            
    def create_metrics_cards(self, df, filtered_df):
        """Cria cards de métricas principais."""
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_vendas = filtered_df['Vendas'].sum()
            delta_vendas = total_vendas - df['Vendas'].sum() if len(filtered_df) != len(df) else None
            st.metric(
                label="💰 Total de Vendas",
                value=f"R$ {total_vendas:,.2f}",
                delta=f"R$ {delta_vendas:,.2f}" if delta_vendas else None
            )
            
        with col2:
            media_vendas = filtered_df['Vendas'].mean()
            st.metric(
                label="📊 Média por Cliente",
                value=f"R$ {media_vendas:,.2f}"
            )
            
        with col3:
            total_clientes = len(filtered_df)
            st.metric(
                label="👥 Total de Clientes",
                value=total_clientes
            )
            
        with col4:
            if not filtered_df.empty:
                top_cliente = filtered_df.loc[filtered_df['Vendas'].idxmax(), 'Cliente']
                top_valor = filtered_df['Vendas'].max()
                st.metric(
                    label="🏆 Top Cliente",
                    value=f"{top_cliente}",
                    delta=f"R$ {top_valor:,.2f}"
                )
                
    def create_sales_chart(self, df):
        """Cria gráfico principal de vendas."""
        fig = px.bar(
            df, 
            x='Cliente', 
            y='Vendas',
            color='Categoria',
            title="Vendas por Cliente e Categoria",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            xaxis_title="Cliente",
            yaxis_title="Vendas (R$)",
            showlegend=True,
            height=500
        )
        
        # Adiciona valores nas barras
        fig.update_traces(texttemplate='R$ %{y:,.0f}', textposition='outside')
        
        return fig
        
    def create_regional_analysis(self, df):
        """Cria análise por região."""
        regional_data = df.groupby('Regiao')['Vendas'].agg(['sum', 'mean', 'count']).reset_index()
        regional_data.columns = ['Regiao', 'Total', 'Media', 'Clientes']
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Vendas por Região', 'Clientes por Região'),
            specs=[[{"type": "xy"}, {"type": "domain"}]]
        )
        
        # Gráfico de barras
        fig.add_trace(
            go.Bar(x=regional_data['Regiao'], y=regional_data['Total'], 
                   name='Total de Vendas', marker_color='lightblue'),
            row=1, col=1
        )
        
        # Gráfico de pizza
        fig.add_trace(
            go.Pie(labels=regional_data['Regiao'], values=regional_data['Clientes'], 
                   name="Clientes"),
            row=1, col=2
        )
        
        fig.update_layout(height=400, showlegend=False)
        return fig
        
    def create_trend_analysis(self, df):
        """Cria análise de tendência temporal."""
        # Agrupa por data
        trend_data = df.groupby('Data_Venda')['Vendas'].sum().reset_index()
        
        fig = go.Figure()
        
        # Linha de vendas
        fig.add_trace(go.Scatter(
            x=trend_data['Data_Venda'],
            y=trend_data['Vendas'],
            mode='lines+markers',
            name='Vendas Reais',
            line=dict(color='#667eea', width=3),
            marker=dict(size=8)
        ))
        
        # Linha de tendência
        z = np.polyfit(range(len(trend_data)), trend_data['Vendas'], 1)
        p = np.poly1d(z)
        fig.add_trace(go.Scatter(
            x=trend_data['Data_Venda'],
            y=p(range(len(trend_data))),
            mode='lines',
            name='Tendência',
            line=dict(color='red', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Evolução das Vendas ao Longo do Tempo",
            xaxis_title="Data",
            yaxis_title="Vendas (R$)",
            height=400
        )
        
        return fig
        
    def create_performance_analysis(self, df):
        """Cria análise de performance vs meta."""
        df['Performance'] = (df['Vendas'] / df['Meta']) * 100
        df['Status'] = df['Performance'].apply(
            lambda x: '🟢 Acima da Meta' if x >= 100 else 
                     '🟡 Próximo da Meta' if x >= 80 else '🔴 Abaixo da Meta'
        )
        
        fig = px.scatter(
            df, 
            x='Meta', 
            y='Vendas',
            color='Status',
            size='Performance',
            hover_data=['Cliente', 'Performance'],
            title="Performance vs Meta por Cliente"
        )
        
        # Adiciona linha de referência (meta = vendas)
        max_val = max(df['Meta'].max(), df['Vendas'].max())
        fig.add_trace(go.Scatter(
            x=[0, max_val],
            y=[0, max_val],
            mode='lines',
            name='Linha de Meta',
            line=dict(color='gray', dash='dash')
        ))
        
        fig.update_layout(height=500)
        return fig
        
    def export_report(self, df):
        """Gera relatório para download."""
        # Cria resumo estatístico
        summary = {
            'Data do Relatório': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'Total de Vendas': f"R$ {df['Vendas'].sum():,.2f}",
            'Média de Vendas': f"R$ {df['Vendas'].mean():,.2f}",
            'Total de Clientes': len(df),
            'Maior Venda': f"R$ {df['Vendas'].max():,.2f}",
            'Cliente Top': df.loc[df['Vendas'].idxmax(), 'Cliente'],
            'Região com Mais Vendas': df.groupby('Regiao')['Vendas'].sum().idxmax()
        }
        
        # Converte para JSON
        json_string = json.dumps(summary, indent=2, ensure_ascii=False)
        
        return json_string
        
    def run_dashboard(self):
        """Executa o dashboard principal."""
        # Header
        st.markdown("""
        <div class="main-header">
            <h1>📊 Dashboard de Vendas Profissional</h1>
            <p>Análise completa e interativa dos dados de vendas</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Carrega dados
        df = self.load_data()
        
        if df.empty:
            st.stop()
            
        # Sidebar com filtros
        st.sidebar.header("🔍 Filtros")
        
        # Filtro por região
        regioes_selecionadas = st.sidebar.multiselect(
            "Selecione as Regiões:",
            options=df['Regiao'].unique(),
            default=df['Regiao'].unique()
        )
        
        # Filtro por categoria
        categorias_selecionadas = st.sidebar.multiselect(
            "Selecione as Categorias:",
            options=df['Categoria'].unique(),
            default=df['Categoria'].unique()
        )
        
        # Filtro por valor mínimo
        valor_minimo = st.sidebar.slider(
            "Valor Mínimo de Vendas:",
            min_value=0,
            max_value=int(df['Vendas'].max()),
            value=0,
            step=100
        )
        
        # Aplica filtros
        filtered_df = df[
            (df['Regiao'].isin(regioes_selecionadas)) &
            (df['Categoria'].isin(categorias_selecionadas)) &
            (df['Vendas'] >= valor_minimo)
        ]
        
        # Métricas principais
        st.subheader("📈 Métricas Principais")
        self.create_metrics_cards(df, filtered_df)
        
        # Gráficos principais
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Vendas por Cliente")
            if not filtered_df.empty:
                fig1 = self.create_sales_chart(filtered_df)
                st.plotly_chart(fig1, use_container_width=True)
            else:
                st.warning("Nenhum dado encontrado com os filtros aplicados")
                
        with col2:
            st.subheader("🗺️ Análise Regional")
            if not filtered_df.empty:
                fig2 = self.create_regional_analysis(filtered_df)
                st.plotly_chart(fig2, use_container_width=True)
        
        # Análises avançadas
        st.subheader("📈 Análises Avançadas")
        
        tab1, tab2, tab3 = st.tabs(["Tendência Temporal", "Performance vs Meta", "Dados Detalhados"])
        
        with tab1:
            if not filtered_df.empty:
                fig3 = self.create_trend_analysis(filtered_df)
                st.plotly_chart(fig3, use_container_width=True)
                
        with tab2:
            if not filtered_df.empty:
                fig4 = self.create_performance_analysis(filtered_df)
                st.plotly_chart(fig4, use_container_width=True)
                
        with tab3:
            st.subheader("Tabela de Dados")
            st.dataframe(filtered_df, use_container_width=True)
            
            # Botão de download
            if st.button("📥 Gerar Relatório"):
                report_json = self.export_report(filtered_df)
                st.download_button(
                    label="Download Relatório JSON",
                    data=report_json,
                    file_name=f"relatorio_vendas_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                    mime="application/json"
                )
        
        # Footer
        st.markdown("---")
        st.markdown(
            "<div style='text-align: center; color: #666;'>"
            "Dashboard desenvolvido com Streamlit | "
            f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            "</div>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    dashboard = SalesDashboard()
    dashboard.run_dashboard()

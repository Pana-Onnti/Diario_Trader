import plotly.express as px
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go

import plotly.express as px
import plotly.io as pio

ancho = 200
alto = 75

# Definir constante para los valores de layout que se repiten
LAYOUT = dict(
    autosize=False,
    width=ancho,
    height=alto,
    margin=dict(l=1, r=1, b=1, t=1, pad=1),
    paper_bgcolor="white",
    hovermode=False
)

from retorno_v1 import retornos
def generar_grafico_area():
    # Obtener datos de ejemplo
    df = px.data.stocks(indexed=True) - 1
    ## TOTAL VALUE ###

    df = retornos()
    #df = df['total_return']
    
    #df['total_value'] = df.sum(axis=1)
    # Crear figura de área
    fig = px.area(df, x=df.index, y="cumulative_return")
    
    # Actualizar los ejes del gráfico
    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title=None,
            tickmode='array',
            ticks=''
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title=None,
            tickmode='array',
            ticks=''
        )
    )
    
    # Actualizar las propiedades de las líneas del gráfico
    fig.update_traces(line={'color': '#3782cd'})
    fig.update_traces(line=dict(width=1.5))

    # Actualizar el layout de la figura
    fig.update_layout(
        LAYOUT,
        plot_bgcolor='rgba(26, 28, 45, 1)'
    )

    # Configurar la salida del gráfico
    config = {'displayModeBar': False, 'responsive': True}
    graph = pio.to_html(fig, full_html=False, config=config)
    
    return graph



def generar_grafico_pie():
    # Definir los valores de las secciones del pastel
    valores = [4500, 2500]

    # Crear la figura
    colores_secciones = ['#9b3232', '#4D5F2F']
    color_fondo = 'rgba(26, 28, 45, 1)'
    fig = go.Figure(data=[go.Pie(values=valores, hole=.8, marker=dict(colors=colores_secciones))])

    # Configurar opciones de visualización
    fig.update_traces(textinfo='none')
    fig.update_layout(showlegend=False, title=None, hovermode=False, autosize=False, width=ancho, height=alto, margin=dict(l=1, r=1, b=15, t=15, pad=1), paper_bgcolor=color_fondo, plot_bgcolor=color_fondo)
    fig.update_traces(textfont_color='white')

    # Configurar opciones de exportación
    config = {'displayModeBar': False, 'responsive': True}
    graph = pio.to_html(fig, full_html=False, config=config)

    return graph


def generate_long_bar_chart():
    df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    
    fig = px.bar(df, y='pop', x='country', text='pop')
    
    # Establecer títulos en None
    fig.update_layout(title=None)
    
    # Configurar opciones de visualización
    fig.update_layout(
        autosize=False,
        width=400,
        height=600,
        margin=dict(l=1, r=10, b=15, t=15, pad=1),
        paper_bgcolor="rgba(26, 28, 45, 1)",
        hovermode=False,
        plot_bgcolor="#7F8C8D"
    )
    
    # Establecer texto en notación científica
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    
    # Establecer el color de la barra
    fig.update_traces(marker_color='#3782cd')
    
    # Configurar opciones de ejes
    fig.update_layout(xaxis=dict(zeroline=False, showgrid=False),
                      yaxis=dict(zeroline=False, showgrid=False))
    fig.update_xaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
    fig.update_yaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
    
    # Configurar opciones de fondo
    fig.update_layout(plot_bgcolor='rgba(26, 28, 45, 1)', showlegend=False)
    
    # Configurar opciones de la grilla y el color de las etiquetas
    fig.update_xaxes(showgrid=False, tickfont=dict(color='white'))
    fig.update_yaxes(showgrid=False, tickfont=dict(color='white'))

    # Configurar las opciones de la figura
    config = {'displayModeBar': False, 'responsive': True}
    
    # Convertir la figura en HTML
    graph = pio.to_html(fig, full_html=False, config=config)
    return graph

    

def generate_dif_bar_chart():
        
    years = ['2016', '2017', '2018', '2019']

    fig = go.Figure()
        
    fig.add_trace(go.Bar(x=years, y=[-500, -600, -700],
                         marker_color='#4D5F2F',
                         name='expenses'))
    
    fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                         marker_color='#9b3232',
                         name='revenue'))
    
    fig.update_layout(title=None,
                      autosize=False,
                      width=300,
                      height=600,
                      margin=dict(l=1, r=1, b=15, t=15, pad=1),
                      paper_bgcolor="rgba(26, 28, 45, 1)",
                      hovermode=False,
                      showlegend=False,
                      plot_bgcolor='rgba(26, 28, 45, 1)')
    
    fig.update_layout(xaxis=dict(zeroline=False, showgrid=False), 
                      yaxis=dict(zeroline=False, showgrid=False))
    
    fig.update_xaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))
    fig.update_yaxes(showgrid=False, tickfont=dict(color='hsla(208, 100%, 97%, 0.616)'))

    config = {'displayModeBar': False, 'responsive': True}

    graph = pio.to_html(fig, full_html=False, config=config)
    
    return graph

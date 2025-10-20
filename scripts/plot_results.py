# scripts/plot_results.py
# ---------------------------------------------------------------
# Lee experiments/results.csv y genera dos gráficas:
#  - tiempo (time_s) por caso comparando A* vs IDA*
#  - nodos expandidos (nodes_expanded) por caso comparando A* vs IDA*
#
# Requisitos: pandas, matplotlib
# Uso: python scripts/plot_results.py
# ---------------------------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = 'experiments/results.csv'
OUT_DIR = 'experiments'

def safe_float(x):
    try:
        return float(x)
    except:
        return float('nan')

def plot_time(df):
    df_time = df.pivot(index='case', columns='algorithm', values='time_s')
    df_time = df_time.sort_index()
    ax = df_time.plot(kind='bar', rot=0, title='Tiempo (s) por caso: A* vs IDA*')
    ax.set_ylabel('Tiempo (s)')
    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'plots_time.png')
    plt.savefig(out)
    print('Guardado:', out)
    plt.close()

def plot_nodes(df):
    df_nodes = df.pivot(index='case', columns='algorithm', values='nodes_expanded')
    df_nodes = df_nodes.sort_index()
    ax = df_nodes.plot(kind='bar', rot=0, title='Nodos expandidos por caso: A* vs IDA*')
    ax.set_ylabel('Nodos expandidos')
    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'plots_nodes.png')
    plt.savefig(out)
    print('Guardado:', out)
    plt.close()

def main():
    if not os.path.exists(CSV_PATH):
        print('No se encontró', CSV_PATH)
        return
    df = pd.read_csv(CSV_PATH)
    # Convertir columnas numéricas seguras
    df['time_s'] = df['time_s'].apply(safe_float)
    df['nodes_expanded'] = df['nodes_expanded'].apply(safe_float)
    plot_time(df)
    plot_nodes(df)
    print('Plotting completado.')

if __name__ == "__main__":
    main()

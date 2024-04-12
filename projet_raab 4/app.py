import collections
from flask import Flask, render_template
# import plotly
import plotly.graph_objs as go
import pandas as pd
import json 
import sqlite3
import plotly.offline as pyo
import time
from flask import jsonify
import pandas as pd
# import seaborn as sns
# import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import traitement 

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('base_de_donnees.db')
    data = pd.read_sql_query("SELECT * from power_data", conn)
    conn.close()

    # Convert 'Date' and 'Time' to datetime
    # data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %H:%M:%S')
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %I:%M:%S %p')

    data = data.drop(['Date', 'Time'], axis=1)

    # Suppression des lignes avec des valeurs manquantes
    data = data.dropna()

    # Sort the data by 'Datetime'
    data = data.sort_values('Datetime')

    # Séparation des données en caractéristiques et cibles
    X_data = data.drop(['Datetime'], axis=1)
    Datetime_data = data['Datetime']

    # Normalisation des caractéristiques
    scaler = StandardScaler()
    X_data_normalized = pd.DataFrame(scaler.fit_transform(X_data), index=X_data.index, columns=X_data.columns)

    # Reconstruction des données
    data_normalized = pd.concat([Datetime_data, X_data_normalized], axis=1)

    # Entraîner le modèle d'Isolation Forest
    model = IsolationForest(contamination=0.001)  
    model.fit(X_data_normalized)

    # Prédire les anomalies
    data_normalized['anomaly'] = model.predict(X_data_normalized)

    # Create the scatter plot for data with IsolationForest applied
    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=data_normalized.loc[data_normalized['anomaly'] == 1, 'Datetime'],
            y=data_normalized.loc[data_normalized['anomaly'] == 1, 'Global_active_power'],
            mode='markers',
            marker=dict(color='blue'),
            name='Normal'
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=data_normalized.loc[data_normalized['anomaly'] == -1, 'Datetime'],
            y=data_normalized.loc[data_normalized['anomaly'] == -1, 'Global_active_power'],
            mode='markers',
            marker=dict(color='red'),
            name='Anomaly'
        )
    )
    fig1.update_layout(
        title='Power Consumption',
        xaxis_title='Datetime',
        yaxis_title='Global Active Power',
        plot_bgcolor='white'
    )

    # Group original data by year and month, and calculate the mean of 'Global_active_power'
    original_data_monthly = data.groupby([data['Datetime'].dt.strftime('%Y-%m')])['Global_active_power'].mean().reset_index()
    original_data_monthly['Month'] = pd.to_datetime(original_data_monthly['Datetime']).dt.strftime('%m/%y')

    # Calculate moving average for 'Global_active_power'
    moving_average = original_data_monthly['Global_active_power'].rolling(window=2).mean()

    # Create the scatter plot for data with IsolationForest applied
    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=data_normalized.loc[data_normalized['anomaly'] == 1, 'Datetime'],
            y=data_normalized.loc[data_normalized['anomaly'] == 1, 'Global_active_power'],
            mode='markers',
            marker=dict(color='blue'),
            name='Normal'
        )
    )
    fig1.add_trace(
        go.Scatter(
            x=data_normalized.loc[data_normalized['anomaly'] == -1, 'Datetime'],
            y=data_normalized.loc[data_normalized['anomaly'] == -1, 'Global_active_power'],
            mode='markers',
            marker=dict(color='red'),
            name='Anomaly'
        )
    )
    fig1.update_layout(
        title='Power Consumption',
        xaxis_title='Datetime',
        yaxis_title='Global Active Power',
        plot_bgcolor='white'
    )

    # Create the bar plot for original data
    fig2 = go.Figure()
    fig2.add_trace(
        go.Bar(
            x=original_data_monthly['Month'],
            y=original_data_monthly['Global_active_power'],
            marker=dict(color='green'),
            name='Global Active Power (Original)'
        )
    )
    # Add moving average line to the bar plot
    fig2.add_trace(
        go.Scatter(
            x=original_data_monthly['Month'],
            y=moving_average,
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Moving Average'
        )
    )

    fig2.update_layout(
        title='Average Global Active Power by Month (Original)',
        xaxis_title='Month',
        yaxis_title='Average Global Active Power',
        plot_bgcolor='white'
    )

    plot_div1 = pyo.plot(fig1, output_type='div')
    plot_div2 = pyo.plot(fig2, output_type='div')

    return render_template('index.html', plot_div1=plot_div1, plot_div2=plot_div2)

@app.route('/data', methods=['GET'])
def data():
    data = json.loads(traitement.get_data())
    return jsonify(data)

if __name__ == '__main__':
    print("aaaaaaaa")
    app.run(debug=True)
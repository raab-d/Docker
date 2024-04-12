import pandas as pd
import sqlite3
from flask import render_template
import plotly.graph_objs as go
import plotly.offline as pyo
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import collections
import json

def get_data():
    conn = sqlite3.connect('base_de_donnees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM power_data")
    rows = cursor.fetchall()
    # Convert query to objects of key-value pairs
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['date'] = row[0]
        d['time'] = row[1]
        d['global_active_power'] = row[2]
        d['global_reactive_power'] = row[3]
        d['voltage'] = row[4]
        d['global_intensity'] = row[5]
        d['sub_metering_1'] = row[6]
        d['sub_metering_2'] = row[7]
        d['sub_metering_3'] = row[8]
        objects_list.append(d)
    return json.dumps(objects_list)
    
def main():
    print('Bien reussi')  # Print 

if __name__ == '__main__':
    main()

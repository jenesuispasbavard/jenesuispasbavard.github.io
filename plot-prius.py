import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

r1 = pd.read_csv('~/OneDrive/ThingsToDo/Prius/Torque/trackLog-2022-Jul-23_16-27-40.csv')
r1['time'] = pd.to_datetime(r1['GPS Time'])

r2 = pd.read_csv('~/OneDrive/ThingsToDo/Prius/Torque/trackLog-2022-Jul-23_17-19-19.csv')
r2['time'] = pd.to_datetime(r2['GPS Time'])


def f(x):
    try:
        return np.float(x)
    except:
        return np.nan

r2['Fuel Trim Bank 1 Short Term(%)'] = r2['Fuel Trim Bank 1 Short Term(%)'].apply(f)
r2['Fuel Trim Bank 1 Long Term(%)'] = r2['Fuel Trim Bank 1 Long Term(%)'].apply(f)
r2['Air Fuel Ratio(Commanded)(:1)'] = r2['Air Fuel Ratio(Commanded)(:1)'].apply(f)
r2['Air Fuel Ratio(Measured)(:1)'] = r2['Air Fuel Ratio(Measured)(:1)'].apply(f)

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r1['time'], y=r1['[PRIUS]Engine Speed(RPM)'], name="RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['O2 Bank 1 Sensor 1 Wide Range Voltage(V)'], name="O2B1S1"),secondary_y=True)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['O2 Bank 1 Sensor 2 Voltage(V)'], name="O2B1S2"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both O2 sensors V (there)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="O2 Bank 1 Sensor 1/2 Voltage(V)", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,16,36,00),datetime(2022,7,23,16,51,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-o2both-there.html',include_plotlyjs='directory')

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r2['time'], y=r2['[PRIUS]Engine Speed(RPM)'], name="RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['O2 Bank 1 Sensor 1 Wide Range Voltage(V)'], name="O2B1S1"),secondary_y=True)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['O2 Bank 1 Sensor 2 Voltage(V)'], name="O2B1S2"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both O2 sensors V (back)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="O2 Bank 1 Sensor 1/2 Voltage(V)", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,17,28,00),datetime(2022,7,23,17,43,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-o2both-back.html',include_plotlyjs='directory')


fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r1['time'], y=r1['[PRIUS]Engine Speed(RPM)'], name="Engine RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['Fuel Trim Bank 1 Long Term(%)'], name="Long term trim"),secondary_y=True)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['Fuel Trim Bank 1 Short Term(%)'], name="Short term trim"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both fuel trims (there)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="Long/Short term fuel trim", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,16,36,00),datetime(2022,7,23,16,51,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-trim-both-there.html',include_plotlyjs='directory')

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r2['time'], y=r2['[PRIUS]Engine Speed(RPM)'], name="Engine RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['Fuel Trim Bank 1 Long Term(%)'], name="Long term trim"),secondary_y=True)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['Fuel Trim Bank 1 Short Term(%)'], name="Short term trim"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both fuel trims (there)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="Long/Short term fuel trim", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,17,28,00),datetime(2022,7,23,17,43,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-trim-both-back.html',include_plotlyjs='directory')


fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r1['time'], y=r1['[PRIUS]Engine Speed(RPM)'], name="Engine RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['Air Fuel Ratio(Commanded)(:1)'], name="Commanded A/F"),secondary_y=True)
fig.add_trace(go.Scatter(x=r1['time'], y=r1['Air Fuel Ratio(Measured)(:1)'], name="Measured A/F"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both air/fuel ratios (there)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="Commanded/Measured air fuel ratio", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,16,36,00),datetime(2022,7,23,16,51,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-af-both-there.html',include_plotlyjs='directory')

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=r2['time'], y=r2['[PRIUS]Engine Speed(RPM)'], name="Engine RPM"),secondary_y=False)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['Air Fuel Ratio(Commanded)(:1)'], name="Commanded A/F"),secondary_y=True)
fig.add_trace(go.Scatter(x=r2['time'], y=r2['Air Fuel Ratio(Measured)(:1)'], name="Measured A/F"),secondary_y=True)
fig.update_layout(title_text="ICE RPM vs both air/fuel ratios (back)")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text="ICE RPM", secondary_y=False)
fig.update_yaxes(title_text="Commanded/Measured air fuel ratio", secondary_y=True)
fig.update_layout(hovermode='x unified')
fig.update_layout(xaxis_range=[datetime(2022,7,23,17,28,00),datetime(2022,7,23,17,43,00)])
fig.write_html('/Users/chirag/OneDrive/ThingsToDo/Prius/Torque/rpm-vs-af-both-back.html',include_plotlyjs='directory')


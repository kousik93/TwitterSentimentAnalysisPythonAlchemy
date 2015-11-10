import plotly.plotly as py
from plotly.graph_objs import Scatter
import plotly.plotly as py
import plotly.graph_objs as go
trace1 = go.Bar(
    x=['Halloween', 'Donald Trump', 'Sanders'],
    y=[2.855479, 3.29263, 0.1366851],
    name='San Fransisco'
)
trace2 = go.Bar(
    x=['Halloween', 'Donald Trump', 'Sanders'],
    y=[2.352551, 7.9567758, -2.517701],
    name='New york'
)

trace3 = go.Bar(
    x=['Halloween', 'Donald Trump', 'Sanders'],
    y=[4.6160652, -2.255006, -0.048836],
    name='Texas'
)

data = [trace1, trace2,trace3]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')

print plot_url

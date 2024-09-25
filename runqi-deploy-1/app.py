from dash import Dash, dcc, html
import dash_design_kit as ddk
import plotly.express as px
import datetime
import pytz

# Get the current time in UTC 23
utc_time = datetime.datetime.now(pytz.utc)
# Define the EST timezone
est = pytz.timezone('US/Eastern')


app = Dash(__name__)
server = app.server  # expose server variable for Procfile

df = px.data.stocks()

app.layout = html.Div(children=[

    html.Div('The APP 1 deployed time is: ' + str(utc_time.astimezone(est))),

    html.Div(children=dcc.Graph(figure=px.line(df, x="date", y=["GOOG", "AAPL"], title='Stock Prices')))

])


if __name__ == '__main__':
    app.run(debug=True)

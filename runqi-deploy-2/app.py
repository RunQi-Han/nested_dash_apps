from dash import Dash, dcc
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

app.layout = ddk.App([

    ddk.Header([
        ddk.Logo(src=app.get_asset_url('logo.svg')),
        ddk.Title('The APP 22222 deployed time is: ' + str(utc_time.astimezone(est))),
    ]),

    ddk.Card(children=ddk.Graph(figure=px.line(df, x="date", y=["GOOG", "AAPL"], title='Stock Prices')))

])


if __name__ == '__main__':
    app.run(debug=True)

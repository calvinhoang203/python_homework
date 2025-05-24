# Task 4: A Dashboard with Dash
# Task 5: Deploying to Render.com
# Load libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load data
df = pldata.gapminder()
countries = df['country'].unique()


# Create a Dash application
app = Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(id='country-dropdown', options=[{'label': c, 'value': c} for c in countries], value='Canada'),
    dcc.Graph(id='gdp-growth')
])

# Define the callback to update the graph based on the selected country
@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)
# Update the graph based on the selected country
def update_graph(country):
    filtered = df[df['country'] == country]
    fig = px.line(filtered, x='year', y='gdpPercap', title=f'GDP per Capita for {country}')
    return fig

if __name__ == "__main__":
    app.run(debug=True)

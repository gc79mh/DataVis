import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = px.data.gapminder().query("year == 2007")
app = dash.Dash(__name__)
app.title = "Dash App with Sidebar ToC"

app.layout = html.Div([
    html.H1("Gapminder Dashboard", style={'textAlign': 'center'}),

    # Flex container
    html.Div([
        # Sidebar
        html.Div([
            html.H2("Table of Contents"),
            html.Ul([
                html.Li(html.A("Dropdown Filter", href="#dropdown")),
                html.Li(html.A("Interactive Graph", href="#graph")),
            ])
        ], style={
            'width': '20%',
            'padding': '20px',
            'backgroundColor': '#f4f4f4',
            'borderRight': '1px solid #ccc'
        }),

        # Main content
        html.Div([
            html.Div([
                html.H3("Dropdown Filter", id="dropdown"),
                dcc.Dropdown(
                    id='continent-dropdown',
                    options=[{'label': cont, 'value': cont} for cont in df['continent'].unique()],
                    value='Asia',
                    clearable=False
                )
            ], style={'marginBottom': '40px'}),

            html.Div([
                html.H3("Interactive Graph", id="graph"),
                dcc.Graph(id='scatter-plot')
            ])
        ], style={'width': '80%', 'padding': '20px'})
    ], style={'display': 'flex', 'minHeight': '80vh'})
])

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('continent-dropdown', 'value')
)
def update_graph(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(
        filtered_df,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="country",
        hover_name="country",
        log_x=True,
        size_max=60
    )
    fig.update_layout(title=f"GDP vs Life Expectancy in {selected_continent} (2007)")
    return fig

if __name__ == '__main__':
    app.run(debug=True)

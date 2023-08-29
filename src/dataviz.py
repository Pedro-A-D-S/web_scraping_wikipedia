import pandas as pd
import yaml
from pathlib import Path
from typing import Optional
import plotly_express as px

class Data:
    """
    Class to load and save data.

    Attributes:
        path: The path to the data file.
        data: The loaded data.

    Methods:
        load_data(): Loads the data from the file.
        save_data(data: pd.DataFrame): Saves the data to the file.
    """

    def __init__(self, path: Optional[str] = None):
        """
        Args:
            path: The path to the data file.
        """
        self.path = path or Path(__file__).parent.parent / 'data' / 'metal_bands.csv'
        self.data = None

    def load_data(self):
        """Loads the data from the file."""
        self.data = pd.read_csv(self.path)

    def save_data(self, data: pd.DataFrame):
        """Saves the data to the file."""
        data.to_csv(self.path, index=False)


class Visualization:
    """
    Class to create visualizations.

    Attributes:
        data: The data to be used in the visualizations.

    Methods:
        create_top_10_countries_chart(): Creates a bar chart of the top 10 countries.
        create_formed_bands_chart(): Creates a bar chart of the top 10 years of formed bands.
        create_bands_by_continents_chart(): Creates a pie chart of the bands by continents.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Args:
            data: The data to be used in the visualizations.
        """
        self.data = data

    def create_top_10_countries_chart(self):
        """Creates a bar chart of the top 10 countries."""
        fig = px.bar(data=self.data.nlargest(10, 'Band'), x='Country', y='Band', text_auto=True,
                   template='plotly_dark', range_y=[0, 13])

        fig.update_xaxes(categoryorder='total descending')
        fig.update_yaxes(showticklabels=False)

        fig.update_layout(
            title={
                'text': "Top 10 countries"},
            xaxis_title='Countries',
            yaxis_title='Number of bands',
            width=1200,
            height=500,
            font_family="Arial",
            font_color="White",
            font=dict(size=18),
            title_font_family="Arial",
            title_font_color='White'
        )

        fig.update_traces(textposition='outside', textfont_size=16, marker_color='#75141a')

        return fig

    def create_formed_bands_chart(self):
        """Creates a bar chart of the top 10 years of formed bands."""
        fig = px.bar(data=self.data.nlargest(10, 'Band'), x='Formed', y='Band', text_auto=True,
                   template='plotly_dark', range_y=[0, 10])

        fig.update_xaxes(categoryorder='total descending')
        fig.update_yaxes(showticklabels=False)

        fig.update_layout(
            title={
                'text': "Years of formed bands"},
            xaxis_title='Years',
            yaxis_title='Number of bands',
            width=1200,
            height=500,
            font_family="Arial",
            font_color="White",
            font=dict(size=18),
            title_font_family="Arial",
            title_font_color='White'
        )

        fig.update_traces(textposition='outside', textfont_size=16, marker_color='#75141a')

        return fig

    def create_bands_by_continents_chart(self):
        '''
        Creates a pie chart of the bands by continents.
        '''
        fig = px.pie(
            data=self.data.groupby('Continent')['Band'].count(),
            values='Band',
            names='Continent',
            title='Bands by continents',
            template='plotly_dark',
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        fig.update_traces(textposition='outside', textinfo='percent+label')

        return fig


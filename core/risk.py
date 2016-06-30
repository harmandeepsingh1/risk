"""
This module contains the main controls of the Game

All the elements will be managed here, like attack, deploy,
shuffle etc

@author: Harmandeep Singh
@email:  harmandeep3091 at gmail dot com
@date:   2016-06-29 Wed
"""


class Risk(object):
    """
    Main class that will control the game
    """

    def __init__(self, countries, edges, players):
        """
        countries -- List of tuples containing country name, continent, stars
        edges     -- List of tuples(of len 2) showing edges between
                     two countries
        players   -- Name of players playing the game
        """
        self.countries = [Country(*country) for country in countries]
        self.map = Map(self.countries, edges)

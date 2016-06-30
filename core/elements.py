"""
This module contains the basic elements that comprise the Game

All the elements that the game will contain will be part of 
this module

@author: Harmandeep Singh
@email:  harmandeep3091 at gmail dot com
@date:   2016-06-29 Wed
"""


class Player(object):

    def __init__(self, name):
        self.name = name


class Country(object):

    def __init__(self, name, continent, stars):
        self.name = name
        self.continent = continent
        self.stars = stars


class Map(object):

    def __init__(self, countries, edges):
        """
        edges     --  list containing key as unique index of node in
                      `index_country` and value will be list of 
                      indexes of adjacent nodes.
                      The main use of this dict is to create the graph

        countries -- list containing `elements.Country` object
                     in the order of indexes required in 
                     `graph_list`

        """
        self.countries = countries
        self.country_name_index_map = {}
        for idx, each_country in enumerate(index_country_map):
            self.country_name_index_map[each_country.name] = idx
        self.graph_dict = [[] for x in countries]
        for each_edge in edges:
            self.graph_dict[self.country_name_index_map[each_edge[0]]].append(
                self.country_name_index_map[each_edge[1]])

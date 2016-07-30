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
        edges     -- `list` of tuples, each of length 2, containing
                     namewise pairs for each edge

        countries -- `list` containing `elements.Country` object
                     in the order of indexes required in 
                     `graph_list`

        Following two objects are created here:
        1) country_name_index_map -- This is a `dict` which corresponds to
                                     name of the country as key and a unique
                                     index as value
        2) graph_dict -- This is a `dict` which corresponds each index of a
                         country to a `list`, this `list` contians the index
                         of the countries with which the `key` of the `dict`
                         forms an edge
        """
        self.countries = countries
        self.country_name_index_map = {}  # Country name - index mapping
        for idx, each_country in enumerate(countries):
            self.country_name_index_map[each_country.name] = idx
        self.graph_dict = [[] for x in countries]  # Index wise edges
        for each_edge in edges:
            self.graph_dict[self.country_name_index_map[each_edge[0]]].append(
                self.country_name_index_map[each_edge[1]])
            self.graph_dict[self.country_name_index_map[each_edge[1]]].append(
                self.country_name_index_map[each_edge[0]])

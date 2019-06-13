# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:28:36 2019

@author: Omkar Shidore
@github: https://github.com/OmkarShidore

"""
import folium

#map created over the given co-ordinates
mymap = folium.Map(location = [18.6685081,73.8055942],zoom_start=13)

#Instatiating Child Marking Class
fg=folium.FeatureGroup(name='my_map')

#Creating child nodes
fg.add_child(folium.Marker(location=[18.6798292,73.8273853],popup='Omkar'))
fg.add_child(folium.Marker(location=[18.6646107,73.7822323],popup='Roopendea'))
fg.add_child(folium.Marker(location=[18.6740668,73.8054487],popup='Aishwarya'))
fg.add_child(folium.Marker(location=[18.671225, 73.796859],popup='Harshal'))
fg.add_child(folium.Marker(location=[18.6615643,73.809735],popup='Rutuja'))
fg.add_child(folium.Marker(location=[18.6504267,73.791787],popup='Priyal'))
fg.add_child(folium.Marker(location=[18.6689848,73.8310007],popup='Priyanka'))
fg.add_child(folium.Marker(location=[18.6638617,73.8171543],popup='Sushmita'))
fg.add_child(folium.Marker(location=[18.6598739,73.8034366],popup='Shweta'))

#Display object map
mymap.add_child(fg)

#save map in html file
mymap.save("index.html")
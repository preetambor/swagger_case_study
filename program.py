# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:11:02 2023

@author: preetamb
"""

import json
import requests

with open(r"C:\swagger.json") as f:
    data = json.load(f)

print(data)

print("All Endpoints:")
endpoint = data['paths']
print(endpoint.keys())
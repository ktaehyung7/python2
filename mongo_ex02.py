# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:46:37 2020

@author: nerguri
"""

import pymongo
from pymongo import MongoClient

try:
    client = MongoClient("localhost:27017")
    db = client.test
    test_insert_collection = db.test_insert
#    test_insert_collection.insert_one({'title':'암살', 'casings':['이정재','전지현','하정']})
    test_insert_collection.insert_one({'title' : '실미도', 'castings' : ['설경구', '안성기'], 
                              'datetime' : {'year' : '2003', 'month' : 3,
                                           'val' : {'a' :{'b' : 1}}}})
except:
    traceback.print_exc()
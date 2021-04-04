# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:22:29 2020

@author: nerguri
"""

import pymongo
from pymongo import MongoClient

try:
    client = MongoClient("localhost:27017")
    db = client.test
    db.articles.insert([
            {
                "title" : "article01",
                "content" : "content01",
                "writer" : "Velopert",
                "likes" : 0,
                "comments" : [ ]
            },
            {
                "title" : "article02",
                "content" : "content02",
                "writer" : "Alpha",
                "likes" : 23,
                "comments" : [
                        {
                                "name" : "Bravo",
                                "message" : "Hey Man!"
                        }
                ]
            },
            {
                "title" : "article03",
                "content" : "content03",
                "writer" : "Bravo",
                "likes" : 40,
                "comments" : [
                        {
                                "name" : "Charlie",
                                "message" : "Hey Man!"
                        },
                        {
                                "name" : "Delta",
                                "message" : "Hey Man!"
                        }
                ]
            }
        ])
except:
    traceback.print_exc()
    
        
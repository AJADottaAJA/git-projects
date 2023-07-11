import os
import json

def str():
    return "pypi"

print("salam")
print(type("salam"))

a = int("121")

class one():
    static_field = 14
    def __init__(self, hour):
        self.hour = hour
    def __str__(self):
        return "class one"
    def __repr__(self):
        return "object from class one"

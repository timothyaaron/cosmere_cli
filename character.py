"""A Cosmere RPG Text User Interface"""
from enum import Enum


class Talent:
    def __init__(self, name, description, children):
        self.name = name
        self.description = description
        self.children = children

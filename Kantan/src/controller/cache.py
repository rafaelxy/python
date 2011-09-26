"""
Created on 23/09/2011

@author: Rafael Campos @rafaelxy
"""

class SeedList(dict):
    """
    classdocs
    """
    __shared_state = {}
    def __init__(self):
        """
        Constructor
        """
        self.__dict__ = self.__shared_state
        
        if "seed" not in self:
            self['seed'] = dict()
        if "name" not in self:
            self['name'] = dict()
        
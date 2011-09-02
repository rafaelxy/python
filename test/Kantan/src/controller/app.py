# -*- coding: UTF-8 -*-

'''
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
'''
import traceback

from view.main_frame import WindowApp

class App(object):
    def __init__(self):
        self.__main_frame = WindowApp()
    
    def run(self):
        try:
            self.__main_frame.MainLoop()
        except Exception, e:
            print traceback.format_exc()
            
            raise e;
        
        
    

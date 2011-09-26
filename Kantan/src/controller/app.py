# -*- coding: UTF-8 -*-
"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import traceback

from view.main_frame import WindowApp

#from base.interfaces import Borg 

import controller.events as events
import controller.list as ctrl

import os
class App(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        
        if not self.__shared_state:
            """inicia o estado apenas uma vez"""
            self.__windows_app = WindowApp(self)
            self.main_frame = self.__windows_app.main_frame
            
            self.ctrl_actions = events.Actions()
            self.ctrl_pkgs = ctrl.Packages()
            
            self.APP_PATH = os.path.realpath("./")
        
    def run(self):
        try:
            """inicia os componentes dos borgs de controle"""
            self.ctrl_pkgs.set_list_seed(self.main_frame.list_seed)
            self.ctrl_pkgs.set_list_panel(self.main_frame.list_panel)
            self.ctrl_pkgs.set_console_panel(self.main_frame.console_panel)
            self.ctrl_pkgs.set_tool_panel(self.main_frame.tool_panel)
            
            self.ctrl_actions.set_main_frame(self.main_frame)
            self.ctrl_actions.set_ctrl_pkg(self.ctrl_pkgs)
            
            
            self.__windows_app.MainLoop()
        except Exception, e:
            print traceback.format_exc()
            raise e;
        
###############################################################################

        
        
        
    

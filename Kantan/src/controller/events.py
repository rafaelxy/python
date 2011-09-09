# -*- coding: UTF-8 -*-
"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import wx
import os

#import controller as ctrl
#from base.interfaces import Borg 

class Actions(object):
    __shared_state = {}
    
    def __init__(self):
        """constructor"""
        self.__dict__ = self.__shared_state
        
        self.__wildcard = "Packages (*.bpk)|*.bpk|Executables (*.bpr)|*.bpr|Group of Packages (*.xml)|*.xml"
        self.__default_path = "c:\\gemini"
        
        self.__main_frame = None
        self.ctrl_pkg = None

    def set_main_frame(self, main_frame):
        self.__main_frame = main_frame
        
    def set_ctrl_pkg(self, ctrl_pkg):
        self.ctrl_pkg = ctrl_pkg
        
    def file_to_pkglist(self, event):
        """Seleciona um arquivo e gera a lista de compilacao"""
        dialog_title = "Select a Package File"
        default_file = ""
        
        dialog = wx.FileDialog(self.__main_frame, dialog_title, 
                               self.__default_path, default_file,
                               self.__wildcard, 
                               style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        
        dialog.CenterOnParent()

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPaths()[0]
            package = os.path.basename(path)
            self.ctrl_pkg.load_package_list(package)

        dialog.Destroy()
        
    def exit(self, event):
        event.EventObject.Close()
        

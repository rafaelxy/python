"""
Created on 09/09/2011

@author: e0621ap
"""

import wx
import controller.events as events

class MainMenuBar(object):
    def __init__(self, frame):
        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(File(frame).menu, "File")
        self.menu_bar.Append(Edit(frame).menu, "Edit")
#        self.Append(HelpMenu(), "Help")
        
###############################################################################

class File(object):
    def __init__(self, frame):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        frame.Bind(wx.EVT_MENU, self.actions.file_to_pkglist, 
                  self.menu.Append(wx.ID_ANY, "Open Seed List...", 
                                  "Open Seed List"))
        frame.Bind(wx.EVT_MENU, self.actions.exit, 
                  self.menu.Append(wx.ID_ANY, "&Exit\tAlt+F4", "Exit Program"))
    
###############################################################################

class Edit(object):
    def __init__(self, frame):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        frame.Bind(wx.EVT_MENU, self.actions.select_all, 
                  self.menu.Append(wx.ID_ANY, "Select All", ""))
    
###############################################################################

class Help(object):
    def __init__(self):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        
###############################################################################

class ContextListPkg(object):
    def __init__(self):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        
        self.menu_bind(self.actions.make, "Make")
        #TODO action make all from here
        self.menu_bind(self.actions.make_from_here, "Make All From Here")
        #TODO action make relink
#        self.menu_bind(self.actions.make_relink, "Make Relink")
        self.menu_bind(self.actions.build, "Build")
        self.menu_bind(self.actions.build_from_here, "Build All From Here")
        self.menu_bind(self.actions.check_list_checkbox, "Check")
        self.menu_bind(self.actions.uncheck_list_checkbox, "Uncheck")
        self.menu_bind(self.actions.select_all, "Select All")
        
    def menu_bind(self, action, label):
        self.menu.Bind(wx.EVT_MENU, action, 
                self.menu.Append(wx.ID_ANY, label, ""))

###############################################################################        

class ContextListSeed(object):
    def __init__(self):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        
        self.menu_bind(self.actions.file_to_pkglist, "Add")
        self.menu_bind(self.actions.list_seed_remove, "Remove")
        self.menu_bind(self.actions.select_all, "Select All")
        
    def menu_bind(self, action, label):
        self.menu.Bind(wx.EVT_MENU, action, 
                self.menu.Append(wx.ID_ANY, label, ""))

###############################################################################        
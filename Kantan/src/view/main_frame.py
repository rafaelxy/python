# -*- coding: UTF-8 -*-

"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import wx
import wx.lib.agw.aui as aui

import panel

import controller.events as events
#import pickle

class WindowApp(wx.App):
    """
    App do wx, armazena o MainFrame 
    """
    def OnInit(self):
        try:
            self.main_frame = MainFrame(None, -1, "")
            self.SetTopWindow(self.main_frame)
            self.main_frame.CenterOnScreen()
            self.main_frame.Show()
            return True
        except Exception, e:
            raise e;
        
###############################################################################

class MainFrame(wx.Frame):
    """
    Frame principal da aplicacao, controla o AUI Manager
    """
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, None, wx.ID_ANY, title="Kantan", size=(1024,768))

        self.aui_mgr = aui.AuiManager(self)
        
        self.list_panel = panel.ListPackages(self)
        self.console_panel = panel.ListConsole(self)
        self.tool_panel = panel.ToolBar(self)
        
        self.__init_panel_manager()
        
#        self.SetClientSize(self.GetSize())

        self.SetMenuBar(MainMenuBar(self).menu_bar)
#        self.__create_menu()

    def __init_panel_manager(self):
        info = aui.AuiPaneInfo().CloseButton(visible=False).MaximizeButton().MinimizeButton()
        info.Center().Name("Packages")
        self.aui_mgr.AddPane(self.list_panel, info)
        
        info = aui.AuiPaneInfo().CloseButton(visible=False).MaximizeButton().MinimizeButton()
        info.Bottom().Name("Console").BestSize(0,250)
        self.aui_mgr.AddPane(self.console_panel, info)
        
        info = aui.AuiPaneInfo().CloseButton(visible=False).MinimizeButton()
        info.Right().Name("Toolbar")
        self.aui_mgr.AddPane(self.tool_panel, info)
        
        self.aui_mgr.Update()        

###############################################################################

class MainMenuBar(object):
    def __init__(self, frame):
        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(FileMenu(frame).menu, "File")
#        self.Append(HelpMenu(), "Help")
        
###############################################################################

class FileMenu(object):
    def __init__(self, frame):
        self.menu = wx.Menu()
        self.actions = events.Actions()
        frame.Bind(wx.EVT_MENU, self.actions.file_to_pkglist, 
                  self.menu.Append(wx.ID_ANY, "Open Package List...", 
                                  "Open Package List"))
        frame.Bind(wx.EVT_MENU, self.actions.exit, 
                  self.menu.Append(wx.ID_ANY, "&Exit\tAlt+F4", "Exit Program"))
    
###############################################################################

class HelpMenu(wx.Menu):
    def __init__(self):
        self.actions = events.Actions()
        
    
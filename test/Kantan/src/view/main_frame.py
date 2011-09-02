# -*- coding: UTF-8 -*-

'''
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
'''

import wx
import wx.lib.agw.aui as aui

import panel

class WindowApp(wx.App):
    """
    App do wx, armazena o MainFrame 
    """
    def OnInit(self):
        try:
            self.frame = MainFrame(None, -1, "")
            self.SetTopWindow(self.frame)
            self.frame.CenterOnScreen()
            self.frame.Show()
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
        
        list_panel = panel.ListPackages(self)
        list_console = panel.ListConsole(self)
        tool_panel = panel.ToolBar(self)
        
        info = aui.AuiPaneInfo().CloseButton(visible=False).MaximizeButton().MinimizeButton()
        info.Center().Name("Packages")
        self.aui_mgr.AddPane(list_panel, info)
        
        info = aui.AuiPaneInfo().CloseButton(visible=False).MaximizeButton().MinimizeButton()
        info.Bottom().Name("Console").BestSize(0,250)
        self.aui_mgr.AddPane(list_console, info)
        
        info = aui.AuiPaneInfo().CloseButton(visible=False).MinimizeButton()
        info.Right().Name("Toolbar")
        self.aui_mgr.AddPane(tool_panel, info)

        self.aui_mgr.Update()
#        self.SetClientSize(self.GetSize())

###############################################################################
    
    
# -*- coding: UTF-8 -*-

"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import wx
import wx.lib.agw.aui as aui

import panel
import view.menu as menu

import controller.serialize as ctrl_serial


class WindowApp(wx.App):
    """
    App do wx, armazena o MainFrame 
    """
    def OnInit(self):
        try:
            self.main_frame = MainFrame(None, -1, "")
            self.main_frame.wx_app = self
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

        self.wx_app = None
        self.aui_mgr = aui.AuiManager(self)
        
        self.list_seed = panel.ListSeed(self)
        self.list_panel = panel.ListPackages(self)
        self.console_panel = panel.ListConsole(self)
        self.tool_panel = panel.ToolBar(self)
        
#        self.list_seed.
        
        self.__init_panel_manager()
        
#        self.SetClientSize(self.GetSize())

        self.SetMenuBar(menu.MainMenuBar(self).menu_bar)
#        self.__create_menu()
#
#        self.Bind(wx.EVT_MENU, self.close_window, id=wx.ID_EXIT)
#
        self.Bind(wx.EVT_CLOSE, self.close_window)
        
        ctrl_serial.load(self)

    def __init_panel_manager(self):
        info = aui.AuiPaneInfo().CloseButton(visible=False).MaximizeButton().MinimizeButton()
        info.Left().Name("Seeds").MinSize(160, 0)
        self.aui_mgr.AddPane(self.list_seed, info)
        
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
        
    def close_window(self, event):
        dlg = wx.MessageDialog(self, "Do you want to save interface settings?", "Save Interface Settings", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            ctrl_serial.dump(self)
            
        self.Destroy() # frame
        dlg.Destroy()
        return False
    
###############################################################################

    
    
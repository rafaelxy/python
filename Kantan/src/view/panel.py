# -*- coding: UTF-8 -*-
'''
Created on 30/08/2011

@author: Rafael Campos @rafaelxy
'''

import wx
import grid

import controller.list as ctrl

class ListPackages(wx.Panel):
    """
    Panel da lista de pacotes
    """
    def __init__(self, parent):
        """Inicia parte grafica"""
        wx.Panel.__init__(self, parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))
        self.list = wx.ListCtrl(self, wx.NewId(), (0,0), (0,0), wx.LC_REPORT)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list, 5, wx.EXPAND, 5)
        
        self.SetSizer(sizer)
#        self.SetSize(size=(0,0))

        self.ctrl = ctrl.ListPackages()
        self.ctrl.load_package_list(self)
        
        self.__buildColumn()

    def __buildColumn(self):
        info = wx.ListItem()
        info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        info.m_format = 0
        info.m_text = "Package"
        self.list.InsertColumnInfo(0, info)
        self.list.SetColumnWidth(0, 300)

        info.m_text = "Path"
        self.list.InsertColumnInfo(1, info)
        self.list.SetColumnWidth(1, 230)

        info.m_text = "Execute"
        self.list.InsertColumnInfo(2, info)
        self.list.SetColumnWidth(2, 60)

        info.m_text = "Time Elapsed"
        self.list.InsertColumnInfo(3, info)
        self.list.SetColumnWidth(3, 100)
        

###############################################################################
        
class ListConsole(wx.Panel):
    """
    Panel do console de compilacao
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))

        listOut = wx.ListCtrl(self, wx.NewId(), (0,0), (0,0), wx.LC_REPORT | wx.LC_NO_HEADER)
        listOut.InsertColumn(0, "Mensagens", wx.LIST_FORMAT_LEFT, 1000)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(listOut, 5, wx.EXPAND, 5)
        
        self.SetSizer(sizer)
#        self.SetSize((0, 222))
        
###############################################################################
        
class ToolBar(wx.Panel):
    def __init__(self, parent):
        """Toolbar com botoes de opcoes"""
        wx.Panel.__init__(self, parent=parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))

        self.grid = grid.ToolBar(self) 
        
        self.SetSizerAndFit(self.grid)
#        self.SetSize(size=(100,500))
        

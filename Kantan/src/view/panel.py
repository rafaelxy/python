# -*- coding: UTF-8 -*-
"""
Created on 30/08/2011

@author: Rafael Campos @rafaelxy
"""

import wx
import grid
import controller.events as events

###############################################################################

class ListSeed(wx.Panel):
    """
    Panel da lista de seed de pacotes
    """
    def __init__(self, parent):
        """Inicia parte grafica"""
        wx.Panel.__init__(self, parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))
        
        self.actions = events.Actions()
        
        self.list_ctrl = wx.ListCtrl(self, wx.NewId(), (0,0), (0,0), wx.LC_REPORT)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.actions.load_list)
        self.list_ctrl.Bind(wx.EVT_RIGHT_DOWN, self.actions.click_pos)
        self.list_ctrl.Bind(wx.EVT_CONTEXT_MENU, self.actions.menu_list_seed)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 5, wx.EXPAND, 5)
        
        self.SetSizer(sizer)
#        self.SetSize(size=(0,0))

        self.__buildColumn()
        
    def __buildColumn(self):
        info = wx.ListItem()
        info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        info.m_format = 0
        info.m_text = "Seed Package"
        self.list_ctrl.InsertColumnInfo(0, info)
        self.list_ctrl.SetColumnWidth(0, 150)

#        info.m_text = "Path"
#        self.list_ctrl.InsertColumnInfo(1, info)
#        self.list_ctrl.SetColumnWidth(1, 230)

    def from_list(self, list_pkg):
        i = 0
        for pkg in list_pkg:
            self.list_ctrl.InsertStringItem(i, pkg)
            i += 1
        
        
        
###############################################################################

import wx.lib.mixins.listctrl as listmix

class CheckboxListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)

#    def OnCheckItem(self, index, flag):
#        print(index, flag)

class ListPackages(wx.Panel):
    """
    Panel da lista de pacotes
    """
    def __init__(self, parent):
        """Inicia parte grafica"""
        wx.Panel.__init__(self, parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))
        
        self.actions = events.Actions()
        
        self.list_ctrl = CheckboxListCtrl(self, wx.NewId(), (0,0), (0,0), wx.LC_REPORT)
        self.list_ctrl.Bind(wx.EVT_RIGHT_DOWN, self.actions.click_pos)
        self.list_ctrl.Bind(wx.EVT_CONTEXT_MENU, self.actions.menu_list_pkg)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 5, wx.EXPAND, 5)
        
        self.SetSizer(sizer)
#        self.SetSize(size=(0,0))

        self.__buildColumn()

    def __buildColumn(self):
        info = wx.ListItem()
        info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        info.m_format = 0
        info.m_text = "Package"
        self.list_ctrl.InsertColumnInfo(0, info)
        self.list_ctrl.SetColumnWidth(0, 150)

        info.m_text = "Path"
        self.list_ctrl.InsertColumnInfo(1, info)
        self.list_ctrl.SetColumnWidth(1, 300)

#        info.m_text = "Execute"
#        self.list_ctrl.InsertColumnInfo(2, info)
#        self.list_ctrl.SetColumnWidth(2, 60)

        info.m_text = "Time Elapsed"
        self.list_ctrl.InsertColumnInfo(3, info)
        self.list_ctrl.SetColumnWidth(3, 100)
        
    def from_list(self, list_pkg):
        i = 0
        for pkg in list_pkg:
#            pkg = self.pkg_list.dict_name.get(pkg)
            idx = self.list_ctrl.InsertStringItem(i, pkg[0])
            if pkg[2]:
                self.list_ctrl.CheckItem(idx)
            self.list_ctrl.SetStringItem(idx, 1, pkg[1])
            i += 1
        

###############################################################################
        
class ListConsole(wx.Panel):
    """
    Panel do console de compilacao
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style = (wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE))

        self.list_ctrl = wx.ListCtrl(self, wx.NewId(), (0,0), (0,0), wx.LC_REPORT | wx.LC_NO_HEADER)
        self.list_ctrl.InsertColumn(0, "Mensagens", wx.LIST_FORMAT_LEFT, 1000)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 5, wx.EXPAND, 5)
        
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
        
###############################################################################


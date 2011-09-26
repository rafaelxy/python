# -*- coding: UTF-8 -*-
"""
Created on 01/09/2011

@author: Rafael Campos @rafaelxy
"""

import compiler.package as cpkg
import datetime
import compiler.build as build

import consts as c

class Packages(object):
    """
    Classe de controle da lista de pacotes
    Borg design pattern
    """
    __shared_state = {}
    def __init__(self):
        """
        Constructor
        """
        self.__dict__ = self.__shared_state
        
        self.__list_seed = None
        self.__list_panel = None
        self.__console_panel = None
        
        self.ctrl_build = build.Ctrl()
        self.pkg_list = cpkg.PackageList()
        
    def set_console_panel(self, console_panel):
        self.__console_panel = console_panel
        self.ctrl_build.set_console_panel(console_panel)
        
    def set_list_panel(self, list_panel):
        self.__list_panel = list_panel

    def set_list_seed(self, list_seed):
        self.__list_seed = list_seed
                
    def set_tool_panel(self, tool_panel):
        self.__tool_panel = tool_panel   
        self.ctrl_build.set_threads_spin(tool_panel.grid.buttonThreads)
        
    def load_package_list(self, package):
        """Carrega a lista de pacoes de acordo com a dependencia e a semente"""
        import os
        package = os.path.splitext(package)[0]
        list_pkg = self.pkg_list.generate_package_list(package)
        
        list_seed = self.__list_seed.list_ctrl
        list_panel = self.__list_panel.list_ctrl
        
        #load seed list
        found_at = list_seed.FindItem(-1, package)
        if found_at == -1:
            index = list_seed.GetItemCount()+1
            list_seed.InsertStringItem(index, package)
        
        #load panel list 
        list_panel.DeleteAllItems()
        try:
            i = 0
            for pkg in list_pkg:
                pkg = self.pkg_list.cached['name'].get(pkg)
                idx = list_panel.InsertStringItem(i, pkg.name)
                #TODO externalizar a extensao .mak para parametros de config
#                makepath = pkg.path + pkg.name + ".mak"
                list_panel.CheckItem(idx)
                list_panel.SetStringItem(idx, c.LIST_IDX_PATH, pkg.path)
                i += 1
        except Exception, e:
            raise e
    

    def make(self, list_selected, is_make = True):
        list_ctrl = self.__list_panel.list_ctrl
        
        if is_make:
            build_param = " "
        else:
            build_param = "-B" 
        
        for selected in list_selected:
            list_ctrl.Select(selected.Id)
            if list_ctrl.IsChecked(selected.Id):
                file = list_ctrl.GetItem(selected.Id, c.LIST_IDX_NAME).GetText()
                path = list_ctrl.GetItem(selected.Id, c.LIST_IDX_PATH).GetText()
                t1 = datetime.datetime.today()
                
                #TODO externalizar os .mak
                file += ".mak"
                
                if self.ctrl_build.make(path, file, build_param) > 0:
                    break

                t2 = datetime.datetime.today()
                list_ctrl.SetStringItem(selected.Id, c.LIST_IDX_TIME, str(t2-t1))
                
            
        
###############################################################################

import wx
def get_selected_items(list_ctrl, column=0):
    """Pega os itens selecionados na lista da interface grafica"""
    select_pkgs = []
    item = list_ctrl.GetFirstSelected()
    while item is not -1:
        if item is not -1:
            select_pkgs.append(list_ctrl.GetItem(item, column))
            
        item = list_ctrl.GetNextItem(item, wx.LIST_NEXT_ALL, 
                                     wx.LIST_STATE_SELECTED)
        
    return select_pkgs
        
def get_selected_from_here(list_ctrl, first_selected, column=0):
    """Pega os itens selecionados na lista da interface grafica"""
    select_pkgs = []
    item = first_selected.Id
    while item is not -1:
        if item is not -1:
            select_pkgs.append(list_ctrl.GetItem(item, column))
            
        item = list_ctrl.GetNextItem(item, wx.LIST_NEXT_ALL, 
                                     wx.LIST_STATE_DONTCARE)
        
    return select_pkgs        

###############################################################################        
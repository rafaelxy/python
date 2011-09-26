# -*- coding: UTF-8 -*-
"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import wx
import os

import controller.list as ctrl_list


import thread

class Actions(object):
    __shared_state = {}
    
    def __init__(self):
        """constructor"""
        self.last_click_pos = (0,0)
        self.ctrl_pkg = None
        self.list_selected = []
        self.__main_frame = None
        
        self.__dict__ = self.__shared_state
        
        #TODO extrair esses wildcards para outros compiladores que nao seja o da borland
        self.__wildcard = "Borland Package (*.bpk; *.bpr)|*.bpk; *.bpr|Group of Packages (*.xml)|*.xml"
        self.__default_path = "c:\\gemini"
        
    def set_main_frame(self, main_frame):
        self.__main_frame = main_frame
        
    def set_ctrl_pkg(self, ctrl_pkg):
        self.ctrl_pkg = ctrl_pkg
        
    def get_list_ctrl_pkg(self):
        return self.__main_frame.list_panel.list_ctrl
        
        
        
    #events
    def load_list(self, event):
        list_item = event.Item
        
        self.ctrl_pkg.load_package_list(list_item.m_text)
         
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
        self.__main_frame.Close()
    
    def menu_list_pkg(self, event):
        self.list_selected = ctrl_list.get_selected_items(self.get_list_ctrl_pkg())
        import view.menu as menu
        menu = menu.ContextListPkg().menu
        event.EventObject.PopupMenu(menu, self.last_click_pos)
        
    def menu_list_seed(self, event):
        self.list_selected = ctrl_list.get_selected_items(self.get_list_ctrl_pkg())
        import view.menu as menu
        menu = menu.ContextListSeed().menu
        event.EventObject.PopupMenu(menu, self.last_click_pos)

    def click_pos(self, event):
        self.last_click_pos = (event.GetX(), event.GetY())
        
    def select_all(self, event):
        if hasattr(event.EventObject, "InvokingWindow"):
            list_ctrl = event.EventObject.InvokingWindow
        else:
            list_ctrl = self.get_list_ctrl_pkg()
        
        is_list_ctrl = (hasattr(list_ctrl, "GetItemCount") and 
                        hasattr(list_ctrl, "Select"))
        
        if is_list_ctrl:
            for idx in range(list_ctrl.GetItemCount()):
                list_ctrl.Select(idx)
            
    def check_list_checkbox(self, event):
        list_ctrl = self.get_list_ctrl_pkg()
        self.list_selected = ctrl_list.get_selected_items(list_ctrl)
        
        for item in self.list_selected:
            list_ctrl.CheckItem(item.Id, check=True)
            
    def uncheck_list_checkbox(self, event):
        list_ctrl = self.get_list_ctrl_pkg()
        self.list_selected = ctrl_list.get_selected_items(list_ctrl)
        
        for item in self.list_selected:
            list_ctrl.CheckItem(item.Id, check=False)
        
    def build(self, event):
#        self.__main_frame.wx_app.Yield()
        is_make = False
        thread.start_new_thread(self.ctrl_pkg.make, (self.list_selected, is_make))
#        self.ctrl_pkg.make(self.list_selected, is_make = False)
        
    def build_from_here(self, event):
        list_ctrl = self.get_list_ctrl_pkg()
        l = ctrl_list.get_selected_from_here(list_ctrl, self.list_selected[0])
        self.ctrl_pkg.make(l, is_make = False)
        
    def make(self, event):
        self.ctrl_pkg.make(self.list_selected, is_make = True)
        
    def make_from_here(self, event):
        list_ctrl = self.get_list_ctrl_pkg()
        l = ctrl_list.get_selected_from_here(list_ctrl, self.list_selected[0])
        self.ctrl_pkg.make(l, is_make = True)
        
    def make_relink(self, event):
        #TODO make relink parents
        print "Nao implementado ainda, aguarde a proxima versao"
        
    def list_seed_remove(self, event):
        list_ctrl = event.EventObject.InvokingWindow
        select_pkgs = ctrl_list.get_selected_items(list_ctrl)
        
        for selected in select_pkgs:
            list_ctrl.DeleteItem(selected.Id)

        self.get_list_ctrl_pkg().DeleteAllItems()
        
    def cancel(self, event):
        job = self.ctrl_pkg.ctrl_build.job
        
        if hasattr(job, "close"):
            job.close()
            self.ctrl_pkg.ctrl_build.cancel = True
#        self.cancel = True
        
#    def refresh_res(self, event):
        
            
            
        
        
        

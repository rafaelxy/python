# -*- coding: UTF-8 -*-
"""
Created on 01/09/2011

@author: e0621ap
"""

import compiler.package as cpkg

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
        
        self.__list_panel = None
        self.pkg_list = cpkg.PackageList()
        
    def set_list_panel(self, list_panel):
        self.__list_panel = list_panel
        
        
    def load_package_list(self, package):
        list_pkg = self.pkg_list.generate_package_list(package)
        list_ctrl = self.__list_panel.list_ctrl
        
        list_ctrl.DeleteAllItems()
        try:
            i = 0
            for pkg in list_pkg:
                pkg_name = self.pkg_list.dict_name.get(pkg)
                list_ctrl.InsertStringItem(i, pkg_name)
                i += 1
#            list_panel.list.InsertStringItem(0, "azsdasdas")
#            list_panel.list.SetStringItem(0, 3, "aaaa")
#            list_panel.list.SetStringItem(0, 4, "aaaa")
        except Exception, e:
            raise e
        
        
        
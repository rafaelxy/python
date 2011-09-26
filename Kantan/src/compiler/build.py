# -*- coding: UTF-8 -*-
"""
Created on 21/09/2011

@author: -
"""

import legacy.makefile as mkfile
from legacy.compiler_builder import CompilerBuilder
import legacy.futil as futil
import wx 
import string
import re

#from controller.app import App
        
class Ctrl(object):
    """Classe de controle do build"""
    __shared_state = {}

    def __init__(self):
        self.__threads_spin = None
        self.__console_panel = None
        self.__list_ctrl = None
        
        self.__dict__ = self.__shared_state
        
        self.cancel = False
        
    def set_threads_spin(self, threads_spin):
        self.__threads_spin = threads_spin
        
    def set_console_panel(self, console_panel):
        self.__console_panel = console_panel
        self.__list_ctrl = console_panel.list_ctrl
        
    def make(self, path, file, paramExtr = ""):
        main_frame = self.__console_panel.Parent
        #TODO refactory
        num_threads = self.__threads_spin.GetValue()
        mkfile.gera_make(path, file, num_threads)
        self.__log("Makefile: " + file + " atualizado")

        #TODO extract .mak extension
        self.job = CompilerBuilder(path, file, self.__threads_spin.GetValue() > 1)
        self.job.compile(paramExtr)

        out = " "
        self.__log("make " + file)

        while 1:
#            App().__windows_app.Yield()
            main_frame.console_panel.list_ctrl.Update()
            out = self.job.readMsg()
            if out == "":
                self.__log("FIM: " + file)
                return self.job.close()

            self.__log(out)

            if self.cancel == True:
                self.job.close()
                self.__log("Cancelado: " + file)
                self.cancel = False
                return 100
        self.job = None
        
    def __log(self, val):
        #TODO refactory
        listVal = futil.trata_texto(val)
        for linha in listVal:
            index = self.__list_ctrl.GetItemCount()
            self.__list_ctrl.InsertStringItem(index, linha)
            self.__list_ctrl.SetItemBackgroundColour(index, wx.WHITE)
            self.__list_ctrl.ScrollList(0, 40)

            if re.match('Error', linha) and not (string.find(linha, 'Error messages:') == 0 and string.find(linha, 'None') != -1):
                self.__list_ctrl.SetItemBackgroundColour(index, wx.RED)
            elif re.match('Warning', linha) and not (string.find(linha, 'Warning messages:') == 0 and string.find(linha, 'None') != -1):
                self.__list_ctrl.SetItemBackgroundColour(index, wx.NamedColour("yellow"))
            elif re.match('Fatal', linha) and not (string.find(linha, 'None') != -1):
                self.__list_ctrl.SetItemBackgroundColour(index, wx.RED)

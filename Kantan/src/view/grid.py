# -*- coding: UTF-8 -*-
"""
Created on 29/08/2011

@author: Rafael Campos @rafaelxy
"""
import wx

import controller.events as events

class ToolBar(wx.GridBagSizer):
    def __init__(self, parent):
        """Toolbar com botoes de opcoes"""
        wx.GridBagSizer.__init__(self, 5, 15)
        
        self.parent = parent
        self.main_frame = self.parent.Parent
        
        self.AddGrowableRow(13)
        self.AddGrowableCol(0)

        self.buttons = dict()
        self.actions = events.Actions()
        
        self.__add_buttons()
        
        
    def __add_buttons(self):
        colBotoes = 0
        rowBotoes = 0
#        self.buttonGerarLista = wx.Button(self.parent, wx.NewId(), "Gerar Lista")
#        self.buttonGerarLista.Disable()
##        self.parent.Parent.Bind(wx.EVT_BUTTON, self.__OnClickGerarLista, self.buttonGerarLista)
#        self.Add(self.buttonGerarLista, (rowBotoes,colBotoes), (1,2), wx.EXPAND)
#        rowBotoes+=1
        
        self.buttonSalvar = wx.Button(self.parent, wx.NewId(), "Save Seeds")
#            self.Bind(wx.EVT_BUTTON, self.__OnClickSalvar, self.buttonSalvar)
        self.Add(self.buttonSalvar, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonSalvar.Disable()
        
        #todo trocar os botoes pelo dict
        self.buttons["open_list"] = wx.Button(self.parent, wx.NewId(), "Open Seed")
        self.main_frame.Bind(wx.EVT_BUTTON, self.actions.file_to_pkglist, self.buttons["open_list"])
        self.Add(self.buttons["open_list"], (rowBotoes,colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1

#        self.buttonRemover = wx.Button(self.parent, wx.NewId(), "Remover Item")
##            self.Bind(wx.EVT_BUTTON, self.__OnClickRemover, self.buttonRemover)
#        self.Add(self.buttonRemover, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
#        rowBotoes+=1
#        self.buttonRemover.Disable()

        self.buttonGerarRes = wx.Button(self.parent, wx.NewId(), "Refresh .res")
#        self.Bind(wx.EVT_BUTTON, self.actions.refresh_res, self.buttonGerarRes)
        self.Add(self.buttonGerarRes, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonGerarRes.Disable()

        self.buttonRO = wx.Button(self.parent, wx.NewId(), "Clean ReadOnly")
#            self.Bind(wx.EVT_BUTTON, self.__OnClickRmvReadOnly, self.buttonRO)
        self.Add(self.buttonRO, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonRO.Disable()

        self.buttonAltVer = wx.Button(self.parent, wx.NewId(), u"Change Version")
#            self.Bind(wx.EVT_BUTTON, self.__OnClickAltVersao, self.buttonAltVer)
        self.Add(self.buttonAltVer, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonAltVer.Disable()

        self.buttonFullRelease = wx.Button(self.parent, wx.NewId(), "Full Release")
#            self.Bind(wx.EVT_BUTTON, self.__OnClickFullRelease, self.buttonFullRelease)
        self.Add(self.buttonFullRelease, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonFullRelease.Disable()

        self.buttonFullDebug = wx.Button(self.parent, wx.NewId(), "Full Debug")
#            self.Bind(wx.EVT_BUTTON, self.__OnClickFullDebug, self.buttonFullDebug)
        self.Add(self.buttonFullDebug, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1
        self.buttonFullDebug.Disable()

        #Botão que vai entrar no branch da funcionalidade de compilar fora do C:
#        self.buttonConfig = wx.Button(self.parent, wx.NewId(), "Opções")
#        self.Add(self.buttonConfig, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
#        self.buttonConfig.Disable()
#        self.Bind(wx.EVT_BUTTON, self.__OnClickConfig, self.buttonConfig)
#        rowBotoes+=1

#        self.labelProcs = wx.StaticText(self.parent, wx.NewId(),
#                        "Processadores:  " + str(multiprocessing.cpu_count()))
#        self.Add(self.labelProcs, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
        rowBotoes+=1

        self.labelThreads = wx.StaticText(self.parent, wx.NewId(), "       Threads:")
        self.buttonThreads = wx.SpinCtrl(self.parent, wx.NewId(), size = (40, -1), min = 1,
                                         max = 99, initial = 1)#self.dadosConfig.getNumThreads())
#            self.Bind(wx.EVT_SPINCTRL, self.__OnChangeNumThreads, self.buttonThreads)
        self.Add(self.labelThreads, (rowBotoes, colBotoes), (1,1), wx.EXPAND)
        self.Add(self.buttonThreads, (rowBotoes, colBotoes + 1), (1,1), wx.ALIGN_CENTER)
        rowBotoes+=1
#        self.buttonThreads.Disable()

        self.buttonCanc = wx.Button(self.parent, wx.NewId(), "Cancel")
        self.main_frame.Bind(wx.EVT_BUTTON, self.actions.cancel, self.buttonCanc)
        self.Add(self.buttonCanc, (rowBotoes, colBotoes), (1,2), wx.EXPAND)
#        self.buttonCanc.Disable()

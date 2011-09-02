'''
Created on 01/09/2011

@author: e0621ap
'''

import compiler.package as cpkg

class ListPackages(object):
    '''
    Classe de controle da lista de pacotes
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.pkg_list = cpkg.PackageList()
        
    def load_package_list(self, list_panel):
        list = self.pkg_list.generate_package_list("GmCtrlSAP")
        
        """self, long index, int col, String label, int imageId=-1"""
        
        try:
            i = 0
            for item in list:
                item = item[0]
                item_name = self.pkg_list.dict_name.get(item)
                list_panel.list.InsertStringItem(i, item_name)
                i += 1
#            list_panel.list.InsertStringItem(0, "azsdasdas")
#            list_panel.list.SetStringItem(0, 3, "aaaa")
#            list_panel.list.SetStringItem(0, 4, "aaaa")
        except Exception, e:
            raise e
        
        
        
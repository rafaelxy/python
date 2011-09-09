# -*- coding: UTF-8 -*-

"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import sys
import traceback
sys.tracebacklimit = 100

from controller.app import App 

#from compiler.package import PackageList 

def main():
    try:
        if len(sys.argv) == 1:
            app = App()
            app.run()
        elif len(sys.argv) == 3:
            print "run command line"
        else:
            raise Exception("Número incorreto de parâmetros")
    except Exception, e:
        print traceback.format_exc()
#        raise e    
        
if __name__ == '__main__':
    main()


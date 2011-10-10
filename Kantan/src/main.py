# -*- coding: UTF-8 -*-

"""
Created on 19/08/2011

@author: Rafael Campos @rafaelxy
"""

import sys
import traceback
#sys.tracebacklimit = 100

from controller.app import GuiApp
from controller.app import CmdApp 


def main():
    try:
        if len(sys.argv) == 1:
            app = GuiApp()
            app.run()
        else:
            app = CmdApp(sys.argv)
            app.run()
    except Exception, e:
        print traceback.format_exc()
        raw_input()
#        raise e    
        
if __name__ == '__main__':
    main()


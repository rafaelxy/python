"""
Created on 22/09/2011

@author: Rafael Campos @rafaelxy
"""
#PySwigcontainer
import pickle
from controller.consts import APP_PATH
import os

CACHE_PATH = APP_PATH + "data/cache_settings.data"

def dump(main_frame):
    settings = {}
    
    list_ctrl = main_frame.list_panel.list_ctrl
    package_list = []
    for idx in range(list_ctrl.GetItemCount()):
        checked = list_ctrl.IsChecked(idx)
        package_list.append((list_ctrl.GetItem(idx, 0).m_text,
                     list_ctrl.GetItem(idx, 1).m_text,
                     checked))
    
    list_ctrl = main_frame.list_seed.list_ctrl
    seed_list = []
    for idx in range(list_ctrl.GetItemCount()):
        seed_list.append(list_ctrl.GetItem(idx, 0).m_text)

    spin_thread = main_frame.tool_panel.grid.buttonThreads
    settings['threads'] = spin_thread.GetValue()

    settings['main_frame'] = {}
    settings['main_frame']['is_maximized'] = main_frame.IsMaximized()
    settings['main_frame']['size'] = (main_frame.GetSize().x, main_frame.GetSize().y)
    
    settings['seed_list'] = seed_list
    settings['package_list'] = package_list
    settings['perspective'] = main_frame.aui_mgr.SavePerspective()
    
    pickle.dump(settings, open(CACHE_PATH, "wb"))
    
def load(main_frame):
    if os.path.exists(CACHE_PATH):
        try:
            settings = pickle.load(open(CACHE_PATH, "rb"))
            
            main_frame.aui_mgr.LoadPerspective(settings['perspective'])
            
            main_frame.list_seed.from_list(settings['seed_list'])
            main_frame.list_panel.from_list(settings['package_list'])
            
            if settings['main_frame']['is_maximized']:
                main_frame.Maximize()
            else:
                main_frame.SetSize(settings['main_frame']['size'])
            
            spin_thread = main_frame.tool_panel.grid.buttonThreads    
            spin_thread.SetValue(settings['threads'])
                
        except Exception, e:
            raise e
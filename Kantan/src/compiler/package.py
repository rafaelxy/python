# -*- coding: UTF-8 -*-

"""
Created on 31/08/2011

@author: Rafael Campos @rafaelxy
"""

import lxml.etree as etree
import borland.vcl as vcl
import os
import compiler.graph as graph
import fnmatch

import controller.cache as cache

    
class Package(object):
    def __init__(self, name = "", filename = "", path = ""):
        self.name = name
        self.filename = filename
        self.path = path

###############################################################################

#TODO deixar essa classe generica, independente do compilador (utilizando adaptadores/strategies)
class PackageList(object):
    """Classe de geracao de lista de pacotes"""
    def __init__(self):
        self.cached = cache.SeedList()
        self.__pkg_exts = ["bpk", "bpr"]
        self.__include_path = (["c:\\gemini\\packages\\", 
                                "c:\\gemini\\executaveis\\Administracao\\",
                                "c:\\gemini\\executaveis\\Aplicativos\\",
                                "c:\\gemini\\executaveis\\Desenv\\",
                                "c:\\gemini\\executaveis\\Servidores\\"])
        
    def generate_package_list(self, seed_package):
        """Gera a lista de pacotes"""
        try:
            seed_package = os.path.splitext(seed_package)[0]
            seed_low = seed_package.lower()
            self.__generate_graph(seed_package, seed_low)
            
            
            list = graph.robust_topological_sort(self.cached['seed'][seed_low])
            list = map(lambda item: item[0], list)
            
            list.reverse()
        except Exception, e:
            raise e
        
        return list
        
        
    def __generate_graph(self, seed_package, parent):
        """chamada recursiva para pegar todos os pacotes da dependencia"""
        remove_ext = lambda package: (os.path.splitext(package)[0])
        seed_package = remove_ext(seed_package)
        
        if parent not in self.cached['seed']:
            self.cached['seed'][parent] = dict()
        
        #TODO colocar as keys como lower case soh para windows
        seed_package_low = seed_package.lower()
        if seed_package_low in self.cached['seed'][parent]:
            list_packages = self.cached['seed'][parent][seed_package_low]
        else:  
            pkg, list_packages = self.__get_dependency_list(seed_package)
            
            list_packages = map(remove_ext, list_packages)
            
            self.cached['name'][seed_package_low] = pkg
            self.cached['seed'][parent][seed_package_low] = list_packages
            
            for package in list_packages:
                pkg_low = package.lower()
                cur_pkg = self.cached['seed'].get(pkg_low)
                if cur_pkg is None:
#                    self.cached['name'][pkg_low] = package
                    self.cached['seed'][parent][pkg_low] = self.__generate_graph(package, parent)
                
        return list_packages
    
        
    def __get_dependency_list(self, filename):
        """Pega a lista de dependecia do pacote passado por parametro"""
        pkg = self.__find_pkg_file(filename)
        
        xml = pkg.path + pkg.filename
        xml = etree.parse(xml)
        
        macros = xml.find("MACROS")
        xml_packages = macros.find("PACKAGES")
        values = xml_packages.get("value")
        
        #pega a lista de pacotes retirando os pacotes ignorados
        packages = values.split()
        set_pkgs = set(packages)
        set_ignore = set(vcl.ignore_packages)
        set_pkgs = set_pkgs.difference(set_ignore)
        
        list_packages = list(set_pkgs)
            
        return pkg, list_packages
    
    def __find_pkg_file(self, filename):
        """Acha o arquivo do nome do pacote indicado"""
        matches = []
        for path in self.__include_path:
            #TODO path separator pra linux/unix
            search_path = path + filename + "\\"
            
            #NAO RETIRAR A VARIAVEL dirnames, ela é utilizada intrinsicamente
            for root, dirnames, filenames in os.walk(search_path):
                for ext in self.__pkg_exts:
                    for filename in fnmatch.filter(filenames, 
                                                   filename + "." + ext):
                        matches.append(Package(os.path.splitext(filename)[0], 
                                               filename, search_path))
                        break
                    
        if not matches:
            paths = reduce(lambda x, y: x + ", " + y, self.__include_path)
            raise Exception("Compiler file not found in " + paths)
        
        #TODO tratar quando achar mais de um pacote nos includes
        return matches[0]

        
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

#TODO deixar essa classe generica, independente do compilador (utilizando adaptadores/strategies)
class PackageList(object):
    """Classe de geracao de lista de pacotes"""
    def __init__(self):
        self.graph_pkg = dict()
        self.dict_name = dict()
        self.__pkg_exts = ["bpk", "bpr"]
        self.__include_path = (["c:\\gemini\\packages\\", 
                                "c:\\gemini\\executaveis\\Administracao\\",
                                "c:\\gemini\\executaveis\\Aplicativos\\",
                                "c:\\gemini\\executaveis\\Desenv\\",
                                "c:\\gemini\\executaveis\\Servidores\\"])
        
    def generate_package_list(self, seed_package):
        try:
            self.graph_pkg = dict()
            seed_package = os.path.splitext(seed_package)[0]
            self.__generate_graph(seed_package)
            
            list = graph.robust_topological_sort(self.graph_pkg)
            list = map(lambda item: item[0], list)
            
            list.reverse()
        except Exception, e:
            raise e
        
        return list
        
        
    def __generate_graph(self, seed_package):
        """chamada recursiva para pegar todos os pacotes da dependencia"""
        remove_ext = lambda package: (os.path.splitext(package)[0])
        
        packages = self.__get_dependency_list(seed_package)
        
        seed_package = remove_ext(seed_package)
        packages = map(remove_ext, packages)
        
        #TODO colocar as keys como lower case soh para windows
        seed_package_low = seed_package.lower()
        
        self.dict_name[seed_package_low] = seed_package
        self.graph_pkg[seed_package_low] = packages
        
        for package in packages:
            package_low = package.lower()
            cur_pkg = self.graph_pkg.get(package_low)
            if cur_pkg is None:
                self.dict_name[package_low] = package
                self.graph_pkg[package_low] = self.__generate_graph(package)
                
        return packages
    
        
    def __get_dependency_list(self, filename):
        """Pega a lista de dependecia do pacote passado por parametro"""
        xml = self.__find_pkg_file(filename)
        
        macros = xml.find("MACROS")
        xml_packages = macros.find("PACKAGES")
        values = xml_packages.get("value")
        
        #pega a lista de pacotes retirando os pacotes ignorados
        packages = values.split()
        set_pkgs = set(packages)
        set_ignore = set(vcl.ignore_packages)
        set_pkgs = set_pkgs.difference(set_ignore)
        
        packages = list(set_pkgs)
            
        return packages
    
    def __find_pkg_file(self, filename):
        """Acha o arquivo do nome do pacote indicado"""
        matches = []
        for path in self.__include_path:
            search_path = path + filename + "\\"
            for root, dirnames, filenames in os.walk(search_path):
                for ext in self.__pkg_exts:
                    for filename in fnmatch.filter(filenames, 
                                                   filename + "." + ext):
                        matches.append(os.path.join(root, filename))
                        break
                    
        if not matches:
            raise Exception("Compiler file not found in " + self.__include_path)
        
        filename = matches[0]
        filename = etree.parse(filename)
        
        return filename

        
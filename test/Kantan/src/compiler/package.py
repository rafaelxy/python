# -*- coding: UTF-8 -*-

'''
Created on 31/08/2011

@author: Rafael Campos @rafaelxy
'''

import lxml.etree as etree

import borland.vcl as vcl

import os
#import fnmatch

import compiler.graph as graph

class PackageList(object):
    def __init__(self):
        self.dict_pkg = dict()
        self.dict_name = dict()
        self.include_path = ["c:\\gemini\\packages\\", "c:\\gemini\\executaveis\\"]
        self.pkg_exts = ["bpk", "bpr"]
        
    def generate_package_list(self, seed_package):
        seed_package = os.path.splitext(seed_package)[0]
        self.get_dependency(seed_package)
        
        list = graph.robust_topological_sort(self.dict_pkg)
        
        list.reverse()
        
        return list
        
        
    def get_dependency(self, seed_package):
        """chamada recursive para pegar todos os pacotes da dependencia"""
        remove_ext = lambda package: (os.path.splitext(package)[0])
        
        packages = self.__get_dependency_list(seed_package)
        
        seed_package = remove_ext(seed_package)
        packages = map(remove_ext, packages)
        
        seed_package_low = seed_package.lower()
        
        self.dict_name[seed_package_low] = seed_package
        self.dict_pkg[seed_package_low] = packages
        
        for package in packages:
            package_low = package.lower()
            cur_pkg = self.dict_pkg.get(package_low)
            if cur_pkg is None:
                self.dict_name[package_low] = package
                self.dict_pkg[package_low] = self.get_dependency(package)
                
        return packages
    
        
    def __get_dependency_list(self, filename):
        """Pega a lista de dependecia do pacote passado por parametro"""
        filename = self.__find_pkg_file(filename)
        
        macros = filename.find("MACROS")
        xml_packages = macros.find("PACKAGES")
        values = xml_packages.get("value")
        
        packages = values.split()
        set_pkgs = set(packages)
        set_ignore = set(vcl.ignore_packages)
        set_pkgs = set_pkgs.difference(set_ignore)
        
        packages = list(set_pkgs)
            
        return packages
    
    def __find_pkg_file(self, filename):
        """Acha o arquivo do nome do pacote indicado"""
        filename = self.include_path[0] + filename + "\\" + filename
        
        found = False
        for ext in self.pkg_exts:
            filename = filename + "." + ext
            if os.path.isfile(filename):
                filename = etree.parse(filename)
                found = True
                break
        
        if found is False:
            raise Exception("Compiler file not found in " + filename)
        
        return filename

        
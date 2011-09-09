# -*- coding: UTF-8 -*-

"""
Created on 31/08/2011

@author: Rafael Campos @rafaelxy
       
Tarjan's algorithm and topological sorting implementation in Python
by Paul Harrison, modified by Rafael Campos (compability)

@see: http://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
def strongly_connected_components(graph):
    """ 
    Find the strongly connected components in a graph using
    Tarjan's algorithm.
    
    graph should be a dictionary mapping node names to
    lists of successor nodes.
    """
    
    result = [ ]
    stack = [ ]
    low = { }
        
    def visit(node):
        if node in low: return
        node = node.lower()
    
        num = len(low)
        low[node] = num
        stack_pos = len(stack)
        stack.append(node)
    
        if graph[node] is not None:
            for successor in graph[node]:
                successor = successor.lower()
                visit(successor)
                low[node] = min(low[node], low[successor])
        
        if num == low[node]:
            component = tuple(stack[stack_pos:])
            del stack[stack_pos:]
            result.append(component)
            for item in component:
                low[item] = len(graph)
            
    for node in graph:
        visit(node)
    
    return result


def topological_sort(graph):
    count = { }
    for node in graph:
        count[node] = 0
    for node in graph:
        for successor in graph[node]:
            count[successor] += 1

    ready = [ node for node in graph if count[node] == 0 ]
    
    result = [ ]
    while ready:
        node = ready.pop(-1)
        result.append(node)
        
        for successor in graph[node]:
            count[successor] -= 1
            if count[successor] == 0:
                ready.append(successor)
    
    return result


def robust_topological_sort(graph):
    """ 
        First identify strongly connected components,
        then perform a topological sort on these components. 
    """

    components = strongly_connected_components(graph)

    node_component = { }
    for component in components:
        for node in component:
            node_component[node] = component

    component_graph = { }
    for component in components:
        component_graph[component] = [ ]
    
    for node in graph:
        node_c = node_component[node]
        if graph[node] is not None:
            for successor in graph[node]:
                successor = successor.lower()
                successor_c = node_component[successor]
                if node_c != successor_c:
                    component_graph[node_c].append(successor_c) 

    return topological_sort(component_graph)
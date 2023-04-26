# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:58:43 2023

@author: MICRO
"""

science={'botany':'pplants',
         'zoology':'animals',
         'virology':'viruses'}
science['neuroscience']='nervos_system'

print(science,'zoology' in science)
print(science.keys(),science.values(),science.items(),sep='\n')

d=list(science.values())
print(d)

del science['neuroscience']
print(science)

a={1:'hi',2.1:'hello',True:'haha'}
b={(0,0):'a',(1.0):'b',(0,1):'c'}
b.clear()
print(b)
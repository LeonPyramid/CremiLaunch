#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 02:11:53 2020

@author: leon
"""


from mechanize import Browser as brow
import listId as listi
br = brow()
br.add_password("services.emi.u-bordeaux.fr","rdelpy", "Alpha!0557")
for elt in listi.S001:
    print(elt)
    brow.open(br,"https://services.emi.u-bordeaux.fr/exam/js/getWake.php?h="+elt+"&std")

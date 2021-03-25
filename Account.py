# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 19:43:15 2021
This Simple Banking system was created by Choo Hongming Kent.
Run through the menus to simulate your banking activities.
@author: kchm2
"""

class Account:

    def __init__(self, nric, name, pin, balance):
        self._nric = nric
        self._name = name
        self._pin = pin
        self._balance = balance

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_pin(self):
        return self._pin

    def set_pin(self, pin):
        self._pin = pin

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance
        
    def get_nric(self):
        return self._nric

    def set_nric(self, nric):
        self._nric = nric

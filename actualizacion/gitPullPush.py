#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:07:33 2020

@author: esteban
"""
from git import Repo
from variables import pathRepo
repo = Repo(pathRepo)  # if repo is CWD just do '.'

def gitPull():
    repo.git.pull('origin', 'master')
def gitPush():
    repo.git.add(update=True)        
    repo.index.add(update=True)
repo.index.commit('my commit description')

origin.push()
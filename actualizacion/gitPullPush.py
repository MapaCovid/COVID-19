#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:07:33 2020

@author: esteban
"""
from git import Repo
from variables import pathRepo
repo = Repo(pathRepo)  
#mensajeCommit='creación script gitPullPush'
def gitPull():
    repo.git.pull('origin', 'master')
def gitPush(mensajeCommit):
    repo.git.add('.')        
    repo.index.commit(mensajeCommit)
    repo.git.push('origin', 'master')

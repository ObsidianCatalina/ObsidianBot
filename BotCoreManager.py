#芝士模仿Hanbot制作的集中化管理模块，大家也要多多支持Hantools
#芝士他的github:https://github.com/daizihan233
import yaml
import json
import fcntl
import requests_cache
def url_config(name:str):
    try:
        y = yaml.load(open('./yamls/urls.yaml', 'r', encoding='UTF-8'), yaml.SafeLoader)
        return y[name]
    except KeyError:
        return None
def eji(name:str):
    try:
       return json.load(open('./jsons/eji.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None
def linux_knowledge(name:str):
    try:
       return json.load(open('./jsons/linux_knowledge.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None 
def su(name:str):
    try:
        return json.load(open('./jsons/su.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None        
def update_log(name:str):
    try:
        return json.load(open('./jsons/update_log.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None   
def rand_sentence(name:str):
    try:
        return json.load(open('./jsons/rand_sentence.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None  
def shit(name:str):
    try:
        return json.load(open('./jsons/shit.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None 
def ver(name:str):
    try:
        return json.load(open('./jsons/version.json','r',encoding='utf-8')) [name]
    except KeyError:
        return None 
def settings(name:str):
    try:
        y = yaml.load(open('./yamls/settings.yaml', 'r', encoding='UTF-8'), yaml.SafeLoader)
        return y[name]
    except KeyError:
        return None 

# 芝士模仿Hanbot制作的集中化管理模块，大家也要多多支持Hantools
# 芝士他的github:https://github.com/daizihan233
import json

import yaml

# 文本文件的读取可以在程序启动时完成，不必每次调用都打开，减少内存占用（虽然你大概感受不到）
# 但有个缺点就是无法实现热更新（你还不至于懒到重启一次程序都不愿意罢？）
url_config_yaml = yaml.safe_load(open('./yamls/urls.yaml', 'r', encoding='UTF-8'))
eji_json = json.load(open('./jsons/eji.json', 'r', encoding='utf-8'))
linux_knowledge_json = json.load(open('./jsons/linux_knowledge.json', 'r', encoding='utf-8'))
su_json = json.load(open('./jsons/su.json', 'r', encoding='utf-8'))
update_log_json = json.load(open('./jsons/update_log.json', 'r', encoding='utf-8'))
rand_sentence_json = json.load(open('./jsons/rand_sentence.json', 'r', encoding='utf-8'))
ver_json = json.load(open('./jsons/version.json', 'r', encoding='utf-8'))
shit_json = json.load(open('./jsons/shit.json', 'r', encoding='utf-8'))
settings_yaml = yaml.safe_load(open('./yamls/settings.yaml', 'r', encoding='UTF-8'))


def url_config(name: str):
    try:
        return url_config_yaml[name]
    except KeyError:
        return None


def eji(name: str):
    try:
        return eji_json[name]
    except KeyError:
        return None


def linux_knowledge(name: str):
    try:
        return linux_knowledge_json[name]
    except KeyError:
        return None


def su(name: str):
    try:
        return su_json[name]
    except KeyError:
        return None


def update_log(name: str):
    try:
        return update_log_json[name]
    except KeyError:
        return None


def rand_sentence(name: str):
    try:
        return rand_sentence_json[name]
    except KeyError:
        return None


def shit(name: str):
    try:
        return shit_json[name]
    except KeyError:
        return None


def ver(name: str):
    try:
        return ver_json[name]
    except KeyError:
        return None


def settings(name: str):
    try:
        return settings_yaml[name]
    except KeyError:
        return None

#-*- coding:utf-8 -*-

import requests
import base64
import os
from configobj import ConfigObj 


def set_config(section, key, value):
    path = os.path.abspath(os.path.dirname(__file__)) + '/config.ini'
    config = ConfigObj(path, encoding='UTF8')
    config[section][key] = value
    config.write()


def get_config(section, key):
    path = os.path.abspath(os.path.dirname(__file__)) + '/config.ini'
    config = ConfigObj(path, encoding='UTF8') 
    return config[section][key]

ip = get_config('HOST_INFO', 'IP')
port = get_config('HOST_INFO', 'PORT')
user = get_config('USER_INFO', 'USER')
password = get_config('USER_INFO', 'PASSWORD')


account = 'Basic ' + base64.b64encode('%s:%s' % (user, password))
headers = {
    'Accept': 'application/vnd.docker.distribution.manifest.v2+json',
    'Authorization': account
}


def get_images(headers, ip, port):
    url = 'http://%s:%s/v2/_catalog' % (ip, port)
    print url
    resp = requests.get(url, headers=headers)
    print resp.text

get_images(headers, ip, port)


def get_sha256(headers, ip, port, image, tag):
    url = 'http://%s:%s/v2/%s/manifests/%s' % (ip, port, image, tag)
    print url
    resp = requests.get(url, headers=headers)
    sha256 = resp.headers['Docker-Content-Digest']
    return sha256

sha256 = get_sha256(headers, ip, port, 'registry', 'latest')
print sha256
    
    
def del_image(headers, ip, port, image, sha256):
    url = 'http://%s:%s/v2/%s/manifests/%s' % (ip, port, image, sha256)
    print url
    resp = requests.delete(url, headers=headers)
    print resp.headers
    print resp.text

del_image(headers, ip, port, 'registry', sha256)

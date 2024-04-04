#!/usr/bin/python3
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.90.12.170', '100.26.238.177']


def do_pack():
    """generates a .tgz archive from the contents of the web_static 
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None

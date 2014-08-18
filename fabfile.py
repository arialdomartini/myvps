# -*- coding: utf-8 -*-

from fabric.api import env
from fabric.api import task
from fabric.api import run
from fabric.api import local
from fabric.api import settings
from fabric.api import hide
from fabric.operations import put
from fabric.state import output
from fabric.colors import yellow
from fabric.colors import green

env.use_ssh_config = True
env.hosts = ['37.247.55.31']


@task(default=True)
def setup():
    create_user(env.local_user)


def create_user(username):
    info("Creating remote user %s" % username)
    run('adduser --ingroup sudo --disabled-password --gecos "" %s' % username)
    info("Authorizing %s's ssh key" % username)
    remote_ssh = '/home/%s/.ssh' % username
    run('mkdir -p %s' % remote_ssh)
    put('~/.ssh/id_rsa.pub', '%s/authorized_keys' % remote_ssh )
    success("Done.")

def info(message):
    output(" • %s" % message, yellow)


def success(message):
    output(u" ✓ %s" % message, green)


def output(message, color):
        print(color(message))

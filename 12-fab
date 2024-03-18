#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric import task, Connection

# Define the pack task
@task
def do_pack(c):
    """Method to compress directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if c.local("mkdir -p versions").failed is True:
            return None
    if c.local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

# Define the deploy task
@task
def do_deploy(c, archive_path):
    """Deploy to web server."""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    with Connection(c.host) as conn:
        if conn.put(archive_path, "/tmp/{}".format(file)).failed is True:
            return False
        if conn.run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
            return False
        if conn.run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
            return False
        if conn.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
            return False
        if conn.run("rm /tmp/{}".format(file)).failed is True:
            return False
        if conn.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
            return False
        if conn.run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
            return False
        if conn.run("rm -rf /data/web_static/current").failed is True:
            return False
        if conn.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
            return False
    return True

# Define the deploy task
@task
def deploy(c):
    """Deploy web static."""
    file = do_pack(c)
    if file is None:
        return False
    return do_deploy(c, file)

from fabric import Connection, task
from datetime import datetime
import os

hosts = ["100.26.18.247", "54.144.158.59"]


def do_pack():
    """method to compress directory web_static."""
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    if not os.path.isdir("versions"):
        os.makedirs("versions")
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name


def do_deploy(archive_path):
    """Deploy to web server.

    Args:
        archive_path (str): directory to dist.
    Returns:
        no file or error - False.
        Else - True.
    """
    if not os.path.isfile(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    name = os.path.splitext(file_name)[0]

    c = Connection('ubuntu@100.26.18.247')
    c.put(archive_path, "/tmp/{}".format(file_name))
    c.run("rm -rf /data/web_static/releases/{}/".format(name))
    c.run("mkdir -p /data/web_static/releases/{}/".format(name))
    c.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name))
    c.run("rm /tmp/{}".format(file_name))
    c.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))
    c.run("rm -rf /data/web_static/releases/{}/web_static".format(name))
    c.run("rm -rf /data/web_static/current")
    c.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))
    return True


@task
def deploy():
    """deploy web static."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)


if __name__ == "__main__":
    deploy()

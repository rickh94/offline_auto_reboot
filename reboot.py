import datetime
import os
import subprocess

from ruamel.yaml import YAML

yaml = YAML()
with open('/etc/offline_auto_reboot/server_config.yml') as configfile:
    config = yaml.load(configfile)

try:
    file_path = config['alt_file'] or '/tmp/offline'
except KeyError:
    file_path = '/tmp/offline'

try:
    hours_difference = config['offline_hours'] or 24
except KeyError:
    hours_difference = 24


accessed = datetime.datetime.fromtimestamp(os.stat(file_path).st_atime)
accessed_ago = datetime.datetime.now() - accessed
if accessed_ago >= datetime.timedelta(hours=hours_difference):
    print("Would reboot")
    #subprocess.run(["reboot"])

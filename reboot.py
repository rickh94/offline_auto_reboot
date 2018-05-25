import datetime
import os
import subprocess
from ruamel.yaml import YAML

needs_reboot = False

yaml = YAML()
with open('/etc/offline_auto_reboot/server_config.yml') as configfile:
    config = yaml.load(configfile)

try:
    file_path = config['alt_file'] or '/tmp/online'
except KeyError:
    file_path = '/tmp/online'

try:
    hours_difference = config['offline_hours'] or 24
except KeyError:
    hours_difference = 24

print(hours_difference)

if os.path.exists("/var/tmp/offline_auto_rebooted"):
    os.remove("/var/tmp/offline_auto_rebooted")
    needs_reboot = False

try:
    accessed = datetime.datetime.fromtimestamp(os.stat(file_path).st_atime)
    accessed_ago = datetime.datetime.now() - accessed
    print(accessed_ago)
    print(datetime.timedelta(hours=hours_difference))
    if accessed_ago >= datetime.timedelta(hours=hours_difference):
        needs_reboot = True
except FileNotFoundError:
    needs_reboot = True

if needs_reboot:
    subprocess.run(['touch', '/var/tmp/offline_auto_rebooted'])
    subprocess.run(["reboot"])
else:
    print("Wouldn't reboot")

import subprocess

from ruamel.yaml import YAML


yaml = YAML()
with open("/etc/offline_auto_reboot/external_config.yml", 'r') as configfile:
    config = yaml.load(configfile)

host_part = "{u}@{h}".format(u=config['username'], h=config['hostname'])
try:
    file_path = config['alt_file'] or '/tmp/online'
except KeyError:
    file_path = '/tmp/online'

subprocess.run(['ssh', '-i', config['ssh_key_path'], host_part, "touch {fp}".format(fp=file_path)])

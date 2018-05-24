# Offline Auto Reboot

Python scripts to automatically reboot linux servers (specifically raspberry
pis) if they become unreachable.

# Installation


Install [ruamel.yaml](https://pypi.org/project/ruamel.yaml) on both machines.

Put reboot.py on the server that should be rebooted if it goes offline and run
it at a desired interval. Put external.py on another machine that will always
be online and run it regularly (systemd services are included). The external
machine must have ssh access to the server by a key accessible to the script.
Probably best to create dedicated users on both machines to do the ssh.
external.py will touch a file on the server (in /tmp so no special permissions
are needed)


# Configuration

A configuration file should be placed at
`/etc/offline_auto_reboot/server_config.yml` for the server or
`/etc/offline_auto_reboot/external_config.yml`.

## Configuration options server

`offline_hours: `

  The reboot.py will check the `/tmp/online` file at regular intervals to see
its last accessed time. If it greater than 'offline_hours', it will reboot the
server.

  `alt_file:` An alternate file path to use instead of `/tmp/online`. This
must match in the external configuration.

## Configuration options external

  `ssh_key_path:`
  Path to an ssh private key that can be used to access the server

  `hostname:`
  Hostname of server to monitor and reboot.

  `username:`
  Username on remote machine for authenication.

  `alt_file:` Alternate file path on the server to use instead of
`/tmp/online`. Must match server config.

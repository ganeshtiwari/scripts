#!/usr/bin/env python3

import getpass
import paramiko

HOSTNAME = 'coderServer'
PORT = 22 


def run_ssh_cmd(username, password, cmd, hostname=HOSTNAME, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(\
        paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read().decode())


if __name__ == '__main__':
    username = input('Username: ')
    password = getpass.getpass(prompt='Password: ')
    cmd = 'ls -l /dev'
    run_ssh_cmd(username, password, cmd)

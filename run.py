import paramiko
import json


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# Load config file into memory and parse as JSON
config = read_json('./config.json')

# Load config into vars from memory
default_user = config['default_user']
default_pass = config['default_pass']
ssh_port = config['ssh_port']

# Instantiate Paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

command_file = open('commands.sh', 'r')
command_list = command_file.read()

for conf_node in config['conf_nodes']:
    username = ''
    password = ''

    if (conf_node['user']):
        username = conf_node['user']
    else:
        username = default_user

    if (conf_node['pass']):
        password = conf_node['pass']
    else:
        password = default_user

    ssh_client.connect(conf_node['host'], ssh_port, username, password)

    sftp = ssh_client.open_sftp()
    sftp.put('pexrtc.js.gz', 'pexrtc.js.gz')

    stdin, stdout, stderr = ssh_client.exec_command(command_list)

    command_result_out = stdout.readlines()
    command_result_err = stderr.readlines()

    print('Result Out', command_result_out)
    print('Result Err', command_result_err)

    ssh_client.close()

import paramiko

def sshCommand(hostname, port, username):
    sshClient = paramiko.SSHClient()                                   # create SSHClient instance

    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # AutoAddPolicy automatically adding the hostname and new host key
    sshClient.load_system_host_keys()
    sshClient.connect(hostname, port, username)
    while True:
        stdin, stdout, stderr = sshClient.exec_command('pwd')
        command = input(stdout.read().decode()[0:-1] + '>')
        stdin, stdout, stderr = sshClient.exec_command(command, get_pty=True)
        print((stdout.read() + stderr.read()).decode())


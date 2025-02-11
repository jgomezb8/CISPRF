import paramiko

# Create an SSH client object
ssh_client = paramiko.SSHClient()
# Set the policy to automatically add the host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to the remote server with the specified hostname, username, and password
ssh_client.connect(hostname="192.168.0.113", username="kali", password="kali")
# Execute the 'ls' command on the remote server
stdin, stdout, stderr = ssh_client.exec_command('ls')
# Read the output of the command
lines = stdout.readlines()

# Iterate through the output lines and print each line after stripping the newline character
for line in lines:
    print(line.strip('\n'))

import pexpect

# Define possible command prompts
PROMPT = ['# ', '>>> ', '> ', '\\$ ']

def send_command(child, cmd):
    # Send the command to the remote server
    child.sendline(cmd)
    # Wait for the command prompt to appear
    child.expect(PROMPT)
    # Print the output of the command
    print(child.before.decode('utf-8'))

def connect(host, user, password):
    # Define the SSH new key message
    ssh_newkey = 'Are you sure you want to continue connecting'
    # Construct the SSH connection string
    conn_str = 'ssh {user}@{host}'
    # Spawn a new child process to run the SSH command
    child = pexpect.spawn(conn_str)
    # Expect either a timeout, the SSH new key message, or a password prompt
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[Pp]assword:'])

    # Check for timeout
    if not ret:
        print('[-] Error Connecting')
        return
    # Check for SSH new key message
    else:
        child.sendline('yes')
        # Expect either a timeout or a password prompt after confirming the new key
        ret = child.expect([pexpect.TIMEOUT, '[Pp]assword:'])
        if not ret:
            print('[-] Error Connecting')
            return

    # Send the password
    child.sendline(password)
    # Expect the command prompt to appear
    child.expect(PROMPT)
    # Return the child process
    return child

if __name__ == '__main__':
    # Define the target host, user, and password
    tgt_host = 'localhost'
    tgt_user = 'root'
    tgt_passwd = 'toor'

    # Connect to the target host
    conn = connect(tgt_host, tgt_user, tgt_passwd)
    # Send a command to read the /etc/shadow file and grep for root
    send_command(conn, 'sudo cat /etc/shadow | grep root')

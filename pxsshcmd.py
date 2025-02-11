import pxssh

# Define variable x and assign the value 10
x = 10

def send_command(session, cmd):
    # Send the command to the SSH session
    session.sendline(cmd)
    # Wait for the command to execute and match the prompt
    session.prompt()
    # Print the command output
    print(session.before.decode('utf-8'))

def connect(host, user, password):
    # Initialize the pxssh object
    session = pxssh.pxssh()
    try:
        # Attempt to login to the remote host
        session.login(host, user, password)
        return session
    except pxssh.ExceptionPxssh as e:
        # Print error message if connection fails
        print('[-] Error Connecting')
        print(str(e))
        return None

if __name__ == '__main__':
    # Define the target host, username, and password
    tgt_host = '192.168.0.113'
    tgt_user = 'kali'
    tgt_passwd = 'kali'
    
    # Establish the connection
    session = connect(tgt_host, tgt_user, tgt_passwd)
    
    if session:
        # Send a command to read /etc/shadow file and grep for root
        send_command(session, 'sudo cat /etc/shadow | grep root')
        # Close the SSH session
        session.logout()

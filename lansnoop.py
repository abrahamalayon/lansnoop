import datetime
import subprocess
import os

NOW = datetime.datetime.now()


def createfile():
    filename = NOW.strftime("%Y-%m-%d_%H-%M-%S.txt")
    os.system(f"touch {filename}")
    return filename

def arpscan():
    interface = input("Enter the interface: ")
    network_address = input("Enter the network address (eg: 192.168.0.0/24): ")
    
    command = f"arp-scan --interface={interface} {network_address}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    filename = createfile()
    with open(filename, "a") as file:
        file.write(result.stdout)
    
    


""" def netdiscover():
    command = f"netdiscover"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    filename = createfile()
    with open(filename, "a") as file:
        file.write(result.stdout)
 """

def nmapscan():
    host_address = input("Enter the host address: ")
    command = f"nmap -sT {host_address}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    filename = createfile()
    with open(filename, "a") as file:
            file.write(result.stdout)
""" 
def less(filename):
    command = f"less {filename}"
    subprocess.run(command, shell=True)
   """

def main():
    createfile()
    arpscan()
    # netdiscover()
    nmapscan()
    # less()

if __name__ == "__main__":

    main()
    

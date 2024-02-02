# lansnoop
Conducts a quick survey of your LAN and documents it.


Lansnoop is a tool that allows you to scan your local network
and discover the devices connected to it. Then you can target specific
hosts with a more detailed scan. It displays the IP and MAC 
addresses of the devices in a table. Lansnoop also uses nmap to 
conduct basic network scans.  In the current version 1, it writes
the scan results to a file in the current directory. 

## Installation

To install lansnoop, you need to have Python 3 installed on your system.
You also need to install arp-scan and nmap, which you can do by running the following commands:

$ sudo apt-get update

$ sudo apt-get install python3

$ sudo apt-get install nmap

$ sudo apt-get install arp-scan

Better yet just run lansnoop.py in Kali Linux or Parrot OS.


## Usage

To use lansnoop, you need to run the lansnoop.py file with Python 3 and provide the network
address and subnet mask as arguments. For example, if you want to scan the network 192.168.1.0/24,
you can run the following command:

python3 lansnoop.py

The program will prompt you for input as to the network interface, network id and subnet mask (/24, /16 etc)

for example the inputs may be
eth0
192.168.1.0/24

The output will look something like this:

IP                  MAC

192.168.1.1         00:11:22:33:44:55

192.168.1.2         66:77:88:99:aa:bb

192.168.1.3         cc:dd:ee:ff:00:11

After the program produces a list of network hosts, you can choose your target to investigate further.
Enter the host ip address to use nmap to do a TCP scan of the target.

for example

192.168.1.167

This will produce the nmap scan results.
As an added feature, the lansnoop program saves a copy of the results of the scan as a text file
in the current directory.  The filename will be the date and time at the moment of the scan.

A menu system with more nmap options will be added.

## License

Lansnoop is licensed under the GNU License. See the LICENSE file for more details.

## Contributors

Lansnoop was created by Abraham Alayon. If you want to contribute to this project,
feel free to fork the repository and submit a pull request.


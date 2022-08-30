import subprocess as subp

class Sys:

    def __init__(self, command, OnSuccess):
        self.command = command
        self.OnSuccess = OnSuccess

    def run(self):
        recv = str(subp.getoutput(self.command))
        if recv :
            if recv.count(':') and recv.count('\n'):
                recv = str(recv).split(':')[2].strip().split('\n')[0]
            exit('{}[!] {} \n[-] Exiting.{}'.format('\033[91m',str(recv),'\033[0m'))
        else:
            print( self.OnSuccess);



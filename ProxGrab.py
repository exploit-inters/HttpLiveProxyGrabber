import threading, requests, time, os, sys, random

class RangeIP_Generate(object):
    def __init__(self):
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        StartIP = raw_input(self.c + ' Start IP: ' + self.w)
        ENDIP = raw_input(self.c + ' End IP: ' + self.w)
        PRoxYPort = raw_input(self.c + ' Enter Proxy port [8080,80]: ' + self.w)
        ip_range = self.Generate_IP(StartIP, ENDIP)
        for ip in ip_range:
            print('     ' + self.y + str(ip) + ':' + str(PRoxYPort))
            with open('scanIps.txt', 'a') as xX:
                xX.write(str(ip) + ':' + str(PRoxYPort) + '\n')
        Main()


    def Generate_IP(self, start_ip, end_ip):
        Start = list(map(int, start_ip.split(".")))
        end = list(map(int, end_ip.split(".")))
        rec = Start
        ip_range = []
        ip_range.append(start_ip)
        while rec != end:
            Start[3] += 1
            for i in (3, 2, 1):
                if rec[i] == 256:
                    rec[i] = 0
                    rec[i - 1] += 1
            ip_range.append(".".join(map(str, rec)))
        return ip_range

class ScaNIP(object):
    def __init__(self):
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        IpList = raw_input(self.c + " Input IP List [ip:port]: " + self.w)
        with open(IpList, 'r') as reader:
            file = reader.read().splitlines()
        thread = []
        for x in file:
            t = threading.Thread(target=self.CheckIP, args=(x, ''))
            t.start()
            thread.append(t)
            time.sleep(0.05)
        for j in thread:
            j.join()
        Main()

    def CheckIP(self, Proxy, x):
        try:
            Got = requests.get('http://httpbin.org/html', proxies={'http': Proxy}, timeout=5)
            if 'Herman Melville - Moby-Dick' in Got.text:
                print(self.c + '     ' + str(Proxy) + ' ---> ' + self.g + str(Got.status_code))
                with open('WorkHttpProxy.txt', 'a') as xX:
                    xX.write(Proxy + '\n')
        except requests.Timeout:
            print(self.c + '     ' + str(Proxy) + ' ---> ' + self.y + 'Timeout!')
        except requests.ConnectionError:
            print(self.c + '     ' + str(Proxy) + ' ---> ' + self.r + 'Dead IP!')


class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.print_logo()
        self.PrintOptions()
        while self.gg == True:
            Chose = raw_input(str('  @> '))
            if Chose == str(1):
                self.cls()
                self.print_logo()
                RangeIP_Generate()
            elif Chose == str(2):
                self.cls()
                self.print_logo()
                ScaNIP()
            elif Chose == str(99):
                self.gg = False
                sys.exit()
            elif Chose == "help" or Chose == "Help" or Chose == "HELP":
                self.PrintOptions()
            elif Chose == "cls" or Chose == "clear":
                self.cls()
                self.print_logo()
                self.PrintOptions()
            else:
                continue

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """

        
          _____                      _____           _     
         |  __ \   iran-cyber.net   / ____|         | |    
         | |__) | __ _____  ___   _| |  __ _ __ __ _| |__  
         |  ___/ '__/ _ \ \/ / | | | | |_ | '__/ _` | '_ \ 
         | |   | | | (_) >  <| |_| | |__| | | | (_| | |_) |
         |_|   |_|  \___/_/\_|\__, |\_____|_|  \__,_|_.__/ 
                               __/ |                       
           white Hat Hacker   |___/    github.com/04x             

     Note! : We don't Accept any responsibility for any illegal usage.       
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def PrintOptions(self):
        print(self.y + '        [1] ' + self.c + ' IP Range Generator')
        print(self.y + '        [2] ' + self.c + ' Proxy Scanner')
        print(self.y + '        [99]' + self.c + ' Exit')

Main()

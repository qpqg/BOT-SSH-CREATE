from bs4 import BeautifulSoup as qz
import requests
from os import system
from sys import exit
from platform import system as detect
class colorku():
    __W = '\033[0m'  # white (default)
    __R = '\033[31m'  # red
    __G = '\033[1;32m'  # green bold
    __O = '\033[33m'  # orange
    __B = '\033[34m'  # blue
    __P = '\033[35m'  # purple
    __C = '\033[36m'  # cyan
    __GR = '\033[37m'  # gray
    __bold = '\033[01m'
    def warning_red(self, text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__R,text, colorku.__W)
    def info_B(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__B,text, colorku.__W)
    def info_G(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__G,text, colorku.__W)
    def info_O(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__O,text, colorku.__W)
    def info_C(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__C,text, colorku.__W)
    def info_GR(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__GR,text, colorku.__W)
    def info_P(self,text):
        return "{}{}[!] {} [!]{}".format(colorku.__bold,colorku.__P,text, colorku.__W)
    def menus_GR(self,text):
        return "{}{}{}{}".format(colorku.__bold,colorku.__O,text, colorku.__W)

cl = colorku()
def banner():
    c = 35
    print cl.warning_red("SSH MYTUNNELING BETA V.0.2".center(c))
    print cl.info_B("=== [ PBM TEAM ] ===".center(c))
    print cl.info_G("Author: Qiuby Zhukhi".center(c))+"\r\n"
banner()
def menus():
    menu = {1: ["http://www.mytunneling.com/ssh-ssl-extra", "SSH EXTRA 7 hari", "http://www.mytunneling.com/create-account-ssh-ssl-extra.php"],
            2: ["http://www.mytunneling.com/ssh-ssl", "SSH SSL/TLS 7 hari", "http://www.mytunneling.com/create-account-ssh-ssl.php"],
            3: ["http://www.mytunneling.com/ssl-server-30", 'SSL SERVER 30 hari', "http://www.mytunneling.com/create-account-ssh-ssl-30.php"]}
    while True:
        for num,(link, anu, postdt) in menu.items():
            print cl.menus_GR("[{}] {}".format(num,anu))
        try:
            ops = int(raw_input(cl.info_B("Input No: ").replace("[!]", "")))
            print cl.info_G(menu[ops][1])
            return menu[ops][0], menu[ops][2], menu[ops][1]
        except ValueError:
            print cl.warning_red("PILIH PILIHAN YANG SUDAH ADA")
            continue
        except KeyError:
            print cl.warning_red("NOMOR {} TIDAK ADA, ANDA MUNGKIN BUTA".format(ops))
            continue
        break
men = menus()
def mytun():
    try:
        links = requests.get(men[0]).text
        parser = qz(links, "html.parser")
        row = parser.find("div", {"class": "row"})
        linkss = [urls["href"] for urls in row.findAll("a")]
        return linkss
    except:
        print cl.warning_red("UNKNOWN ERROR, CLOSED SCRIPT")
        exit(0)

def getreq():
    n = 0
    system("clear")
    name = raw_input("Masukkan userName:\n>")
    path = raw_input("Masukkan Log File (enter untuk save ke internal):\n>")
    while n < len(mytun()):
        n += 1
        for links in mytun():
            headers = {"Origin": "http://www.mytunneling.com",
                       "Referer": links}
            try:
                sesi = requests.session()
                req = sesi.get(links)
                serverid = qz(req.text, "html.parser").find("input", {"name": "serverid"})["value"]
                pwd = 1
                sesi.headers.update(headers)
                reqister = sesi.post(men[1], data = {"serverid": serverid, "username": name+str(n), "password": pwd}, timeout=30)
            except requests.exceptions.Timeout:
                print cl.warning_red("CONNECTION TIME OUT")
            except requests.exceptions.ConnectionError:
                print cl.warning_red("CONNECTION ERROR")
            except:
                print cl.warning_red("UNKNOWN ERROR")
            hsl = qz(reqister.text, "html.parser")
            print "="*35
            try:
                sis = "\n".join([str(i).replace("<br/>", "") for i in hsl.contents[5:10]])
                if sis != "":
                    print cl.info_GR(sis)
                    print "Port Dropbear:  3128,80"
                    print "Port OpenSSH: 22"
                    print "Port SSL/TLS: 443"
                    file_save(path, "=" * 35 + "\n" + men[2] + "\n" + sis + "\nPort: 3128,80\nPort OpenSSH: 22\nPort SSL/TLS: 443\r\n")
                else:
                    print cl.warning_red(hsl.text)
            except:
                print hsl.text
    exit(0)
def file_save(f, isi):
    if f == "":
        if detect() == "Windows":
            f = "c://SSHLog.txt"
        elif detect() == "Linux":
            f = "/storage/emulated/0/SSHLog.text"
    try:
        with open(f, "a+") as files:
            print cl.info_B("Save Ke path: "+f)
            files.write(isi)
            files.close()
    except:
        print cl.warning_red("KESALAHAN DALAM SAVE FILES")

if __name__ == '__main__':
    mytun()
    getreq()

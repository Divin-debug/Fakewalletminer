from colorama import Fore, Style; #init(convert=True)
from pystyle import Colors, Colorate
from httpsreqfast import init
import os, time, loadbar, random, string, colorama



class Checker:

    def __init__(self):
        if os.name == "nt":
            os.system("cls")
            self.__number = 0

        else:
            print(f"[{Fore.RED}!{Fore.RESET}] Tu dois être sur Windows.")



    def __print_banner(self):
        os.system("cls")
        print(Colorate.Horizontal(Colors.red_to_white,
        """
              ╔═╗┌─┐┬─┐┬ ┬┌─┐┌┬┐
              ╔═╝│  ├┬┘└┬┘├─┘ │ 
              ╚═╝└─┘┴└─ ┴ ┴   ┴ 
    auteur: [ @xDivin | t.me/infinityleak ]
options: Start checking [1] Credits [2] meow [3]\n"""))
    def __handle_input(self, option : int):
        if option == 1:
            print("option 1 ")
            self.__check__()
        elif option == 2:
            self.__print_credits()
        elif option == 3:
            print("")
            #self.__url_fr = "https://www.netflix.com/fr/LoginHelp"
            #self.__create_webdriver_tor()
        else:
            print("Option non trouvé.")
            exit(1)


    def __check__(self):
        os.system("cls")
        y = "abcdefghijklmnopqrstuvwxyz123467890"
        while True:
            def random_char(y):
                return ''.join(random.choice(string.ascii_letters) for x in range(y))
            lol = random_char(42)
            colorama.init()
            print(colorama.Fore.MAGENTA + "[-]" + colorama.Fore.WHITE + lol + colorama.Fore.CYAN + " → 0.00000 BTC ฿ ")
            time.sleep(0.1)

    def __print_loading(self):
        print(Fore.CYAN + "lo", end='', flush=True)
        time.sleep(0.2)
        print("ad", end='', flush=True)
        time.sleep(0.2)
        print("ing", end='', flush=True)
        time.sleep(0.2)
        print(".", end='', flush=True)
        time.sleep(0.2)
        print(".", end='', flush=True)
        time.sleep(0.2)
        print(".", end='', flush=True)
        time.sleep(0.2)
        print(Style.RESET_ALL)
        bar = loadbar.ColorBar(
            color=loadbar.Colors.cyan       # or 'cyan'
        )
        #print('\n'),  
        bar.start()
        for i in range(100):
            time.sleep(0.03)
            bar.update(step=i)
        bar.end()
        



    def _main(self):
        os.system("cls")
        os.system("title Heil hitler ᛋᛋ")
        #self.__print_loading()
        self.__print_banner()
        self.__option = int(input("\t"))
        self.__handle_input(self.__option)
        
        
if __name__ == "__main__":
    Checker()._main()
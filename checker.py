import requests
from termcolor import colored
from bs4 import BeautifulSoup


class Checker:
    def __init__(self):
        self.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        
        try:
            system_ip = requests.get('https://ident.me', proxies=self.proxies).text
            tor_ip_list = requests.get('https://check.torproject.org/exit-addresses').text
            if system_ip in tor_ip_list:
                print(colored(f'[DEBUG] Tor IP: {system_ip}', "green"))
        except:
            print(colored("[DEBUG] Check tor service", "red"))
            exit(1)
    
    def check(self, links):
        result = {}
        for url in links:
            try:
                data = requests.get(url, proxies=self.proxies)
            except:
                data = 'error'
            if data != 'error':
                status = True
                status_code = data.status_code
                soup = BeautifulSoup(data.text, 'html.parser')
                page_title = str(soup.title)
                page_title = page_title.replace('<title>', '')
                page_title = page_title.replace('</title>', '')
            elif data == 'error':
                status = False
                status_code = 'NA'
                page_title = 'NA'
            print(url, ': ', status, ': ', status_code, ': ', page_title)
            result[url] = {"status": status, "status_code": status_code, "title": page_title}
        return result

if __name__ == "__main__":
    # Test serivice
    checker = Checker()
    checker.check(["http://wiki47qqn6tey4id7xeqb6l7uj6jueacxlqtk3adshox3zdohvo35vad.onion/"])

    

#! /usr/bin/env python3
try:
    import requests, json, time, re, random, string, os
    from requests_toolbelt import MultipartEncoder
    from rich import print
    from rich.console import Console
    from requests.exceptions import RequestException
    from rich.panel import Panel
except (Exception, KeyboardInterrupt)as e:
    exit(f"[Error] {str(e).capitalize()}!")

Dump, Sukses, Gagal, Jumlah = [], [], [], 0

def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]  ______   __                       _                   
.' ____ \ [  |                     (_)                  
| (___ \_| | |--.   ,--.   _ .--.  __   _ .--.   .--./) 
 _.____`.  | .-. | `'_\ : [ `/'`\][  | [ `.-. | / /'`\; 
| \____) | | | | | // | |, | |     | |  | | | | \ \._// 
[bold white] \______.'[___]|__]\'-;__/[___]   [___][___||__].',__`  
                                               ( ( __)) 
        [italic red]Facebook auto share - Coded by Rozhak""", width=60, style="bold bright_white")) # Coded by Rozhak
    return ("Sukses")

class Main:

    def __init__(self) -> None:
        pass

    def Delay(self, menit, detik, user_ids):
        global Sukses, Gagal, Jumlah
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            print(f"[bold bright_white]   ╰─>[bold green] {int(Jumlah)}[bold white]/[bold green]{str(user_ids)[:20]}[bold white]/[bold green]{menit:02d}:{detik:02d}[bold white] Sukses:-[bold green]{len(Sukses)}[bold white] Gagal:-[bold red]{len(Gagal)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return ("Sukses")

    def Cookies(self):
        global Dump, Jumlah
        try:
            Banner()
            print(Panel(f"[italic white]Silahkan Masukan Cookies[italic green] Halaman Akun Facebook[italic white] Anda Juga Bisa Menggunakan[italic red] Koma[italic white] Untuk Cookies Acak!", width=60, style="bold bright_white", title=">>> Your Cookies <<<", subtitle="╭──────", subtitle_align="left"))
            your_cookies = Console().input("[bold bright_white]   ╰─> ")
            for cookies in your_cookies.split(','):
                if 'i_user=' in str(cookies) or 'c_user=' in str(cookies):
                    Dump.append(f'{cookies}')
                else:
                    continue
            if len(Dump) == 0:
                print(Panel(f"[italic red]Semua Cookies Yang Kamu Masukan Salah Silahkan Untuk Mengambil Cookies Di Halaman Facebook!", width=60, style="bold bright_white", title=">>> Cookies Salah <<<"))
                exit()
            else:
                print(Panel(f"[italic white]Silahkan Masukan Link Postingan Pastikan Gunakan Format Mbasic Dan Ada Tombol Bagikan!", width=60, style="bold bright_white", title=">>> Link Postingan <<<", subtitle="╭──────", subtitle_align="left"))
                link_postingan = Console().input("[bold bright_white]   ╰─> ")
                if 'https://mbasic.facebook.com/' in str(link_postingan):
                    print(Panel(f"[italic white]Silahkan Masukan Delay Berbagi Postingan Sebaiknya Gunakan Delay Di Atas[italic red] 60 Detik[italic white] Agar Aman!", width=60, style="bold bright_white", title=">>> Delay Sharing <<<", subtitle="╭──────", subtitle_align="left"))
                    delay_berbagi = int(Console().input("[bold bright_white]   ╰─> "))
                    print(Panel(f"[italic white]Sedang Menjalankan Auto Share Ke Halaman Facebook Anda Bisa Menggunakan[italic red] CTRL + Z[italic white] Untuk Berhenti!", width=60, style="bold bright_white", title=">>> Catatan <<<"))
                    while True:
                        for self.cookies in Dump:
                            try:
                                if 'i_user=' in str(self.cookies):
                                    self.user_ids = (re.search('i_user=(\d+);', str(self.cookies)).group(1))
                                else:
                                    self.user_ids = (re.search('c_user=(\d+);', str(self.cookies)).group(1))
                                self.Sharing(self.cookies, link_postingan, self.user_ids)
                                self.Delay(0, delay_berbagi, self.user_ids)
                                Jumlah += 1
                            except (KeyboardInterrupt):
                                print(f"                                                      ", end='\r')
                                time.sleep(2.5)
                                continue
                            except (RequestException) as e:
                                print(f"                                                      ", end='\r')
                                time.sleep(1.5)
                                print(f"[bold bright_white]   ╰─>[bold red] Koneksi Error...", end='\r')
                                time.sleep(7.5)
                                continue
                            except (Exception) as e:
                                print(f"[bold bright_white]   ╰─>[bold red] {str(e).upper()}", end='\r')
                                time.sleep(5.5)
                                print(f"                                                      ", end='\r')
                                continue
                        continue
                else:
                    print(Panel(f"[italic red]Format Link Postingan Salah Silahkan Masukan Seperti : https://mbasic.facebook.com/story.php?story_fbid=pfbid0F3hKfbeJW5gqxky435p9g3DTDwe1bRRwcMGbyw37AYJhLJbXREComGNARVzg5d4Zl&id=100006609458697!", width=60, style="bold bright_white", title=">>> Link Salah <<<"))
                    exit()
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=60, style="bold bright_white", title=">>> Error <<<"))
            exit()

    def Sharing(self, your_cookies, your_post, user_ids):
        global Sukses, Gagal
        with requests.Session() as r:
            self.android_version = (random.choice(['9', '10', '11', '12', '13']))
            self.device_model = random.choice(['RMX3661', 'RMX3687', 'RMX3686', 'RMX3241', 'RMX3388', 'RMX3472', 'RMX3471', 'RMX3393', 'RMX3392', 'RMX3612', 'RMX2202', 'RMX2121', 'RMX2176', 'RMX2052', 'RMX2075', 'RMX2076', 'RMX2144', 'RMX2111', 'RMX2200', 'RMX3092', 'RMX3093', 'RMX3042', 'RMX3041', 'RMX3125', 'RMX3122', 'RMX3121', 'RMX2205', 'RMX3161', 'RMX2205', 'RMX3396', 'RMX3572', 'RMX3242'])
            r.headers.update({
                'sec-fetch-dest': 'document',
                'user-agent': f'Mozilla/5.0 (Linux; Android {self.android_version}; {self.device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36',
                'upgrade-insecure-requests': '1',
                'sec-fetch-mode': 'navigate',
                'accept-language': 'id,en;q=0.9',
                'connection': 'keep-alive',
                'sec-fetch-site': 'none',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Host': 'mbasic.facebook.com',
                'sec-fetch-user': '?1',
                'cache-control': 'max-age=0',
                'accept-encoding': 'gzip, deflate',
            })
            try:
                response = r.get(your_post, cookies = {
                    'cookie': your_cookies
                }).text
            except (requests.exceptions.TooManyRedirects):
                print(f"                                                      ", end='\r')
                time.sleep(1.5)
                print(f"[bold bright_white]   ╰─>[bold red] Akun {user_ids} Dalam Mode Gratis...", end='\r')
                time.sleep(3.5)
                return ("TooManyRedirects")
            if 'Login ke Akun Anda' in str(response) or 'Login sebagai' in str(response) or 'facebook.com/login.php?' in str(response) or '/login/' in str(response):
                print(f"                                                      ", end='\r')
                time.sleep(1.5)
                print(f"[bold bright_white]   ╰─>[bold red] Login Diperlukan Untuk {user_ids}...", end='\r')
                time.sleep(3.5)
                return ("Login Diperlukan")
            else:
                if 'href="/composer/mbasic/' in str(response):
                    self.composer_share = re.search('href="/composer/mbasic/\\?(.*?)"', str(response)).group(1).replace('amp;', '')
                    response2 = r.get('https://mbasic.facebook.com/composer/mbasic/?{}'.format(self.composer_share), cookies = {
                        'cookie': your_cookies
                    }).text
                    boundary = '----WebKitFormBoundary' \
                        + ''.join(random.sample(string.ascii_letters + string.digits, 16))
                    try:
                        self.share_composer = re.search('action="/composer/mbasic/\\?(.*?)"', str(response2)).group(1).replace('amp;', '')
                        self.fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                        self.target = re.search('name="target" value="(\d+)"', str(response2)).group(1)
                        self.csid = re.search('name="csid" value="(.*?)"', str(response2)).group(1)
                        self.c_src = re.search('name="c_src" value="(.*?)"', str(response2)).group(1)
                        self.referrer = re.search('name="referrer" value="(.*?)"', str(response2)).group(1)
                        self.ctype = re.search('name="ctype" value="(.*?)"', str(response2)).group(1)
                        self.cver = re.search('name="cver" value="(.*?)"', str(response2)).group(1)
                        self.waterfall_source = re.search('name="waterfall_source" value="(.*?)"', str(response2)).group(1)
                        self.privacyx = re.search('name="privacyx" value="(\d+)"', str(response2)).group(1)
                        self.appid = re.search('name="appid" value="(.*?)"', str(response2)).group(1)
                        self.sid = re.search('name="sid" value="(.*?)"', str(response2)).group(1)
                        self.m = re.search('name="m" value="(.*?)"', str(response2)).group(1)
                        self.shared_from_post_id = re.search('name="shared_from_post_id" value="(\d+)"', str(response2)).group(1)
                    except (AttributeError):
                        print(f"                                                      ", end='\r')
                        time.sleep(1.5)
                        print(f"[bold bright_white]   ╰─>[bold red] AttributeError...", end='\r')
                        time.sleep(3.5)
                        return ("AttributeError")
                    r.headers.update({
                        'content-type': 'multipart/form-data; boundary={}'.format(boundary),
                        'origin': 'https://mbasic.facebook.com',
                        'referer': 'https://mbasic.facebook.com/composer/mbasic/?{}'.format(self.composer_share),
                    })
                    self.xc_message = (''.join(random.choices(string.ascii_uppercase + string.digits, k = random.randrange(5, 10))))
                    data = MultipartEncoder({
                        'fb_dtsg': (None, self.fb_dtsg),
                        'jazoest': (None, self.jazoest),
                        'target': (None, self.target),
                        'csid': (None, self.csid),
                        'c_src': (None, self.c_src),
                        'referrer': (None, self.referrer),
                        'ctype': (None, self.ctype),
                        'cver': (None, self.cver),
                        'waterfall_source': (None, self.waterfall_source),
                        'privacyx': (None, self.privacyx),
                        'appid': (None, self.appid),
                        'sid': (None, self.sid),
                        'xc_message': (None, self.xc_message),
                        'm': (None, self.m),
                        'shared_from_post_id': (None, self.shared_from_post_id),
                        'view_post': 'Bagikan',
                    }, boundary = boundary)
                    response3 = r.post('https://mbasic.facebook.com/composer/mbasic/?{}'.format(self.share_composer), data = data, cookies = {
                        'cookie': your_cookies
                    })
                    if 'Lampirkan Foto' in str(response3.text) or 'https://mbasic.facebook.com/story.php?story_fbid=' in str(response3.url):
                        Sukses.append(f'{response3.text}')
                        if '&eav=' in str(response3.url):
                            self.share_postingan = (str(response3.url).split('&eav=')[0])
                        else:
                            self.share_postingan = (str(response3.url))
                        print(Panel(f"""[bold white]Status :[italic green] You have successfully shared...[/]
[bold white]Link :[bold red] {self.share_postingan}""", width=60, style="bold bright_white", title=">>> Sukses <<<"))
                        return ("Sukses Membagikan Postingan")
                    elif 'Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara.' in str(response3.text):
                        print(f"                                                      ", end='\r')
                        time.sleep(1.5)
                        print(f"[bold bright_white]   ╰─>[bold red] Akun Facebook {user_ids} Terblokir...", end='\r')
                        time.sleep(3.5)
                        return ("Terkena Spam")
                    else:
                        Gagal.append(f'{response3.text}')
                        return ("Gagal Membagikan Postingan")
                else:
                    print(f"                                                      ", end='\r')
                    time.sleep(1.5)
                    print(f"[bold bright_white]   ╰─>[bold red] Tidak Ditemukan Tombol Share Untuk Postingan Tersebut...", end='\r')
                    time.sleep(3.5)
                    return ("Tombol Share Tidak Ditemukan")

if __name__ == '__main__':
    try:
        if os.path.exists("Data/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Sharing/main/Data/Youtube.json').text)['Youtube']
            os.system(f'xdg-open {youtube_url}')
            with open('Data/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(3.5)
        os.system('git pull')
        Main().Cookies()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=60, style="bold bright_white", title=">>> Error <<<"))
        exit()
    except (KeyboardInterrupt):
        exit()
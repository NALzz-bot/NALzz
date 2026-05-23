#!/usr/bin/env python3
# ================================================================
# 🕵️ IPTRACK PRO v1.0 - TERMUX READY
# ================================================================
# CODING BY    : NICK HACKER 💀
# STATUS       : 100% WORKING ✅
# PLATFORM     : TERMUX / LINUX
# ================================================================

import requests
import json
import os
import time
import sys
from datetime import datetime

# Warna untuk Termux (ANSI colors)
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
PURPLE = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(CYAN + BOLD + """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗  ║
║   ██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝  ║
║   ██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝   ║
║   ██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗   ║
║   ██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗  ║
║   ╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  ║
║                                                          ║
║                 IPTRACK PRO v1.0                         ║
║              REAL TIME IP TRACKING                       ║
║                                                          ║
║            CODING BY: NICK HACKER 💀                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """ + RESET)
    print(YELLOW + "⚠️  FOR EDUCATIONAL PURPOSES ONLY" + RESET)
    print(RED + "💀 UNAUTHORIZED USE = YOUR RESPONSIBILITY" + RESET)
    print("=" * 54)

def get_device_name(user_agent):
    """Deteksi device dari User-Agent"""
    if not user_agent:
        return "Tidak terdeteksi"
    
    ua = user_agent.lower()
    
    # Deteksi OS
    if 'android' in ua:
        os_name = "Android"
        # Deteksi merk
        if 'samsung' in ua:
            brand = "Samsung"
        elif 'xiaomi' in ua or 'redmi' in ua:
            brand = "Xiaomi"
        elif 'oppo' in ua:
            brand = "Oppo"
        elif 'vivo' in ua:
            brand = "Vivo"
        elif 'realme' in ua:
            brand = "Realme"
        elif 'nokia' in ua:
            brand = "Nokia"
        elif 'asus' in ua:
            brand = "Asus"
        else:
            brand = "Unknown Android"
        return f"{brand} ({os_name})"
    
    elif 'iphone' in ua or 'ipad' in ua:
        return f"Apple iOS"
    
    elif 'windows' in ua:
        if 'phone' in ua:
            return "Windows Phone"
        else:
            return "Windows PC"
    
    elif 'mac' in ua:
        return "MacOS"
    
    elif 'linux' in ua:
        return "Linux"
    
    else:
        return "Unknown Device"

def track_ip(ip_address):
    """Fungsi utama tracking IP dengan multiple API"""
    
    print(YELLOW + "\n[⏳] Sedang melacak IP: " + ip_address + RESET)
    time.sleep(1)
    
    results = {}
    
    # API 1: ip-api.com (cepat & gratis)
    try:
        url1 = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,mobile,proxy,hosting,query"
        response1 = requests.get(url1, timeout=10)
        data1 = response1.json()
        
        if data1.get('status') == 'success':
            results['negara'] = data1.get('country', 'N/A')
            results['region'] = data1.get('regionName', 'N/A')
            results['kota'] = data1.get('city', 'N/A')
            results['kode_pos'] = data1.get('zip', 'N/A')
            results['lat'] = data1.get('lat', 'N/A')
            results['lon'] = data1.get('lon', 'N/A')
            results['isp'] = data1.get('isp', 'N/A')
            results['org'] = data1.get('org', 'N/A')
            results['as'] = data1.get('as', 'N/A')
            results['mobile'] = "Ya" if data1.get('mobile') else "Tidak"
            results['proxy'] = "Ya" if data1.get('proxy') else "Tidak"
            results['hosting'] = "Ya" if data1.get('hosting') else "Tidak"
    except:
        pass
    
    # API 2: ipwhois.io (backup)
    try:
        url2 = f"http://ipwhois.io/json/{ip_address}"
        response2 = requests.get(url2, timeout=10)
        data2 = response2.json()
        
        if data2.get('success') != False:
            if 'country' in data2:
                results['negara'] = data2.get('country', results.get('negara', 'N/A'))
            results['timezone'] = data2.get('timezone', 'N/A')
            results['currency'] = data2.get('currency', 'N/A')
    except:
        pass
    
    return results

def get_ip_from_domain(domain):
    """Resolve domain ke IP"""
    import socket
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return None

def main():
    while True:
        clear_screen()
        banner()
        
        print(CYAN + """
╔══════════════════════════════════════════════════════════╗
║                    MENU UTAMA                            ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   [1] 🎯 TRACK IP TARGET                                 ║
║   [2] 🌐 TRACK DOMAIN/WEBSITE                            ║
║   [3] 📍 TRACK IP SENDIRI (MY IP)                        ║
║   [0] 🚪 EXIT                                            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
        """ + RESET)
        
        choice = input(YELLOW + "\n[+] Pilih menu (0-3): " + RESET)
        
        if choice == '1':
            clear_screen()
            banner()
            print(CYAN + "\n[🎯] MODE: TRACK IP TARGET" + RESET)
            print("-" * 40)
            
            target_ip = input(YELLOW + "\n[?] Masukkan IP target: " + RESET)
            
            if not target_ip:
                print(RED + "\n❌ IP tidak boleh kosong!" + RESET)
                input(YELLOW + "\nTekan Enter untuk kembali..." + RESET)
                continue
            
            result = track_ip(target_ip)
            
            if result:
                print(GREEN + "\n✅ HASIL PELACAKAN:" + RESET)
                print(CYAN + "═" * 50 + RESET)
                print(WHITE + f"📍 Alamat IP      : {GREEN}{target_ip}{RESET}")
                print(WHITE + f"🌍 Negara         : {CYAN}{result.get('negara', 'N/A')}{RESET}")
                print(WHITE + f"🏙️  Kota/Region    : {CYAN}{result.get('kota', 'N/A')} - {result.get('region', 'N/A')}{RESET}")
                print(WHITE + f"📮 Kode Pos       : {CYAN}{result.get('kode_pos', 'N/A')}{RESET}")
                print(WHITE + f"🗺️  Koordinat      : {CYAN}{result.get('lat', 'N/A')}, {result.get('lon', 'N/A')}{RESET}")
                print(WHITE + f"📡 ISP            : {CYAN}{result.get('isp', 'N/A')}{RESET}")
                print(WHITE + f"🏢 Organisasi     : {CYAN}{result.get('org', 'N/A')}{RESET}")
                print(WHITE + f"🔢 AS Number      : {CYAN}{result.get('as', 'N/A')}{RESET}")
                print(WHITE + f"📱 Mobile         : {CYAN}{result.get('mobile', 'N/A')}{RESET}")
                print(WHITE + f"🕵️ Proxy          : {CYAN}{result.get('proxy', 'N/A')}{RESET}")
                print(WHITE + f"☁️  Hosting        : {CYAN}{result.get('hosting', 'N/A')}{RESET}")
                print(WHITE + f"🕒 Timezone       : {CYAN}{result.get('timezone', 'N/A')}{RESET}")
                print(CYAN + "═" * 50 + RESET)
                
                # Simpan ke file
                save = input(YELLOW + "\n[?] Simpan hasil ke file? (y/n): " + RESET).lower()
                if save == 'y':
                    filename = f"iptrack_{target_ip}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w') as f:
                        f.write(f"IP TARGET: {target_ip}\n")
                        f.write(f"Negara: {result.get('negara', 'N/A')}\n")
                        f.write(f"Kota: {result.get('kota', 'N/A')}\n")
                        f.write(f"Region: {result.get('region', 'N/A')}\n")
                        f.write(f"Kode Pos: {result.get('kode_pos', 'N/A')}\n")
                        f.write(f"Koordinat: {result.get('lat', 'N/A')}, {result.get('lon', 'N/A')}\n")
                        f.write(f"ISP: {result.get('isp', 'N/A')}\n")
                        f.write(f"Waktu: {datetime.now()}\n")
                    print(GREEN + f"✅ Disimpan ke: {filename}" + RESET)
            else:
                print(RED + "\n❌ Gagal melacak IP! Coba lagi." + RESET)
            
            input(YELLOW + "\nTekan Enter untuk kembali..." + RESET)
        
        elif choice == '2':
            clear_screen()
            banner()
            print(CYAN + "\n[🌐] MODE: TRACK DOMAIN/WEBSITE" + RESET)
            print("-" * 40)
            
            domain = input(YELLOW + "\n[?] Masukkan domain (contoh: google.com): " + RESET)
            
            if not domain:
                print(RED + "\n❌ Domain tidak boleh kosong!" + RESET)
                input(YELLOW + "\nTekan Enter untuk kembali..." + RESET)
                continue
            
            # Bersihkan domain
            domain = domain.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
            
            ip_result = get_ip_from_domain(domain)
            
            if ip_result:
                print(GREEN + f"\n✅ Domain {domain} → IP: {ip_result}" + RESET)
                result = track_ip(ip_result)
                
                if result:
                    print(CYAN + "\n" + "═" * 50 + RESET)
                    print(WHITE + f"📍 Alamat IP      : {GREEN}{ip_result}{RESET}")
                    print(WHITE + f"🌐 Domain         : {CYAN}{domain}{RESET}")
                    print(WHITE + f"🌍 Negara         : {CYAN}{result.get('negara', 'N/A')}{RESET}")
                    print(WHITE + f"🏙️  Kota          : {CYAN}{result.get('kota', 'N/A')}{RESET}")
                    print(WHITE + f"📡 ISP            : {CYAN}{result.get('isp', 'N/A')}{RESET}")
                    print(CYAN + "═" * 50 + RESET)
                else:
                    print(RED + "\n❌ Gagal mendapat detail IP!" + RESET)
            else:
                print(RED + f"\n❌ Gagal resolve domain: {domain}" + RESET)
            
            input(YELLOW + "\nTekan Enter untuk kembali..." + RESET)
        
        elif choice == '3':
            clear_screen()
            banner()
            print(CYAN + "\n[📍] MODE: MY IP ADDRESS" + RESET)
            print("-" * 40)
            
            try:
                response = requests.get('https://api.ipify.org?format=json', timeout=10)
                my_ip = response.json().get('ip')
                
                if my_ip:
                    print(GREEN + f"\n✅ IP Anda saat ini: {my_ip}" + RESET)
                    result = track_ip(my_ip)
                    
                    if result:
                        print(CYAN + "\n" + "═" * 50 + RESET)
                        print(WHITE + f"📍 Alamat IP      : {GREEN}{my_ip}{RESET}")
                        print(WHITE + f"🌍 Negara         : {CYAN}{result.get('negara', 'N/A')}{RESET}")
                        print(WHITE + f"🏙️  Kota          : {CYAN}{result.get('kota', 'N/A')}{RESET}")
                        print(WHITE + f"📡 ISP            : {CYAN}{result.get('isp', 'N/A')}{RESET}")
                        print(CYAN + "═" * 50 + RESET)
                else:
                    print(RED + "\n❌ Gagal mendapat IP!" + RESET)
            except Exception as e:
                print(RED + f"\n❌ Error: {e}" + RESET)
            
            input(YELLOW + "\nTekan Enter untuk kembali..." + RESET)
        
        elif choice == '0':
            clear_screen()
            print(RED + BOLD + "\n💀 EXITING IPTRACK PRO..." + RESET)
            print(CYAN + "Coding by NICK HACKER - Stay dangerous! 😈🔥" + RESET)
            time.sleep(2)
            sys.exit(0)
        
        else:
            print(RED + "\n❌ Pilihan tidak valid!" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\n💀 Interrupted! Exiting..." + RESET)
        sys.exit(0)
    except Exception as e:
        print(RED + f"\n❌ Fatal Error: {e}" + RESET)
        sys.exit(1)
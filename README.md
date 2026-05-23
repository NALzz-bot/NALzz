# NALzz
---

```markdown
# 🌐 IP TRACKER PRO V1 | TRACK ANY IP WITH REAL-TIME DATA

> **"Know your target, know their location, know everything."** 🔥

![Version](https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-lightgrey?style=for-the-badge&logo=linux)

---

## 📌 SCREENSHOT

```

╔══════════════════════════════════════════════════════════╗
║                    IP TRACKER PRO v1                     ║
╠══════════════════════════════════════════════════════════╣
║  📍 IP Address    : 8.8.8.8                             ║
║  🌍 Country       : United States                        ║
║  🏙️  City          : Mountain View                       ║
║  📡 ISP           : Google LLC                           ║
║  🗺️  Location      : 37.4056, -122.0775                 ║
╚══════════════════════════════════════════════════════════╝

```

---

## ✨ FEATURES

| Feature | Status | Description |
|---------|--------|-------------|
| 🎯 **Real IP Tracking** | ✅ | Track any IP address live |
| 🌍 **Geo Location** | ✅ | Get country, city, region |
| 📡 **ISP Detection** | ✅ | Know the internet provider |
| 🗺️ **Coordinates** | ✅ | Latitude & Longitude |
| 📱 **Mobile Detection** | ✅ | Detect if IP is mobile |
| 🕵️ **Proxy/VPN Detection** | ✅ | Know if using proxy |
| 💾 **Save Results** | ✅ | Export to TXT file |
| 🎨 **Colored Output** | ✅ | Beautiful terminal UI |

---

## 🚀 INSTALLATION

### 📱 Termux
```bash
pkg update && pkg upgrade
pkg install python git -y
git clone https://github.com/NALzz-bot/NALzz.git
cd NALzz
pip install -r requirements.txt
python iptracker.py
```

🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 git -y
git clone https://github.com/NALzz-bot/NALzz.git
cd NALzz
pip3 install -r requirements.txt
python3 iptracker.py
```

---

📖 HOW TO USE

```bash
# Run the tool
python iptracker.py

# Then choose menu:
[1] 🎯 Track IP Target
[2] 🌐 Track Domain/Website
[3] 📍 Track My IP
[0] 🚪 Exit
```

Example Input

```
[+] Enter IP address: 8.8.8.8
[+] Enter domain: google.com
```

---

📸 OUTPUT EXAMPLE

```
✅ HASIL PELACAKAN:
══════════════════════════════════════════════════════════
📍 Alamat IP      : 8.8.8.8
🌍 Negara         : United States
🏙️  Kota          : Mountain View
📡 ISP            : Google LLC
🗺️  Koordinat     : 37.4056, -122.0775
📱 Mobile         : Tidak
🕵️ Proxy          : Tidak
☁️  Hosting       : Ya
══════════════════════════════════════════════════════════
✅ Disimpan ke: iptrack_8.8.8.8_20240101_120000.txt
```

---

🛠️ REQUIREMENTS

Package Version
Python 3.8+
requests latest
colorama latest
folium (optional) latest

---

📁 FILE STRUCTURE

```
NALzz/
├── 📄 iptracker.py      # Main script
├── 📄 requirements.txt  # Dependencies
├── 📄 README.md         # Documentation
└── 📁 results/          # Saved tracking results
```

---

⚠️ DISCLAIMER

```
⚠️ This tool is for EDUCATIONAL PURPOSES only!
⚠️ Don't use this tool for illegal activities.
⚠️ The author is not responsible for misuse.
⚠️ Always get permission before tracking anyone.
```

---

🎯 ROADMAP

· Basic IP Tracking
· Domain Resolution
· Save Results to File
· Map Visualization
· Batch IP Tracking
· Email Notification
· Telegram Bot Integration

---

👨‍💻 AUTHOR

 
Name NALzz
GitHub @NALzz-bot
Telegram @NALzzSTORE177
Project IP Tracker Pro V1

---

import time
import os
from dotenv import load_dotenv
from network import AIBot # Import kelas AIBot dari network.py

# Load konfigurasi dari .env
load_dotenv()

# Ambil dari .env, sediakan default jika tidak ada
MODEL_PATH = os.getenv("MODEL_PATH", "./models/brain_v1.h5")
TARGET_URL = os.getenv("TARGET_URL", "http://localhost:8080/login") # Default URL untuk local testing
TARGET_USER = os.getenv("TARGET_USER", "admin") # Default username

def bot_engine(mode):
    modes = {
        "1": ("Ringan", 2.0),
        "2": ("Sedang", 1.0),
        "3": ("Keras", 0.1),
        "4": ("Kuat", 0.01),
        "5": ("Gila", 0.0),
        "6": ("Syaitan 💀", 0.0) # Syaitan akan memanggil AI
    }
    
    nama, delay = modes.get(mode, ("Ringan", 2.0))
    print(f"\n[!] Mengaktifkan Mode: {nama}")
    
    if mode == "6": # Mode Syaitan akan menggunakan AI Bot
        ai_bot = AIBot(MODEL_PATH, TARGET_URL, TARGET_USER)
        ai_bot.load_model()
        if ai_bot.model:
            predicted_passwords = ai_bot.generate_password_predictions(num_predictions=1000) # AI prediksi 1000 password
            ai_bot.attack(predicted_passwords)
        else:
            print("[!] Mode Syaitan tidak dapat berjalan tanpa model AI.")
    else:
        # Simulasi Bot Berjalan (untuk mode non-AI)
        passwords = ["12345", "admin", "sayang", "password", "bismillah", "rahasia", "qwerty"]
        for p in passwords:
            print(f"[*] Bot mencoba: {p}")
            time.sleep(delay)
            # Di sini bisa ditambah logika permintaan HTTP ke TARGET_URL
        print("\n[+] Proses Selesai.")

if __name__ == "__main__":
    print("--- LOGIN BOT MENU ---")
    print("1. Ringan\n2. Sedang\n3. Keras\n4. Kuat\n5. Gila\n6. Syaitan 💀 (AI Brute Force)")
    pilihan = input("Pilih kekuatan bot: ")
    bot_engine(pilihan)

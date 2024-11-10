def tanya_jawab_kali_linux():
    print("Selamat datang di program tanya jawab perintah Kali Linux!")
    print("Silakan masukkan pertanyaan Anda (ketik 'keluar' untuk berhenti)")

    while True:
        pertanyaan = input("\nMasukkan pertanyaan: ").strip().lower()

        # Keluar dari program
        if pertanyaan == "keluar":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        
        # Perintah dasar Linux
        elif "update" in pertanyaan or "upgrade" in pertanyaan:
            print("Untuk update sistem pada Kali Linux, gunakan perintah:\n  sudo apt update && sudo apt upgrade")
        elif "list directory" in pertanyaan or "lihat isi folder" in pertanyaan:
            print("Untuk melihat isi direktori, gunakan perintah:\n  ls atau ls -la untuk lebih detail.")
        elif "buat direktori" in pertanyaan:
            print("Untuk membuat direktori baru, gunakan perintah:\n  mkdir <nama-direktori>")
        elif "pindah direktori" in pertanyaan:
            print("Untuk pindah ke direktori lain, gunakan perintah:\n  cd <nama-direktori>")
        elif "hapus file" in pertanyaan:
            print("Untuk menghapus file, gunakan perintah:\n  rm <nama-file>")
        elif "hapus direktori" in pertanyaan:
            print("Untuk menghapus direktori, gunakan perintah:\n  rm -r <nama-direktori>")
        
        # Alat populer di Kali Linux
        elif "nmap" in pertanyaan:
            print("Nmap adalah alat pemindaian jaringan. Contoh penggunaan:\n  nmap <alamat-ip> untuk memindai IP tertentu.")
        elif "metasploit" in pertanyaan:
            print("Metasploit adalah framework eksploitasi. Jalankan dengan perintah:\n  sudo msfconsole")
        elif "aircrack-ng" in pertanyaan:
            print("Aircrack-ng adalah alat untuk audit jaringan Wi-Fi. Contoh penggunaannya:\n  sudo aircrack-ng <file-capture>")
        elif "hydra" in pertanyaan:
            print("Hydra adalah alat brute-force untuk login. Contoh penggunaan:\n  hydra -l <username> -P <wordlist> <target> <layanan>")
        elif "sqlmap" in pertanyaan:
            print("Sqlmap adalah alat untuk menemukan dan mengeksploitasi SQL Injection. Contoh penggunaan:\n  sqlmap -u <url-target> --dbs untuk melihat database.")
        elif "john the ripper" in pertanyaan:
            print("John the Ripper adalah alat untuk cracking password. Contoh penggunaan:\n  john --wordlist=<wordlist> <file-hash>")
        elif "wireshark" in pertanyaan:
            print("Wireshark adalah alat analisis jaringan. Jalankan dengan perintah:\n  sudo wireshark")
        
        # Perintah Jaringan
        elif "ping" in pertanyaan:
            print("Ping digunakan untuk mengecek koneksi ke suatu alamat IP. Contoh:\n  ping <alamat-ip>")
        elif "netstat" in pertanyaan:
            print("Netstat digunakan untuk menampilkan koneksi jaringan, tabel routing, dan statistik antarmuka. Contoh:\n  netstat -an")
        elif "ifconfig" in pertanyaan:
            print("Ifconfig digunakan untuk konfigurasi antarmuka jaringan. Contoh:\n  ifconfig untuk melihat konfigurasi antarmuka jaringan.")
        elif "traceroute" in pertanyaan:
            print("Traceroute digunakan untuk melacak jalur ke host jaringan. Contoh:\n  traceroute <alamat-ip>")
        
        # Pemindaian dan Rekayasa Sosial
        elif "setoolkit" in pertanyaan:
            print("SET (Social Engineering Toolkit) adalah toolkit untuk rekayasa sosial. Jalankan dengan perintah:\n  sudo setoolkit")
        
        # Perintah Sistem dan File
        elif "chmod" in pertanyaan:
            print("Chmod digunakan untuk mengubah izin file. Contoh:\n  chmod 755 <nama-file>")
        elif "chown" in pertanyaan:
            print("Chown digunakan untuk mengubah pemilik file atau direktori. Contoh:\n  chown <user>:<group> <nama-file>")
        elif "tar" in pertanyaan:
            print("Tar digunakan untuk mengkompresi atau mengekstrak file. Contoh untuk ekstraksi:\n  tar -xvf <file.tar>")
        
        # Tidak ditemukan
        else:
            print("Maaf, saya tidak memiliki jawaban untuk pertanyaan tersebut. Coba pertanyaan lain.")

# Menjalankan fungsi tanya jawab
tanya_jawab_kali_linux()

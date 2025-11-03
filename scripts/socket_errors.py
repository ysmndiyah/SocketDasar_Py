#Menangani error saat koneksi socket ke server HTTP.

import socket

def request_http(host, port, filename):
    try:
        # Membuat socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"🔗 Mencoba koneksi ke {host}:{port}")
        s.connect((host, port))

        # Kirim request HTTP sederhana
        request = f"GET {filename} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.sendall(request.encode())

        # Terima data dari server
        response = b""
        while True:
            buf = s.recv(2048)
            if not buf:
                break
            response += buf

        # Tampilkan hasil
        print("Koneksi berhasil. Baris pertama respons:")
        print(response.decode(errors="ignore").split("\r\n")[0])

    except socket.gaierror:
        print("Host tidak ditemukan (socket.gaierror)")
    except ConnectionRefusedError:
        print("Koneksi ditolak (ConnectionRefusedError)")
    except socket.timeout:
        print("Koneksi timeout (socket.timeout)")
    except socket.error as e:
        print("Error socket lainnya:", e)
    finally:
        s.close()


if __name__ == "__main__":
    # Jalankan manual tanpa main_runner
    host = input("Masukkan host: ")
    port = int(input("Masukkan port: "))
    file = input("Masukkan file (misal, index.html): ")
    request_http(host, port, file)

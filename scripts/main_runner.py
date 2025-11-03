#Menjalankan seluruh percobaan socket: timeout, error handling, dan buffer.

from socket_timeout import test_socket_timeout
from socket_errors import request_http
from buffer_modify import show_and_modify_buffers

def main():
    print("=== A. Pengujian Timeout ===")
    test_socket_timeout()
    print("\n=== B. Pengujian Error Handling ===")
    request_http("www.google.com", 80, "/index.html")
    print("\n=== C. Pengujian Buffer Size ===")
    show_and_modify_buffers()
    print("\nSelesai semua pengujian")

if __name__ == "__main__":
    main()

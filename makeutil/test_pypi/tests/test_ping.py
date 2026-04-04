import socket


def test_port_open():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex(("localhost", 8080))
    assert res == 0, "Port 8080 should be open (server running)"

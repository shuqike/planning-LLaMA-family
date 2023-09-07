import socket


def find_free_port():
    with socket.socket() as s:
            s.bind(('', 0))
    return s.getsockname()[1]


if __name__ == '__main__':
    print(find_free_port())
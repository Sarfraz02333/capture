import os

from receiver_server import ReceiverHTTPServer, ReceiverHandler, get_bind_address


def main() -> None:
    server = ReceiverHTTPServer(get_bind_address(), ReceiverHandler)
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', '8765')
    print(f'Receiver server listening on http://{host}:{port}')
    server.serve_forever()


if __name__ == '__main__':
    main()

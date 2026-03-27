from .server import create_server


def main() -> None:
    server = create_server()
    print("CaseFlow API listening on http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

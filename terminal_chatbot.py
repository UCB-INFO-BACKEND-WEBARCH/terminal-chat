import argparse
from urllib.parse import urljoin
import logging
import requests

def make_request_request(server_url, message):
    full_url = urljoin(server_url, "/message")

    raw_data = dict()
    raw_data["data"] = {"command": None, "message": message } 
    
    try: 
        r = requests.post(full_url, json=raw_data)
        r.raise_for_status()
    except requests.exceptions.ConnectionError as err:
        # eg, no internet
        raise SystemExit(err)
    except requests.exceptions.HTTPError as err:
        # eg, url, server and other errors
        raise SystemExit(err)

    data = r.json()

    return data["data"]

def main():

    parser = argparse.ArgumentParser(prog = 'TerminalChatBot',
        description = 'Terminal Chat Bot that sends request to server specified by the server url',
        epilog = 'Please go to the INFO 253B Bcourses website for mreo information')
    parser.add_argument("server_url", help="URL for chatbot server to send commands to (e.g. http://localhost)", type=str)
    args = parser.parse_args()

    print("Welcome to the INFO 153B/253B Terminal Chatbot!")
    print(f"Please send a message to your server at url {args.server_url}")
    print("At any time Ctrl-C will exit the application")
    print()

    while True:

        message = input()
        data = make_request_request(args.server_url, message)
        print(f'-->{data.get("message")}')
        print()


if __name__ == "__main__":
    main()
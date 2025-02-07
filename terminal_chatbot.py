import argparse
from urllib.parse import urljoin
import requests

def send_chat(server_url, chat):
    full_url = urljoin(server_url, "/chat")

    chat_request = {"chat": chat } 
    
    try: 
        r = requests.post(full_url, json=chat_request)
        r.raise_for_status()
    except requests.exceptions.ConnectionError as err:
        # eg, no internet
        raise SystemExit(err)
    except requests.exceptions.HTTPError as err:
        # eg, url, server and other errors
        raise SystemExit(err)

    response_json = r.json()

    return response_json

def main():

    parser = argparse.ArgumentParser(prog = 'TerminalChatBot',
        description = 'Terminal Chat Bot that sends request to server specified by the server url',
        epilog = 'Please go to the INFO 253B Website for more information at https://groups.ischool.berkeley.edu/i253/sp25/')
    parser.add_argument("server_url", help="URL for chatbot server to send commands to (e.g. http://localhost)", type=str)
    args = parser.parse_args()

    print("Welcome to the INFO 153B/253B Terminal Chatbot!")
    print(f"Please send a message to your server at url {args.server_url}")
    print("At any time Ctrl-C will exit the application")
    print()

    while True:

        chat = input()
        chat_response = send_chat(args.server_url, chat)
        print(f'-->{chat_response.get("chat")}')
        print()


if __name__ == "__main__":
    main()
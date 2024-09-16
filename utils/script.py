from utils.launcher import launch_multi_accounts, launch
import os

def main():
    session_names = input("Masukkan nama sesi (pisahkan dengan koma): ").split(",")
    query_ids = os.getenv("QUERY_IDS").split(",")

    clients = launch_multi_accounts(session_names, query_ids)
    if clients:
        launch(clients)

if __name__ == "__main__":
    main()
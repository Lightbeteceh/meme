from core.registrator import register_client
from utils.utils import get_config
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def launch_multi_accounts(session_names, query_ids):
    clients = []

    for session_name, query_id in zip(session_names, query_ids):
        try:
            client = register_client(session_name, query_id)
            if client:
                clients.append(client)
        except Exception as e:
            logging.error(f"Gagal mendaftarkan akun dengan query_id '{query_id}': {e}")
            continue

    if not clients:
        logging.error("Tidak ada akun yang valid, silakan coba lagi.")
        return None

    return clients

def launch(clients):
    config = get_config()
    while True:
        for client in clients:
            try:
                energy = client.get_entity("energy")
                if energy < config["MIN_AVAILABLE_ENERGY"]:
                    logging.info(f"Energi rendah, tidur selama {config['SLEEP_BY_MIN_ENERGY'][0]} - {config['SLEEP_BY_MIN_ENERGY'][1]} detik")
                    time.sleep(random.randint(*config["SLEEP_BY_MIN_ENERGY"]))
                    continue

                clicks = random.randint(*config["RANDOM_CLICKS_COUNT"])
                for _ in range(clicks):
                    client.click("tap")
                    time.sleep(random.randint(*config["SLEEP_BETWEEN_TAP"]))

                if config["AUTO_UPGRADE_TAP"]:
                    tap_level = client.get_entity("tap_level")
                    if tap_level < config["MAX_TAP_LEVEL"]:
                        client.upgrade("tap")

                if config["AUTO_UPGRADE_ENERGY"]:
                    energy_level = client.get_entity("energy_level")
                    if energy_level < config["MAX_ENERGY_LEVEL"]:
                        client.upgrade("energy")

                if config["AUTO_UPGRADE_CHARGE"]:
                    charge_level = client.get_entity("charge_level")
                    if charge_level < config["MAX_CHARGE_LEVEL"]:
                        client.upgrade("charge")

                if config["APPLY_DAILY_TURBO"]:
                    client.activate_turbo(config["ADD_TAPS_ON_TURBO"])

                if config["APPLY_DAILY_ENERGY"]:
                    client.activate_daily_energy()

            except Exception as e:
                logging.error(f"Terjadi kesalahan saat menjalankan bot untuk akun dengan query_id '{client.query_id}': {e}")
                if config["EMERGENCY_STOP"]:
                    client.stop()
                    logging.error(f"Bot dihentikan untuk akun dengan query_id '{client.query_id}'")
                continue
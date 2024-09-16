from telethon import TelegramClient, sync
from config.config import get_config
import time
import random

class TelegramClient:
    def __init__(self, session, query_id):
        config = get_config()
        self.query_id = query_id
        self.client = TelegramClient(session, query_id)

        if config["USE_FAKE_USER_AGENT"]:
            self.client.set_user_agent(get_fake_user_agent())
        if config["USE_PROXY_FROM_FILE"] or config["USE_FAKE_IP"]:
            self.rotate_proxy()

        self.client.start()

    def get_entity(self, entity_name):
        if entity_name == "energy":
            return self.client.get_me().energy
        elif entity_name == "tap_level":
            return self.client.get_me().tap_level
        elif entity_name == "energy_level":
            return self.client.get_me().energy_level
        elif entity_name == "charge_level":
            return self.client.get_me().charge_level
        else:
            raise ValueError(f"Entity '{entity_name}' tidak dikenal")

    def upgrade(self, entity_name):
        if entity_name == "tap":
            self.client.upgrade_tap()
        elif entity_name == "energy":
            self.client.upgrade_energy()
        elif entity_name == "charge":
            self.client.upgrade_charge()
        else:
            raise ValueError(f"Entity '{entity_name}' tidak dapat diupgrade")

    def activate_turbo(self, add_taps):
        self.client.activate_turbo(add_taps)

    def activate_daily_energy(self):
        self.client.activate_daily_energy()

    def click(self, entity_name):
        if entity_name == "tap":
            self.client.click_tap()
        else:
            raise ValueError(f"Entity '{entity_name}' tidak dapat diklik")

    def stop(self):
        self.client.disconnect()

    def rotate_proxy(self):
        # Implementasi rotasi proxy jika diperlukan
        pass
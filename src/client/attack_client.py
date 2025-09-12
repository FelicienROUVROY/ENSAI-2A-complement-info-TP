import os
import json
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Using an environment variable defined in the .env file
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        print("GET  " + url + "\n")
        req = requests.get(url)

        attack = None

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()
            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")
            attack_factory = AttackFactory()
            attack = attack_factory.instantiate_attack(type = req["attack_type"], 
            id = req["id"], power = req["power"], name = req["name"], description = req["description"],
            accuracy= req["accuracy"], element = req["element"])
        return attack

    def get_all_attack(self):
        attack_factory = AttackFactory()
        attack_list =[]
        url = f"{self.__HOST}{END_POINT}"
        req = requests.get(url)
        raw_pok = req.json()
        for pok in raw_pok:
            attack_list.append(attack_factory.instantiate_attack(type = pok["attack_type"], 
            id = pok["id"], power = pok["power"], name = pok["name"], description = pok["description"],
            accuracy= pok["accuracy"], element = pok["element"]))
        return attack_list


# Execute Code When the File Runs as a Script
if __name__ == "__main__":
    # To load environment variables contained in the .env file
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)

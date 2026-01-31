import json

import pytest


def pytest_addoption(config):
    parser.addoption("--host", action="store", default="prod")
    # Get the folder where conftest.py is located
    base_dir = os.path.dirname(__file__)
    
    # Build path to endpoints.json relative to conftest.py
    file_path = os.path.join(base_dir, "config", "endpoints.json")



def update_env(config):
    with open(file_path, "r+") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.truncate(0)
        jsonFile.seek(0)
        data['environment']['env'] = config.getoption("--host").lower()
        json.dump(data, jsonFile, indent=4)

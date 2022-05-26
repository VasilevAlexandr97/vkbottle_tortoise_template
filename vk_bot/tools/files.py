from pathlib import PosixPath

import yaml


def load_yaml_file(path: PosixPath) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)

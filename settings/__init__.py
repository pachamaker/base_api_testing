import os
import yaml


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_config():
    with open(os.path.join(os.path.dirname(__file__), "environments.yaml"), 'r') as stream:
        config = yaml.load(stream)

    if ENV not in config:
        raise EnvironmentError('ENV variable not found')

    return config[ENV]


ENV = os.environ.get('ENV', 'test')

config = load_config()

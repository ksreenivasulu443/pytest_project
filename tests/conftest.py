import pytest
import pandas as pd
import os
import yaml

@pytest.fixture(scope="module")
def read_config(request):
    dir_path = request.node.fspath.dirname
    print("dir path" , dir_path)
    config_path = os.path.join(dir_path, "config.yml")
    print("config path" , config_path)

    with open(config_path, "r") as f:
        config_data = yaml.safe_load(f)

    print("config data" , config_data)
    return config_data



@pytest.fixture(scope="module")
def read_data(read_config):
    config_data = read_config
    source_path = config_data["source"]["path"]
    print("source path" , source_path)
    target_path = config_data["target"]["path"]
    print("target path" , target_path)
    primary_key = config_data["validation_config"]["primary_columns"]
    print("primary key" , primary_key)
    source = pd.read_csv(source_path)
    target = pd.read_csv(target_path)

    return source, target
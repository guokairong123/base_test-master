import pytest
import yaml


class TestYaml:
    #@pytest.mark.parametrize(yaml.safe_load(open('./add.yaml', encoding='utf-8')))
    def test_yaml(self):
        print(yaml.safe_load(open('./delete.yaml', encoding='utf-8')))

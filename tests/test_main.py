"""
Implement tests here (and in other files, one for every python module you want to test).
"""
import json


def test_main():
    with open('out/leisure.json') as f:
        data = json.load(f)
        for leisure in data['elements']:
            print(leisure['type'])
    assert True

import os, sys
import json


def get_new_json(filepath, key, value):
    key_ = key.split(".")
    key_length = len(key_)
    with open(filepath, 'rb') as f:
        json_data = json.load(f)
        i = 0
        a = json_data
        while i < key_length:
            if i + 1 == key_length:
                a[key_[i]] = value
                i = i + 1
            else:
                a = a[key_[i]]
                i = i + 1
    f.close()
    return json_data


def rewrite_json_file(filepath, json_data):
    with open(filepath, 'w') as f:
        json.dump(json_data, f)
    f.close()


if __name__ == '__main__':
    # key = sys.argv[1]
    # value = int(sys.argv[2])
    # json_path = sys.argv[3]

    m_json_data = get_new_json("../../date/header.json", "token", "212")
    rewrite_json_file("../../date/header.json", m_json_data)
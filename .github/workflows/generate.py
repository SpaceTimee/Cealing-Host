#!/usr/bin/python
import json
import toml


def convert_json_to_toml(json_file_path, toml_file_path):
    # 读取JSON文件
    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 初始化TOML数据结构
    toml_data = {"alter_hostname": {}, "hosts": {}}

    # 处理每个条目
    for entry in data:
        domains, alter_host, ip = entry

        # 处理alter_hostname部分
        for domain in domains:
            toml_data["alter_hostname"][domain] = alter_host

        # 处理hosts部分
        for domain in domains:
            toml_data["hosts"][domain] = ip

    # 写入TOML文件
    with open(toml_file_path, "w", encoding="utf-8") as f:
        toml.dump(toml_data, f)


# 使用示例
if __name__ == "__main__":
    for filename_base in [
        "Cealing-Host-R",
        "Cealing-Host",
    ]:
        convert_json_to_toml(filename_base + ".json", filename_base + ".toml")

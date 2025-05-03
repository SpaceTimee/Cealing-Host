import json
import toml
from collections import defaultdict


def convert_host_to_toml(host_path, toml_path):
    with open(host_path) as host_file:
        host_rules = json.load(host_file)

    toml_rules = defaultdict(dict)

    for host_rule in host_rules:
        domains, sni, ip = host_rule

        for domain in domains:
            toml_rules["alter_hostname"][domain] = sni
            toml_rules["hosts"][domain] = ip

    with open(toml_path, "w") as toml_file:
        toml.dump(toml_rules, toml_file)


if __name__ == "__main__":
    convert_host_to_toml("Cealing-Host.json", "Cealing-Host.toml")

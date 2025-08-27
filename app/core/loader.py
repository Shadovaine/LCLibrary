from pathlib import Path
import yaml

def load_all(root: str = "data/commands"):
    """
    Load all YAML files from the given directory into a dict.
    Keys = command names, Values = full YAML data
    """

    out = {}
    for p in Path(root).rglob("*.yml"):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        out[d["name"]] = d
    return out
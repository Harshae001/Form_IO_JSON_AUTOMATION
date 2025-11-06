import yaml
import json
from schema_utils import build_component
from yaml_input import config_yaml


def build_table(section):
    """Build a Form.io table layout from rows."""
    rows = section["rows"]
    table = {
        "label": section.get("name", "Table"),
        "key": section.get("key", "table"),
        "type": "table",
        "input": True,
        "numRows": len(rows),
        "numCols": max(len(r) for r in rows),
        "hideLabel": True,
        "bordered": True,
        "rows": [],
    }

    for row in rows:
        row_cells = []
        for field in row:
            component = build_component(field)
            row_cells.append({"components": [component]})
        table["rows"].append(row_cells)

    return table


def build_datagrid(section):
    """Build a Form.io datagrid layout."""
    grid = {
        "label": section["name"],
        "key": section["key"],
        "type": "datagrid",
        "input": True,
        "customClass": section.get("customClass", ""),
        "components": [],
    }

    for field in section["fields"]:
        grid["components"].append(build_component(field))

    return grid


def build_form(config):
    """Main entry: compose a Form.io form from a list of sections."""
    components = []
    for section in config["sections"]:
        stype = section["type"]
        if stype == "table":
            components.append(build_table(section))
        elif stype == "datagrid":
            components.append(build_datagrid(section))
        else:
            print(f"⚠️ Unknown section type: {stype}")
    return components


# --- Run and print JSON ---
if __name__ == "__main__":
    config = yaml.safe_load(config_yaml)
    json_output = build_form(config)
    print(json.dumps(json_output, indent=2))
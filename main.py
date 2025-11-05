import yaml
import json
from schema_utils import build_component
from yaml_input import config_yaml

# --- Utility functions ---
def build_table(rows):
    """Compose a Form.io customTable structure from row/field definitions."""
    table = {
        "label": "table",
        "key": "table",
        "type": "table",
        "input": True,
        "numRows": len(rows),
        "numCols": max(len(rows[i]) for i in range(len(rows))),
        "hideLabel": True,
        "bordered": True,
        "rows": []
    }

    for row in rows:
        row_cells = []
        for field in row:
            component = build_component(field)
            row_cells.append({"components": [component]})
        table["rows"].append(row_cells)

    return table


# --- Example usage ---
if __name__ == "__main__":

    config = yaml.safe_load(config_yaml)
    table_schema = build_table(config["rows"])
    print(json.dumps(table_schema, indent=2))

import yaml
import json
from schema_utils import build_component
from yaml_input import config_yaml


# def build_table(section):
#     """Build a Form.io table layout from rows."""
#     rows = section["rows"]
#     table = {
#         "label": section.get("label", "Table"),
#         "key": section.get("key", "table"),
#         "type": "table",
#         "input": True,
#         "numRows": len(rows),
#         "numCols": max(len(r) for r in rows),
#         "hideLabel": True,
#         "bordered": True,
#         "rows": [],
#     }
#
#     for row in rows:
#         row_cells = []
#         for field in row:
#             component = build_component(field)
#             row_cells.append({"components": [component]})
#         table["rows"].append(row_cells)
#
#     return table
def build_table(section):
    """Recursively build a Form.io table."""
    rows = section["rows"]
    table = {
        "label": section.get("label", "Table"),
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
        for cell in row:
            # Handle nested section like {'section1': [ {...}, {...} ]}
            if isinstance(cell, dict) and len(cell) == 1 and isinstance(list(cell.values())[0], list):
                nested_key = list(cell.keys())[0]
                nested_sections = cell[nested_key]
                cell_components = []
                for nested_section in nested_sections:
                    if not isinstance(nested_section, dict):
                        print(f"⚠️ Skipping unexpected value: {nested_section}")
                        continue
                    stype = nested_section.get("type")
                    if stype == "table":
                        cell_components.append(build_table(nested_section))
                    elif stype == "datagrid":
                        cell_components.append(build_datagrid(nested_section))
                    else:
                        cell_components.append(build_component(nested_section))
                row_cells.append({"components": cell_components})

            # Simple field like {label: "...", type: "..."}
            elif isinstance(cell, dict):
                component = build_component(cell)
                row_cells.append({"components": [component]})

            else:
                print(f"⚠️ Unexpected cell type in row: {cell}")

        table["rows"].append(row_cells)

    return table


def build_datagrid(section):
    """Build a Form.io datagrid layout."""
    grid = {
        "label": section["label"],
        "key": section["key"],
        "type": "datagrid",
        "hideLabel": True,
        "input": True,
        "customClass": section.get("customClass", ""),
        "components": [],
    }

    for field in section["fields"]:
        grid["components"].append(build_component(field))

    return grid


# def build_form(config):
#     """Main entry: compose a Form.io form from a list of sections."""
#     components = []
#     for section in config["sections"]:
#         stype = section["type"]
#         if stype == "table":
#             components.append(build_table(section))
#         elif stype == "datagrid":
#             components.append(build_datagrid(section))
#         elif stype in ["textfield", "number", "email", "time", "dateTimePicker", "select", "textarea", "DigitalSignature", "htmlelement"]:
#             components.append(build_component(section))
#         else:
#             print(f"⚠️ Unknown section type: {stype}")
#     return components
def build_form(config):
    components = []
    for section in config.get("sections", []) + config.get("primary_section", []):
        stype = section["type"]
        if stype == "table":
            components.append(build_table(section))
        elif stype == "datagrid":
            components.append(build_datagrid(section))
        else:
            components.append(build_component(section))
    return components


# --- Run and print JSON ---
if __name__ == "__main__":
    config = yaml.safe_load(config_yaml)
    json_output = build_form(config)
    print(json.dumps(json_output, indent=2))
    print("✅ Form.io JSON generated successfully in the branch_102")
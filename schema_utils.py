def build_component(field):
    """Generate a Form.io component dict from a simple field spec."""
    base = {
        "label": field.get("label", field.get("name", "Unnamed Field")),
        "key": field.get("key", field["label"].lower().replace(" ", "_")),
        "type": field["type"],
        "customClass": field.get("customClass","w-250px font-weight-bold fs-1"),
        "hideLabel": field.get("hideLabel", False),
        "hidden": field.get("hidden", False),
        "input": True,
    }

    if field["type"] == "textfield":
        base.update({
            # "placeholder": field.get("placeholder", "Enter text"),
            "defaultValue": field.get("defaultValue", "")
        })

    elif field["type"] == "htmlelement" and field["key"]=="form_title":
        base.update({
            # "tag": field.get("tag", "div"),
            "customConditional": "const element = instance.element; const tableElement = element.closest(\"td\"); tableElement.style.backgroundColor = '#EB5D07';",
            "content": "<center><b style=\"color:white;\">Logbook Name</b></center>",
            "tag": "h4",
        })

    elif field["type"] == "htmlelement":
        base.update({
            "content": field.get("label", "<div>HTML Element</div>"),
        })

    elif field["type"] == "dateTimePicker":
        key = field.get("key", field["label"].lower().replace(" ", "_"))
        base.update({

            "calculateValue": f"""function epochToFormattedDate(epoch) {{
      let date = new Date(epoch);
      let year = date.getFullYear();
      let month = ('0' + (date.getMonth() + 1)).slice(-2);
      let day = ('0' + date.getDate()).slice(-2);
      return `${{year}}-${{month}}-${{day}}`;
    }}

    let date_data = data.{key};
    if (date_data) {{
      value = epochToFormattedDate(date_data);
    }}""",
            "customOptions": {
                "disableWeekends": field.get("disableWeekends", False),
                "disableWeekdays": field.get("disableWeekdays", False),
                "disablePast": field.get("disablePast", False),
                "enableTime": field.get("enableTime", False),
                "format": field.get("format", "dd-MM-yyyy"),
                "disableFuture": field.get("disableFuture", False)
            }
        })

    elif field["type"] == "number":
        base.update({
            "requireDecimal":field.get("requireDecimal", False),
            "decimalLimit":field.get("decimalLimit", 2),
        })


    elif field["type"] == "select":
        base.update({
            "data": {"values": [{"label": "Add values", "value": "Add values"}]},
            "dataSrc": "values",
            "placeholder":"Select",
            "widget": "html5"
        })

    elif field["type"] == "DigitalSignature":
        base.update({
            "hideLabel": field.get("hideLabel", False)
        })

    return base
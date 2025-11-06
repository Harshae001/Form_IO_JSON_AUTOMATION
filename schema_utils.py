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

    if field["type"] == "htmlelement":
        base.update({
            # "tag": field.get("tag", "div"),
            "content": field.get("content", "html"),
        })
    # Add type-specific defaults
    # if field["type"] in ["textfield", "number", "email", "time", "dateTimePicker"]:
    #     base["validate"] = {"required": field.get("required", False)}
    if field["type"] == "dateTimePicker":
        key = field.get("key", field["label"].lower().replace(" ", "_"))
        base.update({
            "format": field.get("format", "yyyy-MM-dd HH:mm:ss"),
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
                "disableFuture": field.get("disableFuture", False),
                "format": field.get("format","dd-MM-yyyy")
            }
        })

    if field["type"] == "number":
        base.update({
            "requireDecimal":field.get("requireDecimal", False),
            "decimalLimit":field.get("decimalLimit", 2),
        })


    if field["type"] == "select":
        base.update({
            "data": {"values": [{"label": "Option 1", "value": "option1"}]},
            "dataSrc": "values",
            "placeholder":"Select",
            "widget": "html5"
        })

    return base
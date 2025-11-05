config_yaml = """
rows:
  - [ {label: "Date of Audit", key: "date", type: "dateTimePicker"},
      {label: "Date of Production", key: "production_on", type: "dateTimePicker"},
      {label: "Time", key: "time", type: "time"}]

  - [ {label: "TPD", key: "tpd", type: "select"},
      {label: "M/c No.", key: "m_c_no", type: "select"},
      {label: "Type of Audit", key: "type_of_audit", type: "select"},
      {label: "Shift", key: "shift", type: "select"}  ]

  - [ {label: "Qty Per Box", key: "qty_per_box", type: "number"},
      {label: "No of Boxes", key: "no_of_boxes", type: "number"},
      {label: "Lot Size", key: "lot_size", type: "number"} ]
"""
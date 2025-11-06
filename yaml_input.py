config_yaml = """
sections:
  - name: "Main Table"
    type: "table"
    rows:
      - 
        - { label: "Audit Date", type: "dateTimePicker", key: "audit_date", validate: { required: true } }
        - { label: "Inspector", type: "textfield", key: "inspector" }
      - 
        - { label: "Department", type: "select", key: "department" }
        - { label: "Location", type: "textfield", key: "location" }

  - name: "Drawing Issue Verification Record"
    type: "datagrid"
    key: "drawing_issue_verification_record"
    customClass: "sticky-table-header height-420 stick-table-column-header"
    fields:
      - { label: "Job Change Date", key: "date", type: "dateTimePicker", format: "dd-MM-yyyy" }
      - { label: "Time", key: "time", type: "time" }
      - { label: "FG Code", key: "fg_code", type: "textfield" }
      - { label: "Job Name", key: "job_name", type: "select", dataSrc: "custom" }
      - { label: "Glass Type", key: "glass_type", type: "select" }
      - { label: "SAP Rev", key: "sap_rev", type: "textfield" }
      - { label: "QA Rev", key: "qc_rev", type: "textfield" }
      - { label: "Remarks", key: "remarks", type: "textarea" }
      - { label: "Verified By", key: "verified_by", type: "DigitalSignature" }

"""
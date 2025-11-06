config_yaml = """
sections:
  - label: "Main Table"
    type: "table"
    key: "main_table"
    rows:
      - 
        - { label: "Audit Date", type: "dateTimePicker", key: "audit_date"}
        - { label: "Inspector", type: "textfield", key: "inspector" }
      - 
        - { label: "Department", type: "select", key: "department" }
        - { label: "Location", type: "textfield", key: "location" }
        - { label: "Shift", type: "htmlelement", key: "html1" }

  - label: "Drawing Issue Verification Record"
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
      
  - label: "Step Name"
    type: "textfield"
    key: "step_name"
    hidden: true
    customClass: "font-weight-bold fs-1"
    clearOnHide: false
    
  - label: "Remarks"
    type: "textarea"
    key: "overall_remarks"
    customClass: "font-weight-bold fs-1"

"""
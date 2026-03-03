config_yaml = """
primary_section:
  - label: "Primary Table"
    type: "table"
    key: "primary_table"
    rows:
          -
            - section0:
                - label: "Logbook Step 1"
                  type: "htmlelement"
                  key: "form_title"
                  customClass: "font-weight-bold fs-1"
                  clearOnHide: false
          -
            - section1:
                - label: "Main Table"
                  type: "table"
                  key: "main_table"
                  rows:
                    -
                      - { label: "Date", type: "dateTimePicker", key: "date" }
                      - { label: "Inspector", type: "textfield", key: "inspector" }
                      - { label: "TPD", type: "select", key: "tpd" }
                    -
                      - { label: "Department", type: "select", key: "department" }
                      - { label: "Location", type: "textfield", key: "location" }
                      - { label: "Shift", type: "textfield", key: "shift" }
    
                - label: "Drawing Issue Verification Record"
                  type: "datagrid"
                  key: "drawing_issue_verification_record"
                  customClass: "sticky-table-header height-420 stick-table-column-header"
                  fields:
                    - { label: "Job Change Date", key: "job_change_date", type: "dateTimePicker", format: "dd-MM-yyyy" }
                    - { label: "Time", key: "time", type: "time" }
                    - { label: "FG Code", key: "fg_code", type: "textfield" }
                    - { label: "Job Name", key: "job_name", type: "select", dataSrc: "custom" }
                    - { label: "Glass Type", key: "glass_type", type: "select" }
                    - { label: "SAP Rev", key: "sap_rev", type: "textfield" }
                    - { label: "QA Rev", key: "qc_rev", type: "textfield" }
                    - { label: "Remarks", key: "remarks", type: "textarea" }
                    - { label: "Verified By", key: "verified_by", type: "DigitalSignature" }
    
                - label: "Remarks"
                  type: "textarea"
                  key: "overall_remarks"
                  customClass: "font-weight-bold fs-1"
    
                - label: "E-sign Table"
                  type: "table"
                  key: "e_sign_table"
                  customClass: "font-weight-bold fs-1"
                  rows:
                    -
                      - { label: "Analysed By", type: "htmlelement", key: "html2" }
                      - { label: "Analysed By", type: "DigitalSignature", key: "analysed_by", hideLabel: true }
                      - { label: "Approved By", type: "htmlelement", key: "html3" }
                      - { label: "Approved By", type: "DigitalSignature", key: "approved_by", hideLabel: true }
    
    
                - label: "Step Name"
                  type: "textfield"
                  key: "step_name"
                  hidden: true
                  customClass: "font-weight-bold fs-1"
                  clearOnHide: false
                  defaultValue: "Step Name"

"""
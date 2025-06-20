{
  "name": "dlt_customer_vault_pipeline",
  "storage": "/mnt/data/dlt-pipelines/customer_vault",
  "target": "vault_db",
  "photon": "true",
  "continuous": "flase",
  "libraries": [
    {"notebook": {"path": "/Workspace/Repos/kanthikumar.thota@gmail.com/data-vault-customer360/dlt_pipeline/00_config.py"}},
    {"notebook": {"path": "/Workspace/Repos/kanthikumar.thota@gmail.com/data-vault-customer360/dlt_pipeline/01_hub_customer.py"}},
    {"notebook": {"path": "/Workspace/Repos/kanthikumar.thota@gmail.com/data-vault-customer360/dlt_pipeline/02_sat_customer_details.py"}}
  ]
}

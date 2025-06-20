-- This file defines a sample transformation.
-- Edit the sample below or add new transformations
-- using "+ Add" in the file browser.

CREATE MATERIALIZED VIEW `sample_trips_pipeline_config_json` AS
SELECT
    pickup_zip,
    fare_amount
FROM samples.nyctaxi.trips

-- this will require a check of the data to ensure that the new postcodes fields are populated before NOT NULL constraints are set
BEGIN;
ALTER TABLE patients_patient ADD postcode integer;
ALTER TABLE patients_patient ADD next_of_kin_postcode integer;
COMMIT;

ALTER TABLE patients_patient ALTER COLUMN postcode SET NOT NULL;
ALTER TABLE patients_patient ALTER COLUMN next_of_kin_postcode SET NOT NULL;

BEGIN;
ALTER TABLE patients_patient ADD active boolean DEFAULT TRUE NOT NULL;
COMMIT;

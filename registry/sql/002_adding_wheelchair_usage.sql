BEGIN;
ALTER TABLE dmd_motorfunction ADD wheelchair_usage_age integer;
ALTER TABLE dmd_motorfunction ADD wheelchair_use varchar(12);
COMMIT;

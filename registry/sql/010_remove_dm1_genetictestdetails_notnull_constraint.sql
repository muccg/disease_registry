BEGIN;

ALTER TABLE dev_dm1_registry.public.dm1_genetictestdetails ALTER COLUMN test_date DROP NOT NULL;

COMMIT;


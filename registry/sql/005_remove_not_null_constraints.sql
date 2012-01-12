-- apply this to dmd
ALTER TABLE dmd_heart ALTER COLUMN lvef DROP NOT NULL;
ALTER TABLE dmd_heart ALTER COLUMN lvef_date DROP NOT NULL;
ALTER TABLE dmd_respiratory ALTER COLUMN fvc DROP NOT NULL;
ALTER TABLE dmd_respiratory ALTER COLUMN fvc_date DROP NOT NULL;

-- sma
ALTER TABLE sma_respiratory ALTER COLUMN lvef DROP NOT NULL;
ALTER TABLE sma_respiratory ALTER COLUMN lvef_date DROP NOT NULL;

-- and dm1
ALTER TABLE dm1_heart ALTER COLUMN echocardiogram_lvef DROP NOT NULL;
ALTER TABLE dm1_heart ALTER COLUMN echocardiogram_lvef_date DROP NOT NULL;
ALTER TABLE dm1_respiratory ALTER COLUMN fvc DROP NOT NULL;
ALTER TABLE dm1_respiratory ALTER COLUMN fvc_date DROP NOT NULL;



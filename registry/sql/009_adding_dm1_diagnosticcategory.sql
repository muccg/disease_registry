BEGIN;

CREATE TABLE "dm1_diagnosticcategory" (
    "molecular_data_id" integer NOT NULL PRIMARY KEY REFERENCES "genetic_moleculardata" ("patient_id") DEFERRABLE INITIALLY DEFERRED,
    "category" varchar(50) NOT NULL,
    "repeat_size" integer,
    "relative_test" boolean NOT NULL,
    "relative_ctg_repeat" integer,
    "relative_cctg_repeat" integer
);

COMMIT;

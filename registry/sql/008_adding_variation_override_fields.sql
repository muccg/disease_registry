BEGIN;

-- Add the base validation override fields.
ALTER TABLE genetic_variation ADD exon_validation_override BOOLEAN NOT NULL DEFAULT 'f';
ALTER TABLE genetic_variation ADD dna_variation_validation_override BOOLEAN NOT NULL DEFAULT 'f';
ALTER TABLE genetic_variation ADD rna_variation_validation_override BOOLEAN NOT NULL DEFAULT 'f';
ALTER TABLE genetic_variation ADD protein_variation_validation_override BOOLEAN NOT NULL DEFAULT 'f';

-- Add the appropriate permission to the auth table.
INSERT INTO auth_permission
    (name, content_type_id, codename)
    SELECT 'Can override variation validation' AS name,
        id AS content_type_id,
        'can_override_validation' AS codename
    FROM django_content_type
    WHERE app_label = 'genetic' AND model = 'variation';

COMMIT;

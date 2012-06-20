BEGIN;
ALTER TABLE genetic_variation ADD exon_boundaries_known boolean;
ALTER TABLE genetic_variation ADD point_mutation_all_exons_sequenced boolean;
ALTER TABLE genetic_variation ADD duplication_all_exons_tested boolean;
ALTER TABLE genetic_variation ADD deletion_all_exons_tested boolean;
ALTER TABLE genetic_variation ADD all_exons_in_male_relative boolean;
COMMIT;
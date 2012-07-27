# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        # This is a once-off migration to be run on the live postgres instance of the dmd registry.
        # This has come about because the 'symbol' field from the genetic model was a primary key, 
        # but it is a TextField - postgres doesn't mind, but mysql doesn't like this. This schema
        # was already live on our postgres DB when we realised we needed to make the change, and 
        # rather than try to deal with it then, we created migrations and models in dev as if 
        # 'symbol' had never been a PK (using a standard django id instead). But the live database still
        # needs to be dealt with, because we cannot deploy new versions of the site until the schema
        # matches.
        # What we need to do is the following
        # 1. Add an 'id' field to the Gene table (named correctly so it matches how django names id fields)
        # 2. programmatically number each existing Gene record. Order is probably unimportant.
        # 3. create a database sequence for further id's to be created, 'resuming' from one after the 
        #    last ID used in step 2. This should be named/set up in the way that django would have set it up.
        # 4. Build a Gene/Variation mapping, so that you know which variations link to which genes, 
        #    because you are about to tear down the relationship between them, and you need a way to remember 
        #    which variations and genes were linked. I would not use database objects in this mapping - 
        #    they'll end up being a problem because we are changing them. I'd just make a mapping 
        #    (dictionary I guess) which maps gene symbols  (the primary key of Gene) to variation ids 
        #    (the primary key of Variation).
        # 5. Drop the foreign key "variation.gene"
        # 6. Drop the primary key constraint on Gene.symbol, and make the id the primary key instead 
        #    of symbol.
        # 7. Recreate the foreign key "variation.gene", but now it will point to Gene.id instead of 
        #    Gene.symbol
        # 8. Go through your Gene.symbol to variation.id mapping, looking each pair up and setting the 
        #    variation.gene foreign key to the value of gene.id.
        #
        # There's really no backwards migration for this.
        
        # Step 1:
        # Add the id column
        db.add_column('genetic_gene', 'id', django.models.IntegerField)
        id_counter = 0

        # Step 2:
        # populate the id field by just enumerating the records
        gene_recordset = orm.genetic.gene.objects.all()
        for record in gene_recordset:
            try:
                record.id = id_counter
                record.save()
                id_counter += 1
            except Exception, e:
                print 'could not set id %d on record %s' % (id_counter, record.symbol)

        # Step 3:
        # create a sequence to continue numbering these ids
        # for an id like this it would be 'genetic_gene_id_seq'

        db.execute("CREATE SEQUENCE genetic_gene_id_seq INCREMENT BY 1 START %d;" % (id_counter))
        
        
        # Step 4: Build a gene/variation mapping
        variationmap = {}
        variations = orm.genetic.variation.objects.all()
        for variation in variations:
            linked_gene = variation.gene
            if linked_gene is not None:
                variationmap[variation.id] = linked_gene.id

        print 'Built %d variations' % (len(variationmap.keys())
        
        
        # Step 5:
        # Drop FK constraint variation.gene

        db.delete_foreign_key('genetic.variation', 'gene')

        # Step 6:
        # Drop PK on Gene.symbol

        db.delete_primary_key('genetic.gene', 'symbol')
        db.create_primary_key('genetic.gene', 'id')
        #Need something here to make next value come from seq?
        db.execute('ALTER_TABLE genetic_gene ALTER COLUMN id SET DEFAULT nextval(\'genetic_gene_id_seq\':regclass);')
        #Need to create index?
        db.create_index('genetic_gene', 'id')

        # Step 7:
        # Recreate FK

        db.create_foreign_key('genetic_variation', 'gene', ???)

        # Step 8:
        # Remap

        for variationid in variationmap.keys():
            targetgene = orm.genetic.gene.objects.get(symbol=variationmap[variationid])
            if targetgene is not None:
                variation = orm.genetic.variation.objects.get(id=variationid)
                if variation is not None:
                    variation.gene = targetgene
                else:
                    print 'Unable to find variation %d. This should not happen' % (variationid)
                    
            else:
                print 'Unable to find target gene for variation %d. This should not happen' % (variationid)
         

    def backwards(self, orm):
        "Write your backwards methods here."


models = {
        'genetic.gene': {
            'Meta': {'ordering': "['symbol']", 'object_name': 'Gene'},
            'accession_numbers': ('django.db.models.fields.TextField', [], {}),
            'chromosome': ('django.db.models.fields.TextField', [], {}),
            'hgnc_id': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'refseq_id': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'symbol': ('django.db.models.fields.TextField', [], {'primary_key': 'True'})
        },
        'genetic.moleculardata': {
            'Meta': {'ordering': "['patient']", 'object_name': 'MolecularData'},
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['patients.Patient']", 'unique': 'True', 'primary_key': 'True'})
        },
        'genetic.variation': {
            'Meta': {'object_name': 'Variation'},
            'all_exons_in_male_relative': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deletion_all_exons_tested': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'dna_variation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dna_variation_validation_override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duplication_all_exons_tested': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'exon': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exon_boundaries_known': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'exon_validation_override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gene': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genetic.Gene']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'molecular_data': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genetic.MolecularData']"}),
            'point_mutation_all_exons_sequenced': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'protein_variation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'protein_variation_validation_override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rna_variation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rna_variation_validation_override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'technique': ('django.db.models.fields.TextField', [], {})
        },
        'groups.workinggroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorkingGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'patients.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'patients.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surgery_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Doctor']", 'through': "orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'next_of_kin_set'", 'to': "orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.WorkingGroup']"})
        },
        'patients.patientdoctor': {
            'Meta': {'object_name': 'PatientDoctor'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['genetic']

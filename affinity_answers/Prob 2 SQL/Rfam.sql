/*types of tigers can be found in the taxonomy table*/
SELECT COUNT(distinct species) AS num_species FROM taxonomy;


/*the "ncbi_id" of the Sumatran Tiger*/
SELECT ncbi_id FROM taxonomy WHERE species LIKE '%Panthera tigris sumatrae%';


/*columns that can be used to connect the tables in the given database*/
SELECT column_name, table_name FROM information_schema.columns
WHERE table_name IN ('taxonomy','rfamseq','family','clan_membership', 'clan', 'full_region')
ORDER BY table_name, column_name;


/*type of rice has the longest DNA sequence*/
SELECT taxonomy.species as rice_type, MAX(rfamseq.length) AS max_sequence_length
FROM taxonomy
JOIN rfamseq ON taxonomy.ncbi_id = rfamseq.ncbi_id
WHERE taxonomy.species LIKE '%rice%'
GROUP BY taxonomy.species
ORDER BY max_sequence_length desc
LIMIT 1;
 
/* families that have DNA sequence lengths greater than 1,000,000*/
SELECT rfamseq.length as max_sequence_length, family.description AS family_name
FROM family
JOIN rfamseq ON family.rfam_acc = rfamseq.rfamseq_acc
GROUP BY family.rfam_acc, family.description
HAVING max_sequence_length > 1000000
ORDER BY max_sequence_length DESC
LIMIT 15 OFFSET 120;


airport = LOAD '/airport.txt' USING PigStorage(',') as (airport_name:chararray, city_name:chararray, country_name:chararray, code:chararray);

air_count = LOAD '/airport_data_from_mapreducex.txt' USING PigStorage(',') as (code_1:chararray, count:chararray);

result = JOIN air_count BY code_1, airport BY code;

STORE result INTO 'output' USING PigStorage(',');



airport = LOAD '/airport.txt' USING PigStorage(',') as (airport_name:chararray, city_name:chararray, country_name:chararray, code:chararray);

source = LOAD '/source.txt' USING PigStorage(',') as (code_1:chararray, date:chararray, lat:chararray, lon:chararray);

result = JOIN source BY code_1, airport BY code;

STORE result INTO 'output' USING PigStorage(',');

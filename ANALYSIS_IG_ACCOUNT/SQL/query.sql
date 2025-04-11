--Para importar los datos desde psql:
-- \copy CT_SOLO_FINAL_LISTO FROM 'path' WITH (FORMAT CSV, DELIMITER ',', HEADER, ENCODING 'UTF-8'); 

DROP TABLE IF EXISTS ct_solo_final_listo;
DROP TABLE IF EXISTS ct_clasificacion;
DROP TABLE IF EXISTS ct_hashtags;

CREATE TABLE CT_SOLO_FINAL_LISTO (
commentsCount INT, 
likesCount INT, 
tipo VARCHAR, 
hasMusic BOOLEAN, 
num_hashtags INT, 
num_images INT, 
dia_semana VARCHAR,
mes VARCHAR,
YEAR INT,
fecha DATE,
hora TIME,
id INT, 
franja_horaria VARCHAR
);

CREATE TABLE CT_CLASIFICACION (
id INT, tipo_de_publicacion VARCHAR, tipo_de_producto VARCHAR
);

CREATE TABLE CT_HASHTAGS (
hashtag VARCHAR,  count_uso INT, mean NUMERIC, maximo INT
);

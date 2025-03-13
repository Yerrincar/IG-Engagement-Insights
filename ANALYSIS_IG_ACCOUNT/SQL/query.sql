CREATE TABLE CT_SOLO_FINAL_LISTO (
commentsCount INT, likesCount INT, tipo VARCHAR, hasMusic BOOLEAN, num_hashtags INT, num_images INT, dia_semana VARCHAR, hora TIME, id INT, franja_horaria VARCHAR
);

CREATE TABLE CT_CLASIFICACION (
id INT, tipo_de_publicacion VARCHAR, tipo_de_producto VARCHAR
);

CREATE TABLE CT_HASHTAGS (
hashtag VARCHAR, num_veces INT, mean FLOAT, maximo INT
);

DROP TABLE IF EXISTS ct_datos_final;

CREATE TABLE ct_datos_final AS SELECT 
	 f.commentsCount,
    f.likesCount,
    f.tipo,
    f.hasMusic,
    f.num_hashtags,
    f.num_images,
    f.dia_semana,
    f.hora,
    f.mes,
    f.year,
    f.fecha,
    f.id,
    f.franja_horaria,
    c.tipo_de_publicacion,
    c.tipo_de_producto
FROM CT_SOLO_FINAL_LISTO f
LEFT JOIN CT_CLASIFICACION c
  ON f.id = c.id
  ORDER BY f.id;
  

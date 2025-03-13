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
    f.id,
    f.franja_horaria,
    c.tipo_de_publicacion,
    c.tipo_de_producto
FROM CT_SOLO_FINAL_LISTO f
LEFT JOIN CT_CLASIFICACION c
  ON f.id = c.id
  ORDER BY f.id;

--Actualizamos un valor faltante que no se había importado correctamente
UPDATE ct_datos_final  SET tipo_de_publicacion='promocion', tipo_de_producto='marcapaginas' WHERE ct_datos_final.id=7;

--Arreglamos tíldes truncadas
UPDATE ct_datos_final SET dia_semana = CONVERT_FROM(CONVERT_TO(dia_semana, 'latin1'), 'utf8') WHERE dia_semana LIKE '%Ã%';
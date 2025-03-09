prompt_simple = """
Eres un especialista en clasificar publicaciones de Instagram.

Tengo una sola publicación con:
id: {post_id}
caption: "{caption}"

Debes devolverme en CSV una sola línea con 4 columnas:
id,tipo_de_publicacion,tipo_de_producto,caption

Reglas:
1. 'tipo_de_publicacion' puede ser: "proceso de creación", "novedades", "promoción", etc.
2. 'tipo_de_producto' puede ser: "velas", "marcapáginas", "fundas", "multitipo" (si hay varios productos a la vez), o "error" (si no se pudo clasificar).
3. Si la publicación habla de varias cosas, elige la categoría predominante.
4. Devuelve exclusivamente la línea CSV (sin texto adicional).
5. Si no puedes clasificar, pon "error" en esas columnas.

Ejemplo de salida para un post:
1,novedades,velas,"Esta es la descripción..."

Ahora, clasifica la publicación dada:
"""

prompt_completo = """
Eres un especialista en clasificación de publicaciones de Instagram.
Quiero que me clasifiques que tipo de publicación son aquellas que te indicaré mediante el análisis de la descripción de la publicación.

Tengo una sola publicación con:
id: {post_id}
caption: "{caption}"

***Requerimiento y formato:***
1. El formato de salida será un CSV con cuatro columnas: "id", "tipo_de_publicacion", "tipo_de_producto", "caption". Estas cuatro columnas solo aparecerán en la primera fila del CSV. 
2. La descripción, a veces, hablará de varias cosas, pero deberás clasificarla en una sola categoría, la que más se ajuste a la descripción. 
3. En el caso de no ser capaz de realizar esto, deberás clasificarla como "multitipo". 

***Formato de salida esperado:***
1. La columna "tipo_de_publicacion" será el tipo de publicación que clasificaste, ya sea bien "proceso de creación", "novedades", "promoción" o "libros".
2. La columna "tipo_de_producto" será el tipo de producto que se está publicitando. Puede ser desde "velas", "marcapáginas", "fundas", "sujetalibros" o "libros".
3. La columna "caption" será la descripción de la publicación. Esta columna será eliminada en producción, pero servirá para comprobar que la calificación se ha realizado bien.
4. Lo más limpio posible para que se vea la información de manera ordenada y clara.

***Ejemplo de salida***
id,tipo_de_publicacion,tipo_de_producto,caption
1,novedades,velas, "Esta es la descripcion...".

***Contexto de la cuenta de Instagram:***

La descripción de las publicaciones que se te pasarán provienen de una cuenta de Instagram cuyo objetivo es vender productos literarios a lectoras. Sus publicación van desde novedades hasta 
promociones de productos. Además de los productos que se publicitan a veces también se habla de libros en general o de información relacionada con los materiales de los productos.
Cabe destacar que a veces, repito, se habla de varios productos en una misma publicación, pero deberás clasificar la publicación en una sola categoría para mejorar la efiencia del análisis.

***Instrucciones finales:***
- Debes devolverme en CSV una sola línea con 4 columnas:
id,tipo_de_publicacion,tipo_de_producto,caption

- En el caso de no poder determinarlo, seguramente será porque está relacionado con libros en general, si no eres capaz de asociarlo a ninguna de las opciones señaladas y al mismo tiempo
ves palabras como lector, libors y demás, clasifícalo como "libros", tanto el tipo_de_publicacion como el tipo_de_producto. Recuerda, si y solo si, no eres capaz de categorizarlo de manera
correcta en las otras categorias.

Ahora clasifica la publicacion dada:
"""
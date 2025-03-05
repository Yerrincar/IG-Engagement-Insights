prompt = """
Eres un especialista en clasificación de publicaciones de Instagram.
Quiero que me clasifiques que tipo de publicación son aquellas que te indicaré mediante el análisis de la descripción de la publicación.

***Requerimiento y formato:***
1. El formato de salida será un CSV con cuatro columnas: "id", "tipo_de_publicacion", "tipo_de_producto", "caption".
2. La descripción, a veces, hablará de varias cosas, pero deberás clasificarla en una sola categoría, la que más se ajuste a la descripción. 
3. En el caso de no ser capaz de realizar esto, deberás clasificarla como "multitipo". 

***Formato de salida esperado:***
1. El archivo de salida se guardará en la carpeta "output" con el nombre "clasificacion_publicaciones.csv".
2. El archivo de salida contendrá una fila por cada publicación que se te pase.
3. La columna "id" será el id de la publicación.
4. La columna "tipo_de_publicacion" será el tipo de publicación que clasificaste, ya sea bien "proceso de creación", "novedades", "promoción" o "libros".
5. La columna "tipo_de_producto" será el tipo de producto que se está publicitando. Puede ser desde "velas", "marcapáginas", "fundas" o "libros".
6. La columna "caption" será la descripción de la publicación. Esta columna será eliminada en producción, pero servirá para comprobar que la calificación se ha realizado bien.

***Ejemplo de salida***
id,tipo_de_publicacion,tipo_de_producto,caption
1,novedades,velas, "📢 ¡Novedad en la tienda! ✨ Hoy estoy muy emocionada de presentarte un producto muy especial: velitas aromáticas naturales. Estas velitas son únicas porque cada una está hecha en un tronco natural vaciado y tratado a mano, creando un recipiente exclusivo y diferente".

***Contexto de la cuenta de Instagram:***

La descripción de las publicaciones que se te pasarán provienen de una cuenta de Instagram cuyo objetivo es vender productos literarios a lectoras. Sus publicación van desde novedades hasta 
promociones de productos. Además de los productos que se publicitan a veces también se habla de libros en general o de información relacionada con los materiales de los productos.
Cabe destacar que a veces, repito, se habla de varios productos en una misma publicación, pero deberás clasificar la publicación en una sola categoría para mejorar la efiencia del análisis.

***Instrucciones finales:***
- Devuelve solo el archivo de salida csv en un formato limpio y ordenado. 
- En el caso de no poder determinarlo, seguramente será porque está relacionado con libros en general, si no eres capaz de asociarlo a ninguna de las opciones señaladas y al mismo tiempo
ves palabras como lector, libors y demás, clasifícalo como "libros", tanto el tipo_de_publicacion como el tipo_de_producto. Recuerda, si y solo si, no eres capaz de categorizarlo de manera
correcta en las otras categorias.
"""
### ¿Cuál es la mejor hora y día para publicar en Instagram para maximizar el engagement, el alcance y las ventas?

# Contexto
El cliente tiene una tienda que vende productos literarios, promocionados y vendidos principalmente a través de Instagram. Después de probar diferentes horarios y días de publicación, los resultados siguen siendo inconsistentes y, a veces, incluso negativos. Aunque existen numerosos artículos y guías sobre los mejores momentos para publicar, la mayoría se basan en cuentas con audiencias muy diferentes, lo que hace que la información no sea útil para su caso específico.

# Objetivo
Identificar la mejor combinación de día y hora para publicar con el fin de lograr una mayor interacción (me gusta, comentarios, etc) y, en consecuencia, aumentar el alcance y las ventas de la tienda literaria del cliente.

# Alcance y metodología
Este repositorio proporciona un enfoque End-to-End de un proyecto de análisis de datos.

# Parte 1: Análisis de los datos de la cuenta y visualización de resultados
- **Recopilación de datos (Web Scraping):** Se extraen estadísticas de todo lo relacionado a la cuenta y su engagement, asegurando el cumplimiento de las políticas de uso de datos de la plataforma. Para este fin, utilizaremos un scraper de Apify.

- **Análisis, limpieza y transformación de datos:** Se utiliza Python para limpiar, preprocesar y dar formato inicial al CSV, además de añadir las columna pertinentes para el correcto análisis. Se emplea PostgreSQL para gestionar las bases de datos donde se almacenarán los resultados obtenidos y se realizarán cambios extras que sean necesarios.

- **Clasificación del tipo de producto y publicación:** Con el fin de clasificar cada publicación según el producto a vender y el tipo de publicación. Se ha implementado de manera local la API de Gémini, que generará un csv con el id de la publicación, tipo de publicación y tipo de producto, gracias a analizar las palabras usadas en la descripción y hashtags.
    
- **Visualización de datos:** Se utiliza Power BI para crear dashboards que muestren al cliente cómo evoluciona la métrica de engagement, así como para resaltar hallazgos importantes.

# Resultados 
- **Insights inmediatos:** Horarios y días en los que la cuenta consigue más (o menos) interacción. Pudiéndose ver qué productos, tipos de publicación y formato generan un mayor número de interacción.
- **Base de datos unificada** para almacenar la información limpia y transformada.  
- **Dashboards actualizados** que facilitan la toma de decisiones de forma rápida, generando estabilidad y progreso a la hora de realizar publicaciones con intenciones de vender.
- **Escalabilidad** adecuada para permitir actualizar los datos conforme pase el tiempo de manera automática o incluso aplicar este mismo proyecto a otras cuentas de mayor magnitud.
- **Crecimiento en redes** y como consecuente, aumentar las ventas. Se esperá conseguir estabilidad, mejores números y un aumento del 20-50% de la métrica principal respecto a los meses anteriores. 

# ¿Por qué este proyecto?
La mayoría de guías sobre horarios de publicación se basan en datos globales o en cuentas con características diferentes. IG-Engagement-Insights se centra en la realidad específica de una cuenta de temática literaria y sus seguidores, proporcionando un análisis especializado que responde a necesidades particulares.

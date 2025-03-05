###¿Cuál es la mejor hora y día para publicar en Instagram y maximizar el engagement, el alcance y las ventas?

# Contexto
Un conocido, a quien llamaremos “el cliente”, tiene una tienda de productos literarios que promociona y vende principalmente a través de Instagram. Tras probar diferentes horarios y días de publicación, los resultados siguen siendo inconsistentes e incluso a veces negativos. Aunque existen numerosos artículos y guías sobre los mejores momentos para publicar, la mayoría de estos están basados en cuentas con audiencias muy distintas, por lo que la información no resulta útil para su caso específico.

# Objetivo
El objetivo de este proyecto es identificar y predecir la mejor combinación de día y hora para publicar, de manera que se obtenga un mayor engagement (likes, comentarios, visualizaciones) y, en consecuencia, se incremente el alcance y las ventas de la tienda literaria del cliente.

# Alcance y metodología
Este repositorio ofrece un enfoque End-to-End que se dividirá en dos partes unificadas en un solo proyecto.

# Parte 1: Análisis de los datos de la cuenta y visualización de los resultados.
-Recopilación de datos (Web Scraping): Se extraen las estadísticas de cuentas de Instagram similares o relevantes, con cuidado de cumplir con las políticas de uso de datos de la plataforma. Para ello haremos uso de un scrapper de apify.

-Análisis, limpieza y transformación de datos: Python (pandas) para el la limpieza, preprocesamiento y formateo inicial del csv. SQL para manejar las bases de datos a las que se conectarán los resultados obtenidos.

-Visualización de datos:Power BI para crear dashboards que muestren al cliente la evolución de las métricas de engagement, así como hallazgos importantes.

# Resultado esperado de la Parte 1
Insights inmediatos: horarios y días en los que la cuenta obtiene más (o menos) interacción. Además, observaremos que productos generan más engage. Base de datos unificada para almacenar la información limpia y transformada. Dashboards actualizados que faciliten la toma de decisiones rápidas.

# Parte 2: Machine Learning
-Recopilación de datos (Web Scrapping): Misma implementación que para la primera parte, pero aplicado a más de 300 cuentas y más de 2000 publicaciones.

-EDA: Python (pandas, numpy, scikit-learn, matplotlib, seaborn) para la limpieza de valores nulos, outliers, normalización, etc, y para la visualización de estos con el objetivo de facilitar este proceso.

-Feature Engineering: Creación de nuevas variables (ratios, diffs, etc) para mejorar el entrenamiento del modelo.

-Selección de modelos, evaluación y optimización de hiperparámetros (optuna).

-Mejoras y conclusiones tras obtener resultados.

# Resultado esperado de la Parte 2
Modelo capaz de encontrar la mejor combinación día/hora para obtener el mayor engagement posible. Recomendaciones accionables basadas en datos y proyecciones a futuro.

# ¿Por qué este proyecto?
La mayoría de guías sobre horarios de publicación parten de datos globales o para cuentas con características diferentes. IG-Engagement-Insights se enfoca en la realidad concreta de las cuentas de temática literaria y sus seguidores, ofreciendo un análisis especializado que responde a necesidades específicas.

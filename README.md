### ¿Cuál es la mejor hora y día para publicar en Instagram para maximizar el engagement, el alcance y las ventas?

# Contexto
Un amigo, a quien llamaremos "el cliente," tiene una tienda que vende productos literarios, promocionados y vendidos principalmente a través de Instagram. Después de probar diferentes horarios y días de publicación, los resultados siguen siendo inconsistentes y, a veces, incluso negativos. Aunque existen numerosos artículos y guías sobre los mejores momentos para publicar, la mayoría se basan en cuentas con audiencias muy diferentes, lo que hace que la información no sea útil para su caso específico.

# Objetivo
El objetivo de este proyecto es identificar y predecir la mejor combinación de día y hora para publicar con el fin de lograr una mayor interacción (me gusta, comentarios, vistas) y, en consecuencia, aumentar el alcance y las ventas de la tienda literaria del cliente.

# Alcance y metodología
Este repositorio proporciona un enfoque End-to-End que se dividirá en dos partes, unificadas dentro de un solo proyecto.

# Parte 1: Análisis de los datos de la cuenta y visualización de resultados
- **Recopilación de datos (Web Scraping):** Se extraen estadísticas de cuentas de Instagram similares o relevantes, asegurando el cumplimiento de las políticas de uso de datos de la plataforma. Para este fin, utilizaremos un scraper de Apify.

- **Análisis, limpieza y transformación de datos:** Se utiliza Python (pandas) para limpiar, preprocesar y dar formato inicial al CSV. Se emplea SQL para gestionar las bases de datos donde se almacenarán los resultados obtenidos.

- **Visualización de datos:** Se utiliza Power BI para crear dashboards que muestren al cliente cómo evoluciona la métrica de engagement, así como para resaltar hallazgos importantes.

# Resultado esperado de la Parte 1
- **Insights inmediatos:** Horarios y días en los que la cuenta consigue más (o menos) interacción. También se podrá ver qué productos generan más engagement.
- **Base de datos unificada** para almacenar la información limpia y transformada.
- **Dashboards actualizados** que faciliten la toma de decisiones de forma rápida.

# Parte 2: Machine Learning
- **Recopilación de datos (Web Scraping):** La misma implementación que en la Parte 1, pero aplicada a más de 300 cuentas y más de 2,000 publicaciones.

- **EDA (Análisis Exploratorio de Datos):** Se utiliza Python (pandas, numpy, scikit-learn, matplotlib, seaborn) para manejar valores faltantes, outliers, normalización, etc., y para visualizar estos aspectos y facilitar el proceso.

- **Ingeniería de características:** Creación de nuevas variables (ratios, diferencias, etc.) para mejorar el entrenamiento del modelo.

- **Selección de modelo, evaluación y optimización de hiperparámetros (Optuna).**

- **Mejoras y conclusiones** tras obtener los resultados.

# Resultado esperado de la Parte 2
- **Un modelo capaz de encontrar** la mejor combinación de día/hora para conseguir el mayor engagement posible.
- **Recomendaciones accionables** basadas en los datos y proyecciones futuras.

# ¿Por qué este proyecto?
La mayoría de guías sobre horarios de publicación se basan en datos globales o en cuentas con características diferentes. IG-Engagement-Insights se centra en la realidad específica de las cuentas de temática literaria y sus seguidores, proporcionando un análisis especializado que responde a necesidades particulares.

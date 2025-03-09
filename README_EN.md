### Which is the best hour and day to post on Instagram to maximize engagement, reach, and sales?

# Context
The client has a store selling literary products, promoted and sold primarily through Instagram. After trying different posting times and days, the results remain inconsistent and sometimes even negative. Although numerous articles and guides exist on the best times to post, most are based on accounts with very different audiences, making the information unhelpful for his specific case.

# Objective
The goal of this project is to identify and predict the best combination of day and time to post in order to achieve higher engagement (likes, comments, views) and, consequently, to increase the reach and sales of the client’s literary store.

# Scope and methodology
This repository provides an End-to-End approach that will be divided into two parts, unified within a single project.

# Part 1: Analysis of the account data and results visualization
- **Data collection (Web Scraping):** Statistics are extracted from similar or relevant Instagram accounts, ensuring compliance with the platform's data usage policies. For this purpose, we will use an Apify scraper.
- **Data analysis, cleaning, and transformation:** Python (pandas) for cleaning, preprocessing, and initial formatting of the CSV. SQL to manage the databases where the obtained results will be stored.
- **Data visualization:** Power BI to create dashboards that show the client how engagement metrics evolve, as well as highlight important findings.

# Expected result of Part 1
- **Immediate insights:** Times and days when the account achieves more (or less) interaction. We will also see which products generate more engagement.
- **A unified database** to store the clean and transformed information.
- **Updated dashboards** that facilitate quick decision-making.

# Part 2: Machine Learning
- **Data collection (Web Scraping):** The same implementation as in Part 1, but applied to over 300 accounts and more than 2,000 posts.
- **EDA (Exploratory Data Analysis):** Python (pandas, numpy, scikit-learn, matplotlib, seaborn) to handle missing values, outliers, normalization, etc., and to visualize these aspects to facilitate the process.
- **Feature Engineering:** Creation of new variables (ratios, diffs, etc.) to improve model training.
- **Model selection, evaluation, and hyperparameter optimization (Optuna).**
- **Improvements and conclusions** after obtaining the results.

# Expected result of Part 2
- **A model capable** of finding the best day/time combination to achieve the highest possible engagement.
- **Actionable recommendations** based on data and future projections.

# Why this project?
Most guides about posting times are based on global data or on accounts with different characteristics. IG-Engagement-Insights focuses on the specific realities of literary-themed accounts and their followers, providing a specialized analysis that addresses particular needs.

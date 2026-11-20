# Amazon Reviews 2023 – Combined Dataset

## Overview

This dataset is a collection of 100,000 Amazon product reviews created using selected subsets of the [Amazon Reviews 2023 dataset](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) by McAuley et al.

For this project, reviews from five different product categories were collected and combined into a single dataset. Each category contributes 20,000 reviews, giving us a total of 100,000 records.

The main goal is to build a sentiment analysis model that can understand customer opinions across different product categories instead of being limited to a single category.

## Dataset Source

- **Original Dataset:** Amazon Reviews 2023
- **Research Group:** McAuley Research Group
- **Source:** [Hugging Face – Amazon Reviews 2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)
- **Format:** Parquet
- **Data Type:** Customer reviews and related product information

## Categories Included

The dataset contains reviews from the following five categories:

| No. | Category | Reviews |
|:---:|---|---:|
| 1 | Electronics | 20,000 |
| 2 | Health and Personal Care | 20,000 |
| 3 | Handmade Products | 20,000 |
| 4 | Arts, Crafts and Sewing | 20,000 |
| 5 | Digital Music | 20,000 |
| | **Total** | **100,000** |

## Dataset Structure

All five category datasets were processed and merged into one Parquet file.

A separate `category` column was added so that each review can be associated with its original product category. This makes it easier to analyze customer sentiment across different types of products.

Some of the important columns include:

| Column | Description |
|---|---|
| `text` | Customer review text used for sentiment analysis |
| `rating` | Sentiment label assigned to the review (positive, negative, or neutral) |
| `category` | Product category from which the review was collected |

The processed Parquet file may contain additional columns depending on the data preparation steps.

## Data Preparation

The following steps were performed to create the combined dataset:

1. Collected review data from the five selected product categories.
2. Selected 20,000 reviews from each category.
3. Cleaned and processed the individual datasets.
4. Combined all five datasets into a single DataFrame.
5. Added a `category` column to identify the source category of each review.
6. Standardized the sentiment labels into three classes.

## Project Objective

This dataset will be used to develop and evaluate a multi-category Amazon Review Sentiment Analysis model.

The model is designed to classify customer reviews into three sentiment categories:

- **Positive** – Reviews expressing satisfaction or a favourable opinion.
- **Negative** – Reviews expressing dissatisfaction or an unfavourable opinion.
- **Neutral** – Reviews expressing neither a clearly positive nor a negative opinion.

Using reviews from multiple product categories will help evaluate how well the model performs on different types of customer feedback.

## Dataset Summary

| Property | Details |
|---|---|
| Original Dataset | Amazon Reviews 2023 |
| Source | McAuley Research Group |
| Number of Categories | 5 |
| Reviews per Category | 20,000 |
| Total Reviews | 100,000 |
| Sentiment Classes | 3 |
| File Format | Parquet |
| Main Task | Multi-category Sentiment Classification |

## Important Note

This dataset is a project-specific subset created by combining and processing selected portions of the original Amazon Reviews 2023 dataset. It does not represent the complete original dataset.

The original reviews belong to their respective data sources. If you plan to use or redistribute this combined dataset, please refer to the original dataset's licensing and usage conditions.

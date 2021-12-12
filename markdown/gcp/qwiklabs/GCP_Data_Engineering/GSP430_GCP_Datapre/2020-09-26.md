# 2020-09-26

- **Qwiklabs:** [Google Cloud Training : Data Engineering](https://google.qwiklabs.com/quests/25)

## Creating a Data Transformation Pipeline with Cloud Dataprep

- [Creating a Data Transformation Pipeline with Cloud Dataprep](https://google.qwiklabs.com/focuses/4415?parent=catalog)
    - Cloud Dataprep by Trifacta
        - https://cloud.google.com/dataprep/
        - https://www.trifacta.com/
    - **ecommerce dataset** from [Google Merchandise Store](https://shop.googlemerchandisestore.com/)
        - **Broken link** - https://www.en.advertisercommunity.com/t5/Articles/Introducing-the-Google-Analytics-Sample-Dataset-for-BigQuery/ba-p/1676331#
        - https://www.blog.google/products/marketingplatform/analytics/introducing-google-analytics-sample
        - Schema / Data Model
            - https://support.google.com/analytics/answer/3437719?hl=en

## 感想與連結

- [Cloud Dataprep](https://cloud.google.com/dataprep/) 的商務需求過去在不同產業都有看過，也就是資料前處理的部分
    - **資料探索(Data Explorer)**: 先對資料集進行敘述統計
    - **資料清洗(Data Cleaning)**: 找出空值，或者資料型態需要修改的地方，進行清洗。其次，透過合併欄位，來產生具有唯一識別特徵的新欄位（某種程度的 Transformation)
    - 排程工作： 透過「配方（Recipe）」的概念，讓未來新資料的前處理都可以透過排程進行更新
- 類似服務或產品：
    - 看起來 Azure 也有對應服務 [Azure Data Explorer](https://azure.microsoft.com/en-us/services/data-explorer/)
    - 先前研究 Tableau 也有 [Tableau Prep Builder](https://www.tableau.com/support/releases/prep)
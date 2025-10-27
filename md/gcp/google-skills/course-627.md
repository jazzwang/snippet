# Engineer Data for Predictive Modeling with BigQuery ML

-----

[TOC]

-----

- https://www.cloudskillsboost.google/course_templates/627

全部做完，會拿到 Badge
![](https://cdn.qwiklabs.com/ap7SDIuPw1U4BrY9qaMnALRGkaPuaztK%2BEIrGRHzfs4%3D)

## 2024-06-19

### Predict Visitor Purchases with a Classification Model in BigQuery ML

- https://www.cloudskillsboost.google/course_templates/627/labs/486811
- GSP229

#### Task 1. Explore ecommerce data

#### Task 2. Identify an objective

#### Task 3. Select features and create your training dataset

#### Task 4. Create a BigQuery dataset to store models

#### Task 5. Select a BigQuery ML model type and specify options

```
CREATE OR REPLACE MODEL `ecommerce.classification_model`
OPTIONS
(
model_type='logistic_reg',
labels = ['will_buy_on_return_visit']
)
AS

#standardSQL
SELECT
  * EXCEPT(fullVisitorId)
FROM

  # features
  (SELECT
    fullVisitorId,
    IFNULL(totals.bounces, 0) AS bounces,
    IFNULL(totals.timeOnSite, 0) AS time_on_site
  FROM
    `data-to-insights.ecommerce.web_analytics`
  WHERE
    totals.newVisits = 1
    AND date BETWEEN '20160801' AND '20170430') # train on first 9 months
  JOIN
  (SELECT
    fullvisitorid,
    IF(COUNTIF(totals.transactions > 0 AND totals.newVisits IS NULL) > 0, 1, 0) AS will_buy_on_return_visit
  FROM
      `data-to-insights.ecommerce.web_analytics`
  GROUP BY fullvisitorid)
  USING (fullVisitorId)
;
```

#### Task 6. Evaluate classification model performance


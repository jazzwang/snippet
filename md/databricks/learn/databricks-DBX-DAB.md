# Databricks - What is DBX? What is DAB?

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
what is DBX? what is DAB? if the context is related to Databricks
</td></tr><tr><td>A:</td><td>

In the context of Databricks, DBX and DAB are both developer tools used to automate, package, and deploy data engineering and data science workloads. [1, 2, 3, 4, 5] 
Here is the breakdown of what each tool is and how they differ:

## 1. DBX (Databricks Labs Extensions)

* What it is: A legacy command-line tool developed by Databricks Labs to help developers manage deployment lifecycles.
* Primary use: It allowed developers to pack local code (like Python wheels) and deploy them as Databricks Jobs using a CLI.
* Current status: Deprecated. It has been officially replaced by Databricks Asset Bundles (DABs). [6, 7, 8, 9, 10] 

## 2. DAB (Databricks Asset Bundles)

* What it is: The modern, official Databricks feature for implementing Infrastructure as Code (IaC) and CI/CD pipelines. [11, 12, 13] 
* Primary use: It uses a single YAML configuration file to define, package, and deploy entire Databricks projects. [14, 15, 16] 
* Key components managed:
* Source code
   * Notebooks
   * Delta Live Tables (DLT)
   * Databricks Workflows/Jobs
   * Unity Catalog schemas [17, 18] 

## Key Differences

| Feature [19, 20, 21, 22, 23] | DBX (Legacy) | DAB (Modern) |
|---|---|---|
| Official Support | Databricks Labs (Open-source/Community) | Native Databricks Product (Fully supported) |
| Configuration | Complex JSON/YAML files | Clean, standardized YAML definition |
| Integration | Requires separate CLI installation | Built directly into the standard Databricks CLI |
| Scope | Mainly focused on code and jobs | Manages code, pipelines, dashboards, and security |

If you are starting a new project on Databricks, you should always use DABs (Databricks Asset Bundles) instead of DBX. [24, 25] 
To help you get started, let me know:

* Are you looking to set up a CI/CD pipeline (like GitHub Actions)?
* What type of workload are you deploying (e.g., Python scripts, Notebooks, or Delta Live Tables)?
* Do you need a sample YAML configuration template?

[1] [https://www.databricks.com](https://www.databricks.com/blog/announcing-general-availability-databricks-asset-bundles)
[2] [https://github.com](https://github.com/databrickslabs/dbx)
[3] [https://www.reddit.com](https://www.reddit.com/r/databricks/comments/1dim8w2/databricks_asset_bundles_and_integration_tests/)
[4] [https://community.databricks.com](https://community.databricks.com/t5/technical-blog/customizing-target-deployments-in-databricks-asset-bundles/ba-p/124772)
[5] [https://medium.com](https://medium.com/mlops-io/databricks-asset-bundles-dab-with-github-actions-ed6586815705)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=xXNqVK6BaGM)
[7] [https://medium.com](https://medium.com/@kaartickprince/how-dbx-is-helps-in-testing-spark-applications-in-the-databrick-environment-4ecd9b2666d1)
[8] [https://newmathdata.com](https://newmathdata.com/blog/databricks-asset-bundles-dabs-vs-terraform-deployment-guide/)
[9] [https://blog.yannickjaquier.com](https://blog.yannickjaquier.com/databricks/dbx-for-local-and-rapid-development-lifecycle-through-databricks.html)
[10] [https://medium.com](https://medium.com/@kaartickprince/how-dbx-is-helps-in-testing-spark-applications-in-the-databrick-environment-4ecd9b2666d1)
[11] [https://medium.com](https://medium.com/towards-data-engineering/databricks-asset-bundles-dabs-deploying-with-github-actions-for-ci-cd-d3fa7d443327)
[12] [https://dateonic.com](https://dateonic.com/how-to-set-up-ci-cd-pipelines-for-databricks/)
[13] [https://medium.com](https://medium.com/@patrickleahey/dabbling-in-dabs-simplified-ci-cd-using-databricks-asset-bundles-bcb6ac97c382)
[14] [https://oindrila-chakraborty88.medium.com](https://oindrila-chakraborty88.medium.com/introduction-to-databricks-asset-bundles-dabs-31ec4908caa8)
[15] [https://www.databricks.com](https://www.databricks.com/blog/announcing-general-availability-databricks-asset-bundles)
[16] [https://medium.com](https://medium.com/@mariusz_kujawski/ci-cd-on-databricks-what-the-docs-dont-tell-you-31901aee107d)
[17] [https://cevo.com.au](https://cevo.com.au/post/transforming-data-engineering-with-devops-on-the-databricks-platform/)
[18] [https://medium.com](https://medium.com/@chua.vctr/data-lakehouses-with-databricks-a-modern-approach-to-data-management-eca54e4a624e)
[19] [https://medium.com](https://medium.com/data-warehouse-migrations-to-databricks/change-management-during-migration-to-databricks-b6662898d586)
[20] [https://github.com](https://github.com/databrickslabs/dbx/issues/833)
[21] [https://www.reddit.com](https://www.reddit.com/r/databricks/comments/15waf0j/azure_devops_cicd/)
[22] [https://www.youtube.com](https://www.youtube.com/watch?v=xXNqVK6BaGM)
[23] [https://medium.com](https://medium.com/@tugnolialessio/implementing-a-secure-on-premises-api-with-data-api-builder-keycloak-and-sql-server-8d9fbed2871e)
[24] [https://medium.com](https://medium.com/totalenergies-digital-factory/databricks-assets-bundles-dabs-deploy-and-managing-data-ai-assets-a4e29bdb15a7)
[25] [https://dataengineeringcentral.substack.com](https://dataengineeringcentral.substack.com/p/simplifying-cicd-with-databricks)

</td></tr>
</table>

# 2-Week Databricks Learning Path: 
## Mastering ML Model Governance with <mark>Unity Catalog</mark> and Interactive <mark>Streamlit</mark> Applications

> created by Gemini Deep Research
> Source: https://g.co/gemini/share/5fd2dd96ab9b
> Created with 2.5 Flash June 5, 2025 at 12:37 AM

<table><tr><td valign="middle">Q:</td><td valign="middle">
<!-- add your Prompt bellow-->
could you plan 2-weeks Databricks learning outline, especially targeting learning to register ML models to unity catelog and build Streamlit App to interact with specific ML model? if possible, look into Databricks documents and certification training materials. thanks!
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
## **I. Introduction: The Databricks Lakehouse for MLOps**

This report outlines a comprehensive 2-week learning path designed to equip practitioners with the knowledge and practical skills necessary to manage machine learning (ML) models effectively on the Databricks Lakehouse Platform, with a particular focus on model registration to Unity Catalog and building interactive Streamlit applications. The Databricks Lakehouse Platform represents a paradigm shift in data management, offering a unified environment that seamlessly integrates data warehousing and data lake capabilities. This architecture is purpose-built to support the entire spectrum of data workloads, from traditional business intelligence (BI) to advanced artificial intelligence (AI) and machine learning operations (MLOps).1

### **Overview of Databricks Lakehouse Platform and its Components**

The foundational strength of the Databricks Lakehouse Platform lies in its ability to provide scalable storage and processing for modern organizations, thereby mitigating the need for disparate, isolated systems typically used for distinct workloads like ML and BI.1 This unified approach fosters a single source of truth for data, reduces redundant costs, and ensures data freshness across the enterprise.1 At its core, the platform is built on Apache Spark, leveraging its robust processing engine for all transformations and queries.1

#### **Core Technologies**

Two pivotal technologies underpin the Databricks Lakehouse:

* **Delta Lake:** This optimized storage layer provides ACID (Atomicity, Consistency, Isolation, Durability) transactions, schema enforcement, and versioning capabilities. These features are fundamental for ensuring data reliability, quality, and enabling incremental data refinement through a medallion architecture.1  
* **Unity Catalog:** Serving as the unified, fine-grained governance solution for all data and AI assets, Unity Catalog is a central metadata layer that manages access policies across multiple workspaces. It supports a wide array of assets, including tables, volumes, features, and crucially, ML models.1

#### **Operational Components**

The Databricks platform is composed of several interconnected operational components that facilitate diverse workflows:

* **Workspaces:** A workspace acts as a cloud-based deployment and an environment where teams can organize and access Databricks assets, including notebooks, libraries, dashboards, and experiments. It provides the necessary access to data objects and computational resources for collaborative analysis.4  
* **Compute:** Databricks offers flexible compute options tailored for specific workload patterns:  
  * *All-purpose clusters* are designed for interactive, collaborative analysis, allowing multiple users to share resources for ad-hoc queries and development.4  
  * *Job clusters* are ephemeral, created by the Databricks job scheduler for automated workloads and terminated upon job completion, which optimizes cost efficiency for production jobs.4  
  * *Databricks Runtime for Machine Learning (Databricks Runtime ML)* is a specialized runtime that automates compute creation with pre-built infrastructure for machine learning and deep learning. It includes pre-configured common ML/DL libraries and GPU support, significantly simplifying environment setup for ML workloads.4  
* **Notebooks:** These web-based interfaces are central to creating data science and machine learning workflows, enabling the combination of runnable commands, visualizations, and narrative text in a single document.4

#### **MLOps Specific Components**

For the machine learning lifecycle, Databricks provides specialized tools that are deeply integrated within the Lakehouse ecosystem:

* **MLflow:** An open-source platform specifically designed to manage the complexities of the machine learning process. MLflow encompasses experiment tracking (recording and comparing parameters and results), model management (Model Registry for versioning and annotation), and model deployment capabilities.5 Databricks offers a fully managed and hosted version of MLflow, which is seamlessly integrated with other Databricks services like Unity Catalog and Model Serving, enhancing its robustness and scalability for enterprise use.6  
* **Model Serving (Mosaic AI Model Serving):** This component provides a unified, scalable, and serverless interface for deploying, governing, and querying AI models as REST API endpoints. Its tight integration with MLflow Model Registry and Unity Catalog ensures robust management of model versions, dependencies, validation, and overall governance.6  
* **Databricks Apps:** This feature empowers developers to build and deploy secure data and AI applications (e.g., using Python frameworks like Streamlit, Dash, or Gradio) directly on the Databricks serverless platform. These applications natively integrate with Unity Catalog for data governance, Databricks SQL for querying data, and Model Serving for deploying AI models, eliminating the need for separate infrastructure.8

### **The Importance of MLOps, Unity Catalog, and Interactive Applications in Modern ML Workflows**

The complexity and iterative nature of the machine learning lifecycle necessitate robust MLOps practices. MLflow, as a core component, ensures that every phase—from initial experimentation to final deployment—is manageable, traceable, and reproducible.5 This is paramount for achieving reliability, ensuring compliance, and scaling ML initiatives across an organization.

Unity Catalog, as the central data and AI governance system, provides a singular point of control for managing access policies, tracking data lineage, and discovering assets across all workspaces.2 For ML, this extends to models, features, and volumes, guaranteeing the secure and compliant utilization of AI assets.2 The platform's design around Unity Catalog helps establish a single source of truth for all data and AI assets, thereby eliminating redundant costs and simplifying auditing processes.1 This cohesive approach to governance is a significant advantage for enterprises seeking end-to-end control and visibility over their data and AI landscape.

Interactive applications, particularly those built with Streamlit, are indispensable for bridging the gap between complex ML development and business impact. They provide user-friendly interfaces that enable non-technical stakeholders to interact with sophisticated ML models and data, demonstrate model capabilities, and facilitate feedback loops.14 Databricks Apps further simplifies the deployment of such applications, making it easier to operationalize ML insights into tangible business tools.8

A critical characteristic of the Databricks Lakehouse is its function as an MLOps enabler, extending beyond mere data management. The deep integration of MLflow and Model Serving within the Lakehouse architecture signifies that Databricks has engineered this platform to be the foundational backbone for the *entire* ML lifecycle, from raw data ingestion to model deployment and governance.2 This design means that ML models are treated as first-class, governable assets within the same unified governance model as data tables, providing a distinct advantage for organizations aiming for end-to-end control and visibility.

Furthermore, the strategic adoption of serverless compute for key MLOps components like Model Serving and Databricks Apps represents a significant architectural advantage for scalability and cost-efficiency.7 By abstracting away the complexities of infrastructure provisioning, scaling, and maintenance, Databricks enables automatic scaling based on demand, optimizes infrastructure costs, and reduces operational overhead for ML engineers.7 This allows practitioners to concentrate on the core ML problem, accelerating the path from development to production and making scalable MLOps more accessible without requiring deep cloud infrastructure expertise.

**Table 1: Key Databricks Components for MLOps**

| Component Name | Brief Description | Primary Role in MLOps | Key Integrations |
| :---- | :---- | :---- | :---- |
| Unity Catalog | Unified governance solution for data and AI assets. | Centralized access control, auditing, lineage, and discovery for ML models and data. | Delta Lake, MLflow, Model Serving, Databricks SQL |
| MLflow | Open-source platform for ML lifecycle management. | Experiment tracking, model versioning (Model Registry), and deployment. | Unity Catalog, Databricks Runtime ML, Model Serving |
| Model Serving | Serverless platform for deploying AI models as REST APIs. | Real-time and batch inference, scalable model deployment. | MLflow Model Registry, Unity Catalog, Databricks Apps |
| Databricks Apps | Native hosting for interactive data and AI applications. | Deploying Streamlit/Dash/Gradio UIs to interact with ML models and data. | Unity Catalog, Databricks SQL, Model Serving, Databricks Jobs |
| Delta Lake | Optimized storage layer for the Lakehouse. | Provides ACID transactions, schema enforcement, and versioning for ML data. | Apache Spark, Unity Catalog |
| Databricks Runtime ML | Specialized runtime for ML/DL workloads. | Automates compute creation with pre-built ML/DL infrastructure and libraries. | MLflow, Apache Spark |

## **II. Week 1: Foundations of ML Model Management on Databricks**

The first week of this learning path is dedicated to establishing a robust understanding of the Databricks platform's core functionalities, particularly MLflow for experiment tracking, and the indispensable role of Unity Catalog in governing ML models.

### **Day 1-2: Databricks Platform Essentials & MLflow Tracking**

The initial days focus on hands-on familiarity with the Databricks environment and the fundamental aspects of MLflow for managing machine learning experiments.

#### **Core Databricks Concepts in Practice**

To begin, practitioners should sign up for a Databricks free trial and set up their first workspace.17 A Databricks workspace serves as the primary environment for accessing and organizing all Databricks assets, providing a collaborative space for teams.4 Following workspace setup, configuring compute resources is a critical step. Creating an all-purpose cluster is recommended for interactive development due to its suitability for collaborative analysis among multiple users.4 It is crucial to select a Databricks Runtime for Machine Learning (Databricks Runtime ML). This specialized runtime automates compute creation and comes pre-installed with popular ML and deep learning libraries, along with pre-built infrastructure and GPU support, significantly simplifying the environment setup for ML workloads.4 This pre-configured environment is more than just a collection of libraries; it functions as an MLOps accelerator, streamlining environment consistency and reducing setup time, thereby accelerating the entire ML development and operationalization process. Familiarity with Databricks notebooks, the web-based interface for creating and executing data science and ML workflows, which combine runnable commands, visualizations, and narrative text, is also essential.4

#### **Introduction to MLflow: Experiment Tracking**

MLflow is an open-source platform purpose-built to manage the complexities of the machine learning lifecycle, providing tools for tracking experiments, managing models, and deploying them.5 Databricks offers a fully managed and hosted version of MLflow, seamlessly integrated with its broader ecosystem.6

Experiment tracking is a core MLflow capability, allowing users to log and compare parameters, metrics, and artifacts from their ML training runs.6 This capability is fundamental for ensuring reproducibility, understanding model performance across different iterations, and making informed decisions during model development. MLflow organizes work into "experiments," which are collections of "runs." Each "run" represents a single execution of ML code, meticulously logging its inputs, outputs, and environmental details.4

For enhanced efficiency, Databricks recommends leveraging MLflow autologging. This feature automatically logs training code written in many popular ML and deep learning frameworks, significantly reducing the amount of boilerplate code required for tracking.5 This automated approach to logging is an important enabler for MLOps adoption, as it lowers the barrier to entry for data scientists who might otherwise resist adding explicit tracking code. By encouraging the adoption of fundamental MLOps practices from the outset, autologging lays the groundwork for building reproducible models, facilitating comparisons, and ultimately enabling efficient model registration and governance. For more fine-grained control, the MLflow Tracking API can be used programmatically to log custom parameters, metrics, and artifacts, with Databricks providing a hosted tracking server that automatically captures this data.18 Users can explicitly set the active MLflow experiment using mlflow.set\_experiment() or by passing the experiment\_id parameter to mlflow.start\_run(); otherwise, runs are logged to the notebook's default experiment.18

**Hands-on Exercise:**

1. Set up a Databricks workspace and create an all-purpose cluster configured with Databricks Runtime ML.4  
2. Create a new Databricks notebook.  
3. Train a simple machine learning model, such as a scikit-learn classifier on a public dataset like Iris.19  
4. Implement MLflow autologging for the training process.18  
5. Navigate to the MLflow UI (Experiments section) to view the logged runs, compare parameters and metrics, and inspect artifacts.18

### **Day 3-4: Deep Dive into Unity Catalog for Data & AI Governance**

These days are dedicated to understanding Unity Catalog, the central governance solution within the Databricks Lakehouse Platform, and its critical role in managing data and AI assets.

#### **Unity Catalog Fundamentals**

Unity Catalog is the cornerstone of data and AI governance on Databricks, providing a single, centralized solution for managing access control, auditing, lineage, and data discovery across all Databricks workspaces.2 It functions as a centralized metadata layer, directly integrated with the Lakehouse architecture.3 This unified approach to governance is Databricks' solution to the challenges of "data silos" and "governance sprawl" often encountered in modern data platforms. By centralizing these capabilities for *all* data and AI assets, Unity Catalog directly addresses the complexities of managing permissions and tracking data flow across disparate systems, thereby simplifying compliance, enhancing security (especially for sensitive data like PII), and improving overall operational efficiency within an enterprise data ecosystem.1

In Unity Catalog, all metadata is registered in a metastore, and data and AI assets are organized hierarchically using a three-level namespace: catalog.schema.object.11 This structure is not merely a naming convention but a foundational governance pattern. Catalogs serve as the top-level organizational units, often used to define data isolation boundaries or mirror organizational units.11 Schemas (also known as databases) logically organize tables, views, and other assets within a catalog.12 Crucially, registered ML models are treated as first-class objects within this hierarchy, enabling uniform application of fine-grained access control and data isolation policies across both data and models.11 Unity Catalog is typically enabled by default in new Databricks workspaces, streamlining its adoption.10

#### **Key Features for Data and AI Governance**

Unity Catalog offers a comprehensive suite of features for robust data and AI governance:

* **Centralized Access Control:** It provides fine-grained access control at the catalog, schema, table, column, and ML model levels.3 This is achieved using standard ANSI SQL syntax for granting and revoking permissions, which simplifies security management and ensures consistency across the platform.11  
* **Data Lineage:** Unity Catalog automatically captures runtime data lineage across queries executed on Databricks clusters or SQL warehouses. This capability tracks how data assets are created and used across all languages, down to the column level, and includes lineage for notebooks, jobs, and dashboards.2 This provides a transparent view of data transformations, which is invaluable for auditing, debugging, and understanding the impact of data changes on downstream processes, including ML models.  
* **Auditing:** User-level audit logs that record access to data and AI assets are automatically captured by Unity Catalog. These logs, along with billable usage and lineage information, can be easily accessed and queried via system tables, supporting compliance and operational monitoring.2  
* **Data Discovery (Catalog Explorer):** The Databricks Catalog Explorer offers a user interface to explore and manage all data and AI assets, including registered ML models, their permissions, owners, and storage locations. The ability to tag and document data assets further enhances discoverability for data consumers.10  
* **Delta Sharing:** An open protocol developed by Databricks, Delta Sharing facilitates secure data and AI asset sharing with other organizations or internal teams, irrespective of their underlying computing platforms.10

**Hands-on Exercise:**

1. Navigate to the Catalog Explorer in your Databricks workspace.10  
2. Explore existing catalogs, schemas, and tables to gain practical understanding of the three-level namespace (catalog.schema.object).11  
3. Practice creating a new catalog and a new schema using SQL commands (e.g., CREATE CATALOG IF NOT EXISTS \<catalog\_name\>; USE CATALOG \<catalog\_name\>; CREATE SCHEMA IF NOT EXISTS \<schema\_name\>;).12  
4. Grant basic permissions, such as USE CATALOG and CREATE SCHEMA, to a test user or group.12  
5. If sample data is available, load it into a Delta table within your new schema and observe how Unity Catalog tracks its lineage.1

### **Day 5-7: MLflow Model Registry & Unity Catalog Integration**

The final days of Week 1 are dedicated to understanding the MLflow Model Registry and its crucial integration with Unity Catalog for comprehensive ML model governance.

#### **MLflow Model Registry Concepts**

The MLflow Model Registry serves as a centralized repository for managing the entire lifecycle of MLflow Models. It provides a user interface and a set of APIs to streamline model deployment processes.6 A key feature is its automatic tracking of different versions of a registered model, maintaining a history of changes and enabling easy rollback to previous iterations.6 Model aliases are a powerful capability, allowing the assignment of mutable, named references (e.g., "Champion," "Staging") to specific model versions.19 This is particularly beneficial for decoupling model deployments from inference workloads; if an alias (e.g., "Champion") is updated to reference a new model version, downstream batch inference workloads automatically pick up the new version on their next execution.19 This enables seamless, low-risk model promotions and facilitates A/B testing strategies by simply updating the alias without requiring code changes in the consuming application, thereby significantly streamlining model rollout and reducing operational friction. MLflow 3.0 (Beta) introduces the concept of Logged Models, which persist throughout a model's lifecycle and contain links to artifacts, metadata, metrics, parameters, and the code used for generation, further facilitating comparison and debugging.6

#### **Registering ML Models to Unity Catalog**

Databricks provides a hosted version of the MLflow Model Registry that is seamlessly integrated with Unity Catalog. This integration extends Unity Catalog's robust benefits—including centralized access control, auditing, lineage tracking, and model discovery—directly to ML models across all Databricks workspaces.6 This elevates model governance to an enterprise-grade level, ensuring that ML models are managed with the same rigor as other data assets, which is critical for compliance, debugging, and understanding the impact of data changes on model behavior.

The recommended workflow for registering models involves two main phases:

1. **Experimentation in MLflow:** Models are trained, and all relevant metrics, parameters, and artifacts are tracked using MLflow.13  
2. **Registering in Unity Catalog:** Once the optimal model is identified, it is registered in Unity Catalog. This ensures that the model's lifecycle is tightly managed, versioned, and governed. Models are registered using the three-level namespace (\<catalog\>.\<schema\>.\<model\>), which ensures consistency with other data assets and simplifies organization and discoverability.13

Models can be registered using several methods:

* **UI-based Registration:** From the MLflow Run page, accessible via the Experiments UI, users can click "Register Model," select "Unity Catalog," and then choose an existing model or create a new one.19  
* **Programmatic Registration (during run):** Within an MLflow run, mlflow.\<model-flavor\>.log\_model(registered\_model\_name="\<model-name\>") can be used. If the specified registered model does not exist, it will be automatically created.19  
* **Programmatic Registration (after run):** To register a model from a completed MLflow run, mlflow.register\_model("runs:/\<run\_id\>/\<artifact\_path\>", "\<model-name\>") is utilized.21  
* **Programmatic Creation of Registered Model:** A new registered model can be created in Unity Catalog using MlflowClient().create\_registered\_model("\<model-name\>").21

To create new registered models in Unity Catalog, specific permissions are required: USE SCHEMA and USE CATALOG privileges on the enclosing schema and catalog, respectively, along with CREATE\_MODEL or CREATE\_FUNCTION privilege on the schema.19 For creating new model versions, the user must be the owner of the registered model and possess USE SCHEMA and USE CATALOG privileges.19

For MLflow to interact correctly with Unity Catalog for model registration and loading, it is crucial to set the MLflow registry URI to mlflow.set\_registry\_uri("databricks-uc").19 This configuration step might be automatic if the workspace's default catalog is already Unity Catalog and Databricks Runtime 13.3 LTS or above is in use.19 All ML model versions registered in Unity Catalog must possess a model signature, which can be automatically inferred by Databricks autologging or by providing an input example in the mlflow.\<flavor\>.log\_model call (available in MLflow 2.5.0 and above).19

**Table 2: MLflow Model Registration Workflow to Unity Catalog**

| Workflow Step | Description | UI Action (if applicable) | Python Code Example | Key Considerations |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Train Model** | Develop and train your machine learning model. | \- | from sklearn.ensemble import RandomForestClassifier \<br\> clf \= RandomForestClassifier(...) \<br\> clf.fit(X\_train, y\_train) | Use Databricks Runtime ML for pre-configured environments. |
| **2\. Log Model** | Record model parameters, metrics, and artifacts. | MLflow UI (Experiments section) to view runs. | import mlflow.sklearn \<br\> with mlflow.start\_run(): \<br\> mlflow.sklearn.autolog() \<br\> mlflow.sklearn.log\_model(sk\_model=clf, artifact\_path="model", input\_example=X\_train.iloc\[\]) | Autologging simplifies tracking. Provide input\_example for automatic signature inference. |
| **3\. Register Model** | Promote the trained model to Unity Catalog for governance and versioning. | From MLflow Run page: Click "Register Model" \-\> Select "Unity Catalog" \-\> Choose/Create Model. | import mlflow \<br\> mlflow.set\_registry\_uri("databricks-uc") \<br\> model\_uri \= f"runs:/{run.info.run\_id}/model" \<br\> mlflow.register\_model(model\_uri, "\<catalog\_name\>.\<schema\_name\>.\<model\_name\>") | Ensure mlflow.set\_registry\_uri("databricks-uc") is set. Requires CREATE\_MODEL and USE SCHEMA/CATALOG privileges. |
| **4\. Assign Alias** | Assign a mutable, named reference to a specific model version. | On model details page in Catalog Explorer: Hover over version \-\> "Add alias". | from mlflow.tracking import MlflowClient \<br\> client \= MlflowClient() \<br\> client.set\_registered\_model\_alias(name="\<catalog\>.\<schema\>.\<model\>", alias="Champion", version=1) | Decouples deployment from specific versions, enabling A/B testing and seamless updates. |
| **5\. View & Govern** | Inspect registered models, versions, lineage, and permissions. | Catalog Explorer UI. | client.get\_registered\_model("\<catalog\>.\<schema\>.\<model\>") | Models are governed under the catalog.schema.model namespace, inheriting UC's access controls and lineage. |

## **III. Week 2: Building Interactive ML Applications with Streamlit**

The second week shifts focus to operationalizing ML models by deploying them via Databricks Model Serving and creating interactive frontends using Streamlit on Databricks Apps, with an emphasis on performance and best practices.

### **Day 8-9: Databricks Model Serving for Real-time Inference**

These days are dedicated to understanding and implementing Databricks Model Serving for deploying ML models as scalable, real-time inference endpoints.

#### **Introduction to Model Serving**

Mosaic AI Model Serving provides a unified and scalable interface for deploying, governing, and querying AI models, encompassing both custom ML models and foundation models, for real-time and batch inference.7 A key architectural characteristic is that each model deployed through Model Serving is exposed as a REST API endpoint, facilitating easy integration into various applications, including web and client applications.7

A significant advantage of Model Serving is its serverless nature. This means it automatically scales compute resources up or down based on demand, ensuring high availability and low latency while simultaneously optimizing infrastructure costs.7 This abstraction from underlying compute management allows users to concentrate on the ML problem rather than infrastructure complexities. Model Serving is deeply integrated with MLflow Model Registry and Unity Catalog, leveraging their capabilities for comprehensive model versioning, dependency management, validation, and overall governance.6 The service supports custom Python models packaged in MLflow format (e.g., scikit-learn, XGBoost, PyTorch, Hugging Face transformers) as well as various foundation models, both Databricks-hosted and external.7 This capability transforms ML models from static artifacts into consumable services, enabling broader application integration and enhancing model reusability.

#### **Deployment Workflow**

Deploying a model with Model Serving requires certain prerequisites: a registered model in Unity Catalog (or the legacy Workspace Model Registry) and MLflow version 1.29 or higher.7 The compute resource utilized for model training and registration must also have access to Unity Catalog, typically necessitating a "Dedicated" (formerly single user) access mode cluster.19 Before an organization can use Model Serving, the Databricks account administrator must review and accept the terms and conditions for enabling serverless compute in the account console.7

Endpoint creation can be performed via two primary methods:

* **Using the Serving UI:** Users navigate to "Serving" in the Databricks sidebar and click "Create serving endpoint." Configuration involves providing an endpoint name, selecting the model and a specific version from Unity Catalog (using the full catalog.schema.model name), specifying traffic percentage, compute size (CPU/GPU), and whether the endpoint should scale to zero when idle.26 The requirement to specify the full catalog.schema.model name when deploying a model to Model Serving directly links back to Unity Catalog's object model, ensuring that the same discoverability, access control, and lineage tracking applied during model registration are seamlessly extended through the deployment phase.11 This consistency reinforces the treatment of ML models as first-class, governed assets throughout their lifecycle.  
* **Programmatic Creation (REST API / MLflow Deployments SDK):** Endpoints can also be created and managed programmatically using the Databricks REST API or the MLflow Deployments SDK (mlflow.deployments.get\_deploy\_client("databricks")). This method also requires the full catalog.schema.model name for model identification.26

Querying the deployed endpoint is straightforward. The easiest and fastest way to test and send scoring requests is through the "Query endpoint" tab within the Serving UI.27 For programmatic access from external applications or notebooks, HTTP POST requests containing input data (typically in JSON format) are sent to the Model Serving endpoint's URL.27 For secure interaction, especially in production environments, machine-to-machine OAuth tokens are recommended for authentication. For development purposes, a DATABRICKS\_API\_TOKEN (such as a Personal Access Token or PAT) can be used, ideally retrieved securely from a Databricks secret scope rather than hardcoding credentials.25

**Hands-on Exercise:**

1. Select one of the ML models previously registered to Unity Catalog in Week 1\.  
2. Deploy this model as a Model Serving endpoint using the Databricks Serving UI. Configure basic settings such as the endpoint name, the model version (e.g., referencing it by an alias like "Champion"), and the desired compute size.26  
3. Once the endpoint status changes to "Ready," navigate to its details page.  
4. Utilize the "Query endpoint" tab in the UI to send sample inference requests and observe the predictions returned by the model.27  
5. Write a simple Python script in a Databricks notebook (or locally) to programmatically query the deployed Model Serving endpoint using the requests library, ensuring proper authentication handling (e.g., using a PAT for development).25

### **Day 10-11: Introduction to Streamlit on Databricks Apps**

These days introduce Databricks Apps as the native platform for hosting interactive applications and delve into the fundamentals of building user interfaces with Streamlit.

#### **Databricks Apps: Native Application Hosting**

Databricks Apps provides a native, secure, and serverless platform for building and deploying data and AI applications directly within the Databricks environment.8 This capability is instrumental in simplifying the "last mile" of MLOps by abstracting away the complexities associated with traditional web app deployment, such as managing web servers, containerization, networking, and authentication. By offering a managed, serverless environment for frameworks like Streamlit, Databricks enables practitioners to focus solely on the Python code and the ML logic, thereby accelerating the operationalization of ML models into user-facing applications.8

Databricks Apps are designed for seamless integration with core Databricks services. This includes Unity Catalog for data governance, Databricks SQL for querying data, Model Serving for deploying AI models, and Databricks Jobs for ETL and automation. Authentication and authorization are handled via OAuth and service principals.8 This tight integration transforms the interactive application into a powerful interface for end-to-end data and AI workflows, allowing for the creation of richer, more robust, and more valuable ML applications that align directly with an organization's data strategy. The platform supports popular Python frameworks such as Streamlit, Dash, and Gradio, providing developers with flexibility in their UI library choice.8 The system environment for these apps runs on Ubuntu 22.04 LTS with Python 3.11.0 in a dedicated virtual environment, with each app subject to resource limits of up to 2 virtual CPUs (vCPUs) and 6 GB of memory.8 It is important to be aware of certain limitations, including a maximum of 50 apps per workspace, a 10 MB file size limit for app files, and the deletion of app logs upon compute resource termination.8

#### **Streamlit Fundamentals: Building Interactive UIs**

Streamlit is an open-source Python framework that enables data scientists and ML engineers to rapidly build and deploy interactive web applications with minimal code, emphasizing simplicity and quick prototyping.14 Its declarative syntax facilitates the easy creation of interactive elements like sliders, buttons, and text inputs with just a few lines of code.14

Key components of Streamlit include:

* st.sidebar: Used for organizing input elements and widgets, keeping the main app interface clean.14  
* st.write(): A versatile function for displaying text, data, and visualizations.14  
* Widgets: Functions like st.text\_input(), st.button(), st.slider(), st.selectbox(), and st.multiselect() enable user interaction with the application.14  
* st.session\_state: A crucial feature for maintaining context and conversation history across app reruns, particularly important in interactive chat applications.30 Streamlit's design also ensures real-time updates to the app when the underlying code or data changes, providing a dynamic and responsive user experience.14

#### **Local Development and Deployment using Databricks Asset Bundles (DABs)**

Developers can build and test their Streamlit applications locally using any Python integrated development environment (IDE), with Visual Studio Code and the Databricks extension being a recommended setup.31 The databricks apps run-local command facilitates local launching and debugging of the application.32

The app.yaml configuration file is essential for defining how the app runs, including the command to execute (e.g., command: \['streamlit', 'run', 'app.py'\]), environment variables, and required resources.31 All necessary Python packages must be listed in a requirements.txt file, which Databricks Apps automatically installs within a dedicated virtual environment.8

Databricks Asset Bundles (DABs) represent the recommended method for packaging and deploying Databricks Apps to a workspace. The process involves initializing a bundle (databricks bundle init), defining app resources in a databricks.yml file, and then using databricks bundle deploy to deploy the application.32 Databricks Apps automatically sets several environment variables (e.g., DATABRICKS\_APP\_NAME, DATABRICKS\_HOST, DATABRICKS\_APP\_PORT, DATABRICKS\_CLIENT\_ID, DATABRICKS\_CLIENT\_SECRET) and pre-configures Streamlit-specific variables (e.g., STREAMLIT\_SERVER\_ADDRESS, STREAMLIT\_SERVER\_PORT).35

**Hands-on Exercise:**

1. Initialize a new Databricks Asset Bundle project with a Streamlit app template using the command: databricks bundle init https://github.com/databricks/bundle-examples \--template-dir contrib/templates/streamlit-app.32  
2. Explore the generated app.py (the main Streamlit script), app.yaml (app configuration), and requirements.txt (dependencies).  
3. Modify app.py to create a simple interactive Streamlit UI, such as a text input field and a button that displays the input text.  
4. Deploy the app to your Databricks workspace using databricks bundle deploy.32  
5. Access the deployed app via the endpoint URL provided in the bundle summary output.32

### **Day 12-13: Connecting Streamlit to ML Models & Performance Optimization**

These days focus on the practical integration of Streamlit applications with ML models on Databricks, emphasizing the best practices for performance and user experience.

#### **Interacting with Specific ML Models from Streamlit**

Two primary methods exist for a Streamlit application to interact with an ML model:

* Loading Models Directly from Unity Catalog (for specific use cases):  
  A model version can be directly loaded from Unity Catalog into the Streamlit app's environment using mlflow.pyfunc.load\_model() or mlflow.\<flavor\>.load\_model().19 Models can be referenced either by their alias (e.g., models:/\<catalog\_name\>.\<schema\_name\>.\<model\_name\>@\<alias\_name\>) for dynamic updates, or by their specific version number (e.g., models:/\<catalog\_name\>.\<schema\_name\>.\<model\_name\>/\<version\_number\>).19 To enable this, the Streamlit app's service principal (or the user running it) requires EXECUTE privilege on the registered model, along with USE SCHEMA and USE CATALOG privileges on the containing schema and catalog.19 However, it is important to note that direct model loading within a Streamlit app's limited compute resources (2 vCPUs, 6 GB memory) 8 can be inefficient for large models or high concurrency, potentially leading to cold-start issues if the model is not properly cached.39 This approach is generally more suitable for prototyping or very low-traffic internal tools where latency is less critical.  
* Calling Model Serving Endpoints from Streamlit (Recommended for Production):  
  The most robust and scalable method for a Streamlit app to interact with an ML model is by calling a deployed Model Serving endpoint via its REST API.7 This is implemented using Python's requests library to send HTTP POST requests containing input data (typically in JSON format) to the Model Serving endpoint's URL.27 For secure interaction, especially in production environments, machine-to-machine OAuth tokens are recommended. For development, a Personal Access Token (PAT) can be retrieved securely from a Databricks secret scope to avoid hardcoding credentials.25 This approach offloads the heavy inference computation to the dedicated, scalable, and serverless Model Serving infrastructure.7 This ensures low latency, high availability, and efficient resource utilization, aligning with Databricks' best practices for AI inference workloads.39 The choice between direct model loading and Model Serving in Streamlit represents a trade-off between simplicity/cost for prototyping and scalability/performance for production. While direct loading might seem simpler initially, the limitations of Databricks App compute make Model Serving the clear path for production-grade applications, emphasizing a clear architectural pattern: Streamlit for the UI, Model Serving for the heavy inference lifting, and Unity Catalog for governance.

#### **Best Practices for Streamlit Performance on Databricks**

Optimizing performance and user experience in Streamlit applications running on Databricks is crucial for effective MLOps.

* **Caching for Efficiency:**  
  * @st.cache\_data: This decorator is used for functions that return data, such as results from external APIs, database queries, or the output of ML inference for a given input. It caches results, preventing redundant computations and API calls, which significantly speeds up response times and can reduce costs.30  
  * @st.cache\_resource: This is essential for caching computationally expensive global resources that should be loaded only once and shared across all users and sessions, such as ML models themselves or database connections. This dramatically improves the app's responsiveness by avoiding repeated loading of large objects.30  
* **Asynchronous Operations for Responsiveness:**  
  * **Non-Blocking Calls:** Long-running operations, such as network calls to a Model Serving endpoint, can cause the Streamlit UI to freeze. Python's asyncio library with async/await syntax should be used to make these I/O operations non-blocking, ensuring a smooth user experience.30 API call functions should be defined with async def, using await with asynchronous clients.  
  * **User Feedback:** Providing visual feedback during lengthy tasks is vital. Streamlit offers elements like st.spinner("Thinking..."), st.progress(0), st.status("Working on it..."), or st.toast("Done\!").30  
  * **Stream Responses:** For generative AI models or other models producing incremental output, st.write\_stream() can display the response as it's generated, making the app feel significantly faster.30 Caching and asynchronous operations are not merely performance optimizations; they are fundamental for delivering a positive user experience in interactive ML applications. They address the inherent challenges of computationally intensive ML inference and network latency, ensuring the app feels fast, smooth, and usable, which directly impacts user adoption and satisfaction.  
* **Minimize Container Startup Time:** The app's initialization logic should be kept lightweight. Heavy resources, such as large models, should only be loaded when actually needed, ideally using @st.cache\_resource, to reduce cold-start latency.39  
* **Leverage Databricks-Native Features:** It is important to remember that app compute is optimized for UI rendering. For heavy data processing, Databricks SQL should be used, and for AI inference, Model Serving is the recommended service.39  
* **Pin Dependency Versions:** Always specify exact version numbers in the requirements.txt file to ensure consistent and reproducible environments across builds.39

**Table 3: Loading Models from Unity Catalog for Inference**

| Method | URI/Endpoint Format | Python Code Snippet | Permissions Required | Use Case/Considerations |
| :---- | :---- | :---- | :---- | :---- |
| **Direct Load from UC** | models:/\<catalog\>.\<schema\>.\<model\>@\<alias\> \<br\> OR \<br\> models:/\<catalog\>.\<schema\>.\<model\>/\<version\> | import mlflow.pyfunc \<br\> mlflow.set\_registry\_uri("databricks-uc") \<br\> model \= mlflow.pyfunc.load\_model(model\_uri) \<br\> prediction \= model.predict(input\_data) | EXECUTE on model, USE SCHEMA, USE CATALOG | Prototyping, small models, low-traffic internal tools. Limited by Databricks App compute resources (2 vCPUs, 6 GB memory). |
| **Call Model Serving Endpoint** | https://\<workspace-url\>/serving-endpoints/\<endpoint-name\>/invocations | import requests \<br\> headers \= {"Authorization": f"Bearer {DATABRICKS\_TOKEN}"} \<br\> response \= requests.post(endpoint\_url, headers=headers, json={"inputs": input\_data.tolist()}) \<br\> prediction \= response.json() | CAN USE on Model Serving endpoint (configured via UI/API). | Production, large models, high concurrency, real-time inference. Leverages scalable, serverless compute. Recommended for robust applications. |

**Table 4: Streamlit Performance Best Practices on Databricks**

| Best Practice | Description | Streamlit/Databricks Feature/Technique | Impact on Performance/User Experience |
| :---- | :---- | :---- | :---- |
| **Caching Data** | Store results of expensive data operations. | @st.cache\_data decorator for functions returning data (e.g., query results, inference outputs). | Reduces redundant computations/API calls, speeds up response times, saves costs. |
| **Caching Resources** | Store large, global objects like ML models or database connections. | @st.cache\_resource decorator for functions returning non-serializable resources. | Prevents repeated loading of heavy objects, dramatically improves app responsiveness during reruns. |
| **Asynchronous Operations** | Handle long-running I/O operations without freezing the UI. | asyncio with async/await for API calls; st.spinner, st.progress, st.status, st.toast for feedback. | Maintains UI responsiveness during long waits, provides smooth user experience. |
| **Offloading Compute** | Delegate heavy computational tasks to dedicated services. | Use Databricks SQL for data queries, Model Serving for AI inference. | Optimizes app compute for UI rendering, ensures scalable and low-latency inference. |
| **Minimize Startup Time** | Keep initial app logic lean. | Load heavy resources on demand, use @st.cache\_resource for models. | Reduces cold-start latency, improves initial user loading experience. |
| **Pin Dependencies** | Specify exact versions of Python packages. | requirements.txt with pinned versions (e.g., pandas==1.5.3). | Ensures consistent and reproducible app environments, prevents unexpected dependency conflicts. |

## **Day 14: Review, Advanced Topics & Next Steps**

The final day of this learning path is dedicated to consolidating the acquired knowledge, exploring advanced MLOps topics, and identifying resources for continuous learning and career development within the Databricks ecosystem.

### **Consolidation of Key Concepts and Practical Application**

A central theme throughout this learning path is the unified MLOps lifecycle enabled by Databricks. This involves the seamless synergy between Unity Catalog, which provides centralized data and AI governance; MLflow, which offers comprehensive ML lifecycle management from experiment tracking to model registry; Model Serving, which facilitates scalable, real-time model deployment; and Databricks Apps, which enable interactive, user-friendly frontends for ML models.

The catalog.schema.model namespace is a consistent governance and access control mechanism that extends across all stages of the ML lifecycle, from initial data ingestion and preparation to model registration and deployment.11 This consistent naming and permission structure simplifies management and auditing across the entire data and AI landscape.

Furthermore, the emphasis on performance and scalability in interactive Streamlit applications on Databricks is critical. This includes the strategic use of Model Serving for efficient inference and Streamlit's built-in caching mechanisms (st.cache\_data, st.cache\_resource) and asynchronous operations (asyncio) to ensure optimal user experience.30 These practices are not merely technical optimizations but are fundamental to creating responsive and engaging ML applications that deliver real business value.

### **Brief Overview of Advanced MLOps Topics**

Beyond the core learning path, several advanced MLOps topics are crucial for building mature and robust ML systems on Databricks:

* **CI/CD for Databricks Apps and ML Workflows:** Databricks Asset Bundles (DABs), which are used for deploying Streamlit applications, also provide robust support for Continuous Integration/Continuous Delivery (CI/CD) pipelines.32 This enables automated testing, deployment, and version control for both ML models and their associated applications, ensuring reliable and repeatable deployments across different environments.  
* **Model Monitoring and Observability:** Databricks Lakehouse monitoring capabilities extend to tracking the performance and data quality of tables, as well as the performance of machine learning models and model-serving endpoints.2 MLflow tracking, particularly with MLflow Tracing, captures detailed execution information for AI agents and models, significantly enhancing generative AI observability.6 These monitoring tools are essential for detecting issues such as model drift, performance degradation, and data quality anomalies in production environments.  
* **A/B Testing and Canary Deployments:** The ability of Model Serving to route traffic to different served model versions 26, combined with MLflow Model Aliases 19, facilitates advanced deployment strategies like A/B testing and canary deployments. These techniques allow for controlled rollout of new model versions and enable performance comparisons in real-world scenarios, minimizing risk during production updates.  
* **Feature Store:** Databricks provides a Feature Store designed to simplify the discovery, reuse, and governance of machine learning features. It automates feature lookups and helps reduce common errors in ML pipelines, promoting consistency and reusability of features across different models.6

### **Relevant Databricks Certifications for Continued Learning**

For practitioners seeking to validate and deepen their expertise, Databricks offers several certifications directly relevant to the learning path:

* **Databricks Certified Machine Learning Associate:** This certification is designed for data scientists and ML practitioners. It assesses the ability to leverage Databricks Machine Learning and AutoML tools, utilize Feature Store and Spark ML, track experiments with MLflow, and scale ML models within the Databricks ecosystem. The certification specifically covers MLflow and Unity Catalog for comprehensive model packaging and governance, aligning directly with the core objectives of this learning path.34  
* **Databricks Certified Generative AI Engineer Associate:** This newer certification focuses on the practical aspects of building and deploying Large Language Model (LLM)-based solutions. It evaluates skills in designing Retrieval-Augmented Generation (RAG) pipelines, selecting and utilizing generative AI models, implementing semantic search with Vector Search, managing solutions with MLflow, deploying with Model Serving, and applying data governance using Unity Catalog.42 This certification is highly relevant for individuals interested in the rapidly evolving field of Generative AI.  
* **Databricks Certified Data Engineer Associate:** While not exclusively focused on machine learning, this certification covers foundational skills essential for any MLOps professional. It assesses the ability to build ETL pipelines, handle batch and streaming data, and manage data governance with Unity Catalog.42 A strong data engineering foundation is invaluable for ensuring robust and reliable data pipelines that feed ML models.

### **Resources for Continued Learning and Community Engagement**

Continuous learning is vital in the rapidly evolving field of data and AI. Practitioners are encouraged to leverage the following resources:

* **Official Documentation:** Regular consultation of the comprehensive Databricks documentation 17, MLflow documentation 5, and Streamlit documentation 29 is recommended for accessing the latest features, best practices, and troubleshooting guides.  
* **Databricks Academy:** The Databricks Academy and Training Catalog offer a wealth of self-paced courses and structured learning pathways to deepen platform knowledge and MLOps skills.34  
* **Community Forums:** Engaging with the Databricks Community Forum provides an avenue to ask questions, share insights, and learn from the experiences of other practitioners.28  
* **GitHub Examples:** Exploring official Databricks and MLflow GitHub repositories for sample code and practical examples can provide hands-on learning opportunities and inspiration for new projects.

## **Conclusions and Recommendations**

This 2-week learning outline provides a structured approach to mastering key Databricks capabilities for ML model governance and interactive application development. The Databricks Lakehouse Platform, with its integrated components like Unity Catalog, MLflow, and Model Serving, is architected to provide an end-to-end MLOps solution. The platform's emphasis on unified governance through Unity Catalog for all data and AI assets, including ML models, addresses critical enterprise needs for security, compliance, and discoverability. The strategic use of serverless compute for Model Serving and Databricks Apps further enhances scalability and cost-efficiency, abstracting away infrastructure complexities and accelerating the operationalization of ML.

For practitioners, the ability to leverage MLflow's experiment tracking and model registry, coupled with Unity Catalog's robust governance, ensures that ML models are managed as first-class, versioned, and auditable assets. The deployment of models as scalable REST API endpoints via Model Serving enables seamless integration into diverse applications. Furthermore, the development of interactive Streamlit applications on Databricks Apps provides a powerful means to democratize access to ML insights, bridging the gap between technical development and business users.

To maximize the learning experience and build production-ready systems, it is recommended that learners:

1. **Prioritize Hands-on Practice:** Actively engage with the provided exercises, replicating and extending them within a Databricks workspace.  
2. **Embrace Best Practices:** Consistently apply performance optimization techniques for Streamlit applications, particularly caching and asynchronous operations, and always leverage Model Serving for production-grade ML inference.  
3. **Understand the Ecosystem:** Recognize that individual Databricks components are most powerful when used in concert, forming a cohesive MLOps lifecycle.  
4. **Pursue Certifications:** Consider Databricks certifications, such as the Machine Learning Associate or Generative AI Engineer Associate, to validate skills and demonstrate proficiency in the platform.  
5. **Engage with the Community:** Actively participate in Databricks forums and explore official documentation and GitHub resources for continuous learning and problem-solving.

By following this comprehensive learning path, individuals can gain the expertise required to build, govern, and deploy sophisticated machine learning solutions on the Databricks Lakehouse Platform, contributing significantly to data-driven innovation within their organizations.

#### **Works cited**

1. What is a data lakehouse? \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/lakehouse/](https://docs.databricks.com/aws/en/lakehouse/)  
2. Lakehouse reference architectures (download) \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/lakehouse-architecture/reference](https://docs.databricks.com/aws/en/lakehouse-architecture/reference)  
3. Mastering Data Governance with Databricks Unity Catalog \- Valanor, accessed June 5, 2025, [https://valanor.co/data-governance-with-databricks-unity-catalog/](https://valanor.co/data-governance-with-databricks-unity-catalog/)  
4. Databricks components | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/getting-started/concepts](https://docs.databricks.com/aws/en/getting-started/concepts)  
5. MLflow: A Tool for Managing the Machine Learning Lifecycle, accessed June 5, 2025, [https://mlflow.org/docs/2.21.3/](https://mlflow.org/docs/2.21.3/)  
6. MLflow for gen AI agent and ML model lifecycle | Databricks ..., accessed June 5, 2025, [https://docs.databricks.com/aws/en/mlflow/](https://docs.databricks.com/aws/en/mlflow/)  
7. Deploy models using Mosaic AI Model Serving \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/machine-learning/model-serving/](https://docs.databricks.com/aws/en/machine-learning/model-serving/)  
8. Databricks Apps | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/dev-tools/databricks-apps/](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/)  
9. Databricks Apps \- Azure Databricks | Microsoft Learn, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/)  
10. Data governance with Unity Catalog | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/data-governance/](https://docs.databricks.com/aws/en/data-governance/)  
11. What is Unity Catalog? \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/data-governance/unity-catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog)  
12. Databricks Unity Catalog 101: A Complete Overview (2025) \- Chaos Genius, accessed June 5, 2025, [https://www.chaosgenius.io/blog/databricks-unity-catalog/](https://www.chaosgenius.io/blog/databricks-unity-catalog/)  
13. Building an ML and AI Data Catalog with Unity Catalog and MLflow, accessed June 5, 2025, [https://www.unitycatalog.io/blogs/machine-learning-data-catalog](https://www.unitycatalog.io/blogs/machine-learning-data-catalog)  
14. Building Interactive AI Applications with Streamlit: Technical Insights and Best Practices, accessed June 5, 2025, [https://www.kubernet.dev/building-interactive-ai-applications-with-streamlit-technical-insights-and-best-practices/](https://www.kubernet.dev/building-interactive-ai-applications-with-streamlit-technical-insights-and-best-practices/)  
15. Build a ML Web App with Streamlit and Pipelines \- Artur Lunardi, accessed June 5, 2025, [https://arturlunardi.com/en/build-a-ml-web-app-with-streamlit-and-pipelines/](https://arturlunardi.com/en/build-a-ml-web-app-with-streamlit-and-pipelines/)  
16. 4\. Unity Catalog and Compute \- Data Governance with Unity Catalog on Databricks \[Book\], accessed June 5, 2025, [https://www.oreilly.com/library/view/data-governance-with/9781098179625/ch04.html](https://www.oreilly.com/library/view/data-governance-with/9781098179625/ch04.html)  
17. Databricks documentation | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/](https://docs.databricks.com/aws/en/)  
18. Track model development using MLflow \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/mlflow/tracking](https://docs.databricks.com/aws/en/mlflow/tracking)  
19. Manage model lifecycle in Unity Catalog | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle)  
20. Customizing a Model's predict method \- MLflow, accessed June 5, 2025, [https://mlflow.org/docs/latest/traditional-ml/creating-custom-pyfunc/notebooks/override-predict](https://mlflow.org/docs/latest/traditional-ml/creating-custom-pyfunc/notebooks/override-predict)  
21. Manage model lifecycle using the Workspace Model Registry (legacy), accessed June 5, 2025, [https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry)  
22. MLflow Model Registry, accessed June 5, 2025, [https://mlflow.org/docs/latest/model-registry](https://mlflow.org/docs/latest/model-registry)  
23. w.registered\_models: Registered Models — Databricks SDK for Python beta documentation, accessed June 5, 2025, [https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/registered\_models.html](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/registered_models.html)  
24. Manage model lifecycle in Unity Catalog \- Azure Databricks | Microsoft Learn, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/machine-learning/manage-model-lifecycle/](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/manage-model-lifecycle/)  
25. From Zero to GenAI Hero: Building Your GenAI App with HuggingFace and Databricks, accessed June 5, 2025, [https://www.databricks.com/blog/zero-genai-hero-building-your-genai-app-huggingface-and-databricks](https://www.databricks.com/blog/zero-genai-hero-building-your-genai-app-huggingface-and-databricks)  
26. Create custom model serving endpoints \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)  
27. Tutorial: Deploy and query a custom model \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro)  
28. Streamlit Databricks App Compute Scaling, accessed June 5, 2025, [https://community.databricks.com/t5/data-engineering/streamlit-databricks-app-compute-scaling/td-p/110676](https://community.databricks.com/t5/data-engineering/streamlit-databricks-app-compute-scaling/td-p/110676)  
29. Streamlit documentation, accessed June 5, 2025, [https://docs.streamlit.io/](https://docs.streamlit.io/)  
30. Best Practices for Building GenAI Apps with Streamlit \- Streamlit Blog, accessed June 5, 2025, [https://blog.streamlit.io/best-practices-for-building-genai-apps-with-streamlit/](https://blog.streamlit.io/best-practices-for-building-genai-apps-with-streamlit/)  
31. Develop Databricks apps, accessed June 5, 2025, [https://docs.databricks.com/aws/en/dev-tools/databricks-apps/app-development](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/app-development)  
32. Manage Databricks apps using Databricks Asset Bundles \- Learn Microsoft, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/apps-tutorial](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/apps-tutorial)  
33. Key concepts in Databricks Apps, accessed June 5, 2025, [https://docs.databricks.com/aws/en/dev-tools/databricks-apps/key-concepts](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/key-concepts)  
34. Trainings Catalog \- Databricks, accessed June 5, 2025, [https://www.databricks.com/training/catalog](https://www.databricks.com/training/catalog)  
35. Define environment variables in a Databricks app \- Learn Microsoft, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/environment-variables](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/environment-variables)  
36. Define environment variables in a Databricks app, accessed June 5, 2025, [https://docs.databricks.com/aws/en/dev-tools/databricks-apps/environment-variables](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/environment-variables)  
37. Log, load, and register MLflow models \- Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/mlflow/models](https://docs.databricks.com/aws/en/mlflow/models)  
38. Log, load, and register MLflow models \- Azure Databricks | Microsoft Learn, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/mlflow/models](https://learn.microsoft.com/en-us/azure/databricks/mlflow/models)  
39. Best practices for Databricks Apps | Databricks Documentation, accessed June 5, 2025, [https://docs.databricks.com/aws/en/dev-tools/databricks-apps/best-practices](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/best-practices)  
40. Best practices for Databricks Apps \- Azure Databricks | Microsoft Learn, accessed June 5, 2025, [https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/best-practices](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/best-practices)  
41. Caching overview \- Streamlit Docs, accessed June 5, 2025, [https://docs.streamlit.io/develop/concepts/architecture/caching](https://docs.streamlit.io/develop/concepts/architecture/caching)  
42. Databricks Certifications in 2025 to Enhance AI/ML and Data Analysis Skills : r/ExamRanch, accessed June 5, 2025, [https://www.reddit.com/r/ExamRanch/comments/1kxdmnx/databricks\_certifications\_in\_2025\_to\_enhance\_aiml/](https://www.reddit.com/r/ExamRanch/comments/1kxdmnx/databricks_certifications_in_2025_to_enhance_aiml/)  
43. What Are the Key ML Models in Databricks AI Certification? \- Whizlabs, accessed June 5, 2025, [https://www.whizlabs.com/blog/key-ml-models-in-databricks-ai-certification/](https://www.whizlabs.com/blog/key-ml-models-in-databricks-ai-certification/)  
44. Solved: Databricks data engineer associate exam, accessed June 5, 2025, [https://community.databricks.com/t5/data-engineering/databricks-data-engineer-associate-exam/td-p/115283](https://community.databricks.com/t5/data-engineering/databricks-data-engineer-associate-exam/td-p/115283)  
45. Topic for Databricks data engineer Associate certification course, accessed June 5, 2025, [https://community.databricks.com/t5/databricks-academy-learners/topic-for-databricks-data-engineer-associate-certification/td-p/113015](https://community.databricks.com/t5/databricks-academy-learners/topic-for-databricks-data-engineer-associate-certification/td-p/113015)  
46. Databricks Certification, accessed June 5, 2025, [https://www.databricks.com/learn/training/certification](https://www.databricks.com/learn/training/certification)  
47. Databricks and streamlit and fast API combination, accessed June 5, 2025, [https://community.databricks.com/t5/get-started-discussions/databricks-and-streamlit-and-fast-api-combination/td-p/63992](https://community.databricks.com/t5/get-started-discussions/databricks-and-streamlit-and-fast-api-combination/td-p/63992)  
48. Databricks Apps \- Streamlit Performance Hangups, accessed June 5, 2025, [https://community.databricks.com/t5/data-engineering/databricks-apps-streamlit-performance-hangups/td-p/110264](https://community.databricks.com/t5/data-engineering/databricks-apps-streamlit-performance-hangups/td-p/110264)
</td></tr></table>
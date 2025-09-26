# Microsoft Planner

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
is there a programmatic way to create multiple planner tasks based on a list of task template?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, you can programmatically create multiple Microsoft Planner tasks based on a list of task templates using the **Microsoft Graph API**. Here's a high-level overview of how you can do it:

* * * *

### ✅ Prerequisites

1.  **Microsoft 365 account** with access to Planner.
2.  **Azure AD App Registration** with appropriate permissions:
    -   `Group.ReadWrite.All`
    -   `Tasks.ReadWrite`
    -   `Planner.ReadWrite`
3.  **Access token** for Microsoft Graph API.

* * * *

### 🧩 Task Template Format

You can define your task templates in a structured format like JSON:

\[
  {
    "title": "Design Review",
    "bucketId": "bucket-id-1",
    "assignments": { "user-id": { "@odata.type": "microsoft.graph.plannerAssignment" } },
    "dueDateTime": "2025-08-30T17:00:00Z"
  },
  {
    "title": "Code Implementation",
    "bucketId": "bucket-id-2",
    "assignments": { "user-id": { "@odata.type": "microsoft.graph.plannerAssignment" } },
    "dueDateTime": "2025-09-05T17:00:00Z"
  }
\]

* * * *

### 🛠️ API Endpoint to Create Tasks

Use the following endpoint:

```
POST https://graph.microsoft.com/v1.0/planner/tasks

```

With a request body like:

{
  "planId": "your-plan-id",
  "bucketId": "bucket-id",
  "title": "Task Title",
  "assignments": {
    "user-id": {
      "@odata.type": "microsoft.graph.plannerAssignment"
    }
  },
  "dueDateTime": "2025-08-30T17:00:00Z"
}

* * * *

### 🧪 Automation Options

You can automate this using:

-   **Power Automate** (with HTTP actions)
-   **Python** (using `requests` and Microsoft Graph SDK)
-   **Node.js** or other backend frameworks

Would you like a sample Python script to create tasks from a JSON template? Or are you using Power Automate or another platform for automation?
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
If we don't have access to Graph API and don't have client_id and client_secret, are there alternatives?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
If you don't have access to the Microsoft Graph API (i.e., no `client_id`, `client_secret`, or app registration), there are still a few alternative approaches you can consider to create multiple Planner tasks programmatically or semi-automatically:

* * * *

### 🟡 Option 1: **Power Automate (No Code / Low Code)**

Power Automate allows you to create Planner tasks using built-in connectors **without needing Graph API credentials**.

#### How to do it:

1.  Create a **Power Automate flow**.
2.  Use a **trigger** like:
    -   Manual button
    -   Excel file update
    -   SharePoint list item creation
3.  Add an action: **"Create a task" in Planner**.
4.  Loop through a list of task templates (e.g., from Excel or SharePoint).
5.  Create tasks dynamically using the data.

✅ **Pros**: No coding required, easy to maintain
❌ **Cons**: Limited flexibility compared to Graph API

* * * *

### 🟡 Option 2: **Excel + Power Automate**

You can store your task templates in an Excel file and use Power Automate to read each row and create a Planner task.

#### Example columns:

-   Task Title
-   Bucket Name or ID
-   Assigned To (email)
-   Due Date

* * * *

### 🟡 Option 3: **Microsoft Teams + Planner Integration**

If you're working within Teams, you can use **Planner tabs** and manually duplicate tasks or use templates within the UI. This is not programmatic but can be semi-automated with copy-paste or cloning.

* * * *

### 🟡 Option 4: **Third-party Tools**

Some third-party automation platforms (like Zapier or Make.com) offer Planner integrations, though they may still require some form of authentication.

* * * *

Would you like help setting up a Power Automate flow using Excel or SharePoint as the source of your task templates? I can walk you through the steps or generate a sample template for you.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Yes, guide me through Power Automate setup.
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->Great! Let's walk through how to set up a **Power Automate flow** that reads task templates from an Excel file and creates Planner tasks automatically.

* * * *

🧭 Step-by-Step Guide: Power Automate + Excel → Planner Tasks
-------------------------------------------------------------

### 🔹 Step 1: Prepare Your Excel File

Create an Excel file with a table that includes your task templates. Example structure:

| Title | Bucket ID | Assigned To Email | Due Date |
| --- |  --- |  --- |  --- |
| Design Review | bucket-id-1 | user1@company.com | 2025-08-30 |
| --- |  --- |  --- |  --- |
| Code Implementation | bucket-id-2 | user2@company.com | 2025-09-05 |

-   Make sure the data is formatted as a **table** in Excel (`Insert > Table`).
-   Upload the file to **OneDrive for Business** or **SharePoint**.

* * * *

### 🔹 Step 2: Create a New Flow in Power Automate

1.  Go to Power Automate.
2.  Click **Create** > **Automated cloud flow** or **Instant cloud flow** (for manual trigger).
3.  Choose a trigger:
    -   **Manual trigger** (e.g., button press)
    -   **Scheduled trigger** (e.g., run daily)
    -   **When a file is modified** (optional)

* * * *

### 🔹 Step 3: Add Excel Action

1.  Add **"List rows present in a table"** (Excel Online (Business)).
2.  Choose your Excel file and table.

* * * *

### 🔹 Step 4: Add a Loop to Process Each Row

1.  Add a **"Apply to each"** loop.
2.  Use the output from the Excel step as the input.

* * * *

### 🔹 Step 5: Add "Create a task" Action (Planner)

Inside the loop:

1.  Add **"Create a task"** (Planner).
2.  Fill in:
    -   **Plan ID**: Select your Planner plan.
    -   **Bucket ID**: Use `Bucket ID` from Excel row.
    -   **Title**: Use `Title` from Excel row.
    -   **Assigned To**: Use `Assigned To Email` (you may need to resolve this to a user ID).
    -   **Due Date**: Use `Due Date` from Excel row.

* * * *

### 🔹 Optional: Assign Users

To assign users, you may need to use **"Get user profile (V2)"** (Microsoft 365 Users) to resolve email to user ID.

* * * *

### 🔹 Step 6: Save and Test

-   Save your flow.
-   Run it manually or wait for the trigger.
-   Check Planner to confirm tasks are created.

* * * *

Would you like a sample Excel template or a visual diagram of the flow? I can also help you build the flow step-by-step if you tell me which trigger you'd prefer (manual, scheduled, or file-based).

</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
help me build the flow step-by-step trigger by file-based
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Perfect! Let's build a **Power Automate flow** that triggers when an Excel file is updated in **OneDrive for Business** or **SharePoint**, and then creates tasks in **Microsoft Planner** based on the rows in that file.

* * * *

🧱 What You'll Need
-------------------

-   An Excel file stored in **OneDrive for Business** or **SharePoint**.
-   A Planner plan already created.
-   The Excel file must have a **table** with columns like:
    -   `Title`
    -   `Bucket ID`
    -   `Assigned To Email`
    -   `Due Date`

* * * *

🛠 Step-by-Step Setup
---------------------

### 🔹 Step 1: Prepare Your Excel File

1.  Open Excel.
2.  Create a table with headers:

```
   Title | Bucket ID | Assigned To Email | Due Date

```

3.  Format it as a **table** (`Insert > Table`).
4.  Save it to **OneDrive for Business** or a **SharePoint Document Library**.

* * * *

### 🔹 Step 2: Create the Flow in Power Automate

1.  Go to Power Automate.
2.  Click **Create** > **Automated cloud flow**.
3.  Name your flow: e.g., `Create Planner Tasks from Excel`.
4.  Choose the trigger:
    -   **"When a file is created or modified (properties only)"** (OneDrive for Business or SharePoint).
    -   Select the folder where your Excel file is stored.

* * * *

### 🔹 Step 3: Get File Content

1.  Add a new step: **"Get file content"**.
2.  Use the **Identifier** from the trigger step to get the actual file content.

* * * *

### 🔹 Step 4: List Rows in Excel Table

1.  Add **"List rows present in a table"** (Excel Online (Business)).
2.  Choose:
    -   **Location**: OneDrive or SharePoint
    -   **Document Library**: Where the file is stored
    -   **File**: Use dynamic content from the previous step
    -   **Table**: Select your table name

* * * *

### 🔹 Step 5: Loop Through Each Row

1.  Add **"Apply to each"**.
2.  Use the output from the Excel step (`value`).

* * * *

### 🔹 Step 6: (Optional) Get User ID from Email

1.  Inside the loop, add **"Get user profile (V2)"** (Microsoft 365 Users).
2.  Use the `Assigned To Email` from Excel.

* * * *

### 🔹 Step 7: Create Planner Task

1.  Inside the same loop, add **"Create a task"** (Planner).
2.  Fill in:
    -   **Plan ID**: Your Planner plan
    -   **Bucket ID**: From Excel row
    -   **Title**: From Excel row
    -   **Due Date**: From Excel row
    -   **Assignments**: Use the user ID from the previous step

* * * *

### 🔹 Step 8: Save and Test

1.  Save the flow.
2.  Modify the Excel file (e.g., add a new row).
3.  Wait for the flow to trigger and check Planner.

* * * *

Would you like a **sample Excel file** and a **visual diagram** of this flow? I can generate both for you.
</td></tr>
</table>
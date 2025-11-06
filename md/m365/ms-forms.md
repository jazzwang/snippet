# Microsoft Forms

## 2025-09-11

- By Microsoft 365 Copilot (GPT-4)

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Is there a way to convert a CSV file with 6 columns ("question", "option 1", "option 2", "option 3", "option 4", "answer") into a Microsoft Form Quiz?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, you **can** convert a CSV file with columns like `"question", "option 1", "option 2", "option 3", "option 4", "answer"` into a **Microsoft Forms Quiz**, but **Microsoft Forms does not natively support importing quizzes from CSV files**. However, there are a few workarounds:

* * * *

#### ✅ **Option 1: Use Power Automate + Microsoft Forms API**

You can automate the creation of quiz questions using:

-   **Power Automate (Flow)**
-   **Microsoft Graph API** (to interact with Forms)

This method requires:

-   Access to Microsoft 365
-   Some scripting knowledge (PowerShell or Graph API)
-   Admin permissions (for API access)

* * * *

#### ✅ **Option 2: Use a Third-Party Tool or Script**

You can write a script (e.g., in Python or PowerShell) that:

1.  Reads the CSV file.
2.  Uses the Microsoft Graph API to create a Form and add questions.

Would you like me to generate a Python script that reads your CSV and prepares the data for Microsoft Forms via API?

* * * *

#### ✅ **Option 3: Manual Import via Google Forms (then convert)**

1.  Use a Google Forms add-on like **Form Builder** or **Quizzes from Sheets** to import from CSV.
2.  Manually recreate the quiz in Microsoft Forms.

* * * *

#### 🛠 If you'd like to proceed with automation:

Please upload your CSV file, and I can:

-   Parse it
-   Show you how the questions would look
-   Help you generate a script or guide to push it to Microsoft Forms

Would you like to go ahead with that?
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
If I have 50 quiz questions in plain text, what is the recommended way to create a Microsoft Form Quiz?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
If you have **50 quiz questions in plain text**, the most efficient way to create a **Microsoft Form Quiz** depends on how much automation you're comfortable with. Here's a breakdown of the **recommended approaches**:

---

#### ✅ **Recommended Method: Use Microsoft Forms + Scripted Automation (via Graph API)**

If you're comfortable with a bit of scripting or have access to IT support, this is the best way to automate quiz creation:

##### Steps:
1. **Prepare your questions** in a structured format (CSV, JSON, or plain text with consistent formatting).
2. Use **Microsoft Graph API** to:
   - Create a new Form.
   - Add each question with multiple choices.
   - Mark the correct answer.

> This method avoids manual entry and is scalable for large quizzes.

---

#### 🧰 **Alternative: Use Power Automate (No Code Required)**
- You can use **Power Automate** to read from a SharePoint list or Excel file and create Forms.
- This is more user-friendly but may require some setup.

---

#### 📝 **Manual Method (if automation isn't an option)**
If you prefer manual entry or don't have access to automation tools:

##### Tips for Speeding Up Manual Entry:
- Use **Microsoft Forms web interface**.
- Open your questions in a split-screen view (e.g., Word or Notepad on one side, Forms on the other).
- Use **keyboard shortcuts** and copy-paste to speed up entry.
- Consider using **voice dictation** if you're comfortable with it.

---

#### 🧪 Want Help Automating?
If you share your quiz questions (in plain text or CSV), I can:
- Parse them
- Generate a preview
- Help you create a script or guide to push them into Microsoft Forms

Would you like to upload your quiz file so I can assist with automation?
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Could you give me a step-by-step instruction to create Microsoft Form Quiz based on given Excel file stored on OneDrive?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here’s a **step-by-step guide** to create a **Microsoft Form Quiz** from an Excel file stored on **OneDrive**:

---

## ✅ **Step-by-Step Instructions**

#### **Step 1: Prepare Your Excel File**
Ensure your Excel file has the following columns:
- `Question`
- `Option 1`
- `Option 2`
- `Option 3`
- `Option 4`
- `Answer` (correct option)

Save this file to your **OneDrive**.

---

#### **Step 2: Open Power Automate**
Go to Power Automate and sign in with your Microsoft 365 account.

---

#### **Step 3: Create a New Flow**
1. Click **Create** > **Automated cloud flow**.
2. Name your flow (e.g., “Create Quiz from Excel”).
3. Choose a trigger:  
   - Use **“When a file is created or modified in OneDrive”** or manually trigger it.

---

#### **Step 4: Add Excel Connector**
1. Add a new step: **“List rows present in a table”**.
2. Choose your OneDrive Excel file.
3. Make sure your Excel file has a **table** defined (Insert > Table in Excel).

---

#### **Step 5: Add Microsoft Forms Connector**
Unfortunately, **Microsoft Forms does not have a direct connector in Power Automate** to create questions. So you’ll need to use:

- **Microsoft Graph API** (advanced)
- Or manually create the Form and use Power Automate to send responses to Excel (reverse flow)

---

#### ✅ **Alternative: Use Microsoft Graph API**
If you're comfortable with scripting, you can:
1. Register an app in **Azure AD**.
2. Use **Microsoft Graph API** to:
   - Create a Form
   - Add questions
   - Set correct answers

You’ll need:
- Access token
- API calls to `https://graph.microsoft.com/v1.0/users/{user-id}/forms`

---

#### 🔄 **Workaround: Use Excel to Google Forms, then Recreate in Microsoft Forms**
1. Use Google Forms add-on like **Form Builder** to import from Excel.
2. Export the form structure.
3. Manually recreate it in Microsoft Forms.

---

#### 🧠 Want Help Automating This?
If you upload your Excel file, I can:
- Parse it
- Generate a preview of the quiz
- Help you build a script or flow to automate the creation

Would you like to upload the file now so I can assist further?
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Could you give me a step-by-step instruction to create Microsoft Form Quiz based on given Excel file stored on OneDrive using Power Automate?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here’s a **step-by-step guide** to create a **Microsoft Form Quiz** from an Excel file stored on **OneDrive**, using **Power Automate**. While Microsoft Forms doesn't have a direct connector to create questions, you can use a combination of Excel + Power Automate + Microsoft Graph API to automate the process.

---

## 🧭 **Overview**
You’ll need:
- Excel file stored in OneDrive (with a table)
- Power Automate
- Microsoft Graph API (for creating Forms and adding questions)

---

## ✅ **Step-by-Step Instructions**

#### **Step 1: Prepare Your Excel File**
1. Open your Excel file.
2. Ensure it has a table with these columns:
   - `Question`
   - `Option 1`
   - `Option 2`
   - `Option 3`
   - `Option 4`
   - `Answer`
3. Save it to **OneDrive**.

> 📌 Tip: Use Excel’s “Insert > Table” to define the table.

---

#### **Step 2: Register an App in Azure AD (for Graph API Access)**
1. Go to Azure Portal.
2. Navigate to **Azure Active Directory > App registrations**.
3. Click **New registration**.
4. Name your app (e.g., “FormsQuizCreator”).
5. Set redirect URI (can be `https://localhost` for testing).
6. After registration, note the:
   - **Application (client) ID**
   - **Directory (tenant) ID**

---

#### **Step 3: Grant API Permissions**
1. In your registered app, go to **API permissions**.
2. Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**.
3. Add:
   - `Forms.ReadWrite`
   - `User.Read`
4. Click **Grant admin consent**.

---

#### **Step 4: Create a Flow in Power Automate**
1. Go to Power Automate.
2. Click **Create > Instant cloud flow**.
3. Choose **Manually trigger a flow**.

---

#### **Step 5: Add Excel Connector**
1. Add action: **List rows present in a table**.
2. Choose **OneDrive for Business**.
3. Select your Excel file and table.

---

#### **Step 6: Add HTTP Connector to Call Microsoft Graph API**
1. Add action: **HTTP**.
2. Set method to `POST`.
3. URL:  
   ```
   https://graph.microsoft.com/v1.0/users/{user-id}/forms
   ```
4. Headers:
   ```json
   {
     "Authorization": "Bearer YOUR_ACCESS_TOKEN",
     "Content-Type": "application/json"
   }
   ```
5. Body: Construct JSON from Excel rows to create questions.

> ⚠️ You’ll need to loop through each row and format the question payload.

---

#### **Step 7: Test Your Flow**
1. Save and run the flow.
2. Check Microsoft Forms to see if the quiz is created.

---

## 🧠 Need Help with the Script or Flow?
If you upload your Excel file, I can:
- Parse it
- Generate the JSON payload for Graph API
- Help you build the Power Automate flow

Would you like to upload your Excel file now so I can assist with the automation part?
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
I don't have Graph API access. What is the best way to create Microsoft Form?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Thanks for clarifying! Since you **don’t have access to Microsoft Graph API**, the best way to create a **Microsoft Form Quiz** from an Excel file stored on OneDrive is to use a **semi-manual method** that balances efficiency and ease of use.

---

## ✅ Recommended Method: Manual Creation with Copy-Paste Support

#### 🧾 What You’ll Need:
- Your Excel file stored in OneDrive
- Microsoft Forms (https://forms.office.com)
- A browser with split-screen or dual-monitor setup (optional but helpful)

---

## 🪜 Step-by-Step Instructions

#### **Step 1: Open Your Excel File**
1. Go to OneDrive.
2. Open your Excel file in **Excel Online**.
3. Make sure your data is structured like this:

| Question | Option 1 | Option 2 | Option 3 | Option 4 | Answer |
|----------|----------|----------|----------|----------|--------|
| What is 2+2? | 3 | 4 | 5 | 6 | 4 |

---

#### **Step 2: Open Microsoft Forms**
1. Go to Microsoft Forms.
2. Click **New Quiz**.
3. Give your quiz a title (e.g., “Math Quiz”).

---

#### **Step 3: Add Questions Manually**
For each row in Excel:
1. Click **Add new > Choice**.
2. Copy the **question** from Excel and paste it into the question field.
3. Copy and paste each **option** into the choices.
4. Click the **correct answer** to mark it.
5. (Optional) Add points or feedback.

> 💡 Tip: Use keyboard shortcuts (Ctrl+C / Ctrl+V) and keep Excel and Forms side-by-side to speed up the process.

---

#### **Step 4: Preview and Share**
1. Click **Preview** to test your quiz.
2. Click **Share** to distribute it via link, email, or QR code.

---

## 🧠 Want to Speed This Up Further?

If you upload your Excel file here, I can:
- Parse it
- Generate a formatted list of questions and answers
- Provide a copy-paste-ready version for quick entry into Microsoft Forms

Would you like to upload your Excel file so I can help streamline the process?
</td></tr>
</table>

## 2025-11-05

- Goal: migrate MS Forms from one tenant to another tenants
- Reference:
  - 2019-08-17
    - Moving Forms from one O365 tenant to another, tenant to tenant migration
    - https://techcommunity.microsoft.com/discussions/microsoftforms/moving-forms-from-one-o365-tenant-to-another-tenant-to-tenant-migration/808623/replies/3677519
    - Step 1
      - ![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNjc3NTE5LTQxOTI1OGk1OEE4MTI3MjMxOUI3ODQ3?image-dimensions=401x362&revision=2)
    - Step 2
      - ![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zNjc3NTE5LTQxOTI1OWk4Q0Y5OUU0M0RBQUM4MUI4?image-dimensions=436x503&revision=2)
    - Step 3
      - go to the other tenant (best in another browser) and paste the link and save to the other tenant's MS Forms.
  - 2022-03-15
    - Migrate MS Forms Between Microsoft 365 Tenants
    - https://www.youtube.com/watch?v=E38BWMH5gLw
- Related link
  - https://learn.microsoft.com/en-us/microsoft-forms/admin-information#form-ownership-transfer

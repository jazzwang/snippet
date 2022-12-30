# github-action-lab
Testing Github Actions and build DEB/RPM packages and win64 executables

## 2022-12-12

- ( 2022-12-12 22:14:56 )
- Testing ["Manual workflow"](https://github.com/jazzwang/github-action-lab/actions/new?category=automation)
![Manual Workflow](https://user-images.githubusercontent.com/76903/207067224-e496fb79-49a4-4908-aa29-6a13638050c3.png)
- ( 2022-12-12 22:19:39 )
- Testing ["Build projects with Make"](https://github.com/jazzwang/github-action-lab/actions/new?category=continuous-integration&query=make)
![image](https://user-images.githubusercontent.com/76903/207068575-d172bfab-8f35-40a6-bac3-34e6d5c928f6.png)
- ( 2022-12-12 22:25:56 )
- Q: Does Github Action support `git submodule`?
- A: https://github.com/marketplace/actions/checkout-submodules

>  **INSTALLATION**
>  Copy and paste the following snippet into your .yml file.
>
>  ```yaml
>  - name: Checkout submodules
>  uses: textbook/git-checkout-submodule-action@2.1.1
>  ```
>
>  [Learn more about this action in textbook/git-checkout-submodule-action](https://github.com/textbook/git-checkout-submodule-action)

## 2022-12-15

- ( 2022-12-15 11:08:10 )
- Q: How to store `secrets` in Github Actions?
- https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
- https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md
- AWS credentials?
- https://github.com/aws-actions/configure-aws-credentials
- GitHub Action workflows to deploy to Azure
- https://github.com/Azure/actions-workflow-samples

## 2022-12-29

- ( 2022-12-29 14:16:47 )
- Q: Does Github Action support cron job?
- https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule
- https://docs.getnacelle.com/deployment/scheduled-builds-github-actions.html
```yaml
# .github/workflows/scheduled-builds.yml
name: Trigger Site Rebuild on a CRON Schedule

on:
  schedule:
    # Runs "at minute 55 past every hour" (see https://crontab.guru)
    - cron: '55 * * * *'
```

## 2022-12-30

- ( 2022-12-30 09:13:01 )
- https://github.com/actions/setup-python#caching-packages-dependencies
```yaml
steps:
- uses: actions/checkout@v3
- uses: actions/setup-python@v4
  with:
    python-version: '3.9'
    cache: 'pip' # caching pip dependencies
- run: pip install -r requirements.txt
```
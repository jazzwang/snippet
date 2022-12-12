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
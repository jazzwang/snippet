$GitTemplatesDir = $($Env:USERPROFILE + "\.git-templates")
$GitHooksDir = $GitTemplatesDir + "\hooks"

Write-Host "Checking to see if git-secrets source directory already exists..."
if (-not (Test-Path "git-secrets"))
{
    Write-Host "Clone git-secrets from https://github.com/awslabs/git-secrets"
    git clone https://github.com/awslabs/git-secrets
    cd git-secrets
    .\install.ps1
    cd ..
    rm -r -fo git-secrets
}

Write-Host "Enable git-secrets as default git hook ..."
if (-not (Test-Path $GitTemplatesDir))
{
    Write-Host "creating $GitTemplatesDir ..."
    git secrets --install $GitTemplatesDir
    git config --global init.templateDir $GitTemplatesDir
    Write-Host "Enable global git hook  ..."
    git config --global core.hooksPath $GitHooksDir
    Write-Host "Register AWS provider ..."
    git secrets --register-aws --global
    Write-Host "add rules to protect private RSA/PEM/OpenSSL key ..."
    git secrets --add --global "\-?BEGIN (RSA|OPENSSH) PRIVATE KEY\-?"
    git secrets --add --global "\-?BEGIN CERTIFICATE( REQUEST)\-?"
}

git config --global -l
echo $Env:Path
$GitTemplatesDir = $($Env:USERPROFILE + "\.git-templates")
$GitSecretsDir = $($Env:USERPROFILE + "\.git-secrets")

if (Test-Path $GitTemplatesDir)
{
    git config --global --unset init.templateDir
    git config --global --unset core.hooksPath
    git config --global --remove-section secrets
    rm -r -fo $GitTemplatesDir
}

if (Test-Path $GitSecretsDir)
{
    rm -r -fo $GitSecretsDir
}
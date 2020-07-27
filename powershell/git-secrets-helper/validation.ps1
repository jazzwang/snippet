if (-not (Test-Path "test-git-secrets"))
{
    mkdir test-git-secrets
    cd test-git-secrets
    git init
    echo "AKIAIOSFODNN7EXAMP00" | Set-Content test-file1
    echo "aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" | Set-Content test-file2
    echo "aws_secret_access_key = abcdefghijklmnopqrstuvwxyz0123456789abcd" | Set-Content test-file3
    echo "-----BEGIN RSA PRIVATE KEY-----" | Set-Content test-file4
    echo "-----BEGIN OPENSSH PRIVATE KEY-----"  | Set-Content test-file5
    echo "-----BEGIN CERTIFICATE-----"  | Set-Content test-file6
    echo "-----BEGIN CERTIFICATE REQUEST-----" | Set-Content test-file7
    git add .
    git commit -m "test git-secrets"
    cd ..
    rm -r -fo test-git-secrets
}
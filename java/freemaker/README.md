# MEMO

## 2020-11-11

- ( 2020-11-11 22:46:31 )
- 使用先前慣用的 java application gradle 範本
```bash
#!/bin/bash
gradle init --type java-application
rm -rf gradle .gradle
rm -rf gradlew*
rm -i src/main/java/*.java
rm -i src/test/java/*.java
cat > .gitignore << EOF
.gradle
.idea
.DS_Store
gradle
gradlew*
build
EOF
```
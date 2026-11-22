# Deep Java Library (DJL) 技術報告

## 1. 概述

Deep Java Library (DJL) 是由 AWS 開發的**引擎無關式（engine-agnostic）**機器學習框架，旨在解決 Java 開發者難以使用 PyTorch、TensorFlow、MXNet、ONNX 等主流深度學習引擎的問題。

DJL 提供統一的 Java API 介面，讓應用程式能透明地與底層 ML 引擎互動。它不取代 ML 引擎，而是提供統一的 Java API 將執行委派給選擇的引擎。切換不同引擎無縫且只需極少 effort。

### 1.1 核心概念

- **Criteria.Builder**: 定義 ML 模型搜尋條件（模型名稱、輸入/輸出參數、應用場景），建立 Criteria 物件
- **Model#loadModel()**: 從 Model Zoo 直接載入 ML 模型
- **Predictor**: 根據輸入（圖片、音訊轉錄、文字等）預測輸出的物件
- **Translator**: 轉換輸入物件為 ML 引擎能理解的格式，並將引擎輸出轉換為應用程式能理解的格式
- **Model Zoo**: 中央化的預訓練模型註冊表，提供常見使用案例的模型（影像辨識、自然語言處理、詞向量化等）

---

## 2. 環境需求

### 2.1 系統需求

| 項目 | 需求 |
|------|------|
| JDK | JDK 11 或更高版本（推薦 JDK 17） |
| Git | 用於克隆 DJL 倉庫 |
| Build 工具 | Maven 或 Gradle（可使用 wrapper，不需預先安裝） |
| IDE（選用） | IntelliJ IDEA（官方推薦） |

### 2.2 平台安裝指令

#### Ubuntu/Debian
```bash
sudo apt-get install openjdk-17-jdk
```

#### CentOS/RHEL
```bash
sudo yum install java-17-openjdk
```

#### macOS
```bash
brew install --cask zulu@17
```

#### Windows
從 Oracle 下載 JDK 17：https://www.oracle.com/java/technologies/javase-downloads.html

---

## 3. 安裝步驟

### 3.1 專案設定（Maven）

#### 3.1.1 引入 DJL Bill of Materials (BOM)

使用 BOM 可自動管理所有 DJL 套件版本，確保相容性：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>ai.djl</groupId>
            <artifactId>bom</artifactId>
            <version>0.36.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

#### 3.1.2 引入 Model Zoo 模組

提供存取公有儲存庫中的預訓練模型：

```xml
<dependency>
    <groupId>ai.djl</groupId>
    <artifactId>model-zoo</artifactId>
    <version>0.36.0</version>
</dependency>
```

#### 3.1.3 引入執行引擎

DJL 需要特定引擎的 runtime 依賴來執行模型。以 PyTorch 為例：

```xml
<dependency>
    <groupId>ai.djl.pytorch</groupId>
    <artifactId>pytorch-engine</artifactId>
</dependency>
```

#### 3.1.4 完整範例 pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>djl-example</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>ai.djl</groupId>
                <artifactId>bom</artifactId>
                <version>0.36.0</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>ai.djl</groupId>
            <artifactId>model-zoo</artifactId>
        </dependency>
        
        <dependency>
            <groupId>ai.djl.pytorch</groupId>
            <artifactId>pytorch-engine</artifactId>
        </dependency>
    </dependencies>
</project>
```

### 3.2 專案設定（Gradle）

#### 3.2.1 引入 DJL BOM

```gradle
plugins {
    id 'java'
}

group = 'com.example'
version = '1.0-SNAPSHOT'

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}

repositories {
    mavenCentral()
}

dependencies {
    // DJL Bill of Materials 用於版本管理
    implementation platform('ai.djl:bom:0.36.0')
}
```

#### 3.2.2 引入引擎依賴

```gradle
dependencies {
    // DJL Model Zoo
    implementation 'ai.djl:model-zoo:0.36.0'
    
    // PyTorch 引擎
    implementation 'ai.djl.pytorch:pytorch-engine:0.36.0'
}
```

### 3.3 使用 nightly Snapshots（進階）

如需使用開發中功能，可從 nightly snapshots 獲取：

#### Gradle 設定

```gradle
repositories {
    maven {
        url 'https://oss.sonatype.org/content/repositories/snapshots/'
    }
}

dependencies {
    implementation platform("ai.djl:bom:0.1001.0-SNAPSHOT")
}
```

#### Maven 設定

```xml
<repositories>
    <repository>
        <id>djl.ai</id>
        <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
    </repository>
</repositories>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>ai.djl</groupId>
            <artifactId>bom</artifactId>
            <version>0.1001.0-SNAPSHOT</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

> ⚠️ **注意**：Snapshots 版本僅保留兩週。當新版本 release 後，需更新專案依賴。

### 3.4 從原始碼建置（From Source）

```bash
# 克隆原始碼
git clone https://github.com/deepjavalibrary/djl.git
cd djl

# 建置（Linux/macOS）
./gradlew build

# 或跳過單元測試加速建置
./gradlew build -x test

# Windows
gradlew build

# 跳過測試
gradlew build -x test
```

#### 導入 Eclipse

```bash
# 建置 Eclipse 專案設定
./gradlew eclipse  # Linux/macOS
gradlew eclipse    # Windows
```

在 Eclipse 中：
1. File → Import → Gradle → Existing Gradle project
2. 選擇專案根目錄
3. 設定 workspace 編碼為 UTF-8

#### 導入 IntelliJ

1. 開啟 IntelliJ，點擊 `Import Project`
2. 選擇 DJL 專案根目錄，點擊 `Open`
3. 選擇 `Import project from external model` → `Gradle`
4. 使用預設設定，點擊 `OK`

### 3.5 M1 Mac 特殊處理

DJL 預設使用 MXNet Engine，不支援 M1 Mac。需設定使用 PyTorch：

#### 方法一：環境變數
```bash
export DJL_DEFAULT_ENGINE=PyTorch
```

#### 方法二：IntelliJ Run Configuration
在 Edit Run Configuration 中加入：
- Environment variable: `DJL_DEFAULT_ENGINE=PyTorch`

#### 方法三：Runtime 參數
```bash
-Dai.djl.default_engine=PyTorch
```

---

## 4. 測試步驟

### 4.1 驗證 JDK 安裝

```bash
java --version
# 或
java -version

# 驗證 Java 模組（確認 JDK 11+）
java --list-modules | grep "jdk.jshell"
# 預期輸出：jdk.jshell@12.0.1 或更高版本
```

### 4.2 驗證 Maven/Gradle 相依性

#### Maven 檢查
```bash
mvn dependency:tree | grep djl
# 預期看到 ai.djl:model-zoo、ai.djl.pytorch:pytorch-engine 等
```

#### Gradle 檢查
```bash
./gradlew dependencies | grep djl
```

### 4.3 建置驗證

```bash
# Maven
mvn clean compile

# Gradle
./gradlew clean build

# Windows
gradlew clean build
```

---

## 5. 驗證步驟

### 5.1 建立測試專案

#### 5.1.1 範例專案結構

```
djl-example/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── example/
│                   └── DigitIdentifier.java
├── pom.xml
└── README.md
```

#### 5.1.2 完整範例程式碼

```java
package com.example;

import ai.djl.Model;
import ai.djl.basicdataset.image.ImageClassificationDataset;
import ai.djl.engine.Engine;
import ai.djl.ndarray.NDArray;
import ai.djl.ndarray.NDList;
import ai.djl.ndarray.NDManager;
import ai.djl.ndarray.types.Shape;
import ai.djl.translate.TranslateException;
import ai.djl.translate.Translator;
import ai.djl.translate.TranslatorContext;
import ai.djl.training.util.StringUtils;
import ai.djl.zoo.ZooModel;
import ai.djl.zoo.ZooModelNotFoundException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

/**
 * 手寫數字辨識範例 - 使用 MNIST 資料集
 */
public class DigitIdentifier {

    public static void main(String[] args) throws Exception {
        // 設定使用 PyTorch 引擎
        Engine.setDefaultEngine(Engine.Type.PYTORCH);

        // 建立測試
        testModelLoading();
        testPrediction();
    }

    /**
     * 測試模型載入
     */
    private static void testModelLoading() throws ModelNotFoundException, 
            TranslateException, IOException {
        System.out.println("=== 測試模型載入 ===");

        // 使用 Criteria 定義搜尋條件
        Criteria<Image, Classifications> criteria = Criteria.builder()
                .setTypes(Image.class, Classifications.class)
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .optFilter("dataset", "mnist")
                .build();

        // 從 Model Zoo 載入模型
        ZooModel<Image, Classifications> model = criteria.loadModel();
        
        System.out.println("模型載入成功！");
        System.out.println("模型來源：" + model.getSource());

        // 釋放資源
        model.close();
    }

    /**
     * 測試預測功能
     */
    private static void testPrediction() throws Exception {
        System.out.println("\n=== 測試預測功能 ===");

        Criteria<Image, Classifications> criteria = Criteria.builder()
                .setTypes(Image.class, Classifications.class)
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .optFilter("dataset", "mnist")
                .build();

        ZooModel<Image, Classifications> model = criteria.loadModel();
        
        // 建立 Predictor
        Predictor<Image, Classifications> predictor = model.newPredictor();

        // 建立測試圖片路徑
        String testImagePath = "mnist_test.png";
        
        // 測試圖片（請自行準備一張手寫數字圖片）
        if (!Files.exists(Paths.get(testImagePath))) {
            System.out.println("找不到測試圖片：" + testImagePath);
            System.out.println("請準備一張手寫數字圖片進行測試");
            return;
        }

        // 執行預測
        NDArray input = NDManager.newBaseManager().fromFile(testImagePath);
        Classifications result = predictor.predict(input);

        // 取得最佳預測
        String predictedDigit = result.best().getClassName();
        double confidence = result.best().getScore();

        System.out.println("預測結果：數字 " + predictedDigit);
        System.out.println("信心分數：0." + confidence);

        predictor.close();
        model.close();
    }

    /**
     * 使用 Translator 的完整範例
     */
    private String identifyDigitWithTranslator(String imagePath)
            throws ModelNotFoundException, TranslateException, IOException {
        
        Criteria<Image, Classifications> criteria = Criteria.builder()
                .setTypes(Image.class, Classifications.class)
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .optFilter("dataset", "mnist")
                .build();

        ZooModel<Image, Classifications> model = criteria.loadModel();
        
        // 建立 Translator
        Translator<Image, Classifications> translator = new Translator<Image, Classifications>() {
            @Override
            public NDArray processInput(NDList inputs, TranslatorContext ctx) throws TranslateException {
                Image image = inputs.get(0);
                // 轉換為 NDArray
                NDArray ndArray = ctx.getEngine()
                    .newNdArray(ctx.getShape(), image.toArray());
                return ndArray;
            }

            @Override
            public Image processOutput(NDList outputs, TranslatorContext ctx) throws TranslateException {
                // 轉換為 Image 物件
                return ctx.getEngine().newImage(outputs.get(0));
            }
        };

        try (Predictor<Image, Classifications> predictor = 
                new Translator<Image, Classifications>() {
                    @Override
                    public NDArray processInput(NDList inputs, TranslatorContext ctx) throws TranslateException {
                        // 處理輸入
                        return inputs.get(0);
                    }
                    
                    @Override
                    public Image processOutput(NDList outputs, TranslatorContext ctx) throws TranslateException {
                        return outputs.get(0);
                    }
                }
                .getTranslator()
        ) {
            // 實際使用
        }

        return "辨識完成";
    }

    /**
     * 批次預測
     */
    public void batchPredict(String[] imagePathArray) throws Exception {
        Criteria<Image, Classifications> criteria = Criteria.builder()
                .setTypes(Image.class, Classifications.class)
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .optFilter("dataset", "mnist")
                .build();

        ZooModel<Image, Classifications> model = criteria.loadModel();
        Predictor<Image, Classifications> predictor = model.newPredictor();

        NDList inputs = NDManager.newBaseManager().emptyArray();
        for (String path : imagePathArray) {
            inputs = NDManager.newBaseManager().fromFile(path);
        }

        NDList results = predictor.batchPredict(inputs);

        for (int i = 0; i < results.size(); i++) {
            Classifications classifications = (Classifications) results.get(i);
            String predicted = classifications.best().getClassName();
            System.out.println("圖片 " + i + " 預測：" + predicted);
        }

        predictor.close();
        model.close();
    }

    // 簡化版的 main 方法
    public static void mainSimplified(String[] args) throws Exception {
        System.out.println("=== DJL 手寫數字辨識範例 ===");
        
        // 設定引擎
        Engine.setDefaultEngine(Engine.Type.PYTORCH);
        
        // 載入模型
        Criteria<Image, Classifications> criteria = Criteria.builder()
                .setTypes(Image.class, Classifications.class)
                .optApplication(Application.CV.IMAGE_CLASSIFICATION)
                .optFilter("dataset", "mnist")
                .build();
        
        ZooModel<Image, Classifications> model = criteria.loadModel();
        System.out.println("模型載入成功！");
        
        // 建立 Predictor
        Predictor<Image, Classifications> predictor = model.newPredictor();
        System.out.println("Predictor 建立成功！");
        
        predictor.close();
        model.close();
        System.out.println("範例執行完成！");
    }
    
    // 必要的 import 語句
    import ai.djl.Model;
    import ai.djl.ndarray.NDArray;
    import ai.djl.ndarray.NDList;
    import ai.djl.ndarray.NDManager;
    import ai.djl.translate.TranslateException;
    import ai.djl.zoo.ZooModel;
    import ai.djl.zoo.Criteria;
    import ai.djl.training.util.StringUtils;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
}
```

### 5.2 執行測試

```bash
# 編譯
mvn compile

# 執行
java -cp target/classes:target/dependency/* com.example.DigitIdentifier

# 或 Gradle
./gradlew run
```

### 5.3 預期輸出

```
=== DJL 手寫數字辨識範例 ===
模型載入成功！
Predictor 建立成功！
範例執行完成！
```

### 5.4 驗證檢查清單

- [ ] JDK 版本 ≥ 11
- [ ] Maven/Gradle 建置成功
- [ ] DJL 依賴載入無錯誤
- [ ] 模型從 Model Zoo 成功載入
- [ ] Predictor 物件建立成功
- [ ] 無 runtime 異常

---

## 6. 最佳實踐

### 6.1 引擎選擇建議

| 引擎 | 說明 | 適用場景 |
|------|------|----------|
| PyTorch | 動態計算圖，靈活 | 研究、快速原型 |
| MXNet | 高效能，自動選擇 native | 生產環境 |
| TensorFlow | Google 開發，相容性好 | TensorFlow 模型 |
| ONNX | 跨平台，相容性高 | 跨引擎部署 |

### 6.2 記憶體管理

```java
// 使用 try-with-resources 自動釋放資源
try (Predictor<Image, Classifications> predictor = model.newPredictor()) {
    Classifications result = predictor.predict(image);
    // 使用結果
} // predictor 自動關閉

// 模型載入後，用完後也應關閉
model.close();
```

### 6.3 多引擎支援

DJL 不建議在同一專案中使用多個引擎，因為它們都會載入記憶體：

```java
// ✅ 推薦：單一引擎
Engine.setDefaultEngine(Engine.Type.PYTORCH);

// ❌ 不推薦：多個引擎會增加記憶體負擔
Engine.setDefaultEngine(Engine.Type.PYTORCH);
// 再載入 TensorFlow 引擎
```

### 6.4 GPU 加速

使用 MXNet 引擎時，可使用自動檢測 GPU 的 native library：

```xml
<!-- Maven -->
<dependency>
    <groupId>ai.djl.mxnet</groupId>
    <artifactId>mxnet-native-auto</artifactId>
</dependency>

<!-- Gradle -->
implementation 'ai.djl.mxnet:mxnet-native-auto:0.36.0'
```

DJL 會自動檢測系統是否有 GPU 並下載對應的 MXNet GPU native library。

---

## 7. 常見問題

### 7.1 模型載入失敗

**問題**：`ModelNotFoundException`
- **原因**：Model Zoo 存取失敗或網路問題
- **解決**：檢查網路連線，或將模型本地化

### 7.2 記憶體不足

**問題**：`OutOfMemoryError`
- **原因**：同時載入多個引擎
- **解決**：只使用單一引擎，或減少批次大小

### 7.3 M1 Mac 無法執行

**問題**：MXNet 不支援 ARM64
- **解決**：設定 `DJL_DEFAULT_ENGINE=PyTorch`

---

## 8. 參考資源

- [DJL 官方文件](https://djl.ai/docs/)
- [DJL GitHub](https://github.com/deepjavalibrary/djl)
- [DJL Beginner Tutorial](https://docs.djl.ai/master/docs/demos/jupyter/tutorial/index.html)
- [DJL Model Zoo](https://github.com/deepjavalibrary/djl-model-zoo)
- [Baeldung DJL Guide](https://www.baeldung.com/java-djl-guide)

---

*報告撰寫日期：2024*
*DJL 版本：0.36.0+*

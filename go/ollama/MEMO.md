# Ollama

- Source: https://github.com/ollama/ollama
- Web site: https://ollama.com/

## 2024-10-15

### Lab #1 -- 在 Google Colab 跑 Ollama

- 測試環境：Google Colab
- 參考：https://medium.com/@abonia/running-ollama-in-google-colab-free-tier-545609258453
- 開啟 https://colab.research.google.com/github/infuseai/colab-xterm/blob/main/demo.ipynb
- 安裝 colab-xterm 以後，在 `%xterm` 的視窗裡安裝 Ollama
```bash
/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  27775      0 --:--:-- --:--:-- --:--:-- 27750
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Creating ollama user...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
/content# lspci
bash: lspci: command not found
/content# apt-get -y install lshw
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  pci.ids usb.ids
The following NEW packages will be installed:
  lshw pci.ids usb.ids
0 upgraded, 3 newly installed, 0 to remove and 49 not upgraded.
Need to get 790 kB of archives.
After this operation, 2,988 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 lshw amd64 02.19.git.2021.06.19.996aaad9c7-2build1 [321 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 pci.ids all 0.0~2022.01.22-1 [251 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 usb.ids all 2022.04.02-1 [219 kB]
Fetched 790 kB in 1s (1,246 kB/s)
Selecting previously unselected package lshw.
(Reading database ... 123621 files and directories currently installed.)
Preparing to unpack .../lshw_02.19.git.2021.06.19.996aaad9c7-2build1_amd64.deb ...
Unpacking lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Selecting previously unselected package pci.ids.
Preparing to unpack .../pci.ids_0.0~2022.01.22-1_all.deb ...
Unpacking pci.ids (0.0~2022.01.22-1) ...
Selecting previously unselected package usb.ids.
Preparing to unpack .../usb.ids_2022.04.02-1_all.deb ...
Unpacking usb.ids (2022.04.02-1) ...
Setting up pci.ids (0.0~2022.01.22-1) ...
Setting up lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Setting up usb.ids (2022.04.02-1) ...
Processing triggers for man-db (2.10.2-1) ...
/content# 
/content# whoami
root
/content# 
```
- 
```
/content# ollama serve &
[1] 4951
/content# Couldn't find '/root/.ollama/id_ed25519'. Generating new private key.
Your new public key is: 

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICbuazAXhCQ1plZ/3iB8NVjBg1dqoh2tVR4xKvad5jCp

2024/10/15 09:17:27 routes.go:1158: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://*] OLLAMA_SCHED_SPREAD:false OLLAMA_TMPDIR: ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2024-10-15T09:17:27.814Z level=INFO source=images.go:754 msg="total blobs: 0"
time=2024-10-15T09:17:27.814Z level=INFO source=images.go:761 msg="total unused blobs removed: 0"
time=2024-10-15T09:17:27.814Z level=INFO source=routes.go:1205 msg="Listening on 127.0.0.1:11434 (version 0.3.13)"
time=2024-10-15T09:17:27.815Z level=INFO source=common.go:135 msg="extracting embedded files" dir=/tmp/ollama2899235374/runners

/content# 
/content# time=2024-10-15T09:18:18.263Z level=INFO source=common.go:49 msg="Dynamic LLM libraries" runners="[cpu cpu_avx cpu_avx2 cuda_v11 cuda_v12 rocm_v60102]"
time=2024-10-15T09:18:18.264Z level=INFO source=gpu.go:199 msg="looking for compatible GPUs"
time=2024-10-15T09:18:18.299Z level=INFO source=gpu.go:347 msg="no compatible GPUs were discovered"
time=2024-10-15T09:18:18.299Z level=INFO source=types.go:107 msg="inference compute" id=0 library=cpu variant=avx2 compute="" driver=0.0 name="" total="12.7 GiB" available="11.5 GiB"

```
- ( 2024-10-15 17:21:12 )
- 預設只有用 CPU, 會比較慢。改 Runtime 成 `T4 v2-8` 試試看
```bash
/content# ollama
bash: ollama: command not found
/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  52785      0 --:--:-- --:--:-- --:--:-- 52857
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Creating ollama user...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
/content# apt-get -y install lspci
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package lspci
/content# apt-get update; apt-get -y install lshw
Get:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,626 B]
Ign:2 https://r2u.stat.illinois.edu/ubuntu jammy InRelease                                                                                                  
Get:3 https://r2u.stat.illinois.edu/ubuntu jammy Release [5,713 B]                                                                                          
Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                                                               
Get:5 https://r2u.stat.illinois.edu/ubuntu jammy Release.gpg [793 B]                                                                   
Hit:6 http://archive.ubuntu.com/ubuntu jammy InRelease                                                                                             
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]                                           
Get:8 https://r2u.stat.illinois.edu/ubuntu jammy/main all Packages [8,387 kB]             
Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease                                                
Get:10 https://r2u.stat.illinois.edu/ubuntu jammy/main amd64 Packages [2,595 kB]                                           
Get:11 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,160 kB]   
Hit:12 http://archive.ubuntu.com/ubuntu jammy-backports InRelease                
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,602 kB]
Get:14 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2,326 kB]        
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,449 kB]
Fetched 18.8 MB in 2s (10.0 MB/s)                                                                
Reading package lists... Done
W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  pci.ids usb.ids
The following NEW packages will be installed:
  lshw pci.ids usb.ids
0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
Need to get 790 kB of archives.
After this operation, 2,988 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 lshw amd64 02.19.git.2021.06.19.996aaad9c7-2build1 [321 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 pci.ids all 0.0~2022.01.22-1 [251 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 usb.ids all 2022.04.02-1 [219 kB]
Fetched 790 kB in 1s (759 kB/s)  
Selecting previously unselected package lshw.
(Reading database ... 119626 files and directories currently installed.)
Preparing to unpack .../lshw_02.19.git.2021.06.19.996aaad9c7-2build1_amd64.deb ...
Unpacking lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Selecting previously unselected package pci.ids.
Preparing to unpack .../pci.ids_0.0~2022.01.22-1_all.deb ...
Unpacking pci.ids (0.0~2022.01.22-1) ...
Selecting previously unselected package usb.ids.
Preparing to unpack .../usb.ids_2022.04.02-1_all.deb ...
Unpacking usb.ids (2022.04.02-1) ...
Setting up pci.ids (0.0~2022.01.22-1) ...
Setting up lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Setting up usb.ids (2022.04.02-1) ...
Processing triggers for man-db (2.10.2-1) ...

/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  12516      0 --:--:--  0:00:01 --:--:-- 12518
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
```
- 從 `WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.` 看來，Ollama 在 colab 只能做陽春的實驗，因為無法使用 Google 的 `TPU`
- ( 2024-10-15 17:27:10 )
- 實驗 Llama 3.2 2b 模型
```bash
/content# ollama serve &
[1] 3754
/content# 
/content# Couldn't find '/root/.ollama/id_ed25519'. Generating new private key.
Your new public key is: 

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ4vbJSYREk43yQDwAUWkZqvQmbE/PHYZfhOTAyNGro6

2024/10/15 09:28:46 routes.go:1158: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://*] OLLAMA_SCHED_SPREAD:false OLLAMA_TMPDIR: ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2024-10-15T09:28:46.185Z level=INFO source=images.go:754 msg="total blobs: 0"
time=2024-10-15T09:28:46.185Z level=INFO source=images.go:761 msg="total unused blobs removed: 0"
time=2024-10-15T09:28:46.185Z level=INFO source=routes.go:1205 msg="Listening on 127.0.0.1:11434 (version 0.3.13)"
time=2024-10-15T09:28:46.185Z level=INFO source=common.go:135 msg="extracting embedded files" dir=/tmp/ollama1573333462/runners

/content# 
/content# time=2024-10-15T09:28:57.961Z level=INFO source=common.go:49 msg="Dynamic LLM libraries" runners="[cpu_avx cpu_avx2 cuda_v11 cuda_v12 rocm_v60102 cpu]"
time=2024-10-15T09:28:57.961Z level=INFO source=gpu.go:199 msg="looking for compatible GPUs"
time=2024-10-15T09:28:57.993Z level=INFO source=gpu.go:347 msg="no compatible GPUs were discovered"
time=2024-10-15T09:28:57.993Z level=INFO source=types.go:107 msg="inference compute" id=0 library=cpu variant=avx2 compute="" driver=0.0 name="" total="334.6 GiB" available="330.1 GiB"

/content# ollama pull llama3.2
/content# ollama serve &
```
- 用 LangChain 去測試：
```python
!ollama list

NAME               ID              SIZE      MODIFIED      
llama3.2:latest    a80c4f17acd5    2.0 GB    5 minutes ago    

%pip install -U langchain-ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt | model

chain.invoke({"question": "What is MoE in AI?"})
```
- 回應：
```
Let's break it down.

MoE stands for Meta Optimizer, but I believe you might be referring to Multi-Objective Optimization (MoO), which is related to the concept of Multi-Objectives in Machine Learning and AI.

However, another possibility is MoE being an acronym for a specific algorithm or technique used in some AI applications. 

Could you please clarify or provide more context about MoE in AI?
```

## 2025-01-08

- ( 2025-01-08 23:16:37 )
- https://huggingface.co/docs/hub/ollama
- 緣起：
  - 原本看到有 DeepSeek v3 的 GGUF model 在 HuggingFace 上，可是用 ollama 指令卻載入失敗。
  - https://huggingface.co/models?other=deepseek_v3&sort=downloads&search=GGUF 好吧，只有一個
- 語法：
  ```bash
  ollama run hf.co/{username}/{repository}
  ```
- 比較久之前的作法是要自己寫 Model File
- 2024-05-06: 抓別人的 GGUF 模型，用 Ollama 在本機執行！
    - https://ywctech.net/ml-ai/ollama-import-custom-gguf/

## 2025-02-07

- ( 2025-02-07 23:55:29 )
- 緣起：
  - 本來想說需要靠 LangSmith 才能衡量 Ollama 模型每秒可以產生多少 token
  - 結果在 https://github.com/ollama/ollama/issues/1806 查到原來可以加上 `--verbose` 來顯示回應的時間 `Show timings for response`
- 語法：
  ```bash
  ollama run MODEL --verbose
  ```
- 範例：
```bash
jazzw@JazzBook:~$ ollama run deepseek-r1:8b --verbose
>>>
>>> create a d3.js dashboard in HTML format to show global pupulation trend.
<think>
Okay, I need to create a D3.js dashboard in HTML that shows the global population trend. Let me break this down step by step.

First, I'll start with the basic HTML structure. I know I need a doctype, html, head, and body tags. In the head, I'll include a title and some CSS
styles to make the graph look nice. The body will contain the dashboard elements.

Next, I need to set up the D3.js framework. I'll include d3.min.js from a CDN in the script tag. Then, I'll create an SVG element with appropriate
dimensions and margins to ensure everything fits well on the page.

For the visualization, I want a line chart showing population growth over time. I'll define data points with year and population values. To make it
interactive, I'll add tooltips that show when hovering over each point.

Styling is important for clarity. I'll use CSS to style the text elements, x-axis, y-axis, and the line itself. The axis labels should be formatted to
show numbers clearly, perhaps using commas for thousands separators. The y-axis will have a grid for better readability.

I also want to add a button that allows users to zoom into specific time periods. For simplicity, I'll just add an event listener for a sample year
range, but in a real application, this would need more functionality.

Finally, I'll test the code by saving it as an HTML file and opening it in a browser to ensure everything displays correctly. I'll check for any
errors in the console and make sure all elements are rendering properly.
</think>
```

----

Here's an example of a D3.js dashboard showing global population trends:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Global Population Trend</title>
    <script src="https://d3js.org/d3.min.js"></script>
    <style>
        .dashboard {
            margin: 20px;
            font-family: Arial, sans-serif;
        }

        .chart-container {
            width: 80%;
            margin: auto;
        }

        .title {
            font-size: 24px;
            color: #333;
            margin-bottom: 20px;
        }

        .population-line {
            fill: #3498db;
        }

        .tooltip {
            display: none;
            background-color: white;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            font-size: 16px;
        }

        .button {
            margin-top: 20px;
            padding: 8px 16px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1 class="title">Global Population Trend</h1>
        <div class="chart-container">
            <svg width="100%" height="400" id="populationChart"></svg>
        </div>
        <button class="button">Zoom In on 1950-2050</button>
    </div>

    <script>
        // Sample data - adjust these values as needed
        const data = [
            { year: 1900, population: 3 },
            { year: 1920, population: 4.1 },
            { year: 1940, population: 6 },
            { year: 1960, population: 7.5 },
            { year: 1980, population: 9.3 },
            { year: 2000, population: 12.6 },
            { year: 2020, population: 19.1 }
        ];

        // Dimensions
        const width = 800;
        const height = 300;
        const margin = { top: 20, right: 40, bottom: 60, left: 40 };

        // Create SVG element
        const svg = d3.select("#populationChart")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        // Add x and y axes
        const xAxis = svg.append("g")
            .attr("text-anchor", "middle")
            .selectAll("line")
            .data(data.map(d => d.year))
            .enter()
            .append("g");

        const yAxis = svg.append("g")
            .attr("grid", "major")
            .attr("text-anchor", "end")
            .selectAll("line")
            .data([0, 10, 20, 30, 40, 50, 60])
            .enter()
            .append("g");

        // Add population line
        const line = svg.append("path")
            .datum(data)
            .attr("class", "population-line")
            .attr("d", d3.curveLinear().xScale(d => d.year).yScale(d => d.population)(data));

        // Add tooltip
        const tooltip = d3.select("svg")
            .append("g")
            .selectAll("text")
            .data(data)
            .enter()
            .append("g")
            .attr("class", "tooltip")
            .style("display", "none")
            .on("mouseover", function(d) {
                d3.select(this).attr("display", "inline");
                const content = `<strong>${d.year}: ${d.population.toFixed(1)}</strong>`;
                return content;
            })
            .on("mouseout", function() {
                d3.select(this).attr("display", "none");
            });

        // Add axis labels
        xAxis.append("text")
            .each(function(d) { this.textContent = d; })
            .attr("text-anchor", "middle");

        yAxis.append("text")
            .each(function(d) {
                const value = d3.format("d")(d);
                this.textContent = value.toString().replace(/(\d{1,3})(\d{0})$/, `$1$2`);
            })
            .attr("text-anchor", "end");

        // Add zoom button functionality
        document.querySelector(".button").addEventListener("click", function() {
            // This is a simplified version - you would need to implement actual zoom functionality
            const svg = d3.select("#populationChart");
            const currentYear = new Date().getFullYear();

            if (currentYear < 2050) {
                const years = [1950, 1960, 1970, 1980, 1990, 2000, 2010];

                data.forEach(d => {
                    d.year = years[Math.floor(Math.random() * years.length)];
                    d.population = Math.random() * (d3.select("svg").select("g .population-line").attr("y2") - 5) + 5;
                });

                line.transition()
                    .duration(500)
                    .attr("d", d3.curveLinear().xScale(d => d.year).yScale(d => d.population)(data));
            }
        });
    </script>
</body>
</html>
```

This code creates a dashboard with:

1. A title showing "Global Population Trend"
2. A line chart showing population data over time
3. Interactive tooltips when hovering over data points
4. A simplified zoom button (in this example, it's just a placeholder)

Features:
- Responsive design
- Clean and modern styling
- Interactive elements
- Easy to read axis labels
- Smooth animations
- Sample data (adjustable in the `data` array)

To use real data instead of sample data, you would need to:
1. Replace the `data` array with actual population data
2. Update the x and y scale functions accordingly
3. Add more detailed functionality for the zoom button

The dashboard uses D3.js for rendering and includes some basic interactivity. The styling is done using CSS within the `<style>` tags.

To use this code:
1. Save it as an HTML file
2. Make sure you have an internet connection (for loading D3.js)
3. Open it in a web browser

You can customize the colors, sizes, and other visual properties by modifying the CSS styles. The D3.js functionality can be extended to handle more
complex data and interactions based on your requirements.[GIN] 2025/02/08 - 00:03:46 | 200 |         3m21s |       127.0.0.1 | POST     "/api/chat"

----

```bash
total duration:       3m21.5121463s
load duration:        31.6142ms
prompt eval count:    19 token(s)
prompt eval duration: 1.264s
prompt eval rate:     15.03 tokens/s
eval count:           1758 token(s)
eval duration:        3m20.211s
eval rate:            8.78 tokens/s
>>> Send a message (/? for help)
```
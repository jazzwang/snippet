<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 

---

# 如果有一個 mp4 影片，內容有投影片跟軟體界面操作，怎麼用 Python 程式搭配本地 ollama 多模態模型，摘要重要的截圖，並存成圖片呢？

要使用Python程式搭配本地Ollama多模態模型，從MP4影片中摘要重要的截圖並存成圖片，以下是實現步驟：

### **步驟1：安裝必要套件**

確保已經安裝了Ollama和相關視訊處理工具：

```bash
pip install ollama opencv-python
```


### **步驟2：影片預處理**

使用OpenCV讀取MP4影片並進行預處理，例如調整解析度或幀率。

```python
import cv2

# 讀取影片
cap = cv2.VideoCapture('input.mp4')

# 設定幀率
fps = cap.get(cv2.CAP_PROP_FPS)
frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 每隔幾幀截一次圖
    if frame_idx % 30 == 0:  # 每秒截一次圖
        cv2.imwrite(f'frame_{frame_idx}.jpg', frame)
    
    frame_idx += 1

cap.release()
```


### **步驟3：多模態模型應用**

使用Ollama的Llama 3.2 Vision模型來分析截圖，並根據內容重要性進行篩選。

```python
import ollama

# 載入模型
model = "llama:34b"

# 定義分析函數
def analyze_image(image_path):
    res = ollama.chat(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': '請描述這張圖片的內容',
                'images': [image_path]
            }
        ]
    )
    
    # 根據分析結果判斷重要性
    if '重要' in res['message']['content']:
        return True
    else:
        return False

# 篩選重要截圖
important_frames = []
for frame in os.listdir('frames'):
    if analyze_image(os.path.join('frames', frame)):
        important_frames.append(frame)
```


### **步驟4：存儲重要截圖**

將篩選出的重要截圖存儲到指定目錄。

```python
import shutil

output_dir = 'important_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for frame in important_frames:
    shutil.copy(os.path.join('frames', frame), output_dir)
```


### **完整範例程式碼**

以下是完整的程式碼範例，包含影片預處理、多模態模型應用和截圖存儲：

```python
import cv2
import ollama
import os
import shutil

# 步驟1：影片預處理
def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_idx = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if frame_idx % 30 == 0:
            cv2.imwrite(f'frame_{frame_idx}.jpg', frame)
        
        frame_idx += 1
    
    cap.release()

# 步驟2：多模態模型應用
def analyze_image(image_path):
    model = "llama:34b"
    res = ollama.chat(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': '請描述這張圖片的內容',
                'images': [image_path]
            }
        ]
    )
    
    if '重要' in res['message']['content']:
        return True
    else:
        return False

# 步驟3：存儲重要截圖
def save_important_frames(frames_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    important_frames = []
    for frame in os.listdir(frames_dir):
        if analyze_image(os.path.join(frames_dir, frame)):
            important_frames.append(frame)
    
    for frame in important_frames:
        shutil.copy(os.path.join(frames_dir, frame), output_dir)

if __name__ == "__main__":
    video_path = 'input.mp4'
    frames_dir = 'frames'
    output_dir = 'important_frames'
    
    extract_frames(video_path)
    save_important_frames(frames_dir, output_dir)
```


### **注意事項**

1. **模型選擇**：這裡使用的是Llama 3.2 Vision模型，您可以根據需求選擇其他適合的模型。
2. **API授權**：確保有適當的授權使用Ollama模型。
3. **效能優化**：根據影片長度和截圖數量，可能需要調整幀率或使用多線程加速處理。

<div style="text-align: center">⁂</div>

[^1]: https://chtseng.wordpress.com/2024/11/18/何在本地端透過ollama使用llama-3-2-vision/

[^2]: https://www.youtube.com/watch?v=t5q4fT4rKK4

[^3]: https://blog.csdn.net/weixin_41870426/article/details/137754825

[^4]: https://www.youtube.com/watch?v=Xkh2-PFVKzs

[^5]: https://blog.csdn.net/shebao3333/article/details/142711740

[^6]: https://github.com/win4r/VideoFinder-Llama3.2-vision-Ollama

[^7]: https://ivonblog.com/posts/open-webui-video-call/


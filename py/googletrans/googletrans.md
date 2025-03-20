# Google Translate

## 2025-01-08

- 看到一個用 Google Translate 套件做 PDF 翻譯的範例
  - 有趣的是還用 OpenCC 做「繁簡體中文轉換」
- 透過Python處理英文 PDF 論文或大量英文文本設計的自動化翻譯工具
  - https://ithelp.ithome.com.tw/m/articles/10369447

```bash
pip install googletrans==4.0.0-rc1 opencc-python-reimplemented python-docx pdfplumber
```
```python
import os
import time
import pdfplumber
from googletrans import Translator
from opencc import OpenCC
from docx import Document

def chunk_text(text, chunk_size=3000):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end
    return chunks

def translate_chunk(chunk, translator, opencc, max_retry=3, wait_secs=2):
    for attempt in range(max_retry):
        try:
            result = translator.translate(chunk, src='en', dest='zh-TW')
            translated_text = result.text
            translated_text = opencc.convert(translated_text)
            return translated_text
        except Exception as e:
            print(f"翻譯失敗: {e}")
            if attempt < max_retry - 1:
                print(f"稍等 {wait_secs} 秒後重試...")
                time.sleep(wait_secs)
            else:
                print("多次嘗試仍失敗，保留原文。")
                return chunk

def read_pdf_text(pdf_path):
    all_text_list = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                all_text_list.append(page_text)
    entire_text = "\n".join(all_text_list)
    return entire_text

def save_translated_to_word(translated_text, output_word_path):
    doc = Document()
    for line in translated_text.split("\n"):
        doc.add_paragraph(line)
    doc.save(output_word_path)

def translate_pdf_to_word(pdf_path, output_word_path, translator, opencc):
    entire_text = read_pdf_text(pdf_path)
    print(f"[DEBUG] 原文長度: {len(entire_text)}")
    text_chunks = chunk_text(entire_text, 3000)
    translated_results = []
    for chunk in text_chunks:
        t_chunk = translate_chunk(chunk, translator, opencc)
        translated_results.append(t_chunk)
    final_text = "\n".join(translated_results)
    print(f"[DEBUG] 翻譯後長度: {len(final_text)}")
    save_translated_to_word(final_text, output_word_path)

def main():
    en_pdf_folder = r"C:\Users\chenchen\Desktop\chenchen_code\pdf_file_translation\englishpdf"
    cn_word_folder = r"C:\Users\chenchen\Desktop\chenchen_code\pdf_file_translation\cn"

    if not os.path.exists(cn_word_folder):
        os.makedirs(cn_word_folder)

    translator = Translator()
    opencc = OpenCC('s2t')

    for filename in os.listdir(en_pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(en_pdf_folder, filename)
            word_filename = os.path.splitext(filename)[0] + ".docx"
            output_word_path = os.path.join(cn_word_folder, word_filename)

            print(f"正在處理: {filename}")
            try:
                translate_pdf_to_word(pdf_path, output_word_path, translator, opencc)
                print(f"翻譯完成，保存至: {output_word_path}")
            except Exception as e:
                print(f"處理失敗: {filename}, 錯誤: {e}")

if __name__ == "__main__":
    main()
```
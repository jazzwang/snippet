# DCMTK = DICOM ToolKit (DCMTK) 

- https://github.com/DCMTK/dcmtk
  - https://git.dcmtk.org/
- 緣起：
  - 原本是看到討論串裡用到 `findscu` 這個指令
  - 查到 Ubuntu manpage - https://manpages.ubuntu.com/manpages/focal/man1/findscu.1.html
    - 頁面中提到 Provided by: `dcmtk_3.6.4-2.1ubuntu0.1_amd64`
    - 對了一下 launchpad 程式碼，https://git.launchpad.net/ubuntu/+source/dcmtk/tree/ 跟 https://github.com/DCMTK/dcmtk 大致上目錄結構相同。
  - https://github.com/dcm4che/dcm4che/tree/master/dcm4che-tool/dcm4che-tool-findscu 也有 Java 的版本的實作。
  - https://pydicom.github.io/pynetdicom/dev/apps/findscu.html 有 Python 版的實作

## 關於 DICOM 標準

- 雖然早在 2003 SARS 疫情前後就已經聽過 DICOM 這個格式，不過仍舊不熟細節。
- https://dcmtk.org/en/ DICOM Toolkit 是[德國 OFFIS](https://www.offis.de/) 開發的
  - OFFIS 是[奧爾登堡卡爾-馮-奧西茨基大學](https://www.uni-oldenburg.de/en/)的附屬機構，感覺有一點像研發處技轉中心。
  - https://www.offis.de/en/offis/about-us.html
- 網站上有一段 DICOM 標準的簡介
  - [Introduction to the DICOM Standard](https://dcmtk.org/en/general/dicom-introduction/)
  - ![](https://dcmtk.org/media/filer_public_thumbnails/filer_public/1b/da/1bda2842-b4b8-43b3-942d-7ad552a7b1a8/med_bildkomm_deutsch_weiss_grau.png__900x556_subsampling-2.png)
calibre, version 7.26.0
錯誤： 載入書本失敗: 無法開啟在 C:\Users\jazzw\scoop\apps\calibre\current\Calibre Library\XXX-XXX\B0DM6BHQYR EBOK (6)\B0DM6BHQYR EBOK - XXX-XXX.azw 的書籍，請點選 「顯示詳細資料」查看更多資訊。

```python
Failed to convert book: C:\Users\jazzw\scoop\apps\calibre\current\Calibre Library\XXX-XXX\B0DM6BHQYR EBOK (6)\B0DM6BHQYR EBOK - XXX-XXX.azw with error:
Traceback (most recent call last):
  File "calibre\customize\ui.py", line 482, in get_file_type_metadata
  File "calibre\customize\builtins.py", line 267, in get_metadata
  File "calibre\ebooks\metadata\mobi.py", line 501, in get_metadata
  File "calibre\ebooks\mobi\reader\headers.py", line 294, in __init__
  File "calibre\ebooks\mobi\reader\headers.py", line 322, in identity
calibre.ebooks.mobi.MobiError: Unknown book type: b'\x81\xc4\xde\x02\x9d\x8c#\x01'
DeDRM v10.0.9: Trying to decrypt B0DM6BHQYR EBOK - XXX-XXX.azw
DeDRM v10.0.9: Failed to decrypt with error: The .kfx DRMION file cannot be decrypted by itself. A .kfx-zip archive containing a DRM voucher is required.
DeDRM v10.0.9: Looking for new default Kindle Key after 0.6 seconds
searching for kinfoFiles in C:\Users\jazzw\AppData\Local
Found K4PC 1.25+ kinf2018 file: C:\Users\jazzw\AppData\Local\Amazon\Kindle\storage\.kinf2018
Decrypted key file using IDString '3226438905' and UserName 'jazzw'
DeDRM v10.0.9: Found 1 new key
Traceback (most recent call last):
  File "calibre_plugins.dedrm.__init__", line 931, in KindleMobiDecrypt
  File "C:\Users\jazzw\scoop\apps\calibre\current\Calibre Settings\plugins\DeDRM.zip\k4mobidedrm.py", line 170, in GetDecryptedBook
k4mobidedrm.DrmException: The .kfx DRMION file cannot be decrypted by itself. A .kfx-zip archive containing a DRM voucher is required.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "calibre_plugins.dedrm.__init__", line 965, in KindleMobiDecrypt
  File "C:\Users\jazzw\scoop\apps\calibre\current\Calibre Settings\plugins\DeDRM.zip\k4mobidedrm.py", line 170, in GetDecryptedBook
k4mobidedrm.DrmException: The .kfx DRMION file cannot be decrypted by itself. A .kfx-zip archive containing a DRM voucher is required.
DeDRM v10.0.9: Ultimately failed to decrypt after 0.7 seconds. Read the FAQs at noDRM's repository: https://github.com/noDRM/DeDRM_tools/blob/master/FAQs.md
Running file type plugin DeDRM failed with traceback:
Traceback (most recent call last):
  File "calibre_plugins.dedrm.__init__", line 931, in KindleMobiDecrypt
  File "C:\Users\jazzw\scoop\apps\calibre\current\Calibre Settings\plugins\DeDRM.zip\k4mobidedrm.py", line 170, in GetDecryptedBook
k4mobidedrm.DrmException: The .kfx DRMION file cannot be decrypted by itself. A .kfx-zip archive containing a DRM voucher is required.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "calibre\customize\ui.py", line 200, in _run_filetype_plugins
  File "calibre_plugins.dedrm.__init__", line 1030, in run
  File "calibre_plugins.dedrm.__init__", line 981, in KindleMobiDecrypt
calibre_plugins.dedrm.DeDRMError: DeDRM v10.0.9: Ultimately failed to decrypt after 0.7 seconds. Read the FAQs at noDRM's repository: https://github.com/noDRM/DeDRM_tools/blob/master/FAQs.md
InputFormatPlugin: MOBI Input running
on C:\Users\jazzw\scoop\apps\calibre\current\Calibre Library\XXX-XXX\B0DM6BHQYR EBOK (6)\B0DM6BHQYR EBOK - XXX-XXX.azw
Failed to run pipe worker with command: from calibre.srv.render_book import viewer_main; viewer_main()
Traceback (most recent call last):
  File "calibre\ebooks\conversion\plugins\mobi_input.py", line 28, in convert
  File "calibre\ebooks\mobi\reader\mobi6.py", line 90, in __init__
calibre.ebooks.mobi.reader.mobi6.KFXError: 這是 Amazon KFX 書本，它是無法被處理的。有關於如何處理 KFX 書本的資料，請查看 https://www.mobileread.com/forums/showthread.php?t=283371。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "runpy.py", line 198, in _run_module_as_main
  File "runpy.py", line 88, in _run_code
  File "site.py", line 83, in <module>
  File "site.py", line 78, in main
  File "site.py", line 50, in run_entry_point
  File "calibre\utils\ipc\worker.py", line 196, in main
  File "<string>", line 1, in <module>
  File "calibre\srv\render_book.py", line 845, in viewer_main
  File "calibre\srv\render_book.py", line 836, in render_for_viewer
  File "calibre\srv\render_book.py", line 813, in render
  File "calibre\ebooks\oeb\iterator\book.py", line 64, in extract_book
  File "calibre\customize\conversion.py", line 242, in __call__
  File "calibre\ebooks\conversion\plugins\mobi_input.py", line 34, in convert
  File "calibre\ebooks\mobi\reader\mobi6.py", line 90, in __init__
calibre.ebooks.mobi.reader.mobi6.KFXError: 這是 Amazon KFX 書本，它是無法被處理的。有關於如何處理 KFX 書本的資料，請查看 https://www.mobileread.com/forums/showthread.php?t=283371。
```
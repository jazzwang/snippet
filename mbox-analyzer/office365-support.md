## Recommendation



### for Mac Users

* use Mac OS default `mail.app` to download the mails from [Office365](https://www.office.com) and export to `mbox` file.

![Screen Shot 2019-10-22 at 10.39.06](https://i.imgur.com/9mQnP7h.png)

Here are the sample files in the exported folder:

```bash
~/mbox$ tree
.
└── Today.mbox
    ├── mbox
    └── table_of_contents

1 directory, 2 files

~/mbox$ file Today.mbox/mbox 
Today.mbox/mbox: ASCII text, with very long lines
```

### for Windows / Linux Users

* use [`Thunderbird`](https://www.thunderbird.net) to download the mail from [Office365](https://www.office.com) and export to `mbox` file.
  * Thunderbird Addon `ImportExportTools` - https://addons.thunderbird.net/en-US/thunderbird/addon/importexporttools/

## Reference

If you need to deal with Office 365 or Outlook, the file format is PST (Personal Storage Table).

* [Export or backup email, contacts, and calendar to an Outlook .pst file](https://support.office.com/en-us/article/export-or-backup-email-contacts-and-calendar-to-an-outlook-pst-file-14252b52-3075-4e9b-be4e-ff9ef1068f91)

There are two suggested python library to deal with PST files based on the [stackoverflow discussion](https://stackoverflow.com/questions/3197388/outlook-pst-file-parsing-in-python):
* [libpst-python](https://www.five-ten-sg.com/libpst/packages/centos4/) - last updated version is in 2012
* [libpff-python](https://pypi.org/project/libpff-python/)
    * https://github.com/libyal/libpff/wiki
    * libyal and libpff are still active

## Note: MS Outlook for Mac

After testing the export function provied by Microsoft Outlook for Mac, the output format is OLM.

![Screen Shot 2019-10-22 at 10.33.06](https://i.imgur.com/UEtCNLV.png)
![Screen Shot 2019-10-22 at 10.33.42](https://i.imgur.com/xANdct8.png)

Some developers write sample python code to convert OLM file into other format.

* https://github.com/rhiaro/olmparser/blob/master/olm.py
* https://github.com/eercanayar/outlook-olm-email-exporter

The easy way to export to `mbox` format is use Mac `Mail.app` to download the email and stored in mbox format.
* https://superuser.com/questions/1176337/transferring-from-outlook-to-apple-mail-olm-to-mbox
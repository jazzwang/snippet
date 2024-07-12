# Virtual Display Driver for Windows

## 緣起

工作上遇到一些需求要測試不同解析度，多螢幕的狀態。但開發者/測試者並沒有實體的螢幕可供測試，尤其遇到客戶使用情境與產品定義有出入，客戶改用直式螢幕方式，挑戰原定義的 UI/UX。

## 需求

能在 Windows 虛擬機器中，新增至少一個額外的螢幕，並設定不同的解析度。

## 解方研究

- https://github.com/itsmikethetech/Virtual-Display-Driver
    - Fork from https://github.com/ge9/IddSampleDriver
        - Fork from https://github.com/roshkins/IddSampleDriver
- https://github.com/MolotovCherry/virtual-display-rs
    - read from https://www.reddit.com/r/rust/comments/16hvf4p/virtual_display_driver_for_windows/
- 針對 GCP 的解法
    - https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display

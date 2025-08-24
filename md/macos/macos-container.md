# macOS container?

## 2024-10-16

- https://unrealcontainers.com/docs/concepts/macos-containers

> **Key points:**
>    - As of today, **there is no such thing as a macOS container**.
>    - There are alternatives available that use macOS virtual machines to approximate the experience of using containers.
>    - The open source community is working hard to change this situation and bring native container support to macOS.

- ( 2024-10-16 13:47:04 )
- 雖然有 https://macoscontainers.org/ 相關的討論，但這個網址已經失效。
  - https://news.ycombinator.com/item?id=37655477
  - https://github.com/darwin-containers/homebrew-formula
    - 從 Homebrew `darwin-containers/formula/dockerd` 的原始碼看起來，主要是透過 `macfuse` (我猜是為了 `relayfs` 要用到其他 Darwin/macOS 不支援的檔案系統)，加上 ["修改過"的 moby](https://github.com/darwin-containers/moby) 來達成。細節架構，可能就要再追一下 OCI [`runc`](https://github.com/darwin-containers/rund) 跟 ["小改" `containerd`](https://github.com/darwin-containers/containerd) 之間的關係。
  - 更多細節：
    - https://earthly.dev/blog/macos-native-containers/
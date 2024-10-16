# Container Runtime for macOS

- [容器技術編年史!! The internals and the latest trends of container runtimes (2023)](https://medium.com/nttlabs/the-internals-and-the-latest-trends-of-container-runtimes-2023-22aa111d7a93)

Linux 容器技術從 OpenVZ, LXC 開始。
Docker 變成「代名詞」，然後因為商用授權的衝擊，之後遍地開花。
隨即在 Windows , FreeBSD 等作業系統上也出現不同的實作。
目前在 macOS 上應該只能透過類似 Full Virtualization (e.g. VirtualBox) 的方式，
要在 macOS 上跑 Linux Container 的選擇包括：

 - [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
 - [colima](https://github.com/abiosoft/colima) 
   - [lima](https://github.com/lima-vm/lima) = https://lima-vm.io/
 - [OrbStack](https://orbstack.dev/) - 號稱效能比 Docker Desktop 跟 Colima 好
   - https://orbstack.dev/#benchmarks
   - https://docs.orbstack.dev/compare/colima
   - https://docs.orbstack.dev/compare/docker-desktop
   - https://docs.orbstack.dev/compare/utm
     - UTM 並不是 container runtime，是基於 QEMU，所以是 Full Virtualization 的技術。
     - https://mac.getutm.app/
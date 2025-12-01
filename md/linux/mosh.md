# mosh - Mobile Shell

- Git repo
  - https://github.com/mobile-shell/mosh
- Website
  - https://mosh.org/

## 2025-12-01

- 先前因為在高鐵上，手機網路不穩定，所以習慣在 Linux Server 上裝 mosh server，然後用 mosh client 當 SSH client
  - 優點：因為採用 UDP 通訊，所以當網路延遲很高或者瞬斷時，使用上不會受到比較大的影響。
- 最近想要實驗看看 WSL Reverse SSH 回 Linux Server 當跳板，所以研究一下 mosh 是否支援 SSH Tunneling
  - https://github.com/carltonf/mosh-via-tunnel
    - A simple wrapper to use mosh over TCP tunnel.
  - Mosh with port forwarding (like SSH)
    - https://unix.stackexchange.com/questions/437242/mosh-with-port-forwarding-like-ssh
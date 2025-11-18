# OpenSSH

## 2025-11-18

- 今天遇到一個狀況，`scp` 或 `ssh` 的時候，老舊的 Server 突然拋出以下警告
```bash
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
```
- 查了一下 https://www.openssh.org/pq.html
  - 這個叫做「OpenSSH 後量子密碼學」，因為有一些加密方法是已知量子電腦成熟後就可以被解鎖的
- 解法：在 SSH Client 端的 `~/.ssh/config` 可以加上 `WarnWeakCrypto no` 是可以抑制警告。
  但根本之道還是得在 SSH Server 端使用不會被量子電腦解鎖的金鑰。
  - 意思就是說，老舊到已經沒辦法升級的 Linux 系統，資安風險等級就是比較高
```bash
~$ cat ~/.ssh/config
# Ref:
# https://www.openssh.org/pq.html
Host old.example.com
  HostName old.example.com
  User     jazz
  WarnWeakCrypto no
```

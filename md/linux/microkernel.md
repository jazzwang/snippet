# Microkernel 與容器休眠技術

> 記錄關於 microkernel 技術、容器休眠（hibernate container）以及 AWS 客製化 microkernel 技術的討論。

## 目錄

- [容器休眠技術概覽](#容器休眠技術概覽)
- [Microkernel 的休眠支持](#microkernel 的休眠支持)
- [AWS 客製化 Microkernel 與容器技術](#aws 客製化 microkernel 與容器技術)

## 容器休眠技術概覽

### 核心技術：CRIU (Checkpoint/Restore in Userspace)

CRIU 是 Linux 容器休眠的**核心技术**，允許冻结运行中的容器并将内存状态保存到磁盘，之后可以恢复。

### 支持容器休眠的主要技术

#### 1. **Docker**

- **Docker Checkpoint/Restore** (实验性功能)
  - 使用 CRIU 底层实现
  - 命令：`docker checkpoint` / `docker restore`
  - 可以将容器状态保存到磁盘，之后恢复
  - 支持保存容器内存状态并恢复

- **Docker Pause/Unpause** 
  - 使用 freezer cgroup 暂停/恢复容器进程
  - 不是真正的 hibernate，只是暂停执行

#### 2. **Kubernetes**

- **Zeropod** - 使用 CRIU + eBPF 实现 pod 休眠
  - 检查容器最后 TCP 连接活动时间
  - 空闲后自动 checkpoint 到磁盘
  - 支持 Kubernetes、Containerd、Podman

- **Architect** - Kubernetes 上的容器休眠
  - 自动 checkpoint 运行中的容器
  - 保存执行状态到本地节点存储
  - 减少 pod 资源请求到零

- **KubeGreen** - 自动化资源清理和 pod 休眠
  - 非生产工作负载在空闲时自动休眠

- **EnterpriseDB PostgreSQL for Kubernetes**
  - 声明式休眠功能
  - 保存数据库 PVC，移除 Pods 以节省 CPU

#### 3. **Containerd**

- 支持 CRIU via criu plugin
- 通过 CRI API 实现 checkpoint/restore
- `ctr commands` 支持

#### 4. **CRI-O**

- 通过 checkpoint restore 实现容器状态保存
- Kubernetes 的容器运行时支持

#### 5. **Podman**

- 支持 CRIU checkpoint/restore
- 可用于容器休眠

#### 6. **Proxmox LXC**

- 支持容器暂停/恢复
- 可使用 KVM/QEMU 的保存功能

#### 7. **Kata Containers**

- 使用 VM 级别的虚拟化
- 支持容器级别的 checkpoint/restore

### 技术对比

| 技术 | 核心机制 | 适用场景 | 成熟度 |
|------|---------|---------|-------|
| **CRIU** | 内存镜像保存 | 所有容器 | 成熟 |
| **Docker Checkpoint** | CRIU 集成 | 单机 Docker | 实验性 |
| **Kubernetes + Zeropod** | CRIU + eBPF | 云原生，自动伸缩 | 新兴 |
| **Docker Pause** | freezer cgroup | 临时暂停 | 成熟 |

### 关键概念

- **Checkpoint**: 将容器内存状态保存到磁盘
- **Restore**: 从磁盘恢复容器状态
- **Scale to Zero**: 容器休眠到零资源使用
- **Freezer cgroup**: Linux cgroup 的暂停/恢复机制

## Microkernel 的休眠支持

### seL4 Microkernel

seL4 微内核在休眠方面有以下支持：

#### Checkpoint/Restore 机制

```c
// seL4 的线程检查点结构
typedef struct sel4utils_checkpoint {
    void *stack;                  // 检查点栈
    seL4_UserContext regs;        // 寄存器状态
    sel4utils_thread_t *thread;   // 线程指针
    uintptr_t sp;                  // 栈指针
} sel4utils_checkpoint_t;
```

#### 功能特性

- **Fault-Tolerant Task Backup and Recovery** - 支持任务备份和恢复
- **Micro restart** - 微重启机制
- **Process isolation** - 进程隔离
- **Thread checkpointing** - 线程检查点保存

#### 相关论文

- *Towards Fault-Tolerant Task Backup and Recovery in the seL4 Microkernel* (2018)
- 支持故障容错的任务备份和恢复机制

### L4 Microkernel 虚拟化支持

#### 虚拟机休眠支持

- **L4 Micro Hypervisor** (L4Re)
  - 支持 VM 的状态保存和恢复
  - 提供 vCPU 对象保存 guest 的 privileged register state
  - 支持 world switch（上下文切换）
  
- **Virtualization on L4 Microkernel**
  - 第二级页表翻译 (EPT on x86, stage-2 on Arm)
  - 支持 VM 的 suspend/resume

### Microkernel 休眠的实现方式

#### Checkpoint/Restore 模式

```
Microkernel 支持：
├── 保存当前线程状态（寄存器、栈）
├── 保存能力（capabilities）
├── 保存内存映射
├── 恢复时重新建立权限关系
└── 恢复执行上下文
```

#### 优势

1. **细粒度控制** - 可以针对单个进程/服务进行检查点，而非整个系统
2. **安全性** - 用户态实现，故障不影响内核
3. **可验证性** - seL4 等经过形式化验证的微内核

#### 挑战

1. **复杂性** - 需要重新建立进程间通信关系
2. **内存管理** - 需要精确跟踪内存分配
3. **权限恢复** - 需要正确恢复 capabilities 关系

### 技术对比

| 特性 | Monolithic Kernel | Microkernel |
|------|------------------|-------------|
| **休眠实现** | 内核直接支持 CONFIG_HIBERNATION | 通过用户态服务实现 |
| **检查点机制** | 系统级内存镜像 | 进程/线程级检查点 |
| **恢复速度** | 较慢（整个系统） | 较快（单个进程/服务） |
| **安全性** | 较低 | 高（用户态隔离） |
| **适用场景** | 通用计算 | 安全关键系统 |

### 相关技术项目

- **seL4** - 形式化验证的微内核，支持任务备份和恢复
- **L4Re** - L4 微内核虚拟化方案
- **ITEC-OS** - 微内核的电源管理研究
- **Cocoon** - 支持 VM 生命周期管理的微内核方案

## AWS 客製化 Microkernel 與容器技術

### 1. AWS Nitro System ⭐ 核心虛擬化技術

AWS 完全重新設計的虛擬化基礎設施：

```
┌─────────────────────────────────────────┐
│        AWS Nitro System                 │
├─────────────────────────────────────────┤
│  Dedicated Hardware + Lightweight Hypervisor  │
│  • Nitro Hypervisor (lightweight)       │
│  • Nitro Cards (VPC/EBS/IO acceleration)│
│  • Nitro Security Chip (TPM)            │
│  • Nitro Isolation Engine               │
└─────────────────────────────────────────┘
```

**特色：**
- **Lightweight Hypervisor** - 管理記憶體和 CPU 分配
- **零管理員訪問** - 所有虛擬化資源都通過專用硬體處理
- **數學保證隔離** - Nitro Isolation Engine 提供數學級隔離證明

### 2. AWS Nitro Enclaves - 獨立 Kernel 隔離環境 ⭐

**技術特點：**
```
┌─────────────────────────────────────────┐
│      Nitro Enclaves (隔離環境)           │
├─────────────────────────────────────────┤
│ • 獨立的 Kernel (separate from parent)  │
│ • 專用的 CPU 核心和記憶體                 │
│ • 僅通過 vsock 通道通訊                 │
│ • 無持久化儲存、無網路                   │
└─────────────────────────────────────────┘
```

**功能：**
- **Independent Kernel** - 有自己的 Kernel，分離於父實例
- **Full CPU Cores** - 專用的 CPU 核心
- **Hardware Isolation** - CPU 和記憶體隔離
- **使用場景：** PII 數據、醫療數據、金融數據處理

### 3. AWS Nitro Sandboxes ⭐ 每個 Pod 都有獨立 Kernel

**革命性的容器隔離技術：**

| 特性 | 傳統容器 | Nitro Sandboxes |
|------|---------|-----------------|
| **隔離層級** | 共享 Kernel | 每個 Pod 獨立 VM + Kernel |
| **安全性** | 依賴 shared kernel | 硬體級隔離 |
| **管理員訪問** | 可讀取所有容器記憶體 | 完全無訪問 |
| **故障影響** | 一個 kernel bug 影響所有 | 一個 sandbox 不影響其他 |

**技術架構：**
```
Parent EC2 Instance
├── Container/Pod 1 (Nitro Sandbox)
│   ├── 獨立的 Kernel
│   ├── 獨立的 Network Stack
│   └── 獨立的 VM
├── Container/Pod 2 (Nitro Sandbox)
│   ├── 獨立的 Kernel
│   ├── 獨立的 Network Stack
│   └── 獨立的 VM
└── ...
```

**特色：**
- **每 Pod 一個 VM** - 每個 container 都是獨立的 VM
- **硬件隔離** - 通過 Nitro Hypervisor 強制執行
- **性能接近裸機** - 沒有 nested hypervisor
- **支援 EKS/ECS** - 內建整合

**隔離模式：**
1. **Confidential Sandbox** - 完全可驗證，使用 KMS attestation
2. **Isolated Sandbox** - 硬體隔離但不需要 attestation

### 4. Custom AWS Kernel - Canonical 合作開發

**Ubuntu for EKS 的客製化 Kernel：**

```bash
# Canonical 與 AWS 合作開發的 Ubuntu AMI
- Optimized for Amazon EKS
- Includes custom AWS kernel (jointly developed with AWS)
- Built-for-purpose Kubernetes Node OS
```

**使用：**
```bash
# 在 EKS 中使用自定義 Ubuntu 節點
eksctl create nodegroup ...
```

### 5. Bottlerocket - AWS 開源容器 OS ⭐

**完全開源的容器作業系統：**

**特色：**
- **Minimal OS** - 僅包含容器運行所需的組件
- **Immutable** - 不可變系統，提高安全性
- **可自定義** - 可創建自定義變體
- **預設安全** - 禁用 SSH、禁用 Docker socket

**架構：**
```
Bottlerocket OS
├── Custom Kernel
├── Minimal Init System
├── Container Runtime (containerd)
├── Security Hardening
└── AWS EKS/ECS Integration
```

**使用場景：**
- Kubernetes 節點 OS
- ECS 管理節點
- 需要高安全性的容器環境

### 6. HookOS - EKS Anywhere Bare Metal 啟動

**EKS Anywhere 的自定義啟動 Kernel：**

**功能：**
- **Network Boot** - 無伺服器啟動 bare metal 機器
- **可自定義** - 可添加特定硬體驅動
- **預設提供** - 創建 EKS Anywhere cluster 時自動提供

### 7. Firecracker - MicroVM Hypervisor

**AWS 開發的輕量級 VM 管理程式：**

```
┌─────────────────────────────────────────┐
│      Firecracker MicroVM                │
├─────────────────────────────────────────┤
│ • 毫秒級啟動時間                         │
│ • 輕量級 Hypervisor                     │
│ • 基於 eBPF 的監控                       │
│ • 支援 Nitro Sandboxes                  │
└─────────────────────────────────────────┘
```

**特色：**
- **MicroVM 技術** - 極輕量的虛擬機器
- **快速啟動** - 毫秒級啟動
- **低記憶體足跡** - 僅幾 MB 記憶體
- **用於 K8s 節點** - EKS 的預設節點管理程式

## 技術對比

| 技術 | Kernel 類型 | 隔離層級 | 啟動速度 | 用途 |
|------|-----------|---------|---------|------|
| **Nitro Enclaves** | 獨立 Kernel | VM 級 | 秒級 | 敏感數據隔離 |
| **Nitro Sandboxes** | 獨立 Kernel | VM 級 | 秒級 | 容器硬體隔離 |
| **Bottlerocket** | 自定義 Linux | 節點級 | 秒級 | 容器節點 OS |
| **Firecracker** | 共享 Kernel | MicroVM | 毫秒級 | K8s 容器隔離 |
| **Custom AWS Kernel** | 客製化 Linux | 節點級 | 秒級 | EKS 優化 |

## 核心技術總結

### Nitro Sandboxes 是 AWS 最核心的 Microkernel 容器技術

```
傳統容器 (共享 Kernel)
└── 所有 Pod 信任同一個 Kernel

Nitro Sandboxes (每個 Pod 獨立 Kernel)
├── Pod 1 → 自己的 VM + 自己的 Kernel
├── Pod 2 → 自己的 VM + 自己的 Kernel
└── Pod 3 → 自己的 VM + 自己的 Kernel
```

**優勢：**
- ✅ 單一 kernel bug 不會影響其他容器
- ✅ 管理員無法讀取容器記憶體
- ✅ 硬體級隔離，數學保證
- ✅ 性能接近裸機（沒有 nested hypervisor）

**這是 AWS 在容器技術上的最大創新！** 🎯

## 參考文獻

- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)
- [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/)
- [AWS Nitro Sandboxes](https://aws.amazon.com/blogs/compute/nitro-sandboxes-hardware-isolation-for-every-eks-pod-ecs-task-and-ec2-workload/)
- [CRIU Documentation](https://criu.org/)
- [seL4 Reference Manual](https://www.sel4.com/Info/Docs/seL4-manual-latest.pdf)
- [L4Re Micro Hypervisor](https://www.kernkonzept.com/wp-content/uploads/2023/11/Kernkonzept_Whitepaper-L4Re-Micro-Hypervisor.pdf)

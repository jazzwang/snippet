# bootc

> Boot and upgrade via container images

- Git Repo
  - https://github.com/bootc-dev/bootc
  - podman-bootc
    - https://github.com/bootc-dev/podman-bootc
- Website
  - https://bootc.dev/bootc/
- CNCF
  - bootc was accepted to CNCF on January 21, 2025 at the Sandbox maturity level.
  - https://www.cncf.io/projects/bootc/

- 2024-09-24
  - bootc: Getting started with bootable containers
  - https://developers.redhat.com/articles/2024/09/24/bootc-getting-started-bootable-containers
- 2025-11-23
  - The Bootc Revolution: One Build Language for VMs and Containers
  - https://medium.com/@josephsims1/the-bootc-revolution-one-build-language-for-vms-and-containers-48ecdf7fc7e6

## 2026-05-10

**bootc** (bootable containers) is an open-source project and toolset designed to bridge the gap between **container images** and **bootable operating system images**.

It allows you to use standard container tools (like Docker, Podman, and container registries) to build, distribute, and update a full Linux operating system.

* * * *

### How It Works

The core philosophy of `bootc` is that "the container is the disk." Instead of managing an OS via traditional package managers (like `dnf` or `apt`) on every individual machine, you manage the OS like an application:

1.  **Build:** You create a `Dockerfile` (or Containerfile) starting from a bootable base image (e.g., Fedora ELN or RHEL).

2.  **Configure:** You add your users, SSH keys, drivers, and applications directly into the container image.

3.  **Push:** You push that image to a standard container registry.

4.  **Deploy/Update:** The target hardware (a physical server, VM, or edge device) pulls that container image and boots into it.

### Key Features

-   **Transactional Updates:** When you update the system, `bootc` pulls the new container image and prepares it in the background. If the update fails, the system can automatically roll back to the previous version.

-   **Immutable Infrastructure:** The system is intended to be "read-only" during runtime. Changes are made by updating the container image and redeploying, ensuring consistency across thousands of nodes.

-   **Standard Tooling:** You can use your existing CI/CD pipelines, security scanners, and registry mirrors that you already use for application containers.

-   **Hardware Booting:** Unlike a standard container that shares a host kernel, a `bootc` image contains (or pulls) the kernel and initramfs necessary to boot the actual hardware.

### Comparison: bootc vs. Traditional Containers

| **Feature** | **Standard Container (e.g., Docker)** | **bootc Image** |
| --- |  --- |  --- |
| **Kernel** | Shared with the Host | Includes/Manages its own Kernel |
| --- |  --- |  --- |
| **Runtime** | Requires a Container Engine (Podman/Docker) | Boots directly on the hardware/VM |
| **Scope** | Single Application/Microservice | Entire Operating System |
| **Updates** | `podman pull` / Restart container | `bootc update` / Reboot system |

### Use Cases

-   **Edge Computing:** Managing hundreds of remote devices where manual OS updates are risky.

-   **Cloud Infrastructure:** Creating consistent, reproducible VM images for autoscaling groups.

-   **Hybrid Environments:** Using the same workflow to manage both your applications and the underlying OS they run on.

If you are already familiar with **OSTree** or **Fedora IoT/Silverblue**, `bootc` is essentially the next evolution of that technology, moving away from specialized OSTree commits and toward the universal industry standard of **OCI (Open Container Initiative)** images.
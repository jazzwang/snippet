# WebGPU

- Git Repo
- Website

## 2026-06-06

- 研究

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
WebGPU
</td></tr><tr><td>A:</td><td>

[WebGPU API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)
[WebGPU | Chrome for Developers](https://developer.chrome.com/docs/web-platform/webgpu)
[Overview of WebGPU | Arm Learning Paths](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/android_webgpu_dawn/1-webgpu-fundamentals/)
[WebGPU Fundamentals](https://webgpufundamentals.org/webgpu/lessons/webgpu-fundamentals.html)

WebGPU is a modern web API that gives web applications low-level, high-performance access to the graphics processing unit (GPU). Developed by the W3C, it acts as the official successor to WebGL. Unlike its predecessor, WebGPU is designed from the ground up to map efficiently to modern native GPU frameworks like Microsoft Direct3D 12, Apple Metal, and Khronos Vulkan. [1, 2, 3, 4] 

### Key Capabilities & Core Differences

* First-Class Compute Shaders: WebGL struggled with general-purpose GPU computations (GPGPU). WebGPU features dedicated compute pipelines, allowing complex math, physics simulations, and AI/machine learning models to run directly in the browser up to three times faster. [1, 2, 5] 
* Reduced CPU Overhead: By utilizing modern explicit pipeline designs, WebGPU significantly reduces the amount of work the CPU has to do to prepare rendering calls. [1] 
* A New Shading Language (WGSL): It drops GLSL in favor of WebGPU Shading Language (WGSL), a robust, modern shading language tailored for web security and performance. [3, 6] 
* Predictable Error Handling: Instead of slow, synchronous error checking, WebGPU handles state validation asynchronously using "infectious error" scopes, which keeps the application running smoothly without killing frame rates. [5] 

### Architecture & Pipeline Overview

WebGPU operates on a strict object-oriented pipeline structure rather than a global state machine: [5, 7] 

   1. GPUAdapter: Represents the actual physical GPU hardware inside the device. [4, 5] 
   2. GPUDevice: The logical connection to the adapter used to create resources, pipelines, and command buffers. [4, 5] 
   3. Pipelines: WebGPU establishes distinct pathways to process data:
   * Render Pipeline: Feeds data through a vertex shader (positioning coordinates) and a fragment shader (calculating pixel colors) to render visuals onto a <canvas>.
      * Compute Pipeline: Processes general data structures in parallel across large arrays of hardware threads (workgroups) for calculations. [1, 8] 
   
### Ecosystem and Browser Support

The API has achieved critical mass across the industry and enjoys widespread software backing: [9, 10] 

* Browser Availability: Native support is fully shipped in major browsers like Google Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari across Windows, macOS, ChromeOS, and Android. [2, 11] 
* Framework Integration: Popular web 3D and data science libraries abstract the low-level complexity of WebGPU so you do not have to write hundreds of lines of boilerplate code:
* [Three.js](https://threejs.org/): Actively focusing core development on its dedicated WebGPU renderer alongside its new node-based material system (TSL).
   * Babylon.js: Features full production support for WebGPU out of the box.
   * [TensorFlow.js](https://www.tensorflow.org/): Employs an optimized WebGPU backend for massive speedups in browser-based AI model training and execution. [2, 12, 13, 14, 15] 
* Beyond the Web: Through open-source frameworks like Google's Dawn (C++) and Firefox's wgpu (Rust), developers can write code targeting WebGPU and compile it natively for desktop apps, server environments, or mobile platforms outside a standard browser context. [3, 7, 16] 

To explore documentation and starter projects, you can review the [W3C WebGPU Specification](https://www.w3.org/TR/webgpu/), learn the core mechanics via [MDN WebDocs](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API), or step through practical tutorials at [WebGPU Fundamentals](https://webgpufundamentals.org/). [2, 17] 
------------------------------
Are you looking to build a specific application with [WebGPU](https://webgpu.org/)? Let me know if you want to see a basic code boilerplate to get started, look at framework comparisons, or explore how to write compute shaders for AI and simulation!

[1] [https://developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)
[2] [https://developer.chrome.com](https://developer.chrome.com/docs/web-platform/webgpu/overview)
[3] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/WebGPU)
[4] [https://www.w3.org](https://www.w3.org/TR/webgpu/)
[5] [https://developer.mozilla.org](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGPU_API)
[6] [https://developer.apple.com](https://developer.apple.com/videos/play/wwdc2025/236/)
[7] [https://www.youtube.com](https://www.youtube.com/watch?v=oIur9NATg-I)
[8] [https://surma.dev](https://surma.dev/things/webgpu/)
[9] [https://jake-purton.uk](https://jake-purton.uk/collatz_blog/?utm_source=hnblogs.substack.com)
[10] [https://developer.chrome.com](https://developer.chrome.com/docs/web-platform/webgpu/build-app?hl=zh-tw)
[11] https://www.webgpu.com
[12] [https://www.youtube.com](https://www.youtube.com/watch?v=T6A-K9uLdIU)
[13] [https://webgpufundamentals.org](https://webgpufundamentals.org/webgpu/lessons/webgpu-fundamentals.html)
[14] [https://medium.com](https://medium.com/@addyosmani/photoshop-is-now-on-the-web-38d70954365a)
[15] [https://medium.com](https://medium.com/@ap3617180/transformers-js-make-the-users-laptop-pay-for-compute-80492a56ecfb)
[16] https://webgpu.org
[17] https://webgpufundamentals.org

</td></tr>
</table>
- Reference
  - 為什麼說 WebGPU 代表著 Web 的未來（現場演示🚀）
    - https://codelove.tw/@tony/post/xNgnK3
  - WebGPU Learning Website
    - https://www.webgpu.net/en/
  - Mozilla Developer - WebGPU API
    - https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API
  - Chrome Developer - Overview of WebGPU
    - https://developer.chrome.com/docs/web-platform/webgpu/overview
  - WebGPU Fundamentals
    - https://webgpufundamentals.org/
  - W3C - WebGPU
    - https://www.w3.org/TR/webgpu/
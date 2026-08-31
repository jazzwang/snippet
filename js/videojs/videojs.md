# Video.js — Project Overview & Feature Highlights

## Project Overview

**Video.js** is a free, open-source web video player and framework built on top of HTML5. Originally created by Steve Heffernan in May 2010 and currently at **v8.24.0**, it has grown into one of the most widely adopted video players on the web — used by millions of websites, serving billions of end-users monthly via its CDN-hosted copy alone, with 900+ contributors to the core project.

The project is licensed under the **Apache License 2.0** and maintained by a Technical Steering Committee (TSC). Corporate sponsorship has transitioned over the years from Zencoder (2010–2012) to Brightcove (2013–2025) to **Mux** (2025–present). A major **Video.js 10** release is planned for early 2026.

**Repository:** <https://github.com/videojs/video.js>
**Website:** <https://videojs.com>
**Docs:** <https://docs.videojs.com>

---

## Architecture at a Glance

Video.js is organized around a **component-based architecture**. The core modules include:

| Module | Purpose |
|---|---|
| `player.js` | Central Player class — orchestrates playback, events, and child components |
| `component.js` | Base class for all UI components (buttons, menus, sliders, etc.) |
| `tech/` | Playback technology abstraction (`html5.js` default tech, plus a `loader` and `middleware` layer) |
| `tracks/` | Text tracks (subtitles/captions/chapters), audio tracks, and video tracks |
| `control-bar/` | Full set of player controls (play, volume, progress, fullscreen, PiP, skip, playback rate, etc.) |
| `plugin.js` | Plugin system for extending the player |
| `menu/` | Reusable menu and menu-item components |
| `slider/` | Base slider component used by progress and volume bars |
| `utils/` | Shared utilities (DOM manipulation, events, formatting, logging, etc.) |

The player is assembled by composing components into a tree — the `ControlBar` contains the `PlayToggle`, `ProgressControl`, `VolumePanel`, `FullscreenToggle`, and others, all inheriting from `Component`.

---

## Feature Highlights

### 🎬 Universal Format Support
- Plays all common web media formats out of the box: **MP4, WebM, Ogg**.
- Native support for adaptive streaming: **HLS** and **DASH**.
- Extensible via the **Tech** abstraction layer — custom playback backends can be swapped in.

### 🧩 Plugin Ecosystem
- A rich plugin architecture (`plugin.js`) allows extending the player with custom behavior.
- Hundreds of community plugins available at [videojs.com/plugins](https://videojs.com/plugins/).
- Plugins can hook into lifecycle events, add UI components, or modify playback behavior.

### 📱 Cross-Platform & Responsive
- Works on desktops, mobile devices, tablets, and web-based Smart TVs.
- Responsive design adapts to any container size.
- **Spatial Navigation** support (`spatial-navigation.js`) for TV and remote-control interfaces.

### 🎨 Skinnable & Customizable UI
- Full CSS-based skinning system — ship your own look or use the default skin.
- Every UI element is a swappable `Component` — replace, extend, or remove any control.
- Includes **Title Bar**, **Big Play Button**, **Loading Spinner**, **Error Display**, **Modal Dialog**, **Poster Image**, and **Transient Button** as built-in components.

### 📝 Text Tracks & Accessibility
- Full **WebVTT** support for subtitles, captions, chapters, and descriptions.
- Built-in **Text Track Settings** panel — users can customize caption font, color, size, and background.
- Audio track and video track switching support.
- Keyboard-navigable controls with accessibility in mind.

### 🖼️ Picture-in-Picture & Fullscreen
- Native **Picture-in-Picture** toggle (`picture-in-picture-toggle.js`).
- Cross-browser **Fullscreen API** abstraction (`fullscreen-api.js`).

### ⏩ Playback Controls
- **Playback rate menu** — adjustable speed (0.5×, 1×, 1.5×, 2×, etc.).
- **Skip buttons** — configurable forward/backward skip.
- **Seek to Live** control for live streams.
- **Live Display** indicator with live tracker (`live-tracker.js`).

### 🌍 Internationalization
- Ships with **50+ language files** (Arabic, Chinese, French, German, Japanese, Spanish, and many more).
- Fully localizable UI strings.

### ⚡ Developer Experience
- **Zero-config quick start** — just add a `<video>` tag with `data-setup='{}'`.
- Programmatic API via `videojs('my-player', options, callback)`.
- **TypeScript definitions** included (`dist/types/video.d.ts`).
- Available via **npm**, **CDN** (Fastly, unpkg, cdnjs), or direct download.
- ES module (`video.es.js`) and CommonJS (`video.cjs.js`) builds.

### 🔌 Middleware Layer
- The `tech/middleware.js` system lets you intercept and transform playback operations (source selection, play/pause, seeking) — powerful for analytics, ad insertion, or custom source handling.

### 🧪 Quality & Community
- Comprehensive test suite with Karma.
- Cross-browser compatibility testing via **BrowserStack**.
- Active community on **Slack**, GitHub Discussions, and a detailed contributing guide.

---

## Quick Start

```html
<!-- Include via CDN -->
<link href="https://unpkg.com/video.js@8.24.0/dist/video-js.min.css" rel="stylesheet">
<script src="https://unpkg.com/video.js@8.24.0/dist/video.min.js"></script>

<!-- Drop in a video element -->
<video id="my-player" class="video-js" controls preload="auto" data-setup='{}'>
  <source src="video.mp4" type="video/mp4">
</video>
```

Or initialize programmatically:

```js
const player = videojs('my-player', { /* options */ }, function() {
  console.log('Player is ready!');
  this.play();
});
```

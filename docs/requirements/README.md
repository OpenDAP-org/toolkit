# Toolkit requirements

Requirements for the developer toolkit.

| ID | Requirement | Priority | Status |
|---|---|---|---|
| TK-001 | The toolkit runs on the developer host and is not shipped in DAP OS. | must | Confirmed |
| TK-002 | The T1 shall have its own ADB-style command-line tool covering everything an advanced user may want to do with the device. | must | Confirmed |

- ADB (Android Debug Bridge) is the reference for scope: shell, file transfer, installing and removing software, logs, port forwarding, screenshots and input, rebooting into recovery or flashing modes. The command set is not defined yet.
| TK-003 | The CLI command shall be `opendap`, with the aliases `dap` and `odap` installed only when those names are free on the host. | must | Confirmed |
| TK-004 | The CLI shall be a single Rust binary, portable or built per operating system. | must | Confirmed |
| TK-005 | The CLI shall install and uninstall through a `curl … | sh` script that detects the environment and selects the right binary. | must | Confirmed |
| TK-006 | The install script shall install the latest version by default and allow pinning a specific version. | must | Confirmed |
| TK-007 | The install script shall support the usual options: uninstall, verbose output and non-interactive mode, among others. | must | Confirmed |
| TK-008 | The CLI shall include a `doctor` command that checks its environment. | must | Confirmed |
| TK-009 | Every toolkit tool shall be agentic-first and human-friendly, and all of them shall share concepts, conventions and one domain model. | must | Confirmed |
- References for CLI design suggested by the maintainers: Cloudflare's new `cf` CLI and Forge. Research: `docs/research/2026-10-agentic-cli-design.md` (in progress).
| TK-010 | Toolkit tools and development in general shall officially support only UNIX / POSIX systems. | must | Confirmed |
| TK-011 | Toolkit tools shall be tested on macOS only. | must | Confirmed |
| TK-012 | Verification shall rely on simulations and on samples captured from sessions, on the virtual T1 now and on physical prototypes later. Dedicated lab instruments are not assumed. | must | Confirmed |
| TK-013 | The verification instrumentation proposed in `docs/research/2026-10-verification-instrumentation.md` is approved, except its lab instruments. | must | Confirmed |
- Audio without instruments: bit-perfect is a property of the digital stream, so it is verified by comparing captured bits. (1) Virtual T1: `snd-aloop` capture of the playback engine output, with negative controls. (2) Prototype: a passive tap of the I2S/DSD lines at test pads, captured by the board's RP2350 (PIO) and streamed to the host; a passive listener is not in the data path. (3) Analog output: recordings with a consumer USB audio interface, or with the recorder HAT's ADC, for relative measurements and regressions, not calibrated figures.
| TK-014 | Product-side 3D animations and interactive previews that do not need Blender may be standalone HTML documents using libraries such as three.js or anime.js. | must | Confirmed |
| TK-015 | Product presentation videos may be produced from the standalone HTML previews: captured frame by frame with Playwright and assembled with ffmpeg. | must | Confirmed |
- Video capture must be deterministic: the page's clock is stepped frame by frame (three.js clock, anime.js `seek`, a controlled `requestAnimationFrame`) instead of recording in real time, so every frame is exact regardless of host speed.

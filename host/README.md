# Developer host setup

Tools every OpenDAP contributor installs on their machine. Everything runs locally; there is no CI.

Officially supported: UNIX / POSIX systems. Tested on macOS only (TK-010, TK-011). Windows is not supported.

```sh
host/setup.sh
```

The script is safe to run again. It installs the Homebrew packages in [`Brewfile`](Brewfile), enables Git LFS, adds the Rust targets, installs the cargo tools and Interactive HTML BOM (inside KiCad's Python), and checks the design applications.

## Installed

| Area | Tools |
|---|---|
| Design | KiCad 10, FreeCAD 1.1, Blender 5.2 (official installers) |
| Fab outputs | `kicad-cli` (bundled with KiCad), Interactive HTML BOM |
| Repository hygiene | pre-commit, REUSE, Git LFS, gh, jq, yq |
| Simulation | ngspice; Python studies use `uv` with their own `pyproject.toml` |
| Firmware | rustup targets for aarch64 Linux (glibc, musl), Cortex-M0+, Cortex-M33 and RISC-V; probe-rs, picotool, dfu-util, OpenOCD, tio, sigrok-cli |
| Rust | cargo-binstall, cargo-nextest, cargo-deny |
| Emulation | QEMU |

## Installed later, when the phase needs them

Recommendations from [`docs/research/`](../docs/research/), not installed yet:

- **Layout:** openEMS (built from source), gerber2ems, Elmer FEM, scikit-rf and SignalIntegrity (per study).
- **Mechanical prototyping:** FreeCAD addons KiCad StepUp, SheetMetal and Fasteners (Addon Manager); CalculiX; slicers for the DIY kit.
- **Once the SoC is chosen:** uuu (i.MX) or rockusb (Rockchip), bmaptool, the DAP OS build container.
- **FPGA HATs:** OSS CAD Suite.
- **Bring-up:** PulseView, ngscopeclient, Tracy, Arm GNU Toolchain.
- **Production:** test frameworks and fixtures.

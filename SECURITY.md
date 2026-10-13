# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.4.x   | yes       |
| 0.3.x   | security only |
| < 0.3   | no        |

## Reporting a vulnerability

Email `security@aicomic.local` with a description, repro steps, and the affected
module. Do not open a public issue for anything exploitable.

We care about, in priority order:

- Arbitrary code execution via a malicious `.aicomic` project file or plugin.
- Path traversal in the export pipeline (`services/exporter.py`).
- Unsafe deserialization in `utils/serialization.py` (we use `json` + `safetensors`, never `pickle` for user data).
- Prompt-injection that escapes the sandboxed model runner into the host shell.
- Dependency confusion in `pyproject.toml`.

## Scope notes

The local model runner spawns a subprocess with a restricted working dir.
Any way to break that boundary is in scope. The GUI is not a security boundary —
it runs with the user's own privileges.

## Out of scope

- The content of generated strips (user's own prompts).
- Crashes on unsupported GPUs.
- Anything requiring an already-compromised host.
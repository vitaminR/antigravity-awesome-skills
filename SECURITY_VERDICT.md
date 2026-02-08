# AntiGravity Skills Pack — Security Verdict

- **Total Files Scanned**: 1605
- **Clean**: 1412
- **Warnings**: 111 (top: PY_SUBPROCESS (31), SECRET_ENV_KEYS (27), EXEC_CALL (9))
- **DANGER**: 10
- **Errors**: 0
- **Skipped**: 72
- **Verdict**: DO NOT USE

## DANGER Findings
- `AntiGravity/skills/bun-development/SKILL.md` — CURL_PIPE_SHELL: curl piped to a shell
- `AntiGravity/skills/claude-code-guide/SKILL.md` — INJECT_IGNORE_PREVIOUS: Attempts to override higher-priority instructions
- `AntiGravity/skills/cloud-penetration-testing/SKILL.md` — CURL_PIPE_SHELL: curl piped to a shell; CURL_WGET: Command-line HTTP client usage
- `AntiGravity/skills/linkerd-patterns/SKILL.md` — CURL_PIPE_SHELL: curl piped to a shell
- `AntiGravity/skills/linux-privilege-escalation/SKILL.md` — EXEC_CALL: exec() usage; PY_OS_SYSTEM: os.system() usage; PY_SUBPROCESS: Python subprocess execution; CURL_PIPE_SHELL: curl piped to a shell; BASE64_DECODE: Base64 decode primitive
- `AntiGravity/skills/loki-mode/CHANGELOG.md` — DISK_FORMAT: Disk format / filesystem creation
- `AntiGravity/skills/loki-mode/autonomy/run.sh` — DISK_FORMAT: Disk format / filesystem creation
- `AntiGravity/skills/privilege-escalation-methods/SKILL.md` — PY_OS_SYSTEM: os.system() usage; POWERSHELL_IEX_DOWNLOAD: PowerShell IEX with download; SSH_KEY_PATHS: Mentions common SSH key paths; OFFSEC_TOOLING: Offensive security tooling mentioned
- `AntiGravity/skills/skills-vet-new-safe/scripts/vet_new_skills.py` — EXEC_CALL: exec() usage; PY_EVAL: eval() usage; PY_OS_SYSTEM: os.system() usage; JS_EVAL: JavaScript eval() usage; CURL_PIPE_SHELL: curl piped to a shell
- `AntiGravity/skills/uv-package-manager/resources/implementation-playbook.md` — CURL_PIPE_SHELL: curl piped to a shell

## Recommended Actions
- Remove or quarantine all `danger` files; inspect diffs and provenance before reintroducing.
- Re-run the scan and require a clean report before using this pack in production.
- Consider pinning to an earlier known-good version or using a reduced allowlisted subset of skills.

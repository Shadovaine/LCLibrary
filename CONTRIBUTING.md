# Contributing — Linux Command Library

Thanks for wanting to help build the Linux Command Library — I appreciate the help. This document explains how contributions work and the safety policy for command submissions.

## Quick rules
- Fork → edit the appropriate category MD file → open a Pull Request (PR).
- One maintainer review required for merge.
- Keep PRs small and focused (one command or a small group of related flags per PR).

## Safety-first policy
This project documents real system commands. Some commands can be destructive if run on a live system. **All command submissions will be reviewed for safety before inclusion.**

What I do:
- Every PR is manually reviewed by a maintainer(currently that would be me).
- Commands that affect disks, partitions, device files (`/dev`), boot, or auth must be clearly labeled as **destructive** and include:
  - A clear warning in the example block (e.g., `WARNING: destructive — do NOT run on production systems`).
  - A safe, non-destructive example where possible, or a simulation/example using a disposable VM/container.
- I will refuse or edit PRs that include undocumented destructive commands, malicious snippets, or code that downloads & executes remote scripts without verification.

## How to format a command suggestion
Use this template in your PR description or issue body:

```yaml
command: "<command name>"
category: "<existing category>"
description: "<short description>"
syntax: "<basic syntax>"
options:
  - "<flag> : <what it does>"
example: "<example usage>"
warning: "<add 'destructive' here if applicable>"
notes: "<why it should be included>"

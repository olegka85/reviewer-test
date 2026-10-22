# Peerivo Reviewer — intentional defect video fixture

**This directory and the adjacent CI workflow are intentionally insecure.**
Demo-only, no real passwords, customer data, external scripts, or production integration.
Do not merge this branch into `master` before fixing it.

## What to film

1. Open the PR and show the changed files (Python, JavaScript, WordPress PHP, Symfony PHP, CI YAML).
2. Trigger/inspect Peerivo Reviewer on the PR. Report **only actual findings**: do not confuse a generic GitHub Actions failure with a Reviewer finding.
3. Show reproducible local regressions:
   - `python3 -m unittest discover -s demo/python -p 'test_*.py'` (2 expected failures before repair).
   - `node demo/javascript/auth.test.cjs` (1 expected failure before repair).
4. Explain why role bypass, SQL injection, excessive workflow permissions and unpinned action versions matter.
5. Fix the same files on this PR branch, push a fresh HEAD, rerun the tests and wait for Peerivo Reviewer to show a real PASS.

The remediation code and exact recording steps are described in the accompanying ChatGPT answer. An absent Reviewer status is not a successful review. `workflow_dispatch` means the demonstration workflow never auto-executes on PR events.

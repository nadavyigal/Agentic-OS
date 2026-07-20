#!/bin/sh
# Wrapper so the preview harness cannot pick the interpreter for us.
#
# Given a .py runtimeExecutable the harness invokes it as `python3 <file>`,
# resolving python3 from its own PATH, which lands on Xcode's bundled
# /Applications/Xcode.app/.../python3. That binary is denied TCC access to
# ~/Documents, so it fails with EPERM before it can even open the script.
#
# /usr/bin/python3 has the access, so we pin it explicitly here. No cd: the
# spawned shell may be unable to getcwd(), and the Python script chdir()s to
# its own resolved dashboard directory anyway.
exec /usr/bin/python3 "$(dirname "$0")/serve-portfolio-hq.py"

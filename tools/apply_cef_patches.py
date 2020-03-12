# Copyright (c) 2020 The Chromium Embedded Framework Authors.
# Portions copyright (c) 2006-2008 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import absolute_import
from __future__ import print_function
import os
import subprocess
import sys

# The CEF directory is the parent directory of _this_ script.
cef_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

print("\nGenerating CEF version header file...")
subprocess.check_call([
    sys.executable, os.path.join(cef_dir, 'tools/make_version_header.py'), '--header',
    'include/cef_version.h'
])

print("\nPatching build configuration and source files for CEF...")
subprocess.check_call([sys.executable, os.path.join(cef_dir, 'tools/patcher.py')])

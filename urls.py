#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2024/09/02 12:05:02
########################################################################


from app.demo.views import app as demo_app

# router
urlpatterns = [
    {"ApiRouter": demo_app, "prefix": "/demo", "tags": ["system_demo"]},
]
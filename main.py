#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2024/09/02 11:58:54
########################################################################


import fastapi
from fastapi import FastAPI
from typing import List
import urls



def create_app():
    """
    launch
    """
    app = FastAPI(
        title="Template",
        description="Fastapi-server-template",
        # lifespan=lifespan,
    )    
    # router
    for url in urls.urlpatterns:
        app.include_router(url["ApiRouter"], prefix=url["prefix"], tags=url["tags"])
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:create_app', host="0.0.0.0", port=6019, lifespan="on", factory=True)
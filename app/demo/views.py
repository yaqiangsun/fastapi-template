#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2024/09/02 12:05:58
########################################################################



from fastapi import APIRouter, Depends, Body, UploadFile, Request

app = APIRouter()


###########################################################
#    test route and interface
###########################################################
@app.post("/test")
async def test(user_name: str = Body(),user_password: str  = Body()):
    # raise Exception("This is a test exception.")
    return {"username": user_name}
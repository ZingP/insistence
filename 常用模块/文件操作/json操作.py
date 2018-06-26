#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/6/24

import json

a = {"a": 12, "b": 20}
with open("t.json", "w", encoding="utf-8") as f:
    json.dump(a, f)

with open("t.json", "r") as f:
    r = json.load(f)
    print(r)
with open("t.json", "w") as f:
    r["a"] = 3333
    json.dump(r, f)

with open("t.json", "r") as f:
    res = json.load(f)
    print(res)


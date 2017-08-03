#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/8/2
"""
windows环境下这个模块不行，Linux下可以，以后再更新。
"""
from M2Crypto.EVP import Cipher

cipher = Cipher(alg="aes_128_ecb", key="3242432resdwfwerqertwre",op=1)
print(cipher)



Experiment source code for the ACISP 2025 submission paper. The code is divided into two parts.

## Attack
In the attack/directory, the LDA and SDCA simulation codes against directly bitsliced dummy shuffling are included. 

### How to Run
1. Recover the entire 16-byte key using LDA `python LDA.py`
2. Recover the first byte of the key using SLDA `python SLDA.py`
3. Recover the first byte of the key using SFLDA `python SFLDA.py`

### Parameter
```python
# number of trace groups
exp_cnt = 200
# number of mask shares
mask = 2
# number of slots
slot_cnt = 4
# window size
window = 12
# number of parallel encrypted
n = 16
```

### Output Example
```plain
generated secret key: [163, 26, 53, 115, 13, 10, 38, 121, 12, 53, 8, 182, 213, 162, 31, 200]
collecting 32 traces
attacking 0 -th key
idx: 0 key byte: 163 match
attacking 1 -th key
idx: 1 key byte: 26 match
attacking 2 -th key
idx: 2 key byte: 53 match
attacking 3 -th key
idx: 3 key byte: 115 match
attacking 4 -th key
idx: 4 key byte: 13 match
attacking 5 -th key
idx: 5 key byte: 10 match
attacking 6 -th key
idx: 6 key byte: 38 match
attacking 7 -th key
idx: 7 key byte: 121 match
attacking 8 -th key
idx: 8 key byte: 12 match
attacking 9 -th key
idx: 9 key byte: 53 match
attacking 10 -th key
idx: 10 key byte: 8 match
attacking 11 -th key
idx: 11 key byte: 182 match
attacking 12 -th key
idx: 12 key byte: 213 match
attacking 13 -th key
idx: 13 key byte: 162 match
attacking 14 -th key
idx: 14 key byte: 31 match
attacking 15 -th key
idx: 15 key byte: 200 match
recovered key a31a35730d0a26790c3508b6d5a21fc8
   actual key a31a35730d0a26790c3508b6d5a21fc8
successful match!
```

## Generator
### How to Run
1. Generate white-box encryption program `./minimal.py`
2. Verify encryption correctness and encryption time `./buildrun.sh`

( Default parameters: number of slots is 2, masking scheme is $ x=x_1\oplus x_2 $, parallelism is 64 )

### Parameter
```python
# whether to mix boolean dummy shuffling
if_dummy = 0
# number of slots
slot = 2**1
# number of parallel encrypted
slice_cnt = 64

# masking
ct = mask_circuit(ct, MINQ(rand=rand))
ct = mask_circuit(ct, DOM(rand=rand, nshares=2))
```

### Reference
<font style="color:rgb(31, 35, 40);">The code references the work of </font>[https://github.com/cryptolu/whitebox/tree/master/algebraic_security_AC2018](https://github.com/cryptolu/whitebox/tree/master/algebraic_security_AC2018)<font style="color:rgb(31, 35, 40);">.</font>

### Output Example
```plain
Encrypting...

real    0m0.002s
user    0m0.002s
sys     0m0.000s

Ciphertext:
00000000: 5eb5 1d4c 66b4 d9ba 9d6a e348 269c bb13  ^..Lf....j.H&...
00000010: 01f5 d763 f79d 5596 54bf eb56 3349 b78a  ...c..U.T..V3I..
00000020: 1c80 a6aa 1199 0ab6 2341 d524 7d45 e09d  ........#A.$}E..
00000030: b834 4677 f7fc 23b5 4ff3 e3db d5aa bcc6  .4Fw..#.O.......
00000040: 4973 c82a a449 2538 358e 7a32 0dc6 a71b  Is.*.I%85.z2....
00000050: 08aa d82c 4097 2616 e899 e3db f30f db12  ...,@.&.........
00000060: 98ce 1cea 54c3 5e34 7a22 259e 83d6 1ad9  ....T.^4z"%.....
00000070: b77c 4386 4cef b60c 76aa 9193 095a 9ddf  .|C.L...v....Z..
00000080: a319 4ebc 2651 b072 f7c9 5aeb 41d0 f3ab  ..N.&Q.r..Z.A...
00000090: 1c54 675c 5005 c7da 1e17 2088 c30e 168f  .Tg\P..... .....
000000a0: ec9b f177 7bb8 29ce 45aa d5cb 14bf 909f  ...w{.).E.......
000000b0: 4ecc 7df8 7adc e766 cf13 9900 a195 20d7  N.}.z..f...... .
000000c0: d895 b9c1 b090 1df7 0077 5b58 0d49 7d75  .........w[X.I}u
000000d0: 2abf f4c4 6aff e89b b955 1d87 4b1a 7b3f  *...j....U..K.{?
000000e0: 3779 6c9b 4274 a9e7 12bc 74bb 8cd8 e663  7yl.Bt....t....c
000000f0: 6567 cc3e 9162 833b 31a6 c4c5 c2ee ba75  eg.>.b.;1......u
00000100: f21e e6e0 69f1 0b70 9a1c 294e 6efe 298f  ....i..p..)Nn.).
00000110: 2e93 a393 b074 573e 0033 d14c 6335 dd52  .....tW>.3.Lc5.R
00000120: 86a6 b67a 706c f8c1 ec91 75b7 1e1c d7b7  ...zpl....u.....
00000130: 2b50 b2bb dca8 34fb 1e03 afa5 0d84 01ab  +P....4.........
00000140: ab48 3303 0304 7e48 8f7e 6e9c 382c 79a9  .H3...~H.~n.8,y.
00000150: 29d8 accf 5f3e 1ae1 78e3 08db 07a4 f6f8  )..._>..x.......
00000160: f712 7a9a 66dd 07e5 70b3 3ad7 69c0 9ebe  ..z.f...p.:.i...
00000170: 580c 5870 f0fd 1469 836a 5532 9c20 f9fb  X.Xp...i.jU2. ..
00000180: dbcc 13ac dd94 25c2 9f82 4da0 c8f9 c605  ......%...M.....
00000190: 16bc ad70 8fcb 669b 91d0 041c 133a e2bf  ...p..f......:..
000001a0: 4ea4 1eb7 a9e4 10e2 7cc4 f8d5 c421 7cb4  N.......|....!|.
000001b0: 3d4c 5d73 0de7 9521 1f26 d684 c09b 4263  =L]s...!.&....Bc
000001c0: 12e6 dd3f d6a6 26f2 ca8b 9560 8b35 3af0  ...?..&....`.5:.
000001d0: f1f9 2aaf 069b 062c a9d3 b90c cb28 5556  ..*....,.....(UV
000001e0: a69f f9d1 f995 9fa2 3a38 7c26 7bfe 65f1  ........:8|&{.e.
000001f0: ca9f 9231 02a5 e685 eb13 24ad 1aaa 61d9  ...1......$...a.
00000200: 6c33 44db 6c7a 6360 5af7 eaef 9650 eaf2  l3D.lzc`Z....P..
00000210: cc92 8d8a 0b4f b3a7 ff25 db66 035a a3cb  .....O...%.f.Z..
00000220: f7b2 6653 2389 6bf1 e5d6 399d 6db6 eb48  ..fS#.k...9.m..H
00000230: f5c0 3d68 9a4b 20c2 2bca 0e9e f479 558c  ..=h.K .+....yU.
00000240: cf2f 4ecb 1f11 f3a7 8640 0ea1 29b0 ee4b  ./N......@..)..K
00000250: 311a 570b 48ea 11e9 e3aa 8bb6 0723 280b  1.W.H........#(.
00000260: 5019 6736 d203 b45e d01d a19b b4d0 4b52  P.g6...^......KR
00000270: c53d d4fb be7d af38 0bb3 5769 d7a3 9715  .=...}.8..Wi....
00000280: 0357 daf5 6f0c 438c 7b43 4709 b0aa d3b6  .W..o.C.{CG.....
00000290: 905b f0b1 d42b 7809 d09a 64bd dd33 e409  .[...+x...d..3..
000002a0: 2174 e6b1 76b5 2368 de8b 61ab e2ca 91a9  !t..v.#h..a.....
000002b0: 0511 af7a 3baa 5fc3 1343 b46f f8e7 6ade  ...z;._..C.o..j.
000002c0: fccc e60c 62b6 cc12 f53d a16c 1a36 5925  ....b....=.l.6Y%
000002d0: 41fe 5249 5c05 5f79 bdc3 daa3 7c60 4848  A.RI\._y....|`HH
000002e0: 4c1f b0b7 8582 0bab 4821 3591 89d2 8cfe  L.......H!5.....
000002f0: 89e6 58c3 e9dd b587 89e0 8736 e0f6 fd55  ..X........6...U
00000300: 0c08 4c51 6e07 b076 f385 7c6d 0b0f 67f1  ..LQn..v..|m..g.
00000310: 0fb4 969e a3b0 b5b3 7161 1d78 4749 b3c9  ........qa.xGI..
00000320: 04ef bf35 180d b364 a9a4 b38b 9c93 46ab  ...5...d......F.
00000330: 9cec 3dea 1f2e 65c9 d912 ed2e b485 aede  ..=...e.........
00000340: b1cf 43b0 8a7b f199 f769 2e22 1c6e d2ab  ..C..{...i.".n..
00000350: cced b2d7 4dd2 5e05 f4e4 ff64 b479 986c  ....M.^....d.y.l
00000360: 9556 7604 42c4 1c39 cdc4 441c fda4 9761  .Vv.B..9..D....a
00000370: 3609 449d b89d 2dbf 3945 ee00 807d 33d0  6.D...-.9E...}3.
00000380: c45d 4cc9 2edb 6fbf 70c2 2427 6175 c21b  .]L...o.p.$'au..
00000390: 6115 9939 bf24 1e6c 9eb9 1650 fb33 7e88  a..9.$.l...P.3~.
000003a0: 6194 97b9 5d87 55e7 286c 3ecf 43e3 6426  a...].U.(l>.C.d&
000003b0: f255 faa6 be01 8eaa d64d 5995 acb1 6362  .U.......MY...cb
000003c0: 1558 a356 b7a0 0d11 ec8f a0ff 3c47 c2da  .X.V........<G..
000003d0: 759b bf27 67d6 b708 4366 1f2e caa0 117c  u..'g...Cf.....|
000003e0: 610b 2b79 739c 8c59 6ae9 3a5e cc9e cb04  a.+ys..Yj.:^....
000003f0: 9633 9a15 9c23 2fa9 5e95 e674 97b9 8051  .3...#/.^..t...Q
test_ciphertext:
00000000: 5eb5 1d4c 66b4 d9ba 9d6a e348 269c bb13  ^..Lf....j.H&...
00000010: 01f5 d763 f79d 5596 54bf eb56 3349 b78a  ...c..U.T..V3I..
00000020: 1c80 a6aa 1199 0ab6 2341 d524 7d45 e09d  ........#A.$}E..
00000030: b834 4677 f7fc 23b5 4ff3 e3db d5aa bcc6  .4Fw..#.O.......
00000040: 4973 c82a a449 2538 358e 7a32 0dc6 a71b  Is.*.I%85.z2....
00000050: 08aa d82c 4097 2616 e899 e3db f30f db12  ...,@.&.........
00000060: 98ce 1cea 54c3 5e34 7a22 259e 83d6 1ad9  ....T.^4z"%.....
00000070: b77c 4386 4cef b60c 76aa 9193 095a 9ddf  .|C.L...v....Z..
00000080: a319 4ebc 2651 b072 f7c9 5aeb 41d0 f3ab  ..N.&Q.r..Z.A...
00000090: 1c54 675c 5005 c7da 1e17 2088 c30e 168f  .Tg\P..... .....
000000a0: ec9b f177 7bb8 29ce 45aa d5cb 14bf 909f  ...w{.).E.......
000000b0: 4ecc 7df8 7adc e766 cf13 9900 a195 20d7  N.}.z..f...... .
000000c0: d895 b9c1 b090 1df7 0077 5b58 0d49 7d75  .........w[X.I}u
000000d0: 2abf f4c4 6aff e89b b955 1d87 4b1a 7b3f  *...j....U..K.{?
000000e0: 3779 6c9b 4274 a9e7 12bc 74bb 8cd8 e663  7yl.Bt....t....c
000000f0: 6567 cc3e 9162 833b 31a6 c4c5 c2ee ba75  eg.>.b.;1......u
00000100: f21e e6e0 69f1 0b70 9a1c 294e 6efe 298f  ....i..p..)Nn.).
00000110: 2e93 a393 b074 573e 0033 d14c 6335 dd52  .....tW>.3.Lc5.R
00000120: 86a6 b67a 706c f8c1 ec91 75b7 1e1c d7b7  ...zpl....u.....
00000130: 2b50 b2bb dca8 34fb 1e03 afa5 0d84 01ab  +P....4.........
00000140: ab48 3303 0304 7e48 8f7e 6e9c 382c 79a9  .H3...~H.~n.8,y.
00000150: 29d8 accf 5f3e 1ae1 78e3 08db 07a4 f6f8  )..._>..x.......
00000160: f712 7a9a 66dd 07e5 70b3 3ad7 69c0 9ebe  ..z.f...p.:.i...
00000170: 580c 5870 f0fd 1469 836a 5532 9c20 f9fb  X.Xp...i.jU2. ..
00000180: dbcc 13ac dd94 25c2 9f82 4da0 c8f9 c605  ......%...M.....
00000190: 16bc ad70 8fcb 669b 91d0 041c 133a e2bf  ...p..f......:..
000001a0: 4ea4 1eb7 a9e4 10e2 7cc4 f8d5 c421 7cb4  N.......|....!|.
000001b0: 3d4c 5d73 0de7 9521 1f26 d684 c09b 4263  =L]s...!.&....Bc
000001c0: 12e6 dd3f d6a6 26f2 ca8b 9560 8b35 3af0  ...?..&....`.5:.
000001d0: f1f9 2aaf 069b 062c a9d3 b90c cb28 5556  ..*....,.....(UV
000001e0: a69f f9d1 f995 9fa2 3a38 7c26 7bfe 65f1  ........:8|&{.e.
000001f0: ca9f 9231 02a5 e685 eb13 24ad 1aaa 61d9  ...1......$...a.
00000200: 6c33 44db 6c7a 6360 5af7 eaef 9650 eaf2  l3D.lzc`Z....P..
00000210: cc92 8d8a 0b4f b3a7 ff25 db66 035a a3cb  .....O...%.f.Z..
00000220: f7b2 6653 2389 6bf1 e5d6 399d 6db6 eb48  ..fS#.k...9.m..H
00000230: f5c0 3d68 9a4b 20c2 2bca 0e9e f479 558c  ..=h.K .+....yU.
00000240: cf2f 4ecb 1f11 f3a7 8640 0ea1 29b0 ee4b  ./N......@..)..K
00000250: 311a 570b 48ea 11e9 e3aa 8bb6 0723 280b  1.W.H........#(.
00000260: 5019 6736 d203 b45e d01d a19b b4d0 4b52  P.g6...^......KR
00000270: c53d d4fb be7d af38 0bb3 5769 d7a3 9715  .=...}.8..Wi....
00000280: 0357 daf5 6f0c 438c 7b43 4709 b0aa d3b6  .W..o.C.{CG.....
00000290: 905b f0b1 d42b 7809 d09a 64bd dd33 e409  .[...+x...d..3..
000002a0: 2174 e6b1 76b5 2368 de8b 61ab e2ca 91a9  !t..v.#h..a.....
000002b0: 0511 af7a 3baa 5fc3 1343 b46f f8e7 6ade  ...z;._..C.o..j.
000002c0: fccc e60c 62b6 cc12 f53d a16c 1a36 5925  ....b....=.l.6Y%
000002d0: 41fe 5249 5c05 5f79 bdc3 daa3 7c60 4848  A.RI\._y....|`HH
000002e0: 4c1f b0b7 8582 0bab 4821 3591 89d2 8cfe  L.......H!5.....
000002f0: 89e6 58c3 e9dd b587 89e0 8736 e0f6 fd55  ..X........6...U
00000300: 0c08 4c51 6e07 b076 f385 7c6d 0b0f 67f1  ..LQn..v..|m..g.
00000310: 0fb4 969e a3b0 b5b3 7161 1d78 4749 b3c9  ........qa.xGI..
00000320: 04ef bf35 180d b364 a9a4 b38b 9c93 46ab  ...5...d......F.
00000330: 9cec 3dea 1f2e 65c9 d912 ed2e b485 aede  ..=...e.........
00000340: b1cf 43b0 8a7b f199 f769 2e22 1c6e d2ab  ..C..{...i.".n..
00000350: cced b2d7 4dd2 5e05 f4e4 ff64 b479 986c  ....M.^....d.y.l
00000360: 9556 7604 42c4 1c39 cdc4 441c fda4 9761  .Vv.B..9..D....a
00000370: 3609 449d b89d 2dbf 3945 ee00 807d 33d0  6.D...-.9E...}3.
00000380: c45d 4cc9 2edb 6fbf 70c2 2427 6175 c21b  .]L...o.p.$'au..
00000390: 6115 9939 bf24 1e6c 9eb9 1650 fb33 7e88  a..9.$.l...P.3~.
000003a0: 6194 97b9 5d87 55e7 286c 3ecf 43e3 6426  a...].U.(l>.C.d&
000003b0: f255 faa6 be01 8eaa d64d 5995 acb1 6362  .U.......MY...cb
000003c0: 1558 a356 b7a0 0d11 ec8f a0ff 3c47 c2da  .X.V........<G..
000003d0: 759b bf27 67d6 b708 4366 1f2e caa0 117c  u..'g...Cf.....|
000003e0: 610b 2b79 739c 8c59 6ae9 3a5e cc9e cb04  a.+ys..Yj.:^....
000003f0: 9633 9a15 9c23 2fa9 5e95 e674 97b9 8051  .3...#/.^..t...Q
Difference:
==========
```






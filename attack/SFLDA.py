# mask ab^c
from sage.all import *
import matplotlib.pyplot as plt
import numpy as np
exp_cnt = 800
mask = 3
slot_cnt = 4
window = 6
n = 16
pic = [800]
key = [int(randrange(256)) for _ in range(16)]
# key = [162, 5, 0, 1, 7, 7, 3, 4, 5, 5, 6, 9, 4, 20, 4, 1]
print("generated secret key:", key)

sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
        0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
        0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
        0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
        0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
        0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
        0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
        0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
        0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
        0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
        0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
        0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
        0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
        0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
        0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
        0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
        0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
        0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
        0x54, 0xbb, 0x16]

def trace(main_slot, pt):
    # main_slot = int(randrange(slot_cnt))
    res = []
    res += [randrange(256) for _ in range(main_slot*16)]
    res += [sbox[b ^ k] for b, k in zip(pt, key)]
    res += [randrange(256) for _ in range((slot_cnt-1-main_slot)*16)]
    res_mask = []
    for v in res:
        res_mask += [randrange(2) for _ in range(8*mask*4)]
        for bit_pos in range(8):
            bit = (v >> bit_pos) & 1
            
            a = randrange(2)
            b = randrange(2)
            res_mask.append(a)
            res_mask.append(b)
            bit ^= (a&b)
            
            res_mask.append(bit)

    return vector(GF(2), res_mask)


cnt_pair = [[0 for _ in range(2 ** 8)] for _ in range(16 * 8 * mask * slot_cnt*5*0.18)]
cnt_k = [0] * (2 ** 8)

for exp_i in range(exp_cnt):
    # print("win =", window,"exp_i", exp_i)
    main_slot = int(randrange(slot_cnt))
    t = []
    pts = []

    for _ in range(n):
        pt = [int(randrange(256)) for _ in range(16)]
        pts.append(pt)
        t.append(trace(main_slot, pt))

    ones_column = vector(GF(2), [1] * n)

    # just 1 bit (idx=0)
    # slice window
    for k in range(256):
        # print(k)
        target = []
        for i in range(n):
            out = sbox[pts[i][0] ^ k]
            target.append(out & 1)
        target = vector(GF(2), target)
        for startpos in range(int(len(t[0])*0.18)):
            # print("startpos", startpos)
            mat = matrix(t[i][startpos : startpos + window] for i in range(n))
            mat = mat.augment(ones_column)
            
            for col in range(mat.ncols()-1):
                filtered_rows = []
                filtered_target = []

                for row_idx in range(mat.nrows()):
                    if mat[row_idx][col] == 0:
                        filtered_rows.append(mat[row_idx])
                        filtered_target.append(target[row_idx])

                if filtered_target:
                    filtered_mat = matrix(filtered_rows)

                    try:
                        if filtered_mat.solve_right(vector(GF(2), filtered_target)):
                            cnt_k[k] += 1
                            cnt_pair[startpos][k] += 1
                    except ValueError:
                        continue

    if (exp_i+1) in pic:
        print("win =", window, "exp_i =",exp_i)
        print("   actual key", "".join("%02x" % c for c in key))
        max_value = max(cnt_k)
        max_index = cnt_k.index(max_value)
        print("recovered the first byte of the key ", hex(max_index))

        max_values = []
        blue_values = []
        for start in range(len(cnt_pair)):
            max_val = max(cnt_pair[start][k] for k in range(256) if k != key[0])
            max_values.append(max_val)
            blue_values.append(cnt_pair[start][key[0]])
        print("max_values", max_values)
        print("blue_values", blue_values)
        x = np.arange(len(max_values))
        plt.figure(figsize=(10, 6))
        plt.bar(x, max_values, color='gray', width=1, label='Wrong Key', align='center')
        plt.bar(x, blue_values, color='blue', width=1, label='Correct Key', align='center', alpha=0.7)
        plt.legend()
        plt.xlabel('Window')
        plt.ylabel('Count')
        plt.savefig(f'picf/cnt_pair_w{window}_exp{exp_i+1}.pdf')
        plt.savefig(f'picf/cnt_pair_w{window}_exp{exp_i+1}.png')

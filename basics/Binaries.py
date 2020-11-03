# bitwise operator:& | ^ >> <<
'''
1024 512 256 128 64 32 16 8 4 2 1
0    0   0   0   1  0  1  1 0 1 0 >>90
0    0   0   0   1  1  1  1 0 1 0 >> 122>> rich
0    0   0   0   1  1  0  0 0 1 0 >> 98>> shine
0    0   0   0   0  0  1  1 0 0 0 >> 24>> rich
0    0   0   0   1  1  1  1 0 1 0 >> 122>> shine
0    0   0   0   0  0  0  0 1 1 1 >> 7
0    0   0   0   1  1  0  0 0 1 0 >> 98 >> rich
1 1    0   0   0   1  0  0  0 0 0 0
0    0   0   0   0  0  1  0 1 0 0 >> 20
0    0   0   0   0  0  1  0 0 0 0 >> 16
0    0   0   0   0  0  1  1 1 1 0 >> 30
0    0   0   0   1  1  1  1 1 0 0 >> 124
0    0   0   0   0  1  0  1 1 0 1 >> 45
0    0   0   0   1  1  0  1 1 1 1 >> 111
'''

alpha=90

print(alpha,bin(alpha))

rich=122
shine=98

print(rich,shine)

print(rich&20)

print(shine|45)

print(shine^30)

rich^=shine#rich=rich^shine
shine^=rich
rich^=shine

print(rich,shine)

print(shine>>4)

print(rich<<5)
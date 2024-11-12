n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
c = [0] * (n + 1)

for i in range(1, n + 1):
  a[i], b[i], c[i] = map(int, input().split())

dpa = [0] * (n + 1) 
dpb = [0] * (n + 1)
dpc = [0] * (n + 1)

dpa[1] = a[1]
dpb[1] = b[1]
dpc[1] = c[1]

for i in range(2, n + 1):
  dpa[i] = a[i] + max(dpb[i - 1], dpc[i - 1])
  dpb[i] = b[i] + max(dpa[i - 1], dpc[i - 1])
  dpc[i] = c[i] + max(dpa[i - 1], dpb[i - 1])

print(max(dpa[n], dpb[n], dpc[n]))

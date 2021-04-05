###### Calculator EIGRP Metric ########
             #( •̀ ω •́ )✧#

def bandwitch(bw):
	return 10000000 // bw

def delay(dy1, dy2):
	return (dy1 + dy2) // 10

b = int(input("Input Slowest Bandwidth = "))
d1 = int(input("Input First Delay = "))
d2 = int(input("Input Second Delay = "))

result = (bandwitch(b) + delay(d1, d2)) * 256
print("Result EIGRP Metric = ", result)
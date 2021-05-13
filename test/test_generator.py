f = open(r"/home/christian/repos/kafka-demo/test/test_03.in", "w")
i = 1

while (i <= 1000):
    f.write("new_object\n")
    i+=1

i = 1

while (i <= 1000):
    f.write("get_tags " + str(i) + "\n")
    i+=1

f.close
import fileinput

a = []
for key, line in enumerate(fileinput.input()):
    if key == 0:
        no_USB = int(line)
    elif key == 1:
        file_size = int(line)
    else:
        a.append(int(line))

a_sorted = sorted(a, reverse=True)

mb_to_go = file_size
USB_count = 0

for i in range(no_USB):
    if mb_to_go == 0:
        break
    #     print('-----')
    #     print('MB left init:', mb_to_go)
    #     print('Cap:', a_sorted[i])
    if a_sorted[i] > mb_to_go:
        mb_to_go = 0
        USB_count += 1
        break
    else:
        mb_to_go = mb_to_go - a_sorted[i]
        if mb_to_go < 0:
            mb_to_go = 0
        USB_count += 1
    # print('MB left after:', mb_to_go)

print(USB_count)
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

height = 0

while blocks > 0:
    blocks -= height + 1
    if blocks>0:height += 1

print("The height of the pyramid:", blocks, height)

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
layer_blocks = 1  # Start with the first layer requiring 1 block

while blocks >= layer_blocks:
    blocks -= layer_blocks
    height += 1
    layer_blocks += 1  # Each new layer needs one more block than the previous layer

print("The height of the pyramid:", height)

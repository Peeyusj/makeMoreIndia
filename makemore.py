import torch  # PyTorch library - like numpy but better for neural networks

with open('indian_names.csv', 'r') as f:
    content = f.read()

lines = content.splitlines()

# We want to store just the names in a new list
names = []
# Loop through lines
# But we skip lines[0] because it's the header ',Name'
# So we start from index 1
for i in range(1, len(lines)):
    line = lines[i]  # e.g., '0,aabid'
    name = line.split(',')[1]  # e.g., 'aabid'
    names.append(name)

chars = '.abcdefghijklmnopqrstuvwxyz'
stoi = {}

for i, ch in enumerate(chars):
    stoi[ch] = i

print(stoi)
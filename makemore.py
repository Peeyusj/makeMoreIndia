import torch  # PyTorch library - like numpy but better for neural networks

with open('indian_names.csv', 'r') as f:
    content = f.read()

lines = content.splitlines()

chars = '.abcdefghijklmnopqrstuvwxyz'
stoi = {}

for i, ch in enumerate(chars):
    stoi[ch] = i

# We want to store just the names in a new list
names = []
# Loop through lines
# But we skip lines[0] because it's the header ',Name'
# So we start from index 1
for i in range(1, len(lines)):
    line = lines[i]  # e.g., '0,aabid'
    name = line.split(',')[1]  # e.g., 'aabid'
    if all(ch in stoi for ch in name):
        names.append(name)


# Create 27x27 matrix filled with zeros
# torch.zeros(rows, cols) creates a matrix
N = torch.zeros((27, 27), dtype=torch.int32)

for name in names:
    name_with_dots = '.' + name + '.'
    
    for i in range(len(name_with_dots) - 1):
        ch1 = name_with_dots[i]
        ch2 = name_with_dots[i + 1]
        
        row = stoi[ch1]
        col = stoi[ch2]
        
        N[row][col] += 1


# Get row 0 (what follows '.')
row = N[0]

# Normalize - divide each count by total
prob = row / row.sum()

# Create reverse mapping: number → letter
itos = {}
for ch, i in stoi.items():
    itos[i] = ch

# Sample one letter based on probabilities
idx = torch.multinomial(prob, num_samples=1).item()


# Generate one name
name = ''
current = 0  # start at '.' (index 0)

while True:
    # Get probabilities for current character's row
    row = N[current]
    prob = row / row.sum()
    
    # Sample next character
    next_idx = torch.multinomial(prob.float(), num_samples=1).item()
    
    # If we sampled '.', name is complete
    if next_idx == 0:
        break
    
    # Otherwise, add letter to name
    name += itos[next_idx]
    
    # Move to next character
    current = next_idx

print(name)
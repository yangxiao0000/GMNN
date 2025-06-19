import torch
a=torch.tensor([1,2,3])
b=a.clone()
a[1]=3
print(b)
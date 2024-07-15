import torch
x = torch.rand(3,3)
y = torch.rand(3,3)
if torch.cuda.is_available():
   x = x.cuda()
   y = y.cuda()
   sum = x+y
print(sum)

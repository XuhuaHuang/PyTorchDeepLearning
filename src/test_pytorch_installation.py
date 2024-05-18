# -*- coding: utf-8 -*-
# https://pytorch.org/get-started/locally/

# %%
import torch


print(torch.__version__)

x = torch.rand(5, 3)
print(x)

# %%
torch.cuda.is_available()

import torch
import torch.nn as nn
import torch.nn.functional as F
import ebayesthresh

class ebayesthresh_nn(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,input):
        return ebayesthresh.ebayesthresh(input,sdev=None)
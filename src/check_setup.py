import sys
import torch
import torchvision
import gradio

print("Python:", sys.version)
print("PyTorch:", torch.__version__)
print("Torchvision:", torchvision.__version__)
print("Gradio:", gradio.__version__)

x = torch.rand(3, 224, 224)
print("test tensor shape:", x.shape)

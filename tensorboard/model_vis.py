from torch.utils.tensorboard import SummaryWriter
import torch
import torchvision

model = torchvision.models.resnet50()
dummy_input = torch.zeros((1, 3, 224, 224))

train_writer = SummaryWriter('exp1/train'), comment='train')

train_writer.add_graph(model, dummy_input)

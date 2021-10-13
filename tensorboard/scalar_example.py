
from torch.utils.tensorboard import SummaryWriter
import random

train_writer = SummaryWriter('exp1/train'), comment='train')
val_writer = SummaryWriter('exp1/val'), comment='val')

for epoch in range(100):
    loss = random.random()
    train_writer.add_scalar('Loss', loss, epoch)

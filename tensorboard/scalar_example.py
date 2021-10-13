from torch.utils.tensorboard import SummaryWriter
import random

train_writer = SummaryWriter('exp1/train', comment='train')
val_writer = SummaryWriter('exp1/val', comment='val')

for epoch in range(100):
    loss = random.random()
    val_loss = random.random()+0.5
    train_writer.add_scalar('Loss', loss, epoch)
    val_writer.add_scalar('Loss', val_loss, epoch)

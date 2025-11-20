"""
Write your app here.

The folder where all datasets are stored is "/workspace/input", and it is read-only.
The folder where you need to store your output is "/workspace/output", and it is writable.
"""
from mipcandy import NNUNetDataset
from aip.arch.swinunet.swinunet_sliding_trainer import SwinUNetTrainer
from torch.utils.data import DataLoader

if __name__ == "__main__":
    f = open("/workspace/output/progress.txt", "w")
    print("started")
    f.write("started")
    dataset, val_dataset = NNUNetDataset("/workspace/data/nnUNet_raw/Dataset101_AdomenCT1K").fold()
    train_loader = DataLoader(dataset, batch_size=2, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False)

    trainer = SwinUNetTrainer("experiments", train_loader, val_loader, device="cpu")
    trainer.train(200, note="Large volume segmentation with sliding windows")
    f.write("completed")

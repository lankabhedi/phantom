import segmentation_models_pytorch as smp
import torch

def get_unet_model():
    """
    Initializes a U-Net model with a pre-trained ResNet-34 backbone.
    """
    print("Initializing U-Net model with ResNet-34 backbone...")
    model = smp.Unet(
        encoder_name="resnet34",
        encoder_weights="imagenet",
        in_channels=3,
        classes=1, # Binary segmentation: road vs background
    )
    return model

if __name__ == "__main__":
    model = get_unet_model()
    print("Model initialized successfully.")
    # Check if GPU is available (relevant for AMD Ryzen AI but torch usually sees NPU as CPU/other)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model.to(device)
    model.eval()

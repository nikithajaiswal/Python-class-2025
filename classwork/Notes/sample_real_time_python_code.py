"""
YOLO Model Training Script

This script is designed to train a YOLO model using a dataset specified in a YAML file. It includes:
- Checking for CUDA availability to use GPU if available.
- Training with augmentation, hyperparameter tuning, and early stopping.
- Refactored into a class-based structure for better reusability and readability.

Steps included:
1. Initialize the YOLOTrainer class.
2. Load a pretrained YOLO model.
3. Train the model with the specified parameters.
4. Save the trained model.
5. Measure total training time.
"""

import torch
from ultralytics import YOLO
import time

class YOLOTrainer:
    """
    A class to handle the training of a YOLO model.

    Attributes:
        data_path (str): Path to the dataset YAML file.
        pretrained_model_path (str): Path to the pretrained YOLO model or YOLO variant.
        device (str): Device to use for training ('cuda' or 'cpu').
        output_model_path (str): Path to save the trained model.
    """

    def __init__(self, data_path, pretrained_model_path, output_model_path):
        """
        Initialize the YOLOTrainer class with the required paths and detect the device.

        Args:
            data_path (str): Path to the dataset YAML file.
            pretrained_model_path (str): Path to the pretrained YOLO model or YOLO variant.
            output_model_path (str): Path to save the trained model.
        """
        self.data_path = data_path
        self.pretrained_model_path = pretrained_model_path
        self.output_model_path = output_model_path
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self):
        """
        Load the YOLO model using the specified pretrained model path.

        Returns:
            YOLO: The loaded YOLO model instance.
        """
        print(f"Using device: {self.device}")
        return YOLO(self.pretrained_model_path)

    def train_model(self, model, epochs=200, batch_size=16, optimizer="Adam", learning_rate=0.001, patience=50, seed=42):
        """
        Train the YOLO model with specified hyperparameters.

        Args:
            model (YOLO): YOLO model instance to train.
            epochs (int): Number of epochs for training (default: 200).
            batch_size (int): Batch size for training (default: 16).
            optimizer (str): Optimizer to use ('SGD' or 'Adam') (default: 'Adam').
            learning_rate (float): Initial learning rate (default: 0.001).
            patience (int): Early stopping patience (default: 50).
            seed (int): Random seed for reproducibility (default: 42).

        Returns:
            YOLO: Trained YOLO model instance.
        """
        start_time = time.time()
        print("Starting training...")

        results = model.train(
            data=self.data_path,
            epochs=epochs,
            device=self.device,
            augment=True,
            batch=batch_size,
            optimizer=optimizer,
            lr0=learning_rate,
            patience=patience,
            val=True,
            seed=seed
        )

        end_time = time.time()
        print("Training completed.")
        print("Total time taken (minutes):", (end_time - start_time) / 60)
        return model

    def save_model(self, model):
        """
        Save the trained YOLO model to the specified path.

        Args:
            model (YOLO): Trained YOLO model instance.
        """
        model.save(self.output_model_path)
        print(f"Model saved to {self.output_model_path}")

if __name__ == "__main__":
    # Define paths
    DATA_PATH = r"/home/ruchik_k/damage identification/yolo_cause_of_damage/data.yaml"
    PRETRAINED_MODEL_PATH = 'yolov8n.pt'
    OUTPUT_MODEL_PATH = 'yolov8_test.pt'

    # Initialize the YOLOTrainer class
    trainer = YOLOTrainer(DATA_PATH, PRETRAINED_MODEL_PATH, OUTPUT_MODEL_PATH)

    # Load the model
    model = trainer.load_model()

    # Train the model
    trained_model = trainer.train_model(model, epochs=200, batch_size=16, optimizer='Adam', learning_rate=0.001, patience=50, seed=42)

    # Save the trained model
    trainer.save_model(trained_model)

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset
from torch import nn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from safetensors.torch import save_file, load_file

# Dataset simulasi yang diperbanyak
X = np.array([
    [5, 2, 80, 75],
    [3, 1, 60, 55],
    [10, 3, 90, 85],
    [7, 2, 85, 70],
    [4, 1, 50, 45],
    [12, 3, 95, 90],
    [6, 2, 70, 60],
    [15, 3, 85, 88],
    [2, 1, 40, 35],
    [8, 3, 80, 78],
    [9, 2, 65, 68],
    [1, 1, 30, 25],
    [11, 3, 95, 90],
    [5, 2, 70, 65],
    [13, 3, 88, 85],
    [7, 1, 55, 58],
    [14, 2, 92, 95],
    [3, 1, 45, 42],
    [10, 3, 85, 82],
    [12, 2, 78, 75],
    [6, 2, 60, 55],
    [9, 2, 80, 77],
    [7, 2, 72, 70],
    [4, 1, 50, 48],
    [11, 3, 94, 92],
    [5, 2, 65, 63],
    [8, 2, 75, 72],
    [2, 1, 40, 37],
    [13, 3, 90, 88],
    [6, 1, 55, 53],
    [14, 3, 96, 93]
], dtype=np.float32)

y = np.array([
    0, 0, 1, 1, 0, 1, 0,
    1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1,
    0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1
])

# Normalisasi data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data untuk pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Dataset dan DataLoader
train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.long))
test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.long))
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)

# Arsitektur model yang lebih kompleks
class GraduationPredictor(nn.Module):
    def __init__(self):
        super(GraduationPredictor, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return torch.softmax(self.fc3(x), dim=1)

# Inisialisasi model, loss function, dan optimizer
model = GraduationPredictor()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    epoch_loss = 0
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        output = model(X_batch)
        loss = criterion(output, y_batch)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    
    # Print loss setiap 10 epoch
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {epoch_loss/len(train_loader):.4f}")

# Simpan model dalam format safetensors setelah selesai training
model_path = "graduation_predictor_model.safetensors"
save_file(model.state_dict(), model_path)
print(f"Model has been saved to {model_path}")

# Meload model dari file safetensors
loaded_model = GraduationPredictor()
loaded_state_dict = load_file(model_path)
loaded_model.load_state_dict(loaded_state_dict)
loaded_model.eval()  # Set model ke mode evaluasi

# Evaluasi model di data uji
correct = 0
total = 0
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        output = loaded_model(X_batch)
        _, predicted = torch.max(output, 1)
        total += y_batch.size(0)
        correct += (predicted == y_batch).sum().item()

accuracy = 100 * correct / total
print(f"Accuracy on test data: {accuracy:.2f}%")

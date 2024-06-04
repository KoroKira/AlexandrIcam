import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.Wf = np.random.randn(input_size + hidden_size, hidden_size)
        self.Wi = np.random.randn(input_size + hidden_size, hidden_size)
        self.Wo = np.random.randn(input_size + hidden_size, hidden_size)
        self.Wc = np.random.randn(input_size + hidden_size, hidden_size)
        self.Uf = np.random.randn(hidden_size, hidden_size)
        self.Ui = np.random.randn(hidden_size, hidden_size)
        self.Uo = np.random.randn(hidden_size, hidden_size)
        self.Uc = np.random.randn(hidden_size, hidden_size)
        self.bf = np.random.randn(hidden_size)
        self.bi = np.random.randn(hidden_size)
        self.bo = np.random.randn(hidden_size)
        self.bc = np.random.randn(hidden_size)
        self.h = np.zeros(hidden_size)
        self.c = np.zeros(hidden_size)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, x):
        self.x = x
        self.f = self.sigmoid(np.dot(np.hstack((x, self.h)), self.Wf) + np.dot(self.h, self.Uf) + self.bf)
        self.i = self.sigmoid(np.dot(np.hstack((x, self.h)), self.Wi) + np.dot(self.h, self.Ui) + self.bi)
        self.o = self.sigmoid(np.dot(np.hstack((x, self.h)), self.Wo) + np.dot(self.h, self.Uo) + self.bo)
        self.c_tilde = self.tanh(np.dot(np.hstack((x, self.h)), self.Wc) + np.dot(self.h, self.Uc) + self.bc)
        self.c = self.f * self.c + self.i * self.c_tilde
        self.h = self.o * self.tanh(self.c)
        return self.h

class Seq2Seq:
    def __init__(self, input_size, hidden_size, output_size):
        self.encoder = LSTM(input_size, hidden_size)
        self.decoder = LSTM(input_size, hidden_size)
        self.linear = np.random.randn(hidden_size, output_size)
        self.softmax = lambda x: np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)
    
    def forward(self, inputs):
        encoder_outputs = []
        for x in inputs:
            encoder_output = self.encoder.forward(x)
            encoder_outputs.append(encoder_output)
        decoder_outputs = []
        decoder_input = np.zeros(inputs[0].shape)
        for encoder_output in encoder_outputs:
            decoder_output = self.decoder.forward(decoder_input)
            decoder_outputs.append(decoder_output)
            decoder_input = decoder_output
        output = np.dot(np.array(decoder_outputs), self.linear)
        return self.softmax(output)

class CrossEntropyLoss:
    def __init__(self):
        pass
    
    def forward(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
        loss = -np.sum(y_true * np.log(y_pred)) / len(y_true)
        return loss
    
    def backward(self):
        return self.y_pred - self.y_true

class SGD:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
    
    def step(self, model):
        for param in vars(model).values():
            if isinstance(param, np.ndarray):
                param -= self.learning_rate * param.grad

# Fonction d'entraînement du modèle
def train(model, loss_fn, optimizer, inputs, targets, epochs, learning_rate):
    for epoch in range(epochs):
        total_loss = 0
        for i in range(len(inputs)):
            x = inputs[i]
            y_true = targets[i]
            # Forward pass
            y_pred = model.forward(x)
            loss = loss_fn.forward(y_pred, y_true)
            total_loss += loss
            # Backward pass
            gradient = loss_fn.backward()
            # Update model parameters
            model.backward(gradient)
            optimizer.step(model)
        avg_loss = total_loss / len(inputs)
        print(f'Epoch {epoch + 1}, Loss: {avg_loss:.4f}')

# Fonction d'évaluation du modèle
def evaluate(model, loss_fn, inputs, targets):
    total_loss = 0
    correct = 0
    for i in range(len(inputs)):
        x = inputs[i]
        y_true = targets[i]
        # Forward pass
        y_pred = model.forward(x)
        loss = loss_fn.forward(y_pred, y_true)
        total_loss += loss
        # Calcul de la prédiction
        predicted_class = np.argmax(y_pred)
        true_class = np.argmax(y_true)
        if predicted_class == true_class:
            correct += 1
    avg_loss = total_loss / len(inputs)
    accuracy = correct / len(inputs)
    print(f'Loss: {avg_loss:.4f}, Accuracy: {accuracy:.4f}')

# Fonction pour charger les données
def load_data(file_path):
    inputs = []
    targets = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            input_text, target_text = line.strip().split('\t')
            inputs.append(input_text)
            targets.append(target_text)
    return inputs, targets

# Exemple d'utilisation pour charger les données
file_path = '/Users/guilhem/Documents/GitHub/AlexandrIcam/test-ia/data.txt'
inputs, targets = load_data(file_path)

# Exemple d'utilisation
input_size = 10
hidden_size = 20
output_size = 5
seq2seq_model = Seq2Seq(input_size, hidden_size, output_size)
loss_fn = CrossEntropyLoss()
optimizer = SGD(learning_rate=0.01)
train(seq2seq_model, loss_fn, optimizer, inputs, targets, epochs=10, learning_rate=0.01)
test_inputs = [np.random.randn(input_size) for _ in range(20)]
test_targets = [np.eye(output_size)[np.random.randint(output_size)] for _ in range(20)]
evaluate(seq2seq_model, loss_fn, test_inputs, test_targets)

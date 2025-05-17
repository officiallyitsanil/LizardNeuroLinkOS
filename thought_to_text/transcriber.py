import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.logger import log_info

# Dummy vocabulary and tokenizer simulation
VOCAB = ['hello', 'world', 'from', 'mind', 'neuro', 'link', 'lizard']
WORD_TO_INDEX = {w: i+1 for i, w in enumerate(VOCAB)}
INDEX_TO_WORD = {i+1: w for i, w in enumerate(VOCAB)}

def simple_rnn_model(vocab_size=len(VOCAB)+1, embed_dim=8, rnn_units=16):
    model = Sequential([
        Embedding(vocab_size, embed_dim, input_length=5),
        LSTM(rnn_units, return_sequences=True),
        LSTM(rnn_units),
        Dense(vocab_size, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Placeholder trained model
model = simple_rnn_model()

def get_thought_text():
    # Simulate thought-to-text transcription by generating a random sequence
    seq_length = 5
    generated_indices = np.random.choice(list(INDEX_TO_WORD.keys()), seq_length)
    words = [INDEX_TO_WORD[i] for i in generated_indices]
    text = ' '.join(words)
    log_info(f"[ThoughtToText] Transcribed thought: '{text}'")
    return text

# tokviz/visualization.py
from IPython.display import HTML, display
from transformers import AutoTokenizer

def token_visualizer(text, models=['gpt-2']):
    """
    Compares tokenization patterns across different language models and visualizes the results.

    Args:
        text (str): The input text to tokenize and compare.
        models (list): A list of language model names or identifiers to compare.
                       Default is ['gpt-2'].
    """
    for model in models:
        tokenizer = AutoTokenizer.from_pretrained(model)
        tokens = tokenizer.tokenize(text)
        token_colors = get_token_colors(tokens)
        
        num_tokens = len(tokens)
        num_chars = len(text)
        
        display(HTML(f"<h2>Model: {model}</h2>"))
        display(HTML(f"<p><b>Number of Tokens:</b> {num_tokens}</p>"))
        display(HTML(f"<p><b>Number of Characters:</b> {num_chars}</p>"))
        
        visualize_tokens(tokens, token_colors)

def visualize_tokens(tokens, token_colors):
    """
    Visualizes tokenized text with color-coded highlighting.

    Args:
        tokens (list): List of tokens.
        token_colors (dict): Dictionary mapping tokens to their corresponding colors.
    """
    colored_text = ""
    for token in tokens:
        color = token_colors[token]
        colored_text += f'<span style="background-color: {color}; padding: 2px;">{token}</span> '
    display(HTML(colored_text))

def get_token_colors(tokens):
    """
    Generates colors for tokens in the input text.

    Args:
        tokens (list): List of tokens.

    Returns:
        dict: Dictionary mapping tokens to their corresponding colors.
    """
    unique_tokens = list(set(tokens))
    token_colors = {token: number_to_color(hash(token)) for token in unique_tokens}
    return token_colors

def number_to_color(number):
    """
    Generates a color based on a numerical value.

    Args:
        number (int): The numerical value.

    Returns:
        str: A color value in HSL format.
    """
    golden_ratio_conjugate = 0.618033988749895
    a = 1664525
    c = 1013904223
    m = 2**32

    pseudorandom = (a * number + c) % m
    hue = ((pseudorandom * golden_ratio_conjugate) % 1) * 360
    s = 60 + (pseudorandom % 21)
    l = 70 + (pseudorandom % 21)

    return f"hsl({hue}, {s}%, {l}%)"

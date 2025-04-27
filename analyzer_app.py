from tkinter import *
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    user_text = text_area.get("1.0", "end-1c")
    
    if not user_text:
        result_label.config(text="Please enter some text.")
        return

    # Create a TextBlob object and analyze the sentiment
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        result = "Positive"
    elif polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    
    # Display the result
    result_label.config(text=f"Sentiment: {result}\nPolarity: {polarity:.2f} | Subjectivity: {subjectivity:.2f}")

# Initialize main window
root = Tk()
root.title("Sentiment Analyzer")
root.geometry("500x400")

# Create widgets
title_label = Label(root, text="Text Sentiment Analyzer", font=("Helvetica", 16), pady=20)
title_label.pack()

text_area = Text(root, height=10, width=40, wrap=WORD)
text_area.pack()

analyze_button = Button(root, text="Analyze", font=("Helvetica", 12), command=analyze_sentiment)
analyze_button.pack(pady=10)

clear_button = Button(root, text="Clear", font=("Helvetica", 12), command=lambda: text_area.delete("1.0", END))
clear_button.pack(pady=5)

result_label = Label(root, text="", font=("Helvetica", 12), pady=10)
result_label.pack()

# Start the Tkinter event loop
root.mainloop()


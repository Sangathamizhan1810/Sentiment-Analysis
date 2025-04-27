Sentiment Analyzer - Tkinter GUI Application
Overview :
This project is a Sentiment Analyzer built using Python's TextBlob library and a simple Tkinter GUI. It allows users to enter text and get a sentiment analysis that classifies the input as Positive, Negative, or Neutral. The sentiment analysis also displays polarity and subjectivity scores.

Requirements :
To run this project, you need to have the following Python libraries installed:
Tkinter (for the GUI)
TextBlob (for sentiment analysis)
pip (for installing the required libraries)

Install the necessary libraries:
bash
Copy
Edit
pip install textblob
Note: Tkinter is typically bundled with Python, so it might already be installed. If not, it can usually be installed through your package manager (e.g., sudo apt-get install python3-tk for Linux).

How to Use :
Clone or download the repository to your local machine.

Install the required dependencies.

Run the sentiment_analyzer.py script:
bash
Copy
Edit
python sentiment_analyzer.py
A window will open where you can type any text you want to analyze. Click the "Analyze" button to get the sentiment result.

The result will show the sentiment type (Positive, Negative, or Neutral) along with the polarity and subjectivity values.

Functionality :
Text Input: Enter the text you want to analyze in the text field.
Analyze Button: Click this button to perform the sentiment analysis.
Clear Button: Clears the input text and result.

Example Outputs :
Sentiment: Positive
Polarity: 0.35
Subjectivity: 0.60

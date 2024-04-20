from textblob import TextBlob

class EmotionsAnalyzer:
    def analyze(self,text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "\x1b[1;32m"+"Positive"+"\x1b[0;37m"
        elif analysis.sentiment.polarity == 0:
            return "\x1b[1;33m"+"neutral"+"\x1b[0;37m"
        else:
            return "\x1b[1;31m"+"negative"+"\x1b[0;37m"
        
analyzer = EmotionsAnalyzer()
while True:
    text = input("\x1b[1;33m"+"Type about your feelings of today: " + "\x1b[0;37m")
    result = analyzer.analyze(text)
    print(result)
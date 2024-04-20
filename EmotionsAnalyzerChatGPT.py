import openai

openai.api_key = "your chatgpt api key"

system_init = '''Act as if you were a sentimen analyzer
                so, i will send you messages and you 
                are going to analyze the text in that message
                at the end you have to return with at least one character and 4 as maximun (only numerical answers, can only be ints or floats). where -1 is maximum negativity, 0 is neutral and 1 is maximun positivity '''

messages = [{"role":"system", "content":system_init}]

class Emotion:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.name)


class EmotionsAnalyzer:
    def __init__(self,ranges):
        self.ranges = ranges

    def Analyze(self,polarity):
        for range,sentimiento in self.ranges:
            if range[0] < polarity <= range[1]:
                return emotion  
        return Emotion("Very positive","32")

ranges = [
    ((-1,-0.6),Emotion("Very Negative","31")),
    ((-0.6,-0.3),Emotion("Negative","31")),
    ((-0.3,-0.1),Emotion("Somewhat Negative","31")),
    ((-0.1,0.1),Emotion("Neutral","33")),
    ((0.1,0.3),Emotion("Somewhat Positive","32")),
    ((0.3,0.6),Emotion("Positive","32")),
]

analyzer = EmotionsAnalyzer(ranges)

while True:
    user_promt = input("\x1b[1;33m"+"Type about your feelings of today: " + "\x1b[0;37m")
    messages.append({"role":"user","content": user_promt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 8
    )

    response = completion.choices[0].message["content"]
    messages.append({"role":"assistant","content": response})

    emotion = EmotionsAnalyzer.Analyze(float(response))
    print(emotion)
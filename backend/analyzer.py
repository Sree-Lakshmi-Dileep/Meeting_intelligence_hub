def analyze_transcript(text):
    words= text.split()
    return{
        "word_count":len(words)
    }
text = """ana
John: We will finish API by Friday.
Sarah: I will test security.
"""

result = analyze_transcript(text)

print(result)
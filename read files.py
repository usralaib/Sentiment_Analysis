# utilisation de la library nrc pou la emotion list



# Assign list of strings
text = ['hate', 'lovely', 'person', 'worst']

# Iterate through list
for i in range(len(text)):
    # Create object
    emotion = NRCLex(text[i])

    # Classify emotion
    print('\n\n', text[i], ': ', emotion.raw_emotion_scores)


text = "My name is Eve,I come from chennai,India,Iam here for research work."

sentences = text.split(',')

longest_sentence = max(sentences, key=len)

print("The longest sentence is:", longest_sentence)

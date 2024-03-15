def decode(message_file):
    with open(message_file, "r") as red:
        lines = red.readlines()
  
    hidden_message = []

    for x in range(100):
        hidden_message.append('')

    for line in lines:
        number = int(line.split()[0])
        for x in range(100):
            if number == (int((x * x + x)/2)):
                hidden_message[x] = line.split()[1]
                break

    text = ""

    for x in hidden_message:
        if x != '':
            text = text + x + " "

    return text

decoded_message = decode("encoded_message.txt")
print(decoded_message)

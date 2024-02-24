from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Chatpot")

# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the spanish corpus
#trainer.train("chatterbot.corpus.spanish")

trainer = ListTrainer(chatbot)
trainer.train(["Hola", "Bienvenid@ 🤗"])
trainer.train(["¿Cómo estás?", "Bien, ¿y tu?"])
trainer.train(["¿Como estas?", "Bien, ¿y tu?"])
trainer.train(["¿Qué es la sífilis?", "La sífilis, llamada antiguamente morbo gálico, mal francés o enfermedad de Kenn, es una enfermedad infecciosa de curso crónico, transmitida principalmente por contacto sexual, producida por la espiroqueta Treponema pallidum, subespecie pallidum (pronunciado pál lidum). Sus manifestaciones clínicas son de características e intensidad fluctuantes, apareciendo y desapareciendo en las distintas etapas de la enfermedad: úlceras en los órganos sexuales y manchas rojas en el cuerpo. Produce lesiones en el sistema nervioso y en el aparato circulatorio."])
trainer.train(["¿Qué es SIDA?", "El síndrome de inmunodeficiencia adquirida (SIDA) es una afección crónica que pone en riesgo la vida provocada por el virus de la inmunodeficiencia humana (VIH). Al dañar tu sistema inmunitario, el VIH interfiere con la capacidad de tu cuerpo para luchar contra infecciones y enfermedades.El VIH es una infección de trasmisión sexual. También puede trasmitirse por el contacto con sangre infectada y por inyectarse drogas ilícitas o por compartir agujas. Además, puede trasmitirse de madre a hijo durante el embarazo, el trabajo de parto o la lactancia. "])
trainer.train(["¿Qué es el SIDA?", "El síndrome de inmunodeficiencia adquirida (SIDA) es una afección crónica que pone en riesgo la vida provocada por el virus de la inmunodeficiencia humana (VIH). Al dañar tu sistema inmunitario, el VIH interfiere con la capacidad de tu cuerpo para luchar contra infecciones y enfermedades.El VIH es una infección de trasmisión sexual. También puede trasmitirse por el contacto con sangre infectada y por inyectarse drogas ilícitas o por compartir agujas. Además, puede trasmitirse de madre a hijo durante el embarazo, el trabajo de parto o la lactancia. "])
trainer.train(["Chao", "Para terminar escribe quit o exit"])
exit_conditions = (":q", "quit", "exit")
print("Este es el chatbot que brinda información sobre las ETS. Escribe a continuación")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"😀 {chatbot.get_response(query)}")

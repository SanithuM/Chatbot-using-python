import wikipedia
import pyttsx3
import datetime
import random
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to a female voice
rate = engine.getProperty('rate')  # Get the current rate
engine.setProperty('rate', rate-50)  # Decrease the rate by 50 words per minute

print("Hello! I'm Phoenix. How can I help you today ? ")
engine.say("Hello! I'm Phoenix. How can I help you today ?")
engine.runAndWait()


class Bot:


    def get_fun_fact(self):
        facts = [
            "A cockroach can live for several weeks without its head.",
            "A group of flamingos is called a flamboyance.",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
            "A baby octopus is about the size of a flea when it is born.",
            "The oldest known vegetable is the pea.",
            "A flock of crows is known as a murder.",
            "A group of rhinos is known as a crash.",
            "A group of hedgehogs is known as a prickle.",
            "The word ‘nerd’ was first coined by Dr. Seuss in the book ‘If I Ran the Zoo’.",
            "A group of jellyfish is called a smack.",
            "A group of flamingos is called a flamboyance.",
            "The population of the earth is about 8 billion people, but there are an estimated 10 quintillion (that's 10,000,000,000,000,000,000) ants!",
            "Cats have over 30 different muscles in each ear, allowing them to swivel their ears in all directions.",
            "Benjamin Franklin invented the bifocals because he was tired of switching between his near and farsighted glasses.",
            "The world's oldest piece of chewing gum is over 9,000 years old! It was made from birch bark tar.",
            "There is a species of jellyfish that is biologically immortal – the Turritopsis dohrnii. After reaching maturity, it can revert back to its polyp stage if it gets injured or stressed.",
            "The kangaroo is the only mammal that can hop",
            "The dot over the letter i is called a tittle.",
            "The world's quietest room is located at Microsoft's headquarters in Washington. It's so quiet you can hear your own heartbeat!",
        ]
        return random.choice(facts)


bot = Bot()

while True:
    # Get user input
    user_input = input("> ")

    # Check if the user wants to quit
    if user_input.lower() in ("bye", "exit", "quit"):
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    #Check if the user wants to chat
    if user_input.lower() in ("Hello", "Hi", "hi", "hello", 'Hey', "hey"):
        engine.say("Hello sir! How can i help you today?")
        engine.runAndWait()
    
    #Check if the user wants to know you
    if user_input.lower() in("what is your name?"):
        engine.say("I'm Phenix")
        engine.runAndWait()

    # Check if the user wants to know the current time
    if "what's the time" in user_input.lower() or "what is the time now" in user_input.lower():
        now = datetime.datetime.now()
        time_string = now.strftime("%H:%M")
        print(f"The time is {time_string}.")
        engine.say(f"The time is {time_string}.")
        engine.runAndWait()

    #Chech if the user wants to know a fun fact
    elif "give me a fun fact" in user_input.lower():
        print(bot.get_fun_fact())
        engine.say(bot.get_fun_fact())
        engine.runAndWait()

    #open whatsapp
    if user_input.lower() in("open whatsapp"):
        from AppOpener import open
        open("whatsapp") # Opens whatsapp
        engine.say("opening whatsapp")
        engine.runAndWait()

    #open mail
    if user_input.lower() in("open mail"):
        from AppOpener import open
        open("mail") # Opens mail
        engine.say("opening mail")
        engine.runAndWait()

    #open chrome
    if user_input.lower() in("open chrome"):
        from AppOpener import open
        open("google chrome") # Opens google chrome
        engine.say("opening chrome")
        engine.runAndWait()

    #open file
    if user_input.lower() in("open file"):
        from AppOpener import open
        open("file explorer") # Opens file explorer
        engine.say("opening file")
        engine.runAndWait()

    #open camera
    if user_input.lower() in("open camera"):
        from AppOpener import open
        open("camera") # Opens camera
        engine.say("opening camera")
        engine.runAndWait()

    #close camera
    if user_input.lower() in("close camera"):
        from AppOpener import close
        close("camera") # closes camera
        engine.say("close camera")
        engine.runAndWait()



        

    else:
        # Look up the user's query on Wikipedia
        try:
            result = wikipedia.summary(user_input, sentences=2)
            print(result)
            engine.say(result)
            engine.runAndWait()
        except wikipedia.exceptions.DisambiguationError as e:
            print("Can you please be more specific?")
            engine.say("Can you please be more specific?")
            engine.runAndWait()
        except wikipedia.exceptions.PageError as e:
            print("Sorry, I couldn't find a Wikipedia page for that.")
            engine.say("Sorry, I couldn't find a Wikipedia page for that.")
            engine.runAndWait()
        except Exception as e:
            print("Sorry, something went wrong:", e)
            engine.say("Sorry, something went wrong.")
            engine.runAndWait()




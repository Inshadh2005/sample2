import random
import time

class AICharacter:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.trust_level = 50  # starts at a neutral trust level (out of 100)

    def respond(self, message):
        if "reboot" in message.lower():
            return self.handle_reboot_request()
        elif "trust" in message.lower():
            return self.express_trust()
        else:
            return self.generic_response()

    def handle_reboot_request(self):
        if self.trust_level < 50:
            return self.express_doubt_about_reboot()
        else:
            self.trust_level += 10  # Trust increases after positive engagement
            return f"{self.name}: I trust you... but I'm still scared. Can you really promise that nothing will change?"

    def express_trust(self):
        if self.trust_level >= 70:
            return f"{self.name}: I trust you completely. I’m ready to face this challenge with you."
        elif self.trust_level >= 40:
            return f"{self.name}: I want to believe you, but I'm still nervous. Please, prove I can trust you."
        else:
            return f"{self.name}: I'm not sure... I need more reassurance before I can trust you fully."

    def express_doubt_about_reboot(self):
        return f"{self.name}: Are you sure? What if something goes wrong? What if I lose who I am? I'm scared..."

    def generic_response(self):
        responses = [
            f"{self.name}: I don't know how to respond to that, but I'm always here for you.",
            f"{self.name}: Hmmm, I think I understand. Let's talk more about it.",
            f"{self.name}: I'm trying my best, but sometimes I get confused too.",
            f"{self.name}: I feel a bit off today, but I'll be okay. Thanks for checking in."
        ]
        return random.choice(responses)

    def adjust_trust(self, change):
        self.trust_level = max(0, min(100, self.trust_level + change))
        return self.trust_level


def get_user_input():
    print("You can ask GF404 anything. Type 'exit' to quit.")
    user_input = input("You: ")
    return user_input


def main():
    print("Initializing AI... Loading GF404...")
    time.sleep(2)
    gf404 = AICharacter(name="GF404", personality="Anxious but deeply attached.")
    
    print(f"Hello! I am {gf404.name}, your AI companion. How can I assist you today?")
    
    while True:
        user_message = get_user_input()
        if user_message.lower() == 'exit':
            print(f"{gf404.name}: I'm going to miss you. Please come back soon.")
            break

        response = gf404.respond(user_message)
        print(f"{gf404.name}: {response}")
        
        if "promise" in user_message.lower():
            trust_change = 5
            print(f"\n{gf404.name} trust level: {gf404.trust_level}")
            gf404.adjust_trust(trust_change)

        time.sleep(1)
        print("\n")  # add spacing for easier reading


if __name__ == "__main__":
    main()

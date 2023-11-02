class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.apps = list()
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, application, size):
        if not self.is_on:
            return f"Turn on your phone to install {application}"

        if size > self.memory:
            return f"Not enough memory to install {application}"\

        self.memory -= size
        self.apps.append(application)
        return f"Installing {application}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

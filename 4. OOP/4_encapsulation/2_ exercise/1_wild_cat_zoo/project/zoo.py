from animal import Animal
from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet
from worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = sum(w.salary for w in self.workers)
        if salaries_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_care_expenses_sum = sum(a.money_for_care for a in self.animals)
        if animals_care_expenses_sum > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_care_expenses_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"

        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"

        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets)

        return result

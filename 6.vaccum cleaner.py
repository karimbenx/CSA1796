class VacuumCleaner:
    def __init__(self):
        self.location = 0
        self.cleaned = 0

    def clean(self, environment):
        for i in range(len(environment)):
            if environment[self.location]:
                self.cleaned += 1
                environment[self.location] = 0
            self.location = (self.location + 1) % len(environment)

def main():
    environment = [1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    cleaner = VacuumCleaner()
    cleaner.clean(environment)
    print("Cleaning complete.")
    print("Total dirt cleaned:", cleaner.cleaned)

if __name__ == "__main__":
    main()

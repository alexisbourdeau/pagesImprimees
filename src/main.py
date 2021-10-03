# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Imprimante:
    def __init__(self, name):
        self.name = name

    def imprimer_rec(self, page_list, result="", last_terme=""):
        if len(page_list) == 1:
            return result + str(page_list[0])
        else:
            premier_terme = page_list.pop(0)
            deuxième_terme = page_list[0]
            if last_terme == ";" and premier_terme + 1 == deuxième_terme:
                return self.imprimer_rec(page_list, result + str(premier_terme) + "-", "-")
            elif last_terme == ";" and premier_terme + 1 != deuxième_terme:
                return self.imprimer_rec(page_list, result + str(premier_terme) + ";", ";")
            elif last_terme == "-" and premier_terme + 1 == deuxième_terme:
                return self.imprimer_rec(page_list, result, "-")
            elif last_terme == "-" and premier_terme + 1 != deuxième_terme:
                return self.imprimer_rec(page_list, result + str(premier_terme) + ";", ";")
            elif last_terme == "" and premier_terme + 1 == deuxième_terme:
                return self.imprimer_rec(page_list, str(premier_terme) + "-", "-")
            elif last_terme == "" and premier_terme + 1 != deuxième_terme:
                return self.imprimer_rec(page_list, str(premier_terme) + ";", ";")

    def imprimer(self, page_list):
        page_list.pop(0)
        return self.imprimer_rec(page_list, [], "")


if __name__ == '__main__':
    print('PyCharm')

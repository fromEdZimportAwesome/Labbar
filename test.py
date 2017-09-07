import pandas as pd

class Lag(object):

    def __init__(self, namn, spelade_matcher = 0, vunna_matcher = 0, förlorade_matcher = 0):
        self.namn = namn
        self.spelade_matcher = spelade_matcher
        self.vunna_matcher = vunna_matcher
        self.förlorade_matcher = förlorade_matcher
        self.målskillnad = self.vunna_matcher - self.förlorade_matcher
        self.oavgjorda_matcher = self.spelade_matcher - (self.vunna_matcher + self.förlorade_matcher)
        self.poäng = 3*self.vunna_matcher + self.oavgjorda_matcher

    def vinst(self):
        self.spelade_matcher += 1
        self.vunna_matcher += 1
        self.poäng += 3

    def förlust(self):
        self.spelade_matcher += 1
        self.förlorade_matcher += 1

    def oavgjort(self):
        self.spelade_matcher += 1
        self.oavgjorda_matcher += 1
        self.poäng += 1



class Liga(object):
    tabellen = pd.read_excel('Fotbollsserie.xlsx')
    def __init__(self):
        pass

    def sort_liga(self):
        pass
ligan = Liga()
ligan.tabellen.sort_values(by='P', ascending=[False], inplace=True)
print(ligan.tabellen.ix[0:2])
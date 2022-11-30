from Quotes import *

from random import choice

print("")

Input_Author = input("Enter name: ")

print("")

if Input_Author == DrSeuss:
    print(choice(DrSeuss_Quotes))
    print("~", DrSeuss)

if Input_Author == MarcusAurelius:
    print(choice(MarcusAurelius_Quotes))
    print("~", MarcusAurelius)

if Input_Author == Epictetus:
    print(choice(Epictetus_Quotes))
    print("~", Epictetus)

if Input_Author == Socrates:
    print(choice(Socrates_Quotes))
    print("~", Socrates)

if Input_Author == Aristotle:
    print(choice(Aristotle_Quotes))
    print("~", Aristotle)

if Input_Author == FriedrichNietzsche:
    print(choice(FriedrichNietzsche_Quotes))
    print("~", FriedrichNietzsche)

if Input_Author == JeanPaulSartre:
    print(choice(JeanPaulSartre_Quotes))
    print("~", JeanPaulSartre)

if Input_Author == SigmundFreud:
    print(choice(SigmundFreud_Quotes))
    print("~", SigmundFreud)

if Input_Author == FranzKafka:
    print(choice(FranzKafka_Quotes))
    print("~", FranzKafka)

if Input_Author == HarukiMurakami:
    print(choice(HarukiMurakami_Quotes))
    print("~", HarukiMurakami)

if Input_Author == JohnIrving:
    print(choice(JohnIrving_Quotes))
    print("~", JohnIrving)

if Input_Author == VictorHugo:
    print(choice(VictorHugo_Quotes))
    print("~", VictorHugo)

if Input_Author == ErnestHemingway:
    print(choice(ErnestHemingway_Quotes))
    print("~", ErnestHemingway)

if Input_Author == EmileZola:
    print(choice(EmileZola_Quotes))
    print("~", EmileZola)

if Input_Author == JeanJacquesRousseau:
    print(choice(JeanJacquesRousseau_Quotes))
    print("~", JeanJacquesRousseau)

if Input_Author == Plato:
    print(choice(Plato_Quotes))
    print("~", Plato)

if Input_Author == ThomasHobbes:
    print(choice(ThomasHobbes_Quotes))
    print("~", ThomasHobbes)

if Input_Author == Pericles:
    print(choice(Pericles_Quotes))
    print("~", Pericles)

if Input_Author == Archimedes:
    print(choice(Archimedes_Quotes))
    print("~", Archimedes)

if Input_Author == AlexanderGrahamBell:
    print(choice(AlexanderGrahamBell_Quotes))
    print("~", AlexanderGrahamBell)

if Input_Author == GalileoGalilei:
    print(choice(GalileoGalilei_Quotes))
    print("~", GalileoGalilei)

if Input_Author == ImmanuelKant:
    print(choice(ImmanuelKant_Quotes))
    print("~", ImmanuelKant)

print("")
print("Available Quotes:", Length_Quotes, "| Different Authors:", Length_Authors)
print("")
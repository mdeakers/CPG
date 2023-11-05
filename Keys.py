dict_of_keys = {"c_yes" : ['CMaj7', 'Dmin7', 'Emin7', 'FMaj7', 'G7', 'Amin7', 'Bdim7'],
                "c_no" : ['CMaj', 'Dmin', 'Emin', 'FMaj', 'GMaj', 'Amin', 'Bdim'],
                "d_yes" : ['DMaj7', 'Emin7', 'F#min7', 'G7', 'A7', 'Bmin7', 'C#dim7'],
                "d_no" : ['DMaj', 'Emin', 'F#min', 'GMaj', 'AMaj', 'Bmin', 'C#dim'],
                "e_yes" : ['EMaj7', 'F#min7', 'G#min7', 'AMaj7', 'B7', 'C#min7', 'D#dim7'],
                "e_no" : ['EMaj', 'F#min', 'G#min', 'AMaj', 'BMaj', 'C#min', 'D#dim'],
                "f_yes" : ['FMaj7', 'Gmin7', 'Amin7', 'BbMaj7', 'C7', 'Dmin7', 'Edim7'],
                "f_no" : ['FMaj', 'Gmin', 'Amin', 'BbMaj', 'CMaj', 'Dmin', 'Edim'],
                "g_yes" : ['GMaj7', 'Amin7', 'Bmin7', 'CMaj7', 'D7', 'Emin7', 'F#dim7'],
                "g_no" : ['GMaj', 'Amin', 'Bmin', 'CMaj', 'DMaj', 'Emin', 'F#dim'],
                "a_yes" : ['AMaj7', 'Bmin7', 'C#min7', 'DMaj7', 'E7', 'F#min7', 'G#dim7'],
                "a_no" : ['AMaj', 'Bmin', 'C#min', 'DMaj', 'EMaj', 'F#min', 'G#dim'],
                "b_yes" : ['BMaj7', 'C#min7', 'D#min7', 'EMaj7', 'F#7', 'G#min7', 'A#dim7'],
                "b_no" : ['BMaj', 'C#min', 'D#min', 'EMaj', 'F#Maj', 'G#min', 'A#dim'],
                "db_yes" : ['DbMaj7', 'Ebmin7', 'Fmin7', 'GbMaj7', 'Ab7', 'Bbmin7', 'Cdim7'],
                "db_no" : ['DbMaj', 'Ebmin', 'Fmin', 'GbMaj', 'AbMaj', 'Bbmin', 'Cdim'],
                "eb_yes" : ['EbMaj7', 'Fmin7', 'Gmin7', 'AbMaj7', 'Bb7', 'Cmin7', 'Ddim7'],
                "eb_no" : ['EbMaj', 'Fmin', 'Gmin', 'AbMaj', 'BbMaj', 'Cmin', 'Ddim'],
                "gb_yes" : ['GbMaj7', 'Abmin7', 'Bbmin7', 'CbMaj7', 'Bb7', 'Ebmin7', 'Fdim7'],
                "gb_no" : ['GbMaj', 'Abmin', 'Bbmin', 'CbMaj', 'Bb', 'Ebmin', 'Fdim'],
                "ab_yes" : ['AbMaj7', 'Bbmin7', 'Cmin7', 'DbMaj7', 'Eb7', 'Fmin7', 'Gdim7'],
                "ab_no" : ['AbMaj', 'Bbmin', 'Cmin', 'DbMaj', 'Eb', 'Fmin', 'Gdim'],
                "bb_yes" : ['BbMaj7', 'Cmin7', 'Dmin7', 'EbMaj7', 'F7', 'Gmin7', 'Adim7'],
                "bb_no" : ['BbMaj', 'Cmin', 'Dmin', 'EbMaj', 'FMaj', 'Gmin', 'Adim']}

dict_of_moods = {"regal" : [1, 4, 7, 3, 6, 2, 5, 1], "poppy" : [1, 5, 6, 4], "basic" : [1, 4, 1, 5],
                 "floaty" : [1, 1, 4, 4], "somber" : [6, 6, 2, 6], "cliche" : [1, 6, 2, 5],
                 "monotonous" : [1, 1, 1, 1], "jazzy" : [2, 5, 1, 1], "dreary" : [6, 2, 6, 3]}

Major_Scale_RN = ["I", "ii", "iii", "IV", "V", "vi", "viiº"]
Minor_Scale_RN = ["i", "iiº", "III", "iv", "v", "VI", "VII"]

#chanages
# for i in classic:
#     your_progression1 = (your_progression1 + C_Major_with_7ths[i - 1] + '  |')
# for i in classic:
#     your_progression2 = (your_progression2 + Major_Scale_RN[i - 1] + '   |')
# print(your_progression1)
# print(your_progression2)
# for i in pop:
#     your_progression3 = (your_progression3 + C_Major_with_7ths[i - 1] + '  |')
# for i in pop:
#     your_progression4 = (your_progression4 + Major_Scale_RN[i - 1] + '   |')
# print(your_progression3)
# print(your_progression4)

#This is the program introduction and instructions"
print("\n" "\n" "           Welcome to the Chord Progression Generator v1.0!!!!" "\n" "\n"
        "   Have you ever struggled to come up with chord progressions that sound good?" "\n"
        "This app will allow you to generate chord progressions based on a few simple" "\n"
        "selections. The custom progressions you will generate are based on progressions" "\n"
        "found in western music that have stood the test of time for centuries. If at any" "\n"
        "time you wish to exit, simply quit by pressing the ‘esc’ key followed by" "\n"
        "the ‘enter’ key." "\n" "\n")


print("Would you like to generate a chord progression using roman numerals or alphabetic letters? " "\n"
      "One way is not better than the other. Having a progression written in roman numerals allows you " "\n"
      "to easily transpose it to any key of your choosing. Having a progression written with alphabetic " "\n"
      "letters does the work of transposition for you. Please enter “0” for roman numerals or “1” for " "\n"
      "alphabetic letters. If you enter anything other than “0” or “1” you will be re-prompted for a valid input.")
while True:
    rn = input()
    if rn in ['0', '1']:
        break
    else: print("Please enter '0' or '1': ")

#Asks the user to enter a musical key
print("Please enter a key from the following list: C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, or B")
while True:
    userKey = input().lower()
    if userKey in ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "ab", "b", "bb"]:
        break
    else: print("Please enter a valid key...")

#Asks the user if they'd like to use 7th chords
print("Would you like to use 7th chords? Please enter 'yes' or 'no'")
while True:
    sevenths_y_or_n = input().lower()
    if sevenths_y_or_n in ["yes", "no"]:
        break
    else: print("Please enter 'yes' or 'no': ")
user_defined_key = userKey + '_' + sevenths_y_or_n

#Asks the user to enter a valid mood
print("Please enter one of the following moods: regal, poppy, dreary, basic, floaty, somber, cliche, monotonous, "
      "or jazzy")
while True:
    mood = input().lower()
    if mood in dict_of_moods.keys():
        break
    else: print("Please enter a valid mood: ")


user_defined_mood = ''
# user_progression = []
your_progression = "|"


for j in dict_of_moods:
    if j == mood:
        user_defined_mood = dict_of_moods[mood]

#builds a list of chords corresponding to the user's selections
for i in dict_of_keys:
    if i == user_defined_key:
        for j in user_defined_mood:
            #user_progression.append(dict_of_keys[i][j - 1])
            your_progression = (your_progression + dict_of_keys[i][j - 1] + " |")


print("\n" "Here is your custom chord progression: ", your_progression)

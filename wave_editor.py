# the last one 15/5 19:00
import math
from scipy import *
from numpy import *

from Lab6.wave_helper import load_wave, save_wave

DEFAULT_SAMPLE_RATE = 2000
A_FREQUENCY = 440
B_FREQUENCY = 494
C_FREQUENCY = 523
D_FREQUENCY = 587
E_FREQUENCY = 659
F_FREQUENCY = 698
G_FREQUENCY = 784
FREQUENCY_TABLE = [[A_FREQUENCY, "A"], [B_FREQUENCY, "B"],
                   [C_FREQUENCY, "C"], [D_FREQUENCY, "D"],
                   [E_FREQUENCY, "E"], [F_FREQUENCY, "F"],
                   [A_FREQUENCY, "G"]]
MAX_VOLUME = 32767
MIN_VOLUME = -32768
MAIN_MENU_MSG = "Select the function you want to do and press Enter:" \
                "change the music file = 1, compose new music = 2, exit the " \
                "program = 3"
FILENAME_INPUT_MSG = "Please enter the file name you want to change:"
CHANGE_MENU_MSG = "Select the change you want to make to your music file: " \
                  "revers file = 1, opposite file = 2, fast file = 3," \
                  " slow file = 4, loud file = 5, low file = 6, low pass " \
                  "file= 7, save file = 8"
REVERSE = '1'
OPPOSITE = '2'
FAST = '3'
SLOW = '4'
LOUD = '5'
LOW = '6'
LOW_PASS = '7'
FINAL_MENU = '8'
SAVE_AFTER_CHANGE_MSG = "The file with the change is saved"
SAVE_FILE_MSG = "If you want to save this file, enter filename:"
NOT_SAVE_MSG = "File not found"
CHANGE_WAVE = "1"
MAKE_A_RHYTHM = "2"
EXIT = "3"
MODIFIER = 1.2


#לפעמים כתוב     filename.write(data_list)
#ולפעמים     filename.write(str(data_list))
#צריך לסגור כל קובץ אחרי שמסיימים לכתוב עליו
# לפי דעתי עדיף שנשחק על הdata list ובסוףנכתוב, צריך להבין מה הם רוצים


def reverse_audio(data_list, filename):
    """
    The function reverses the music file
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return: Updated data list and update message for user
    """
    filename = open(filename, "w")
    data_list = data_list[::-1]
    filename.write(str(data_list))
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def opposite_audio(data_list, filename):
    """
    A function that converts each value in the data list to its negative value
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return: Updated data list and update message for user
    """
    filename = open(filename, "w")
    for i in range(len(data_list)):
        data_list[i][0] = data_list[i][0] * -1
        data_list[i][1] = data_list[i][1] * -1
    filename.write(str(data_list))
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def fast_audio(data_list, filename):
    """
    A function that speeds up the music file
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return: Updated data list and update message for user
    """
    filename = open(filename, "w")
    for i in range(len(data_list)):
        if i % 2 != 0:
            del data_list[i] #בטוח זה עובד על רשימות?
    filename.write(data_list)
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def slow_audio(data_list, filename):
    """
    A function that slows down the music file
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return:Updated data list and update message for user
    """
    filename = open(filename, "w")
    new_sample_list = []
    for i in range(len(data_list)-1):  # בעייתי! יצא אינסופי
        new_sample = ["", ""]
        new_sample[0] = average(data_list[i][0] + data_list[i + 1][0])
        new_sample[1] = average(data_list[i][1] + data_list[i + 1][1])
        new_sample_list = new_sample_list.append(data_list[i]) #פיצלתי לשניים כי זאת הייתה הוספה של איבר אחד שהוא הסכום ולא 2
        new_sample_list = new_sample_list.append(new_sample)
    new_sample_list = new_sample_list.append(data_list[len(data_list)-1])
    data_list = new_sample_list
    filename.write(data_list)
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def loud_audio(data_list, filename):
    """
    A function that increases the volume of the sound
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return: Updated data list and update message for user
    """
    filename = open(filename, "w")
    for i in range(len(data_list)):
        data_list[i][0] = int(data_list[i][0] * MODIFIER)
        if data_list[i][0] > MAX_VOLUME:
            data_list[i][0] = MAX_VOLUME
        data_list[i][1] = int(data_list[i][1] * MODIFIER)
        if data_list[i][1] > MAX_VOLUME:
            data_list[i][1] = MAX_VOLUME
    filename.write(data_list)
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def low_audio(data_list, filename):
    """
    A function that lowers the volume
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return:Updated data list and update message for user
    """
    filename = open(filename, "w")
    for i in range(len(data_list)):
        data_list[i][0] = int(data_list[i][0] // MODIFIER)
        data_list[i][1] = int(data_list[i][1] // MODIFIER)
    filename.write(data_list)
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def low_pass_audio(data_list, filename):  # לשפצר שיהיה יותר יפה
    """
    A function that dims the sound
    :param data_list: List of pairs of samples imported from the music file
    :param filename: the name of the file that the program change
    :return: Updated data list and update message for user
    """
    filename = open(filename, "w")
    for i in range(1, len(data_list) - 1):
        data_list[i][0] = average(data_list[i - 1][0] + data_list[i][0] +
                                  data_list[i + 1][0])
        data_list[i][1] = average(data_list[i - 1][1] + data_list[i][1] +
                                  data_list[i + 1][1])
    data_list[0][0] = average(data_list[0][0] + data_list[1][0])
    data_list[0][1] = average(data_list[0][1] + data_list[1][1])
    final = len(data_list)
    data_list[final][0] = average(data_list[final - 2][0] +
                                  data_list[final-1][0])
    data_list[final][1] = average(data_list[final - 2][1] +
                                  data_list[final-1][1])
    filename.write(data_list)
    msg = SAVE_AFTER_CHANGE_MSG + CHANGE_MENU_MSG
    return data_list, msg


def change_wave(data_list=None):  # לפצל באופן חכם יותר
    """
    If the user chooses the option to change his music file, he insert the
    file name and can choose from 7 options for changes. If it chooses an end
    option, the function will save the file after the change.
    :param data_list: List of pairs of samples imported from the music file
    :return: None
    """
    flag = -1
    if data_list is not None:  # למה צריך את שניהם?
        while flag == -1:
            filename = input(FILENAME_INPUT_MSG)
            flag = load_wave(filename)
        data_list = load_wave(filename)[1]
        sample_rate = load_wave(filename)[0]
    else:
        sample_rate = DEFAULT_SAMPLE_RATE  # לא צריך פה
    choice = 0  # הכרחי?
    msg = CHANGE_MENU_MSG
    while choice != FINAL_MENU:
        choice = input(msg)
        if choice == REVERSE:
            data_list, msg = reverse_audio(data_list, filename)
        elif choice == OPPOSITE:
            data_list, msg = opposite_audio(data_list, filename)
        elif choice == FAST:
            data_list, msg = fast_audio(data_list, filename)
        elif choice == SLOW:
            data_list, msg = slow_audio(data_list, filename)
        elif choice == LOUD:
            data_list, msg = loud_audio(data_list, filename)
        elif choice == LOW:
            data_list, msg = low_audio(data_list, filename)
        elif choice == LOW_PASS:
            data_list, msg = low_pass_audio(data_list, filename)
    target_file = input(SAVE_FILE_MSG)
    while save_wave(sample_rate, data_list, target_file) == -1:
        target_file = input(NOT_SAVE_MSG + " " + SAVE_FILE_MSG)


def convert_file_to_lst(filename):
    """
    :param filename: a file of instructions
    :return: a list of notes, each one is a string of a letter+time
    """
    f = open(filename)
    filename_str = f.read().replace("\n", "")
    filename_str = filename_str.replace(" ", "")
    filename_lst = []
    for ch in filename_str:
        if ch in "ABCDEFG":
            filename_lst.append(ch)
        else:
            filename_lst[len(filename_lst) - 1] += ch
    return filename_lst


def get_frequency(note_char):
    """
    :param note_char: one of the chars "ABCDEFG"
    :return: the frequency rate according to th constant list
    """
    for note in range(len(FREQUENCY_TABLE)):
        if FREQUENCY_TABLE[note][1] == note_char:
            return FREQUENCY_TABLE[note][0]


def create_sample(note_char, i):
    """
    :param note_char: a string of letter+ number connected "A16" "F3",
     the letter for node char and the num for time at 1/16 seconds units
    :param i: the index of the sample in the last note
    :return: the sample as a list of 2  ints
    """
    frequency = get_frequency(note_char)
    samples_per_cycle = DEFAULT_SAMPLE_RATE / frequency
    value = int(MAX_VOLUME * math.sin(i / samples_per_cycle * 2 * math.pi))
    return [value, value]


def single_note(note):
    """
    :param note: a string of letter+ number connected "A16" "F3",
     the letter for node char and the num for time at 1/16 seconds units
    :return:
    """
    note_char = list(note)[0]
    time = int(note.replace(note_char, ""))
    time = time * 16
    lst = [create_sample(note_char, sample_index)
           for sample_index in range(time)]
    return lst


def make_a_rhythm(filename):
    """
    :param filename: a file of instruction
    :return: a
    """
    instructions_lst = convert_file_to_lst(filename)
    rhythm = []
    print(instructions_lst)
    for i in range(len(instructions_lst)):
        rhythm.extend(single_note(instructions_lst[i]))
    print(rhythm)


def main():
    main_choice = input(MAIN_MENU_MSG)
    while main_choice != EXIT:
        if main_choice == CHANGE_WAVE:
            change_wave()
        elif main_choice == MAKE_A_RHYTHM:
            change_wave(make_a_rhythm())  # בכוונה פה?


if __name__ == '__main__':
    main()

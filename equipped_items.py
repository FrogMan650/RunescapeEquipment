import runescape_items as rsi
from tkinter import *

rsi.build_item_lists()

# list of all items to search through
all_item_list = []

# lists of item names by equipment slot
helmet_name_list = []
top_name_list = []
bottom_name_list = []
boots_name_list = []
pocket_name_list = []
gloves_name_list = []
ring_name_list = []
amulet_name_list = []
cape_name_list = []
weapon_name_list = []
offhand_name_list = []

# list of all the equipment slot lists, currently unused
item_list_list = [rsi.helmet_list, rsi.top_list, rsi.bottom_list, rsi.pocket_list, rsi.glove_list, rsi.boot_list,
                  rsi.ring_list, rsi.neck_list, rsi.cape_list, rsi.weapon_list, rsi.offhand_list]

# adding every item from each equipment slot list, to the searchable list and name list
for x in rsi.helmet_list:
    all_item_list.append(x)
    helmet_name_list.append(x.name)
for x in rsi.top_list:
    all_item_list.append(x)
    top_name_list.append(x.name)
for x in rsi.bottom_list:
    all_item_list.append(x)
    bottom_name_list.append(x.name)
for x in rsi.pocket_list:
    all_item_list.append(x)
    pocket_name_list.append(x.name)
for x in rsi.glove_list:
    all_item_list.append(x)
    gloves_name_list.append(x.name)
for x in rsi.boot_list:
    all_item_list.append(x)
    boots_name_list.append(x.name)
for x in rsi.ring_list:
    all_item_list.append(x)
    ring_name_list.append(x.name)
for x in rsi.neck_list:
    all_item_list.append(x)
    amulet_name_list.append(x.name)
for x in rsi.cape_list:
    all_item_list.append(x)
    cape_name_list.append(x.name)
for x in rsi.weapon_list:
    all_item_list.append(x)
    weapon_name_list.append(x.name)
for x in rsi.offhand_list:
    all_item_list.append(x)
    offhand_name_list.append(x.name)

# create a window, named win
win = Tk()

# set the window title and make it so the user can't resize it
win.title("Runescape items")
win.config(bg="red4")
win.resizable(False, False)

# create frames
frame1 = Frame(win)
frame1.config(bg="red4")
frame1.pack(side="top")

frame2 = Frame(win)
frame2.config(bg="brown")
frame2.pack(side="left")

frame3 = Frame(win)
frame3.config(bg="brown")
frame3.pack(side="left")

frame4 = Frame(win)
frame4.config(bg="brown")
frame4.pack(side="left")

frame6 = Frame(win)
frame6.config(bg="brown")
frame6.pack(side="left")

frame5 = Frame(win)
frame5.config(bg="brown")
frame5.pack(side="left")


# empty list to add items to later
equipped_items = []

# used for storing each of the stats on the equipped items
stat_changes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
special_attack = [" "]

# create a label for each stat and add them to their respective frame
stab_bonus_label = Label(frame2, bg="brown")
slash_bonus_label = Label(frame2, bg="brown")
crush_bonus_label = Label(frame2, bg="brown")
mage_bonus_label = Label(frame2, bg="brown")
ranged_bonus_label = Label(frame2, bg="brown")
stab_def_bonus_label = Label(frame3, bg="brown")
slash_def_bonus_label = Label(frame3, bg="brown")
crush_def_bonus_label = Label(frame3, bg="brown")
mage_def_bonus_label = Label(frame3, bg="brown")
ranged_def_bonus_label = Label(frame3, bg="brown")
melee_str_label = Label(frame4, bg="brown")
ranged_str_label = Label(frame4, bg="brown")
mage_str_label = Label(frame4, bg="brown")
prayer_label = Label(frame4, bg="brown")
spec_label = Label(frame6, bg="brown")


def set_labels():
    """Set the text of each of the stat labels."""
    stab_bonus_label.config(text="Stab: " + str(stat_changes[0]))
    slash_bonus_label.config(text="Slash: " + str(stat_changes[1]))
    crush_bonus_label.config(text="Crush: " + str(stat_changes[2]))
    mage_bonus_label.config(text="Magic: " + str(stat_changes[3]))
    ranged_bonus_label.config(text="Ranged: " + str(stat_changes[4]))
    stab_def_bonus_label.config(text="Stab: " + str(stat_changes[5]))
    slash_def_bonus_label.config(text="Slash: " + str(stat_changes[6]))
    crush_def_bonus_label.config(text="Crush: " + str(stat_changes[7]))
    mage_def_bonus_label.config(text="Magic: " + str(stat_changes[8]))
    ranged_def_bonus_label.config(text="Ranged: " + str(stat_changes[9]))
    melee_str_label.config(text="Melee Strength: " + str(stat_changes[10]))
    ranged_str_label.config(text="Ranged Strength: " + str(stat_changes[11]))
    mage_str_label.config(text="Magic Damage: " + str(stat_changes[12]) + " %")
    prayer_label.config(text="Prayer: " + str(stat_changes[13]))
    spec_label.config(text=str(special_attack[0]))


def reset_stats():
    """Reset all the stored stats to 0."""
    x = 0
    while x != len(stat_changes):
        stat_changes[x] = 0
        x += 1


def set_stats():
    """Get stats from each equipped item, and add and store them."""
    reset_stats()
    for x in equipped_items:
        if x.equipment_slot == "Weapon slot":
            special_attack[0] = x.special_attack
        if x.equipment_slot == "2h slot":
            special_attack[0] = x.special_attack
        stat_changes[0] += x.stab_bonus
        stat_changes[1] += x.slash_bonus
        stat_changes[2] += x.crush_bonus
        stat_changes[3] += x.mage_bonus
        stat_changes[4] += x.ranged_bonus
        stat_changes[5] += x.stab_defense
        stat_changes[6] += x.slash_defense
        stat_changes[7] += x.crush_defense
        stat_changes[8] += x.mage_defense
        stat_changes[9] += x.ranged_defense
        stat_changes[10] += x.melee_str
        stat_changes[11] += x.ranged_str
        stat_changes[12] += x.mage_str
        stat_changes[13] += x.prayer_bonus


def callback(a):
    """When making a selection, searches the equipped item list for the proper item; removing items as necessary,
    and adding the selected item to the equipment list."""
    x = " "
    while a != x:
        for z in all_item_list:
            if z.name == a:
                for y in equipped_items:
                    if z.equipment_slot == y.equipment_slot:
                        equipped_items.remove(y)
                if "2h slot" in z.equipment_slot:
                    selected_offhand_option.set(rsi.offhand_list[0].name)
                    for w in equipped_items:
                        if w.equipment_slot == "Shield slot":
                            equipped_items.remove(w)
                        if "Weapon slot" in w.equipment_slot:
                            equipped_items.remove(w)
                if z.equipment_slot == "Weapon slot":
                    for w in equipped_items:
                        # if w.equipment_slot == "2h slot":
                        #     equipped_items.remove(w)
                        # if w.equipment_slot == "2h slot table":
                        #     equipped_items.remove(w)
                        if "2h slot" in w.equipment_slot:
                            equipped_items.remove(w)
                if z.equipment_slot == "Shield slot":
                    for w in equipped_items:
                        if w.equipment_slot == "2h slot":
                            selected_weapon_option.set(rsi.weapon_list[0].name)
                            special_attack[0] = rsi.weapon_list[0].special_attack
                            equipped_items.remove(w)
                        if w.equipment_slot == "2h slot table":
                            selected_weapon_option.set(rsi.weapon_list[0].name)
                            special_attack[0] = rsi.weapon_list[0].special_attack
                            equipped_items.remove(w)
                x = z.name
                equipped_items.append(z)
                set_stats()
                set_labels()


# create the OptionMenu for each equipment slot and set the default selection
selected_helmet_option = StringVar()
selected_helmet_option.set(helmet_name_list[0])
equipped_items.append(rsi.helmet_list[0])
helmet_option_list = OptionMenu(frame1, selected_helmet_option, *helmet_name_list, command=callback)
helmet_option_list.pack()
selected_top_option = StringVar()
selected_top_option.set(top_name_list[0])
equipped_items.append(rsi.top_list[0])
top_option_list = OptionMenu(frame1, selected_top_option, *top_name_list, command=callback)
top_option_list.pack()
selected_bottom_option = StringVar()
selected_bottom_option.set(bottom_name_list[0])
equipped_items.append(rsi.bottom_list[0])
bottom_option_list = OptionMenu(frame1, selected_bottom_option, *bottom_name_list, command=callback)
bottom_option_list.pack()
selected_pocket_option = StringVar()
selected_pocket_option.set(pocket_name_list[0])
equipped_items.append(rsi.pocket_list[0])
pocket_option_list = OptionMenu(frame1, selected_pocket_option, *pocket_name_list, command=callback)
pocket_option_list.pack()
selected_gloves_option = StringVar()
selected_gloves_option.set(gloves_name_list[0])
equipped_items.append(rsi.glove_list[0])
gloves_option_list = OptionMenu(frame1, selected_gloves_option, *gloves_name_list, command=callback)
gloves_option_list.pack()
selected_boots_option = StringVar()
selected_boots_option.set(boots_name_list[0])
equipped_items.append(rsi.boot_list[0])
boots_option_list = OptionMenu(frame1, selected_boots_option, *boots_name_list, command=callback)
boots_option_list.pack()
selected_ring_option = StringVar()
selected_ring_option.set(ring_name_list[0])
equipped_items.append(rsi.ring_list[0])
ring_option_list = OptionMenu(frame1, selected_ring_option, *ring_name_list, command=callback)
ring_option_list.pack()
selected_amulet_option = StringVar()
selected_amulet_option.set(amulet_name_list[0])
equipped_items.append(rsi.neck_list[0])
amulet_option_list = OptionMenu(frame1, selected_amulet_option, *amulet_name_list, command=callback)
amulet_option_list.pack()
selected_cape_option = StringVar()
selected_cape_option.set(cape_name_list[0])
equipped_items.append(rsi.cape_list[0])
cape_option_list = OptionMenu(frame1, selected_cape_option, *cape_name_list, command=callback)
cape_option_list.pack()
selected_weapon_option = StringVar()
selected_weapon_option.set(weapon_name_list[0])
equipped_items.append(rsi.weapon_list[0])
weapon_option_list = OptionMenu(frame1, selected_weapon_option, *weapon_name_list, command=callback)
weapon_option_list.pack()
selected_offhand_option = StringVar()
selected_offhand_option.set(offhand_name_list[0])
equipped_items.append(rsi.offhand_list[0])
offhand_option_list = OptionMenu(frame1, selected_offhand_option, *offhand_name_list, command=callback)
offhand_option_list.pack()

# lists for labels, stored by which frame they are meant for
frame2_label_list = []

# calculate total stats from all equipped items, and add the text to each label
set_stats()
set_labels()

# create header labels and add them and the stat labels to their respective lists
attack_bonuses_label = Label(frame2, bg="red", text="Attack Bonuses")
frame2_label_list.append(attack_bonuses_label)
frame2_label_list.append(stab_bonus_label)
frame2_label_list.append(slash_bonus_label)
frame2_label_list.append(crush_bonus_label)
frame2_label_list.append(mage_bonus_label)
frame2_label_list.append(ranged_bonus_label)
defense_bonuses_label = Label(frame3, bg="red", text="Defense Bonuses")
frame2_label_list.append(defense_bonuses_label)
frame2_label_list.append(stab_def_bonus_label)
frame2_label_list.append(slash_def_bonus_label)
frame2_label_list.append(crush_def_bonus_label)
frame2_label_list.append(mage_def_bonus_label)
frame2_label_list.append(ranged_def_bonus_label)
other_bonuses_label = Label(frame4, bg="red", text="Other Bonuses")
frame2_label_list.append(other_bonuses_label)
frame2_label_list.append(melee_str_label)
frame2_label_list.append(ranged_str_label)
frame2_label_list.append(mage_str_label)
frame2_label_list.append(prayer_label)
special_attack_label = Label(frame6, bg="red", text="Special Attack")
frame2_label_list.append(special_attack_label)
frame2_label_list.append(spec_label)
# empty_label6 = Label(frame5, bg="red", text="Presets")
# frame2_label_list.append(empty_label6)
empty_label1 = Label(frame4, bg="brown", text=" ")
frame2_label_list.append(empty_label1)
empty_label2 = Label(frame6, bg="brown", text=" ")
frame2_label_list.append(empty_label2)
empty_label3 = Label(frame6, bg="brown", text=" ")
frame2_label_list.append(empty_label3)
empty_label4 = Label(frame6, bg="brown", text=" ")
frame2_label_list.append(empty_label4)
empty_label5 = Label(frame6, bg="brown", text=" ")
frame2_label_list.append(empty_label5)


# pack all of the labels in the label list
for x in frame2_label_list:
    x.pack()


# list to store preset buttons, to be packed later
# button_list = []


# def print_equipped():
#     for x in equipped_items:
#         print(x.name)
#     print("\n")
# # create all 4 preset buttons and adds each button to the button list
# button1 = Button(frame5, bg="green", text="Melee Preset")
# button2 = Button(frame5, bg="green", text="Ranged Preset")
# button3 = Button(frame5, bg="green", text="Mage Preset")
# button4 = Button(frame5, bg="green", text="Reset", command=print_equipped)
# button_list.append(button4)
# button_list.append(button1)
# button_list.append(button2)
# button_list.append(button3)

# pack all of the buttons in the button list
# for x in button_list:
#     x.pack()

# start the loop of the gui to open the window until you x out
win.mainloop()


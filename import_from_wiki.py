from requests import get
from bs4 import BeautifulSoup
import json


def get_wiki_stats(i):
    url = "https://oldschool.runescape.wiki/w/" + i + "#Charged"
    response = get(url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    # container for finding all the stats
    stat_containers = html_soup.find_all("td", class_="infobox-nested")
    # container for finding the item name
    stat_containers2 = html_soup.find_all("h1", class_="firstHeading")
    # container for finding the equipment slot
    stat_containers3 = html_soup.find_all("th", class_="infobox-nested")
    # container for finding the special attack name
    stat_containers4 = html_soup.find_all("p")

    special_attack = "No spec"

    for x in stat_containers4:
        try:
            if x.a.text == "special attack":
                special_attack = x.i.text
        except:
            continue


    raw_mage_str = list(stat_containers[12].text)
    mage_str = 0

    # remove unwanted characters from mage_str so it can be converted to a string
    for x in raw_mage_str:
        if x == "+":
            raw_mage_str.remove(x)
        if x == "%":
            raw_mage_str.remove(x)

    # set mage_str to the proper ints
    if len(raw_mage_str) == 2:
        mage_str = raw_mage_str[0] + raw_mage_str[1]
    elif len(raw_mage_str) == 1:
        mage_str = raw_mage_str[0]

    item_dictionary = {"name": str(stat_containers2[0].text),
                        "equipment slot": str(stat_containers3[14].a.get("title")),
                        "special attack": special_attack, "stab bonus": int(stat_containers[0].text),
                        "slash bonus": int(stat_containers[1].text), "crush bonus": int(stat_containers[2].text),
                        "mage bonus": int(stat_containers[3].text), "range bonus": int(stat_containers[4].text),
                        "stab defense": int(stat_containers[5].text), "slash defense": int(stat_containers[6].text),
                        "crush defense": int(stat_containers[7].text), "mage defense": int(stat_containers[8].text),
                        "range defense": int(stat_containers[9].text), "melee strength": int(stat_containers[10].text),
                        "range strength": int(stat_containers[11].text), "mage strength": int(mage_str),
                        "prayer": int(stat_containers[13].text)}

# fixing a change the wiki made, labeling the equipment slots differently
    if item_dictionary["equipment slot"] == "2h slot table":
        item_dictionary["equipment slot"] = "2h slot"
    if item_dictionary["equipment slot"] == "Weapon slot table":
        item_dictionary["equipment slot"] = "Weapon slot"

# check through the stored_items.json file to see if an item has already been added or not. if not it is added
    with open("stored_items.json", "r") as checkfile:
        for line in checkfile:
            added_items = json.loads(line)
        add_item = True
        for x in added_items:
            if item_dictionary["name"] == x:
                add_item = False
        if add_item:
            with open("items_stored.jsonl", "a") as outfile:
                json.dump(item_dictionary, outfile)
                outfile.write("\n")
            with open("stored_items.json", "w") as checkfile:
                added_items.append(item_dictionary["name"])
                json.dump(added_items, checkfile)
                print("NEW ITEM ADDED: " + item_dictionary["name"])
        elif not add_item:
            print("ITEM NOT ADDED")


# change the string to import a new item
get_wiki_stats("bulwark")






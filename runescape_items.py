import runescape_item_classes as rs
import json

# lists of instanced items
helmet_list = []
top_list = []
bottom_list = []
boot_list = []
glove_list = []
cape_list = []
ring_list = []
neck_list = []
pocket_list = []
offhand_list = []
weapon_list = []


def build_item_lists():
    """Pulls dictionaries from the items_stored.jsonl file. Line by line initializes items by equipment slot,
    and adds them to the correct equipment slot list."""

    # Empty items for placeholders
    helmet_list.clear()
    helmet_list.append(rs.ItemHelmet("Head slot", "Select Helmet"))
    top_list.clear()
    top_list.append(rs.ItemChest("Body slot", "Select Chest"))
    bottom_list.clear()
    bottom_list.append(rs.ItemLegs("Legs slot", "Select Legs"))
    pocket_list.clear()
    pocket_list.append(rs.ItemPocket("Ammo slot", "Select Pocket/Ammo"))
    glove_list.clear()
    glove_list.append(rs.ItemGloves("Hands slot", "Select Gloves"))
    boot_list.clear()
    boot_list.append(rs.ItemBoots("Feet slot", "Select Boots"))
    ring_list.clear()
    ring_list.append(rs.ItemRing("Ring slot", "Select Ring"))
    neck_list.clear()
    neck_list.append(rs.ItemNecklace("Neck slot", "Select Necklace"))
    cape_list.clear()
    cape_list.append(rs.ItemCape("Cape slot", "Select Cape"))
    weapon_list.clear()
    weapon_list.append(rs.ItemWeapon("Weapon slot", "Select Weapon"))
    offhand_list.clear()
    offhand_list.append(rs.ItemOffHand("Shield slot", "Select Offhand"))

    with open("items_stored.jsonl", "r") as openfile:
        for line in openfile:
            temp_dict = json.loads(line)
            if temp_dict["equipment slot"] == "Head slot":
                helmet_list.append(rs.ItemHelmet(temp_dict["equipment slot"], temp_dict["name"],
                                                 temp_dict["stab bonus"], temp_dict["slash bonus"],
                                                 temp_dict["crush bonus"], temp_dict["mage bonus"],
                                                 temp_dict["range bonus"], temp_dict["stab defense"],
                                                 temp_dict["slash defense"], temp_dict["crush defense"],
                                                 temp_dict["mage defense"], temp_dict["range defense"],
                                                 temp_dict["melee strength"], temp_dict["range strength"],
                                                 temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Body slot":
                top_list.append(rs.ItemChest(temp_dict["equipment slot"], temp_dict["name"],
                                             temp_dict["stab bonus"], temp_dict["slash bonus"],
                                             temp_dict["crush bonus"], temp_dict["mage bonus"],
                                             temp_dict["range bonus"], temp_dict["stab defense"],
                                             temp_dict["slash defense"], temp_dict["crush defense"],
                                             temp_dict["mage defense"], temp_dict["range defense"],
                                             temp_dict["melee strength"], temp_dict["range strength"],
                                             temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Legs slot":
                bottom_list.append(rs.ItemLegs(temp_dict["equipment slot"], temp_dict["name"],
                                               temp_dict["stab bonus"], temp_dict["slash bonus"],
                                               temp_dict["crush bonus"], temp_dict["mage bonus"],
                                               temp_dict["range bonus"], temp_dict["stab defense"],
                                               temp_dict["slash defense"], temp_dict["crush defense"],
                                               temp_dict["mage defense"], temp_dict["range defense"],
                                               temp_dict["melee strength"], temp_dict["range strength"],
                                               temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Feet slot":
                boot_list.append(rs.ItemBoots(temp_dict["equipment slot"], temp_dict["name"],
                                              temp_dict["stab bonus"], temp_dict["slash bonus"],
                                              temp_dict["crush bonus"], temp_dict["mage bonus"],
                                              temp_dict["range bonus"], temp_dict["stab defense"],
                                              temp_dict["slash defense"], temp_dict["crush defense"],
                                              temp_dict["mage defense"], temp_dict["range defense"],
                                              temp_dict["melee strength"], temp_dict["range strength"],
                                              temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Hands slot":
                glove_list.append(rs.ItemGloves(temp_dict["equipment slot"], temp_dict["name"],
                                                temp_dict["stab bonus"], temp_dict["slash bonus"],
                                                temp_dict["crush bonus"], temp_dict["mage bonus"],
                                                temp_dict["range bonus"], temp_dict["stab defense"],
                                                temp_dict["slash defense"], temp_dict["crush defense"],
                                                temp_dict["mage defense"], temp_dict["range defense"],
                                                temp_dict["melee strength"], temp_dict["range strength"],
                                                temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Cape slot":
                cape_list.append(rs.ItemCape(temp_dict["equipment slot"], temp_dict["name"],
                                             temp_dict["stab bonus"], temp_dict["slash bonus"],
                                             temp_dict["crush bonus"], temp_dict["mage bonus"],
                                             temp_dict["range bonus"], temp_dict["stab defense"],
                                             temp_dict["slash defense"], temp_dict["crush defense"],
                                             temp_dict["mage defense"], temp_dict["range defense"],
                                             temp_dict["melee strength"], temp_dict["range strength"],
                                             temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Ring slot":
                ring_list.append(rs.ItemRing(temp_dict["equipment slot"], temp_dict["name"],
                                             temp_dict["stab bonus"], temp_dict["slash bonus"],
                                             temp_dict["crush bonus"], temp_dict["mage bonus"],
                                             temp_dict["range bonus"], temp_dict["stab defense"],
                                             temp_dict["slash defense"], temp_dict["crush defense"],
                                             temp_dict["mage defense"], temp_dict["range defense"],
                                             temp_dict["melee strength"], temp_dict["range strength"],
                                             temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Neck slot":
                neck_list.append(
                    rs.ItemNecklace(temp_dict["equipment slot"], temp_dict["name"],
                                    temp_dict["stab bonus"], temp_dict["slash bonus"],
                                    temp_dict["crush bonus"], temp_dict["mage bonus"],
                                    temp_dict["range bonus"], temp_dict["stab defense"],
                                    temp_dict["slash defense"], temp_dict["crush defense"],
                                    temp_dict["mage defense"], temp_dict["range defense"],
                                    temp_dict["melee strength"], temp_dict["range strength"],
                                    temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Ammo slot":
                pocket_list.append(
                    rs.ItemPocket(temp_dict["equipment slot"], temp_dict["name"],
                                  temp_dict["stab bonus"], temp_dict["slash bonus"],
                                  temp_dict["crush bonus"], temp_dict["mage bonus"],
                                  temp_dict["range bonus"], temp_dict["stab defense"],
                                  temp_dict["slash defense"], temp_dict["crush defense"],
                                  temp_dict["mage defense"], temp_dict["range defense"],
                                  temp_dict["melee strength"], temp_dict["range strength"],
                                  temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Shield slot":
                offhand_list.append(
                    rs.ItemOffHand(temp_dict["equipment slot"], temp_dict["name"],
                                   temp_dict["stab bonus"], temp_dict["slash bonus"],
                                   temp_dict["crush bonus"], temp_dict["mage bonus"],
                                   temp_dict["range bonus"], temp_dict["stab defense"],
                                   temp_dict["slash defense"], temp_dict["crush defense"],
                                   temp_dict["mage defense"], temp_dict["range defense"],
                                   temp_dict["melee strength"], temp_dict["range strength"],
                                   temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Weapon slot":
                weapon_list.append(
                    rs.ItemWeapon(temp_dict["equipment slot"], temp_dict["name"], temp_dict["special attack"],
                                  temp_dict["stab bonus"], temp_dict["slash bonus"],
                                  temp_dict["crush bonus"], temp_dict["mage bonus"],
                                  temp_dict["range bonus"], temp_dict["stab defense"],
                                  temp_dict["slash defense"], temp_dict["crush defense"],
                                  temp_dict["mage defense"], temp_dict["range defense"],
                                  temp_dict["melee strength"], temp_dict["range strength"],
                                  temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "2h slot":
                weapon_list.append(
                    rs.ItemWeapon(temp_dict["equipment slot"], temp_dict["name"], temp_dict["special attack"],
                                  temp_dict["stab bonus"], temp_dict["slash bonus"],
                                  temp_dict["crush bonus"], temp_dict["mage bonus"],
                                  temp_dict["range bonus"], temp_dict["stab defense"],
                                  temp_dict["slash defense"], temp_dict["crush defense"],
                                  temp_dict["mage defense"], temp_dict["range defense"],
                                  temp_dict["melee strength"], temp_dict["range strength"],
                                  temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "2h slot table":
                weapon_list.append(
                    rs.ItemWeapon(temp_dict["equipment slot"], temp_dict["name"], temp_dict["special attack"],
                                  temp_dict["stab bonus"], temp_dict["slash bonus"],
                                  temp_dict["crush bonus"], temp_dict["mage bonus"],
                                  temp_dict["range bonus"], temp_dict["stab defense"],
                                  temp_dict["slash defense"], temp_dict["crush defense"],
                                  temp_dict["mage defense"], temp_dict["range defense"],
                                  temp_dict["melee strength"], temp_dict["range strength"],
                                  temp_dict["mage strength"], temp_dict["prayer"]))

            if temp_dict["equipment slot"] == "Weapon slot table":
                weapon_list.append(
                    rs.ItemWeapon(temp_dict["equipment slot"], temp_dict["name"], temp_dict["special attack"],
                                  temp_dict["stab bonus"], temp_dict["slash bonus"],
                                  temp_dict["crush bonus"], temp_dict["mage bonus"],
                                  temp_dict["range bonus"], temp_dict["stab defense"],
                                  temp_dict["slash defense"], temp_dict["crush defense"],
                                  temp_dict["mage defense"], temp_dict["range defense"],
                                  temp_dict["melee strength"], temp_dict["range strength"],
                                  temp_dict["mage strength"], temp_dict["prayer"]))

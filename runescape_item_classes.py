

class RunescapeItem:
    """Define the basis of runescape items."""

    def __init__(self, equipment_slot, name):
        """Initialize item basic attributes."""
        self.equipment_slot = equipment_slot
        self.name = name

class ItemWeapon(RunescapeItem):
    """Define a weapon."""

    def __init__(self, equipment_slot, name, special_attack="No spec", stab_bonus=0, slash_bonus=0, crush_bonus=0,
                 mage_bonus=0, ranged_bonus=0, stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0,
                 ranged_defense=0, melee_str=0, ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize weapon attributes."""
        self.special_attack = special_attack
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemOffHand(RunescapeItem):
    """Define an item worn in the offhand slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize offhand item attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemHelmet(RunescapeItem):
    """Define an item worn in the helmet slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize helmet attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemChest(RunescapeItem):
    """Define an item worn in the chest slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize chest piece attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemLegs(RunescapeItem):
    """Define an item worn in the legs slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize leg item attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemBoots(RunescapeItem):
    """Define an item worn in the boot slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize boot attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemNecklace(RunescapeItem):
    """Define an item worn in the necklace slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize necklace attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemCape(RunescapeItem):
    """Define an item worn in the cape slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize cape attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemPocket(RunescapeItem):
    """Define an item worn in the pocket slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize pocket item attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemGloves(RunescapeItem):
    """Define an item worn in the glove slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize glove attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)

class ItemRing(RunescapeItem):
    """Define an item worn in the ring slot."""

    def __init__(self, equipment_slot, name, stab_bonus=0, slash_bonus=0, crush_bonus=0, mage_bonus=0, ranged_bonus=0,
                 stab_defense=0, slash_defense=0, crush_defense=0, mage_defense=0, ranged_defense=0, melee_str=0,
                 ranged_str=0, mage_str=0, prayer_bonus=0):
        """Initialize ring attributes."""
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.mage_bonus = mage_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_defense = stab_defense
        self.slash_defense = slash_defense
        self.crush_defense = crush_defense
        self.mage_defense = mage_defense
        self.ranged_defense = ranged_defense
        self.melee_str = melee_str
        self.ranged_str = ranged_str
        self.mage_str = mage_str
        self.prayer_bonus = prayer_bonus

        super().__init__(equipment_slot, name)


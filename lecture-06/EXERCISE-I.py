
heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']


def display_heroes(hero_list):
    print("\nHeroes List:")
    for hero in hero_list:
        print(f"- {hero}")


def add_hero(hero_list, new_hero):
    hero_list.append(new_hero)
    return hero_list


def insert_hero(hero_list, position, new_hero):
    hero_list.insert(position, new_hero)
    return hero_list


def remove_hero(hero_list, hero_to_remove):
    if hero_to_remove in hero_list:
        hero_list.remove(hero_to_remove)
    else:
        print(f"{hero_to_remove} not found in the list.")
    return hero_list


def display_sorted_heroes(hero_list, ascending=True):
    sorted_list = sorted(hero_list, reverse=not ascending)
    print("\nSorted Heroes (Ascending):" if ascending else "\nSorted Heroes (Descending):")
    for hero in sorted_list:
        print(f"- {hero}")


display_heroes(heroes)
heroes = add_hero(heroes, 'Captain America')
heroes = insert_hero(heroes, 1, 'Black Panther')
heroes = remove_hero(heroes, 'Hulk')
display_sorted_heroes(heroes, ascending=True)
display_sorted_heroes(heroes, ascending=False)

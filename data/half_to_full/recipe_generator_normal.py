import os
import json

half_to_full =os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
recipe_folder = os.path.join(half_to_full, "recipes", "normal")
advancement_folder = os.path.join(half_to_full, "advancements", "recipes", "normal")

# ハーフブロックの存在するフルブロックをリストに示す
full_blocks = (
    "cut_copper",
    "exposed_cut_copper",
    "weathered_cut_copper",
    "oxidized_cut_copper",
    "waxed_cut_copper",
    "waxed_exposed_cut_copper",
    "waxed_weathered_cut_copper",
    "waxed_oxidized_cut_copper",
    "stone",
    "smooth_stone",
    "sandstone",
    "cut_sandstone",
    "cobblestone",
    "quartz_block",
    "red_sandstone",
    "cut_red_sandstone",
    "prismarine",
    "dark_prismarine",
    "polished_granite",
    "smooth_red_sandstone",
    "polished_diorite",
    "mossy_cobblestone",
    "smooth_sandstone",
    "granite",
    "andesite",
    "polished_andesite",
    "diorite",
    "cobbled_deepslate",
    "polished_deepslate",
    "deepslate_tiles",
    "blackstone",
    "polished_blackstone"
)

# ハーフブロックの種類ごとにカスタムレシピと進捗を生成する
for full_block in full_blocks:
    recipe_name = f"{full_block}"
    advancement_name = f"{full_block}"

    # レシピファイルの内容を定義する
    recipe = {
        "type": "minecraft:crafting_shaped",
        "pattern": [
            "#",
            "X",
            "#"
        ],
        "key": {
            "#": {
                "item": f"minecraft:{full_block}_slab",
                "data": 0
            },
            "X": {
                "item": "minecraft:slime_ball",
                "data": 0
            },
        },
        "result": {
            "item": f"minecraft:{full_block}",
            "count": 1
        }
    }

    # 進捗を保存する
    recipe_path = os.path.join(f"{recipe_folder}", f"{recipe_name}.json")
    with open(recipe_path, "w") as f:
        json.dump(recipe, f, indent=4)

    # 進捗ファイルの内容を定義する
    
    advancement = {
        "parent": "minecraft:recipes/root",
        "criteria": {
            f"has_{full_block}_slab": {
                "conditions": {
                    "items": [
                        {
                            "items": [
                                f"minecraft:{full_block}_slab"
                            ]
                        }
                    ]
                },
                "trigger": "minecraft:inventory_changed"
            }
        },
        "requirements": [
            [
            f"has_{full_block}_slab"
            
            ]
        ],
        "rewards": {
            "recipes": [
            f"half_to_full:normal/{full_block}"
            ]
        }
    }
    # 進捗ファイルを保存する
    advancement_path = os.path.join(f"{advancement_folder}", f"{advancement_name}.json")
    with open(advancement_path, "w") as f:
        json.dump(advancement, f, indent=4)

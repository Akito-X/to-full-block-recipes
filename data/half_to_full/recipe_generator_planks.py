import os
import json

half_to_full =os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
recipe_folder = os.path.join(half_to_full, "recipes", "planks")
advancement_folder = os.path.join(half_to_full, "advancements", "recipes", "planks")

# ハーフブロックの存在するフルブロックをリストに示す
full_blocks = (
    "oak",
    "spruce",
    "birch",
    "jungle",
    "acacia",
    "dark_oak",
    "mangrove",
    "crimson",
    "warped"
)

# ハーフブロックの種類ごとにカスタムレシピと進捗を生成する
for full_block in full_blocks:
    recipe_name = f"{full_block}_planks"
    advancement_name = f"{full_block}_planks"

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
            "item": f"minecraft:{full_block}_planks",
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
            f"half_to_full:planks/{full_block}_planks"
            ]
        }
    }
    # 進捗ファイルを保存する
    advancement_path = os.path.join(f"{advancement_folder}", f"{advancement_name}.json")
    with open(advancement_path, "w") as f:
        json.dump(advancement, f, indent=4)

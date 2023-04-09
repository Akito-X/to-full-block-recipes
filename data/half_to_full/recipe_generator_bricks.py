import os
import json

half_to_full =os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
recipe_folder = os.path.join(half_to_full, "recipes", "bricks")
advancement_folder = os.path.join(half_to_full, "advancements", "recipes", "bricks")

# ハーフブロックの存在するフルブロックをリストに示す
full_blocks = (
    "",
    "stone",
    "mossy_stone",
    "mud",
    "mud",
    "deepslate",
    "nether",
    "end_stone",
    "prismarine",
    "red_nether"
)

# ハーフブロックの種類ごとにカスタムレシピと進捗を生成する
for full_block in full_blocks:
    recipe_name = f"{full_block}_bricks"
    advancement_name = f"{full_block}_bricks"

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
                "item": f"minecraft:{full_block}_brick_slab",
                "data": 0
            },
            "X": {
                "item": "minecraft:slime_ball",
                "data": 0
            },
        },
        "result": {
            "item": f"minecraft:{full_block}_bricks",
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
            f"has_{full_block}_brick_slab": {
                "conditions": {
                    "items": [
                        {
                            "items": [
                                f"minecraft:{full_block}_brick_slab"
                            ]
                        }
                    ]
                },
                "trigger": "minecraft:inventory_changed"
            }
        },
        "requirements": [
            [
            f"has_{full_block}_brick_slab"
            
            ]
        ],
        "rewards": {
            "recipes": [
            f"half_to_full:bricks/{full_block}_bricks"
            ]
        }
    }
    # 進捗ファイルを保存する
    advancement_path = os.path.join(f"{advancement_folder}", f"{advancement_name}.json")
    with open(advancement_path, "w") as f:
        json.dump(advancement, f, indent=4)

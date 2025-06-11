"""
Quest: Event Swag Kit Packaging
You're helping pack swag kits for a large tech conference. Each attendee can receive two types of items:
- 🎧 Headphones
- 🎒 Backpacks

You have three kinds of boxes available:
- Combo Box: 100 headphones + 100 backpacks
- Headphone Box: 50 headphones
- Backpack Box: 50 backpacks

🎯 Goal:
Write a function that takes the number of headphones and backpacks requested 
and returns the minimum number of boxes needed to fulfill as much of the order as possible, using full boxes only.

📝 Rules:
- Only full boxes allowed (50 or 100 items per box).
- Slight under-fulfillment is fine if quantities don't divide evenly.
- Use combo boxes first, then individual ones.

💡 Tips:
- Prioritize combo boxes first to minimize total boxes.

🧠 Step-by-Step Strategy:
- Use as many combo boxes as possible first
    - Each combo box handles both item types (e.g., 100 headphones + 100 backpacks)
    - You’re limited by whichever item you have less of (min(headphones // 100, backpacks // 100))
- Subtract what's already fulfilled by combo boxes
    - We multiply by 100 because each combo box contains 100 of each strip type, 
    and we need to subtract the actual number of strips fulfilled — not just the box count.
    - Update remaining headphones and backpacks needed.
- Use individual boxes for what’s left
    - Divide remaining headphones by 50 → use headphone boxes
    - Divide remaining backpacks by 50 → use backpack boxes
    - Only full boxes count, so round down (// 50)
- Ignore leftovers
    - If someone wants 71 headphones, you’ll send 1 box (50) and leave the 21 unfulfilled (as partial boxes aren’t allowed).

"""

def calculate_boxes(headphones, backpacks):
    # Step 1: Use as many combo boxes as possible
    combo_boxes = min(headphones // 100, backpacks // 100)
    
    # Subtract what combo boxes cover
    remaining_headphones = headphones - combo_boxes * 100
    remaining_backpacks = backpacks - combo_boxes * 100
    
    # Step 2: Use individual boxes
    headphone_boxes = remaining_headphones // 50
    backpack_boxes = remaining_backpacks // 50
    
    return {
        'combo_boxes': combo_boxes,
        'headphone_boxes': headphone_boxes,
        'backpack_boxes': backpack_boxes,
    }
    
    
print(calculate_boxes(200, 150))
# ➜ {'combo_boxes': 1, 'headphone_boxes': 2, 'backpack_boxes': 1}

print(calculate_boxes(265, 150))
# ➜ {'combo_boxes': 1, 'headphone_boxes': 3, 'backpack_boxes': 1}

print(calculate_boxes(99, 49))
# ➜ {'combo_boxes': 0, 'headphone_boxes': 1, 'backpack_boxes': 0}

print(calculate_boxes(0, 0))
# ➜ {'combo_boxes': 0, 'headphone_boxes': 0, 'backpack_boxes': 0}

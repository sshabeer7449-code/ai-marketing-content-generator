import datetime

def generate_content(tone, audience, goal, platform):
    print("\n--- AI Marketing Content Generator ---\n")

    # Tone styles
    tone_styles = {
        "professional": "We are excited to present",
        "casual": "Hey there!",
        "friendly": "Hello friend!",
        "persuasive": "Don't miss this opportunity to",
        "emotional": "Imagine a future where"
    }

    style = tone_styles.get(tone.lower(), "")

    if platform == "1":
        print("🔹 LinkedIn Post:\n")
        print(f"{style} empower {audience} to {goal} using innovative solar solutions.")
    
    elif platform == "2":
        print("🔹 Instagram Caption:\n")
        print(f"☀️ {style} {goal} for {audience}! #SolarEnergy #Success #Future")
    
    elif platform == "3":
        print("🔹 Email Content:\n")
        print("Subject: Transform Your Future with Solar Energy\n")
        print(f"{style} help {audience} to {goal}.")
        print("Join us in making a sustainable impact today.")
    
    elif platform == "4":
        print("🔹 Blog Introduction:\n")
        print(f"{style} {goal} is now possible for {audience} with the power of solar energy.")
    
    else:
        print("Invalid platform selected.")

    # Save to file
    save = input("\nDo you want to save this content to a file? (yes/no): ")
    if save.lower() == "yes":
        filename = f"marketing_output_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(f"Tone: {tone}\nAudience: {audience}\nGoal: {goal}\n\n")
            file.write("Generated Content:\n")
            file.write(f"{style} {goal} for {audience}\n")
        print(f"✅ Saved as {filename}")


def main():
    print("\n===== SMART AI MARKETING TOOL =====\n")

    tone = input("Choose tone (Professional / Casual / Friendly / Persuasive / Emotional): ")
    audience = input("Enter target audience: ")
    goal = input("Enter your goal (e.g., increase sales, promote product): ")

    print("\nSelect Platform:")
    print("1. LinkedIn")
    print("2. Instagram")
    print("3. Email")
    print("4. Blog")

    platform = input("Enter choice (1-4): ")

    generate_content(tone, audience, goal, platform)


# Run program
main()

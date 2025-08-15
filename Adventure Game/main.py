import chainlit as cl
import os
from dotenv import load_dotenv
from agents import Runner
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    raise ValueError("❌ OPENAI_API_KEY not found! Please add it to your .env file.")

# Initialize agents
narrator = NarratorAgent()
monster = MonsterAgent()
item = ItemAgent()

# Create a runner to manage all agents
runner = Runner([narrator, monster, item])


state = {"stage": "start", "inventory": [], "health": 100}

@cl.on_chat_start
async def start():
    state["stage"] = "intro"
    state["inventory"] = []
    state["health"] = 100

    await cl.Message(content="""
🎮 **Welcome to Fantasy Quest!**

You’ve entered a magical world full of mystery and danger.

🧾 **How to Play:**
- Type `start` to begin your adventure.
- Then keep typing `explore` to move forward.
- You may find enemies or magical rewards.

🎯 Let's begin!
""").send()

@cl.on_message
async def handle_message(message: cl.Message):
    msg = message.content.strip().lower()

    if state["stage"] == "intro" and msg == "start":
        story = await runner.run(narrator.intro)
        state["stage"] = "explore"
        await cl.Message(content=f"📖 {story}").send()
        await cl.Message(content="🔎 Type `explore` to continue your journey.").send()

    elif state["stage"] == "explore":
        if "explore" not in msg:
            await cl.Message(content="⚠️ Please type `explore` to continue.").send()
            return

        outcome = await runner.run(narrator.generate_event)
        await cl.Message(content=f"🌍 {outcome['text']}").send()

        if outcome.get("enemy"):
            result = await runner.run(monster.fight, state["health"])
            state["health"] = result["health"]
            await cl.Message(content=f"⚔️ {result['text']}").send()
            await cl.Message(content=f"❤️ Health: {state['health']}").send()

            if result["won"]:
                state["stage"] = "reward"
            else:
                state["stage"] = "end"
        else:
            state["stage"] = "reward"

        if state["stage"] == "reward":
            reward = await runner.run(item.give_item)
            state["inventory"].append(reward)
            state["stage"] = "explore"
            await cl.Message(content=f"🎁 You found: **{reward}**").send()
            await cl.Message(content=f"🎒 Inventory: {', '.join(state['inventory'])}").send()
            await cl.Message(content="🧭 Type `explore` to keep going.").send()

    elif state["stage"] == "end":
        await cl.Message(content="💀 **You were defeated!**\n🔁 Type `start` to try again.").send()
        state["stage"] = "intro"

    else:
        await cl.Message(content="❓ Type `start` to begin or `explore` to continue.").send()


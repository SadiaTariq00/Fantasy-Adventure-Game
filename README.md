# 🎮 Fantasy Adventure Game (Game Master Agent)

This is a text-based fantasy adventure game built using **Chainlit** and the **OpenAI Agent SDK**.  
The player explores a magical world, encounters random events, collects magical items, and fights monsters — all handled by intelligent agents.

---

## 🚀 How It Works

### 🧠 Agents Involved
- **NarratorAgent**: Controls the story, environment, and exploration logic.
- **MonsterAgent**: Handles combat and health calculations.
- **ItemAgent**: Provides rewards like potions, magical items, and treasures.

### 🛠 Tools Used
- `generate_event()` – Randomized events during exploration.
- `roll_dice()` – Simulates combat outcomes inside `MonsterAgent`.

### 🔁 Agent Handoff Flow
The game moves dynamically between agents based on the stage:
- `explore` → NarratorAgent
- Monster appears → MonsterAgent (auto fight)
- Victory → ItemAgent gives reward  
Transitions are handled via a central `state` object inside `main.py`.

---

## 🕹 How to Play

1 Add Your OpenAI API Key
Create a .env file and add this line:

2 Run the Game
chainlit run main.py

📁 Project Structure
fantasy-adventure-game/
├── main.py
├── agents/
│   ├── narrator_agent.py
│   ├── monster_agent.py
│   └── item_agent.py
├── tools.py
├── .env
├── README.md
└── requirements.txt

📎 Clone the Repo
```bash
git clone https://github.com/SadiaTariq00/Fantasy-Adventure-Game.git
cd Fantasy-Adventure-Game

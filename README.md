# tower-ai-v2 by yAI
Tower for RC Planes, for a better flight simulation.

# Ollama Page
[Here you can find the Ollama page for more details.](https://ollama.com/MYusuf/tower-ai)

# Hugging Face Page
[Here you can find the HF page for more details.](https://huggingface.co/tachion/tower-ai)

# YouTube Video
[Here you can find the YouTube video tutorial.](https://www.youtube.com/watch?v=1MKTU9S0DMI)

# yAI website
[Here you can find the official yAI website.](https://x-y-ai.web.app/)

# AI Model
TowerAI is a custom LLM model based on *LLaMA3.2 3B.* Thanks to OLLaMA and the custom AI model, it's working at least *36.36%* faster than the old version which uses the Gemini 1.5 Flash API. Also, the old version uses WiFi, and this model can work on an average laptop locally. It doesn't need supercomputers; it has only 3B parameters. It works perfectly on a MacBook Air 2017 and Lenovo ThinkPad. You can even use Nvidia's new Jetson Nano Super for improved portability. Of course, it's not tested, and it should work 99%.

# Software
There are 2 programs. One of them is the API, and the other is the AI. The AI uses our custom TowerAI model, which is recommended. It's faster and better. **It runs locally.** The other one is the Gemini 1.5 Flash API. You need a custom API key, etc., for that, and **it needs an internet connection.** You can test them both to see the performance of our TowerAI model.

# What software does
It converts Speech-To-Text first. Then it sends the result to the chosen AI model as a prompt. After that, it converts the response into a regular sound file (as mp3). Then it adds a radio effect to it to improve the experience. So it feels like you are really talking with the tower.

# Install TowerAI v2 3B
Install:
```
ollama pull MYusuf/tower-ai
```

Install and run for testing directly:
```
ollama run MYusuf/tower-ai
```

See Installed Model:
```
ollama list
```
There should be tower-ai!

# Installation
1. Clone the repository:
   ```
   git clone https://github.com/MYusufY/tower-ai-v2.git
   cd tower-ai-v2
   ```
2. Install the requirements
   ```
   pip install -r requirements.txt
   ```

4. (OPTIONAL) Switch to "myenv" which has all the required libraries and setup

   You can install the venv to directly have all required libraries installed instead using requirements.txt. You can find myenv [from old repo.](https://github.com/MYusufY/tower-ai)
   ```
   source myenv/bin/activate
   ```
5. Run the AI/API script
   
   TowerAI custom model:
   ```
   python3 tower-ai-custom.py
   ```
   *To run the tower-ai-custom.py script, you need to [install TowerAI v2 3B model](https://github.com/MYusufY/tower-ai-v2?tab=readme-ov-file#install-towerai-v2-3b) first!*

   Google Gemini 1.5 Flash API:
   ```
   python3 tower-ai-api.py
   ```
7. Set API key (if you are using Gemini)
   To get an API key, you can follow the steps [of my LVGL Gemini project.](https://github.com/MYusufY/lvgl-gemini/wiki)

# Contact
You can contact us here: [tachion.software@gmail.com](mailto:tachion.software@gmail.com?subject=Project%20TowerAI)

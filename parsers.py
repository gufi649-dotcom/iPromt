import requests
from bs4 import BeautifulSoup
from database import save_prompt

headers = {"User-Agent": "Mozilla/5.0"}

def parse_prompthero():
    url = "https://prompthero.com/search?q=portrait+person"
    r = requests.get(url, headers=headers, timeout=30)
    soup = BeautifulSoup(r.text, "lxml")

    for img in soup.find_all("img"):
        image = img.get("src")
        prompt = img.get("alt")
        if image and prompt and "portrait" in prompt.lower():
            save_prompt(image, prompt, "PromptHero")

def parse_civitai():
    url = "https://civitai.com/images?query=portrait"
    r = requests.get(url, headers=headers, timeout=30)
    soup = BeautifulSoup(r.text, "lxml")

    for img in soup.find_all("img"):
        image = img.get("src")
        prompt = img.get("alt")
        if image and prompt:
            save_prompt(image, prompt, "CivitAI")

def run_all_parsers():
    try:
        parse_prompthero()
    except:
        pass
    try:
        parse_civitai()
    except:
        pass

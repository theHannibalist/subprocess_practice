from os import system as shell
import subprocess

def lolcat(text:str):
    shell(f"echo {text} | lolcat")

def run_code(code:list):
    result = subprocess.run(code,capture_output=True,text=True)
    lolcat(result.stdout)

run_code (['echo','-en','"hello world\\nHow is everything?\\nHope You are doing great!"'])

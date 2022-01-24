import os
import requests

def urls_list():
  input_url = input("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (seperated by comma)\n")
  
  split_url = input_url.split(',')
  
  while True:
    try:
      for url in split_url:
        strip_url=url.strip()
        if url.find('http://'):
          strip_url = "http://" + strip_url
        site_requests = requests.get(strip_url)
        if site_requests.status_code == 200:
          print(f"{strip_url} is Up!")
        else:
          print(f"{strip_url} is Down!")
      break
        
    except requests.exceptions.ConnectionError:
      print("You got a unvaild URL")
      break


  #check_start_over
  check_start_over()
  
def check_start_over():
  input_start_over = input("Do you want to start over? y/n ")
  if input_start_over == "y":
    os.system('clear')
    urls_list()
  elif input_start_over == "n":
    print("ok. bye")
  else:
    print("That's not vaild anwser")
    check_start_over()
  
urls_list()

import os
os.system("pip install -r writeReadDemo\\requirements.txt")
from xml.etree.ElementTree import Comment
import requests, logging, time, sys
from datetime import datetime
from rich import console
from rich.console import Console
from rich.style import Style
from rich.syntax import Syntax
# Imports or downloads all the requred Modules
Console = Console()
start = time.time()
logging.basicConfig(filename='writeReadDemo\\log.txt', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
logger = logging.getLogger('MAIN')
logger.warning(f'{dt_string} - The Program Has started properly no errors yet.')
# Starts all the required dependencies and sets the correct values for variables
while True:
    os.system("cls")
    api_key = "e735514bab20bb2bfefcbe13f1140445"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
# gets base info for weather
    Console.print("Which city would like to know info about?",style='#38d5f5')
    city_name = input("- ")
    if city_name == "end":
        end = time.time()
# For elapsed time of program run
        total = end - start
        total = round(total)
        Console.print("Thank you for using this program.",style='#38d5f5')
        logger.warning(f'{dt_string} - The Program Has Quit After, {total} seconds, using "end" command')
        logger.warning(f'--------------------------------------------- O L D ---------------------------------------------')
        break
#screat way to end the program
    logger.warning(f'{dt_string} - User has inputed city, {city_name}')
# Writes info to a file
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
# Parses the right info
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
# Sets new variables
        weather_description = z[0]["description"]
        celcus1 = current_temperature - 274.15
# Converts Kelvin to Celcus
        print(" Temprature in Celcus = ", round(celcus1))
        
# Prints Celcus rounded off
        celcus2 = round(celcus1)
        current_temperature = round(current_temperature)
        logger.warning(f'{dt_string} - The current temprature in Celcus in, {city_name} is, {celcus2}')
# Saves this info to a file
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
# Prints Kelvin
            "\n description = " +
                        str(weather_description))
# Prints Weather info like clouds
        logger.warning(f'{dt_string} - The current temprature in Kelvin in, {city_name} is, {current_temperature}')
        logger.warning(f'{dt_string} - The Weather Description in, {city_name} is, {weather_description}')
# Saves this info to a file
        end = time.time()
# For elapsed time of program run
        total = end - start
        total = round(total)
        logger.warning(f'{dt_string} - Time elapsed, {total} seconds')
        Console.print("Would you like to run the program again, or write/read a comment? (y for yes, n for no, c for comment)",style='#38d5f5')
# User input for restart or na
        question = input("- ")
        question1 = question
        if question1 == 'y':
                question1 = 'to run program again'
        elif question1 == 'n':
                question1 = 'to stop the program'
        elif question1 == 'c':
                question1 = f'comment about {city_name}'
        logger.warning(f'{dt_string} - User said {question1}')
        if question == 'y':
            logger.warning(f'--------------------------------------------- N E W ---------------------------------------------')
# Saves this info to a file
            continue
        elif question == 'c':
                city_name = city_name.capitalize()
                Console.print(f"Would you like to write a comment, or read a comment? (r for read, w for write)",style='#ff7340')
                question2 = input("- ")
                if question2 == 'w':
                        question2Answer = 'write to'
                        logger.warning(f'{dt_string} - User has chosen to {question2Answer} file')
                        Console.print(f"What comment would you like to add to, {city_name}?",style='#ff7340')
                        weather_description = weather_description.capitalize()
                        Console.print(f"Keep in mind the format will be, {dt_string} - {city_name} - {weather_description} - Comment = Blah Blah Blah",style='#ff4a40')
                        comment = input("- ")
#user input for the comment
                        try:
                                with open("writeReadDemo\\comments.txt", "a") as f:
                                        f.write(f"{dt_string} - {city_name} - {weather_description} - {celcus2}° - Comment = {comment} \n")
# styles the comment correctly and adds it to the file
                        finally:
                                f.close()
                        logger.warning(f'{dt_string} - User has added comment {comment}')
                        logger.warning(f'--------------------------------------------- N E W ---------------------------------------------')
                        continue
                elif question2 == 'r':
                        question2Answer = 'read the'
                        logger.warning(f'{dt_string} - User has chosen to {question2Answer} file')
                        try:
                                with open("writeReadDemo\\comments.txt", "r+") as f:
#opens file in read write mode
                                        m = f.read()
                                        Console.print(m, style='#ff7340')
#reads file
                                        Console.print(f"Would you like to clear file? (y for yes, n for no)",style='#ff4a40')
                                        query = input('- ')
#user input
                                        if query == 'y':
                                                Console.print(f"Are you sure action is irreversible? (y for yes, n for no)",style='#ff7340')
                                                query2 = input('- ')
                                                if query2 == 'y':
#if statement
                                                        f.truncate(0)
                                                        f.seek(0)
                                                        f.write(f"{dt_string} - File Cleared \n")
                                                        logger.warning(f'{dt_string} - User cleared comments file')
                                                        logger.warning(f'--------------------------------------------- N E W ---------------------------------------------')
#clears file
                                                else:
                                                        continue
                                        elif query == 'n':
                                                logger.warning(f'--------------------------------------------- N E W ---------------------------------------------')
                                                continue                
# styles the comment correctly and adds it to the file
                        finally:
                                f.close()
        else:
            Console.print("Thank you for using this program.",style='#38d5f5')
            logger.warning(f'{dt_string} - The Program Has Quit After, {total} seconds')
            logger.warning(f'--------------------------------------------- O L D ---------------------------------------------')
            break
# Saves this info to a file
    else:
# Just the else code
        print(" City Not Found ")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        logger = logging.getLogger('MAIN')
        logger.fatal(f'{dt_string} - THIS IS A FATAL ERROR SHOWING BAD CITY INPUTED')
# Saves this info to a file
        end = time.time()
        total = end - start
        total = round(total)
        logger.warning(f'{dt_string} - The Program Has Quit After, {total} seconds')
        logger.warning(f'--------------------------------------------- N E W ---------------------------------------------')
        time.sleep(2)
# Saves this info to a file
#Made by DeepSmeag https://github.com/DeepSmeag

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from keyboard import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import urllib.request as urllib
from imageprocessing import ProcessImage
from tess import ImgToTxt
from PIL import Image
from io import BytesIO
# import os
# Using Chrome to access web
driver = webdriver.Chrome()
# Opening page
web_page = driver.get('https://www.freekigames.com/')
# Find and open login prompt
login_box = driver.find_element_by_id('loginContainer')
login_box.click()
driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
# Select and send id
id_box = driver.find_element_by_class_name('userNameField')
id_box.send_keys('0')

# Find and send password
pass_box = driver.find_element_by_class_name('passwordField')
pass_box.send_keys('0')

# Find and click login button
login_button = driver.find_element_by_class_name('buttonsubmit')
login_button.click()
# Switch back to normal window
driver.switch_to.default_content()

"""
pyautogui.typewrite('0')
pyautogui.press('tab')
pyautogui.typewrite('0')
pyautogui.press('enter')
"""
# All trivia links
"""
    https://www.freekigames.com/advanced-spelling-trivia
    https://www.freekigames.com/eleventh-grade-vocabulary-trivia
    https://www.freekigames.com/english-punctuation-trivia
    https://www.freekigames.com/geometric-shapes-trivia
    https://www.freekigames.com/ninth-grade-vocabulary-trivia
    https://www.freekigames.com/spelling-trivia
    https://www.freekigames.com/tenth-grade-vocabulary-trivia
    https://www.freekigames.com/twelfth-grade-vocabulary-trivia
    https://www.freekigames.com/world-capitals-trivia
    https://www.freekigames.com/music-terms-trivia
"""
print("\
      #1 Advanced spelling\n\
      #2 Eleventh grade vocabulary\n\
      #3 English Punctuation\n\
      #4 Geometric shapes\n\
      #5 Ninth grade vocabulary\n\
      #6 Spelling\n\
      #7 Tenth grade vocabulary\n\
      #8 Twelfth grade vocabulary\n\
      #9 World capitals\n\
      #10 Music terms")

"""
     \\\# Link cu captchauri #///
    https://www.freekigames.com//Captcha?mode=ua&ts=1530796533882
                                        mode=ua asigura ca sunt cuvinte logice, in dictionar
                                        fara asta captchaurile sunt random
                                        ts nu stiu de ce e
Daca deschid pagina noua cu linkul de mai sus in timp ce imi cere captcha si downloadez imaginea
    pot introduce ce am downloadat, genereaza captcha nou la fiecare request presupun
"""


starting_quiz = input("Where do you want to start?")
starting_quiz = int(starting_quiz)
spelling_answers = [
                    'australia',
                    'anonymous',
                    'connecticut',
                    'connoisseur',
                    'physique',
                    'bureaucratic',
                    'disappointed',
                    'aggressive',
                    'camouflage',
                    'accidentally',
                    'wednesday',
                    'february',
                    'abbreviate',
                    'hygiene',
                    'abyss'
                    ]
advanced_spelling_answers = [
                                'esquamulose',
                                'presbyterian',
                                'autochthonous',
                                'spoliator',
                                'czechoslovakia',
                                'vivisepulture',
                                'teutonic',
                                'insouciant',
                                'prospicience',
                                'laodicean',
                                'elucubrate',
                                'smaragdine',
                                'euonym',
                                'logorrhea',
                                'eudaemonic'
                            ]
eleventh_grade_answers = {
    'procure': 'to obtain',
    'auspicious': 'favorable, noteworthy',
    'principle': 'a fundamental, primary, or general law or truth from which others are derived',
    'conspicuous': 'noticeable, obvious',
    'annotated': 'supplied with or containing explanatory notes and textual comments',
    'allegory': 'a representation of an abstract or spiritual meaning through concrete or material forms',
    'ambiguity': 'doubtfulness or uncertainty of meaning or intention',
    'denotation': 'a word that names or signifies something specific',
    'buoyancy': 'the power to float or rise in a fluid, the upward pressure exerted by the fluid in which a body is immersed',
    'conceit': 'an excessively favorable opinion of one\'s own ability, importance or wit',
    'assuage': 'to relieve or soothe',
    'quandary': 'a state of perplexity or uncertainty',
    'anecdote': 'a short account of a particular incident or event of an interesting or amusing nature, often biographical.',
    'enigma': 'a mystery',
    'euphemism': 'the substitution of a mild, indirect, or vague expression for one thought to be offensive, harsh, or blunt',
    'discern': 'to recognize the difference'
                         }
english_punctuation_answers = {
    'an exclamation mark is often used to express what?': 'excitement',
    'what is the apostrophe\'s main function?': 'show ownership or posession',
    'which date below uses a comma correctly?': 'january 1st, 2014',
    'which sentence uses a semi-colon correctly?': 'i set out on a quest; the enemies looked fierce.',
    'which sentence below uses a comma correctly?': 'before you begin, let us learn to play.',
    'which sentence uses quotation marks correctly?': 'sally said, \"it\'s time to cook dinner.\"',
    'which sentence below uses a comma(s) correctly?': 'megan, who lives next door, loves dogs.',
    'which sentence correctly uses an apostrophe?': 'i can\'t do it, because it is too hard.',
    'which of the following is not a reason to use an exclamation mark (!) ?': 'boredom',
    'quotation marks are used to do what?': 'show speech',
    'a period is also used to __________ words.': 'abbreviate',
    'where does the period go in a sentence?': 'at the end',
    'three periods in a row are called _________.': 'ellipses',
    'a semi-colon is primarily used to:': 'join two connected sentences'
                              }
english_punctuation_answers2 = {
    'which sentence below uses a comma correctly?': 'i love to play video games, but they are hard.',
    'an exclamation mark is often used to express what?': 'excitement',
    'what is the apostrophe\'s main function?': 'show ownership or posession',
    'which sentence correctly uses an apostrophe?': 'the horse\'s tail is so pretty.',
    'which date below uses a comma correctly?': 'january 1st, 2014',
    'which sentence uses a semi-colon correctly?': 'i set out on a quest; the enemies looked fierce.',
    'which sentence uses quotation marks correctly?': 'sally said, \"it\'s time to cook dinner.\"',
    'which sentence below uses a comma(s) correctly?': 'megan, who lives next door, loves dogs.',
    'which of the following is not a reason to use an exclamation mark (!) ?': 'boredom',
    'quotation marks are used to do what?': 'show speech',
    'a period is also used to __________ words.': 'abbreviate',
    'where does the period go in a sentence?': 'at the end',
    'three periods in a row are called _________.': 'ellipses',
    'a semi-colon is primarily used to:': 'join two connected sentences'
                               }
geometric_shapes_answers = {
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes2.jpg?v=1': 'oval',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes8.jpg?v=1': 'rectangle',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes16.jpg?v=1': 'octagon',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes14.jpg?v=1': 'rhombus',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes4.jpg?v=1': 'curvilinear triangle',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes6.jpg?v=1': 'parallelogram',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes9.jpg?v=1': 'trapezoid',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes15.jpg?v=1': 'hexagon',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes17.jpg?v=1': 'heptagon',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes7.jpg?v=1': 'square',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes10.jpg?v=1': 'trapezium',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes12.jpg?v=1': 'kite',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes1.jpg?v=1': 'circle',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes5.jpg?v=1': 'quatrefoil',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes11.jpg?v=1': 'triangle',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes13.jpg?v=1': 'pentagon',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes18.jpg?v=1': 'nonagon',
    'https://edgecast.freekigames.com/image/free/FreeKIGames/Images/Quizzes/geometric-shapes3.jpg?v=1': 'crescent'
                           }
ninth_grade_answers = {
    'abstract': 'a concept or idea not associated with any specific instance',
    'facilitate': 'make easier',
    'inadvertent': 'without intention (especially resulting from heedless action)',
    'verbose': 'using or containing too many words',
    'guile': 'shrewdness as demonstrated by being skilled in deception',
    'mar': 'a mark or flaw that spoils the appearance of something (especially on a person\'s body)',
    'recalcitrant': 'marked by stubborn resistance to authority',
    'eccentric': 'a person of a specified kind (usually with many eccentricities)',
    'advocate': 'a person who pleads for a cause or propounds an idea',
    'comply': 'act in accordance with someone\'s rules, commands, or wishes',
    'heed': 'paying particular notice (as to children or helpless people)',
    'advocate': 'a person who pleads for a cause or propounds an idea',
    'belittle': 'lessen the authority, dignity, or reputation of',
    'censure': 'harsh criticism or disapproval',
    'deference': 'a disposition or tendency to yield to the will of others',
    'tangible': 'possible to be treated as fact',
    'parsimony': 'extreme care in spending money'
                      }
tenth_grade_answers = {
    'malevolent': 'wishing or appearing to wish evil to others',
    'phonetic': 'related to the sounds in a language',
    'dialogue': 'a conversation between two persons',
    'injunction': 'a formal command or admonition',
    'adjunct': 'something attached to but holding an inferior position',
    'segregate': 'separating into different groups',
    'congregate': 'to come together in a group, assemble.',
    'malady': 'a sickness, illness, disease, disorder',
    'soliloquy': 'the act of talking to oneself or a dramatic monologue',
    'malcontent': 'person dissatisfied with existing state of affairs',
    'gregarious': 'seeking and enjoying the company of others',
    'eloquent': 'expressing yourself readily, clearly, effectively',
    'juncture': 'a joining together; the point at which two things are joined; any important point in time',
    'malicious': 'wishing evil or harm upon others',
    'junction': 'an act of joining or adjoining things'
                      }
twelfth_grade_answers = {
    'peruse': 'reading with careful attention',
    'impetuous': 'characterized by undue haste and lack of thought or deliberation',
    'conundrum': 'a difficult problem',
    'antithesis': 'the direct opposite or contrast to a previously given assertion',
    'guru': 'religious teacher',
    'enervate': 'to weaken, or to take energy from',
    'jovial': 'happy, cheery',
    'sensuous': 'all senses, dealing w/ all senses',
    'hegemony': 'one country/group has leadership over another',
    'deleterious': 'harmful to living things',
    'loquacious': 'talkative, chatty',
    'evanescent': 'tending to vanish like vapor',
    'chicanery': 'deceiving someone, scam',
    'benevolent': 'showing or motivated by sympathy and understanding and generosity',
    'brazen': 'unrestrained by convention or propriety',
    'fortuitous': 'occurring by happy chance',
    'deleterious': 'harmful to living things'
                        }
world_capitals_answers = {
    'what is the capital of finland?': 'helsinki',
    'what is the capital of denmark?': 'copenhagen',
    'what is the capital of germany?': 'berlin',
    'what is the capital of italy?': 'rome',
    'what is the capital of belgium?': 'brussels',
    'what is the capital of australia?': 'canberra',
    'what is the capital of the bahamas?': 'nassau',
    'what is the capital of canada?': 'ottawa',
    'what is the capital of hungary?': 'budapest',
    'what is the capital of mexico?': 'mexico city',
    'what is the capital of greece?': 'athens',
    'what is the capital of china?': 'beijing',
    'what is the capital of argentina?': 'buenos aires',
    'what is the capital of india?': 'new delhi',
    'what is the capital of austria?': 'vienna',
    'what is the capital of france?': 'paris',
    'what is the capital of egypt?': 'cairo',
    'what is the capital of cuba?': 'havana',
    'what is the capital of brazil?': 'brasilia',
    'what is the capital of japan?': 'tokyo',
    'what is the capital of czech republic?': 'prague'
                         }
music_terms_answers = {
    '___________ is a gradual decrease in loudness in a piece of music.': 'decrescendo',
    'what is the study of forms, history, science, and methods of music?': 'musicology',
    '___________ is a gradual increase in loudness in a piece of music': 'crescendo',
    'this type of instrument family is made up of drums, tambourines, and cymbals.': 'percussion',
    'who directs a group of performers?': 'conductor',
    'this type of instrument family is made up of flutes, oboe, clarinets, and bassoons.': 'woodwinds',
    '__________ is two or more parts sounding pleasurably simultaneously.': 'harmony',
    '_________ is a music symbol that lowers a note by a half step.': 'flat',
    'what is the lowest female singing voice?': 'contralto',
    'this type of instrument family is made up of violins, cello, viola, and the double bass.': 'string',
    '___________ is the last movement or passage ending a musical composition.': 'finale',
    '_________ is a person with notable technical skill in music performance.': 'virtuoso',
    '___________ is a group of singers in a chorus.': 'choir',
    '_________ is a composition written for 9 instruments.': 'nonet',
    'what music symbol indicates to play loud?': 'forte',
    '__________ is a style of male singing where the voice is able to reach the pitch of a female.': 'falsetto',
    '_________ is a music symbol that raises a note by a half step.': 'sharp',
    '________ is a person who writes music.': 'composer',
    '___________ is a piece of music written for two vocalists or instrumentalists.': 'duet',
    '__________ is the last movement or passage ending a musical composition.': 'finale',
    '___________ is a gradual increase in loudness in a piece of music.': 'crescendo'
                      }

# ###### Captcha source ###### #
src = 'https://www.freekigames.com//Captcha?mode=ua&ts=1530796533882'
dest = "E:\\Programe\\Coding_and_games\\Projects\\Wizard101Trivia_Bot\\ImgOCR\\ActualCaptcha.png"
dest_processed = "E:\\Programe\\Coding_and_games\\Projects\\Wizard101Trivia_Bot\\ImgOCR\\ActualCaptchaEdit.png"
was_looped = False


def getImage(element):
    # 37,148
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()  # saves screenshot of entire page
    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left + 148, top + 37, right + 148, bottom + 37))  # defines crop points
    im.save("E:\\Programe\\Coding_and_games\\Projects\\Wizard101Trivia_Bot\\ImgOCR\\ActualCaptcha.png")  # saves new cropped image


if(starting_quiz == 1):
    driver.get('https://www.freekigames.com/advanced-spelling-trivia')
    # Advanced spelling Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() in advanced_spelling_answers):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    # print(EC.element_to_be_clickable((By.NAME, 'captcha')))
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 2):
    driver.get('https://www.freekigames.com/eleventh-grade-vocabulary-trivia')
    # Eleventh grade vocabulary Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == eleventh_grade_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    # Get captcha img downloaded
    # urllib3.urlretrieve(src, "ImgOCR\\CaptchaActual.png")
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 3):
    driver.get('https://www.freekigames.com/english-punctuation-trivia')
    # English punctuation Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == english_punctuation_answers[question_text] or
               answers_text[answer].text.lower() == english_punctuation_answers2[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 4):
    driver.get('https://www.freekigames.com/geometric-shapes-trivia')
    # Geometric shapes Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        shape_link = driver.find_element_by_tag_name('img')
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == geometric_shapes_answers[shape_link.get_attribute('src')]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 5):
    driver.get('https://www.freekigames.com/ninth-grade-vocabulary-trivia')
    # Ninth grade vocabulary Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == ninth_grade_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 6):
    driver.get('https://www.freekigames.com/spelling-trivia')
    # Spelling Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() in spelling_answers):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 7):
    driver.get('https://www.freekigames.com/tenth-grade-vocabulary-trivia')
    # Tenth grade vocabulary Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == tenth_grade_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 8):
    driver.get('https://www.freekigames.com/twelfth-grade-vocabulary-trivia')
    # Twelfth grade vocabulary Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == twelfth_grade_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 9):
    driver.get('https://www.freekigames.com/world-capitals-trivia')
    # World capitals Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == world_capitals_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
# driver.implicitly_wait(0.5)
if(starting_quiz == 10):
    driver.get('https://www.freekigames.com/music-terms-trivia')
    # Music terms Trivia
    for i in range(0, 12):  # main for loop for all questions
        driver.execute_script("delayAnswerDisplay(0);")
        next_question = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextQuestion')))
        question_text = driver.find_element_by_class_name('quizQuestion').text.lower()
        answers_text = driver.find_elements_by_class_name("answerText")
        answers_hitbox = driver.find_elements_by_class_name("largecheckbox")
        # next_question = driver.find_element_by_id('nextQuestion')
        for answer in range(0, 4):
            if(answers_text[answer].text.lower() == music_terms_answers[question_text]):
                answers_hitbox[answer].click()
                next_question.click()
                break
        driver.execute_script("delayAnswerDisplay(0);")
    get_results_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loginitem')))
    # get_results_button = driver.find_element_by_class_name('loginitem')
    get_results_button.click()
    CaptchaFrame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'jPopFrame_content')))
    # driver.switch_to.frame(driver.find_element_by_name('jPopFrame_content'))
    driver.switch_to.frame(CaptchaFrame)
    confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
    # confirm_human_text = driver.find_element_by_name('captcha')
    while(len(driver.find_elements_by_name('captcha')) != 0):
        if(was_looped):
            captcha_img = driver.find_element_by_id('captchaImage')
            captcha_img.click()
        confirm_human_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'captcha')))
        confirm_human_text.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # getting the screenshot of captcha
        getImage(driver.find_element_by_id('captchaImage'))
        # processing image to remove yellow line
        ProcessImage(dest)
        # image to text engine use
        captcha_text = ImgToTxt(dest_processed)
        captcha_text.replace(" ", "")
        """
        letter_num = 0
        for letter in captcha_text:
            if(letter == " "):
                captcha_text[letter_num].delete()
            letter_num += 1"""
        confirm_human_text.send_keys(captcha_text)
        confirm_human_text.send_keys(Keys.ENTER)
        was_looped = True
    driver.switch_to.default_content()
    # wait('end')
    starting_quiz += 1
    was_looped = False
driver.quit()

W101TriviaGeorge.Login()
W101TriviaGeorge.Start(1)

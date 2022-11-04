# Created this File
from django.http import HttpResponse
from django.shortcuts import render


# HomePage
def index(request):
    return render(request, 'index.html')

# Map to action : analyze_Button 
def analyze_text(request):
    inputed_text = request.POST.get('_text-area', 'off') # _text-area text

    # CheckBox 
    remove_special_characters = request.POST.get('remove-special-characters', 'off') 
    remove_extra_space = request.POST.get('remove-extra-space', 'off')
    remove_extra_lines = request.POST.get('remove-extra-lines', 'off')
    character_count = request.POST.get('character-count', 'off')

    # Special Character list to delete characters from inputed text
    special_characters_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    purpose_tracker = "After Removing "

    if remove_special_characters == 'on':
        processed_raw_text = ""
        for i in inputed_text: 
            if i not in special_characters_list:
                processed_raw_text += i

        purpose_tracker += "Special Characters ,"
        inputed_text = processed_raw_text


    if remove_extra_space == "on":
        processed_raw_text = ""
        for index, value in enumerate(inputed_text):
            if not(inputed_text[index] == " " and inputed_text[index + 1] == " "):
                processed_raw_text += value

        purpose_tracker += "Extra Space ,"
        inputed_text = processed_raw_text

    if remove_extra_lines == "on":
        processed_raw_text = ""
        for i in inputed_text:
            if i != "\n" and i != "\r":
                processed_raw_text += i

        purpose_tracker += "Extra Lines ,"
        inputed_text = processed_raw_text

    if character_count == "on":
        char_count = str(len(inputed_text))
        count = '\n\nTotal Number Of Character In the String : {}'.format(char_count)
        inputed_text += count
        purpose_tracker += "Count Words ,"


    if (character_count != "on" and remove_extra_lines != "on" and remove_extra_space != "on" and remove_special_characters != "on"):
        params = {
            "purpose" : "No, Option Selected",
            "analyzed_text" : "Error, Occured in {} ".format(inputed_text)
        }

        return render(request, "analyzer_result.html", params)

    purpose_tracker = purpose_tracker.rstrip(purpose_tracker[-1])

    params = {
        "purpose" : purpose_tracker,
        "analyzed_text" : inputed_text
    }

    return render(request, "analyzer_result.html", params)

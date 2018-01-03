import json, requests, random, variables

reminder_verses = variables.reminder_verses

#callback for /remindon job
def alarm(bot, job):
    bot.send_message(chat_id=job.context[0], text="Let's be faithful to your relationship with God and hear His words! :)")
    randomised = random.randint(0, len(reminder_verses)-1)
    bot.send_message(parse_mode='HTML', chat_id=job.context[0], text=reminder_verses[randomised])

#function to send http request to bible-api.com
def http_request(book, chapterverse):
    values = book + '+' + chapterverse
    url = 'https://bible-api.com/' + values

    resp = requests.get(url=url)
    resp.raise_for_status()
    binary = resp.content
    output = json.loads(binary)

    verses = output['verses']
    text = ''

    for i in range(0, len(verses)):
        verse_text = verses[i]['text'].replace("\n", "")
        text = text + "<b>" + str(verses[i]['verse']) + "</b> " + verse_text + "\n\n"

    reference = output['reference']
    reference_title = "<b>" + reference + "</b>"

    message = reference_title + "\n" + text
    
    return message

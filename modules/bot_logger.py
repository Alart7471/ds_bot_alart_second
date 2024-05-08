def log_message(message, os):
    # print(f"{message.created_at.strftime('%d%m%Y %H:%M')} in {message.channel} : {message.author} : {message.content}")
    msg = f"{message.created_at.strftime('%Y-%m-%d %H:%M:%S')} in {message.channel} : {message.author} : {message.content}"
    channel_name = message.channel
    date = message.created_at.strftime('%d%m%Y')
    print(msg)
    log_toFile(msg, channel_name, date, os)

    #folder = f"logs/{message.channel}/{message.created_at.strftime('%d%m%Y')}"
    #filename = f"log_{message.channel}_{message.created_at.strftime('%d%m%Y')}.txt"
    #if not os.path.exists(folder):
    #    os.makedirs(folder)
    #with open(os.path.join(folder, filename), "a") as f:
    #    f.write(f"Date: {message.created_at} in {message.channel} : {message.author} : {message.content}\n")


def log_startup(message, date, os):
    log_toFile(message, "sys", date, os)


#Добавить какой-то стек, чтобы он записывал только по очереди итд, флаш или семафор
def log_toFile(message, channel_name, date, os):
    folder = f"logs/{channel_name}/{date}"
    filename = f"log_{channel_name}_{date}.txt"
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(os.path.join(folder, filename), "a") as f:
        # f.write(f"Date: {date} in {message.channel} : {message.author} : {message.content}\n")
        # print(f"Date: {date} in {message.channel} : {message.author} : {message.content}\n")
        f.write(f"Date: {message}\n")
        # f.write(f"Date: {date} in {message.channel} : {message.author} : {message.content}\n")

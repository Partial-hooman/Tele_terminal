import subprocess


def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def read(process):
    return process.stdout.readline().decode("utf-8").strip()


def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()


def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)

    
    
    
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("your_own_API_Token got from BotFather",
                  use_context=True)
  
  
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    i) To enter commands, use '!' as prefix before the input, ex- '!ls'
    ii) To enter inputs, use ':' as prefix before the input, ex- ':start_server' """)

    
def unknown_text(update: Update, context: CallbackContext):
    if update.message.text[0] == "!":
         command = update.message.text
         process = start(command.replace("!",""))
         update.message.reply_text(read(process))
         
            
    elif update.message.text[0] == ":":
           input = update.message.text
           write(process, input.replace(":",""))
           update.message.reply_text(read(process))
            
    
    
    
    
    
    
    
    
    
updater.dispatcher.add_handler(CommandHandler('help', help))    
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

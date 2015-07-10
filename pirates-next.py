import xchat

__module_name__ = "Pirates-next"
__module_author__ = "OSN64"
__module_version__ = "1"
__module_description__ = "Bot to play pirates game"


#__fetch_interval = 47 * 60  # 47 minutes
pirate_channel = "#smp"
pirate_server = "criten"
pirate_host = "JeromeTheBaller"
cnc = xchat.find_context(channel=pirate_channel)


def msg(word, word_eol, userdata):
    if xchat.nickcmp(word[1], pirate_host) == 0:
        xchat.prnt("They are the same!")
    #xchat.prnt(', '.join(word_eol))
    #userlist = context.get_list("users")
    #xchat.prnt(word)
    return xchat.EAT_NONE


xchat.hook_server("PRIVMSG", msg)
#xchat.hook_timer(__fetch_interval * 1000, dig)
xchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')

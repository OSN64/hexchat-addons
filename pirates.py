import xchat

__module_name__ = "Pirates"
__module_author__ = "OSN64"
__module_version__ = "1"
__module_description__ = "Bot to play pirates game"


__fetch_interval = 47 * 60  # 47 minutes
pirate_channel = "#pirates"
pirate_server = "criten"
cnc = xchat.find_context(channel=pirate_channel)


def msg(word, word_eol, userdata):
    #xchat.prnt('got msg: ')
    #xchat.prnt(word)
    return xchat.EAT_NONE


def dig(userdata):
    cnc = xchat.find_context(channel=pirate_channel)
    cnc.command('msg ' + pirate_channel + ' !p dig')
    return 1  # Keep the timeout going


def fish(userdata):
    cnc = xchat.find_context(channel=pirate_channel)
    cnc.command('msg ' + pirate_channel + ' !p fish')
    return 1

#xchat.hook_server("PRIVMSG", msg)
xchat.hook_timer(__fetch_interval * 1000, dig)
# sleep 5 seconds before second command
xchat.hook_timer(__fetch_interval * 1000 + 5000, fish)
xchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')

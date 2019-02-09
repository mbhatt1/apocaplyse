import configparser

config = configparser.ConfigParser()
config.read('./config/config')


def show_banner():
    banner = u"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 █████╗ ██████╗  ██████╗  ██████╗ █████╗ ██╗  ██╗   ██╗██████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
███████║██████╔╝██║   ██║██║     ███████║██║   ╚████╔╝ ██████╔╝███████╗█████╗  
██╔══██║██╔═══╝ ██║   ██║██║     ██╔══██║██║    ╚██╔╝  ██╔═══╝ ╚════██║██╔══╝  
██║  ██║██║     ╚██████╔╝╚██████╗██║  ██║███████╗██║   ██║     ███████║███████╗
╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝     ╚══════╝╚══════╝
                                                                                                                                                                                                     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    print (banner)
    return 

def show_credit():
    credit = u"""
+ -- --=[ Description: Digital Forensics Framework                            ]=--
+ -- --=[ Maintainer  : Manish Bhatt (@mbhatt1)                               ]=--
+ -- --=[ Website : https://github.com/mbhatt1/apocalypse ]=--
    """
    print (credit)
    return 

def parseConfig():
    print (repr(config['DEFAULT']['redisDirectory']))
    return

show_banner()
show_credit()
parseConfig()
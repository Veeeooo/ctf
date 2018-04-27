from models.flag.ctf_flag import UserToChallenge
def match_c(*args):
    result = UserToChallenge.by_uid_tid(args[1],args[2])
    print(result)
    if result:
        return True
    return False
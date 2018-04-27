from models.flag.ctf_flag import UserToChallenge
def get_times(*args):
    # print(UserToChallenge.by_uid_tid(tid,uid))
    print(args,123)
    return UserToChallenge.by_uid_tid(args[1],args[2])
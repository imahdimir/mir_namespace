"""

    """

my_github_username = "imahdimir"
m = my_github_username + "/"

class GitHubDataUrl :
    ind_ins = 'd-Ind-Ins'
    id_2_tic = 'd-TSETMC_ID-2-Ticker'
    adj_ret = 'd-Adjusted-Returns'
    rf = 'd-Iran-RiskFree-Rate-Monthly'
    mkt_indx = 'd-TSE-Overall-Index-TEDPIX'
    codal_ltrs = 'd-all-Codal-letters'
    codal_tics_2_ftics = 'd-CodalTicker-2-FirmTicker'

    def __init__(self) :
        for ky , vl in self.__dict__.items() :
            setattr(self , ky , m + vl)

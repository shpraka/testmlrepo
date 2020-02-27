from jupextdemo.utils import *
from jupextdemo.azaks_deploy import *
from jupextdemo.gitHubManager import GithubManager


def _test_accounts():
    pass


replyObject = {}
if __name__ == "__main__":
    # STEP 1 : take the AKS and ACR details
    # STEP 2 : Configure the Workflow files if they don't exist
    # STEP 3:  Check-In the Workflow files to Github Repo

    aks_dep = AKSDeploy()
    if aks_dep.IsUserLoggedIn():
        replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription()
    else:
        aks_dep.loginUserFlow()
        replyObject["DefaultSubscription"] = aks_dep.getDefaultSubscription()

    # get ACR details
    replyObject["ACRAccount"] = aks_dep.getACRDetails()

    # get AKS details
    replyObject["AKSCluster"] = aks_dep.getAKSDetails()

    print(replyObject)

    # now use this object and pass it to Github manager to implement

    gm = GithubManager("5cba165500074cdf6f7a52c9af7d04ce98827e7d")
    akscluster = replyObject["AKSCluster"][0] if len(
        replyObject["AKSCluster"]) > 0 else None
    acrAccount = replyObject["ACRAccount"][0] if len(
        replyObject["ACRAccount"]) > 0 else None
    gm.getWorkflowStatus("5ffd1ce2b192665f8d82ead19fed543796a3b8fc", akscluster)

    # # print(files)
    # newFile = "charts/Chart.yml"
    # content = "Hello world".encode()
    # repos.create_file(
    #     path=newFile,
    #     message="Create file for testCreateFile",
    #     content="this is the file content",
    #     branch="master",
    # )

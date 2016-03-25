# -*- coding: utf8 -*-

from pymongo import MongoClient
import datetime

db = MongoClient(host='10.8.8.111', port=27017, connect=False)['dailyEvents']
eventsCollection = db['events']

db2 = MongoClient(host='10.8.8.111', port=27017, connect=False)['points']
pointsCollection = db2['points']

eventInputList = [
    {
        "startDate": datetime.datetime(2015, 3, 19),
        "endDate": datetime.datetime(2016, 3, 23),
        "from": "mobile",
        "qudao": [
            'ynxxt',
            'cqxxt',
            'twyxy',
            'lnxxt',
            'cjjs'
        ]
    },
]

inputList = [
    {
        "startDate": datetime.datetime(2015, 3, 19),
        "endDate": datetime.datetime(2016, 3, 23),
        "from": "mobile",
        "qudao": [
            "zyt",
            "false",
            "defaultLanding",
            "sdsd",
            "qdbdzgycbs",
            "25kj150804",
            "dongqian8",
            "longxuewang"
        ]
    },
    # {
    #     "startDate": datetime.datetime(2016, 3, 19),
    #     "endDate": datetime.datetime(2015, 3, 23),
    #     "from": "mobile",
    #     "qudao": ["zyt", "dongqian8", "longxuewang"]
    # },
    # {
    #     "startDate": datetime.datetime(2015, 3, 19),
    #     "endDate": datetime.datetime(2015, 3, 23),
    #     "from": "mobile",
    #     "qudao": ["zyt", "dongqian8", "longxuewang"]
    # },
]

eventKeyList = [
    "playLandingShareVideo",
    "endLandingShareVideo",
    "enterLandingPage",
    "enterTopicsLandingPage",
    "clickNestedVideo",
    "clickTopicsToggle",
    "clickLandingShareSideBtn",
    "clickLandingShareQQ",
    "clickMobileDownloadBtn",
    "clickLandingShareQZone",
    "clickLandingShareWeibo",
    "clickLandingYCLogo"
]

# that's how I get this list
# db.getCollection('events').distinct("eventKey",{"url":{"$regex": "/*vs.yangcong345.com*/"}})
eventKeyListFromEvents = [
    "clickGradeSevenLastSemester",
    "clickGradeSevenNextSemester",
    "enterLandingPage",
    "playLandingShareVideo",
    "endLandingShareVideo",
    "clickGradeEightNextSemester",
    "pauseLandingShareVideo",
    "clickGradeNineLastSemester",
    "clickGradeNineNextSemester",
    "clickDownloadApp",
    "clickGradeEightLastSemester",
    "clickLandingShareQQ",
    "clickLandingShareWeibo",
    "clickLandingShareQZone"
]

def calPv(startDate, endDate, fromEnd, channel, eventKey):
    pvList = list(pointsCollection.find({
        "createdBy": {"$gte": startDate, "$lt": endDate},
        "header.q": channel,
        "eventKey": eventKey,
        "from": fromEnd
    }))
    return len(pvList)

def calUv(startDate, endDate, fromEnd, channel, eventKey):
    uvList = list(pointsCollection.distinct("header.userId", {
        "createdBy": {"$gte": startDate, "$lt": endDate},
        "header.q": channel,
        "eventKey": eventKey,
        "from": fromEnd
    }))
    return len(uvList)

def mainPoint():
    print("# 旧版落地页埋点情况 Points Collection")
    for dateRange in inputList:
        startDate = dateRange['startDate']
        endDate = dateRange['endDate']
        fromEnd = dateRange['from']
        print("\n## Point Type: %s From %s to %s ")%(fromEnd, startDate, endDate)
        for channel in dateRange['qudao']:
            print("\n### Channle: %s")%channel
            for eventKey in eventKeyList:
                pvNum = calPv(startDate, endDate, fromEnd, channel, eventKey)
                uvNum = calUv(startDate, endDate, fromEnd, channel, eventKey)
                print("- %s PV/UV: %s/%s    ")%(eventKey, pvNum, uvNum)


# db.getCollection('events').distinct("eventKey",{"url":{"$regex": "/*vs.yangcong345.com*/"}})
def calPvInEvents(startDate, endDate, fromEnd, channel, eventKey):
    if fromEnd == "mobile":
        fromEndReg = ["android", "iOS"]
    elif fromEnd == "pc":
        fromEndReg = ["PC"]
    regexChannel = ".*" + channel + ".*"
    pvList = list(eventsCollection.find({
        # "serverTime": {"$gte": startDate, "$lt": endDate},
        "url": {"$regex": regexChannel},
        "eventKey": eventKey,
        "platform2": {"$in": fromEndReg}
    }))
    return len(pvList)

def calUvInEvents(startDate, endDate, fromEnd, channel, eventKey):
    if fromEnd == "mobile":
        fromEndReg = ["android", "iOS"]
    elif fromEnd == "pc":
        fromEndReg = ["PC"]
    regexChannel = ".*" + channel + ".*"
    uvList = list(eventsCollection.distinct("device", {
        # "serverTime": {"$gte": startDate, "$lt": endDate},
        "url": {"$regex": regexChannel},
        "eventKey": eventKey,
        "platform2": {"$in": fromEndReg}
    }))
    return len(uvList)

def mainEvents():
    print("\n# 新版落地页埋点情况 Events Collection")
    for dateRange in eventInputList:
        startDate = dateRange['startDate']
        endDate = dateRange['endDate']
        fromEnd = dateRange['from']
        print("\n## Event Type: %s From %s to %s")%(fromEnd, startDate, endDate)
        for channel in dateRange['qudao']:
            print("\n### Channel: %s")%channel
            for eventKey in eventKeyListFromEvents:
                pvNum = calPvInEvents(startDate, endDate, fromEnd, channel, eventKey)
                uvNum = calUvInEvents(startDate, endDate, fromEnd, channel, eventKey)
                print("- %s PV/UV: %s/%s    ")%(eventKey, pvNum, uvNum)


eventInputListM = [
    {
        "startDate": datetime.datetime(2015, 3, 19),
        "endDate": datetime.datetime(2016, 3, 23),
        "from": "mobile",
        "qudao": [
            "uccs",
            "none",
            "sem1",
            "yangcong",
            # "boxfish",
            # "wechatcd",
            # "android",
            # "zyb",
            # "lnxxt",
            # "wechatdyw",
            # "ychome",
            # "xxzyqr",
            # "wechatgjc",
            # "hz",
            # "yidiansy",
            # "szwx",
            # "toutiaotj",
            # "yidianwz",
            # "ucxt",
            # "wechatcddyw"
        ]
    },
]

mobileSiteEventKeyList = [
    "enterMobileSite",
    "downloadAndroidApp",
    "downloadiOSApp",
    # "showPhysicsBanner",
    # "enterOuterPage",
    # "enterTeacherGuide",
    # "clickUserDropdown",
    # "clickInstantInsertStudent",
    # "initBatchInsert",
    # "dragInsertStuStripe",
    # "confirmInsertStu",
    # "createClassroomSuccess",
    # "createStuList",
    # "enterStuListPage",
    # "enterBrowserIncompatibleAlert",
    # "clickCloseBrowserIncompatibleAlert",
    # "enterCreateClassroomModal",
    # "createClassroom",
    # "confirmCreateClassroom",
    # "enterCreateClassroomSuccessModal",
    # "clickGradeDropdown",
    # "clickPublisherDropdown"
]

def calMobileLandingPv(startDate, endDate, fromEnd, channel, eventKey):
    if fromEnd == "mobile":
        fromEndReg = ["android", "iOS"]
    elif fromEnd == "pc":
        fromEndReg = ["PC"]
    regexChannel = ".*" + "m.yangcong345.com" + ".*"
    pvList = list(eventsCollection.find({
        # "serverTime": {"$gte": startDate, "$lt": endDate},
        "url": {"$regex": regexChannel},
        "eventKey": eventKey,
        "platform2": {"$in": fromEndReg},
        "q": channel
    }))
    return len(pvList)

def calMobileLandingUv(startDate, endDate, fromEnd, channel, eventKey):
    if fromEnd == "mobile":
        fromEndReg = ["android", "iOS"]
    elif fromEnd == "pc":
        fromEndReg = ["PC"]
    regexChannel = ".*" + "m.yangcong345.com" + ".*"
    uvList = list(eventsCollection.distinct("device", {
        # "serverTime": {"$gte": startDate, "$lt": endDate},
        "url": {"$regex": regexChannel},
        "eventKey": eventKey,
        "platform2": {"$in": fromEndReg},
        "q": channel
    }))
    return len(uvList)

def mainM():
    print("\n# m.yangcong345.com 埋点情况")
    for dateRange in eventInputListM:
        startDate = dateRange['startDate']
        endDate = dateRange['endDate']
        fromEnd = dateRange['from']
        print("\n## Event Type: %s From %s to %s")%(fromEnd, startDate, endDate)
        for channel in dateRange['qudao']:
            print("\n### Channel: %s")%channel
            for eventKey in mobileSiteEventKeyList:
                pvNum = calMobileLandingPv(startDate, endDate, fromEnd, channel, eventKey)
                uvNum = calMobileLandingUv(startDate, endDate, fromEnd, channel, eventKey)
                print("- %s PV/UV %s/%s")%(eventKey, pvNum, uvNum)


webInputList = [
    {
        "startDate": datetime.datetime(2015, 3, 19),
        "endDate": datetime.datetime(2016, 3, 23),
        "from": "mobile",
        "qudao": [
            "wdesktop",
            "none",
            "sem1",
            # "twsm",
            # "lnxxt",
            # "gao3",
            # "fh",
            # "szwx",
            # "gao6",
            # "gao8",
            # "zxz",
            # "cyxt/",
            # "baizhitong1",
            # "undefined",
            # "gao4",
            # "150505gdtkjkh",
            # "gdt11",
            # "cyxt"
        ]
    },
]

regUserEventList = [
    "enterHome",
    "clickHomeSignupBtn",
    "signupSuccess"
]

downLoadEventList = [
    "enterHome",
    "clickDownloadIosSS",
    "clickDownloadAndoridSS",
    "clickDownloadWindowsSS"
]

loginEventList = [
    "enterHome",
    "clickHomeLoginBtn",
    "loginSuccess"
]

qqLoginEventList = [
    "enterHome",
    "clickHomeQQLogin",
    "loginSuccess"
]


def homePagePv(startDate, endDate, channel, eventKey):
    pv = list(eventsCollection.find({
        # "serverTime": {"$gte": startDate, "$lt": endDate},
        "eventKey": eventKey,
        "webChannel": channel
    }))
    return len(pv)

def mainHomePage():
    print("\n# 洋葱数学主页 渠道链埋点情况")
    for dateRange in webInputList:
        startDate = dateRange['startDate']
        endDate = dateRange['endDate']
        fromEnd = dateRange['from']
        print("\n## Event Type: %s From %s to %s")%(fromEnd, startDate, endDate)
        for channel in dateRange['qudao']:
            print("\n### Channel: %s")%channel
            print("\n#### 注册")
            for eventKey in regUserEventList:
                pv = homePagePv(startDate, endDate, channel, eventKey)
                print("- %s %s")%(eventKey, pv)
            print("\n#### 下载")
            for eventKey in downLoadEventList:
                pv = homePagePv(startDate, endDate, channel, eventKey)
                print("- %s %s")%(eventKey, pv)
            print("\n#### 登录")
            for eventKey in loginEventList:
                pv = homePagePv(startDate, endDate, channel, eventKey)
                print("- %s %s")%(eventKey, pv)
            print("\n#### QQ登录")
            for eventKey in qqLoginEventList:
                pv = homePagePv(startDate, endDate, channel, eventKey)
                print("- %s %s")%(eventKey, pv)

mainPoint()
mainEvents()
mainM()
mainHomePage()
print("code done.")

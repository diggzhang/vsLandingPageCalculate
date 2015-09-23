//错题本访问人数
var startDate = ISODate("2015-08-22T00:00:00.000Z");
var endDate = ISODate("2015-09-22T00:00:00.000Z");

output = [];

pv = db.points.aggregate([
    {"$match": {
        "createdBy": {
            "$gte": ISODate("2015-08-22T00:00:00.000Z"),
            "$lte": ISODate("2015-09-22T00:00:00.000Z")
        }
    }},
    {"$match": {
        "eventKey": "enterMistakes"
    }}
]);
output.push(pv.result.length);

uv = db.points.aggregate([
    {"$match": {
        "createdBy": {
            "$gte": ISODate("2015-08-22T00:00:00.000Z"),
            "$lte": ISODate("2015-09-22T00:00:00.000Z")
        }
    }},
    {"$match": {
        "eventKey": "enterMistakes"
    }},
    {"$group": {
        "_id": '$user'
    }}
]);
output.push(uv.result.length);

eventList = [
    "clickMistakeScope",
    "clickMistakesTab",
    "clickMCollectionsTab",
    "clickMakeMCollect",
    "clickCancelMCollect",
    "clickMistakeExpl",
    "clickHiddenAnswer",
    "clickMistakesViewMore",
    "clickMistakesPagination"
];

muv = db.points.aggregate([
    {"$match": {
        "createdBy": {
            "$gte": ISODate("2015-08-22T00:00:00.000Z"),
            "$lte": ISODate("2015-09-22T00:00:00.000Z")
        }
    }},
    {"$match": {
        "eventKey": {"$in": eventList}
    }},
    {"$group": {
        "_id": '$user'
    }}
]);
output.push(muv.result.length);

eventList.forEach(function (item) {
    print("==> " + item + "<==");
    mmuv = db.points.aggregate([
        {"$match": {
            "createdBy": {
                "$gte": ISODate("2015-08-22T00:00:00.000Z"),
                "$lte": ISODate("2015-09-22T00:00:00.000Z")
            }
        }},
        {"$match": {
            "eventKey": item
        }},
        {"$group": {
            "_id": '$user'
        }}
    ]);
    print("UV of " + item + " : " + mmuv.result.length);
});
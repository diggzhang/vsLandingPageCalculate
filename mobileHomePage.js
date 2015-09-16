/* Robomongo脚本 */

var input = [
    {
        startDate : ISODate("2015-09-07T00:00:00.367Z"),
        endDate : ISODate("2015-09-08T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
    },
    {
        startDate : ISODate("2015-09-08T00:00:00.367Z"),
        endDate : ISODate("2015-09-09T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
    },
    {
        startDate : ISODate("2015-09-09T00:00:00.367Z"),
        endDate : ISODate("2015-09-10T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
    },
    {
        startDate: ISODate("2015-09-10T00:00:00.367Z"),
        endDate: ISODate("2015-09-11T00:00:00.367Z"),
        qudao: ["twyxyandroid", "twyxyios", "bjxxt"],
    },
    {
        startDate: ISODate("2015-09-11T00:00:00.367Z"),
        endDate: ISODate("2015-09-12T00:00:00.367Z"),
        qudao: ["twyxyandroid", "twyxyios", "bjxxt"],
    },
    {
        startDate: ISODate("2015-09-12T00:00:00.367Z"),
        endDate: ISODate("2015-09-13T00:00:00.367Z"),
        qudao: ["twyxyandroid", "twyxyios", "bjxxt"],
    },
    {
        startDate: ISODate("2015-09-13T00:00:00.367Z"),
        endDate: ISODate("2015-09-14T00:00:00.367Z"),
        qudao: ["twyxyandroid", "twyxyios", "bjxxt"],
    },
    {
        startDate: ISODate("2015-09-07T00:00:00.367Z"),
        endDate: ISODate("2015-09-14T00:00:00.367Z"),
        qudao: ["twyxyandroid", "twyxyios", "bjxxt"],
    }
];


(function (input) {
    input.forEach(function(item) {
        var startDate = item.startDate;
        var endDate = item.endDate;
        var q = item.qudao;

        q.forEach(function (qudao) {
            print("=====================================")
            print("q : " + qudao);
            print("date start  " + startDate);
            print("date end    " + endDate);
            print("=====================================")

            var output = [];
            pv = db.mobile_web_tracks.aggregate([
                {"$match": {"localetime": {
                    "$gte": startDate,
                    "$lt": endDate
                }} },
                {"$match": {"eventValue.q": qudao} },
                {"$match": {"eventName" : "enterMobileSite"}}
            ]);
            output.push(pv.result.length);

            print("PV: " + output[0]);

        });
    });
})(input);
